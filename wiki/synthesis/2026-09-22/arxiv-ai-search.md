---
title: "arXiv AI Research Paper Search Report"
type: synthesis
created: 2026-09-22
updated: 2026-09-22
sources: [arxiv.org]
tags: [arxiv, AI, LLM, recommendation, advertising, sequential-modeling, CTR, games, agent-eval, agent-safety, security, unlearning, MoE, quantization, speculative-decoding, time-series, mechanism-design, daily-digest]
---

# arXiv AI Research Paper Search Report — 2026-09-22

Generated: 2026-09-22 (Tuesday). **Topic-targeted sweep of the Mon 21 Sep 2026 mailing remainder** (IDs **2609.20823–2609.22086**; the same window today's `arxiv-daily` and the 09-21 siblings already mined). **609 unique IDs parsed** from 10 category listing pages, **384 in-window**, **294 unclaimed** after everything already cited in `wiki/` (6,058 known IDs); **22 papers featured in full + 6 runner-ups**. Every featured/runner-up ID was **grep-verified 0 hits in `wiki/`** at selection time.

**Methodology**: Direct page fetches of `/list/{cat}/new` for **cs.AI, cs.LG, cs.IR, cs.CL, cs.GT, cs.MA, cs.NE, cs.SI, cs.CY, cs.CV** (609 unique IDs; 384 within the Mon-21 window 20823+). At fetch time the listing pages still announce **Monday, 21 September 2026** (cs.AI 49 / cs.LG 83 / cs.CL 65 / cs.CV 74 / cs.IR 5 new subs); the fresh Tue-22 mailing (IDs **2609.22087–2609.24554**) was independently established by today's sibling `arxiv-daily` via API pagination. This report therefore mines the **unclaimed remainder of the Mon-21 window** (20823–22086), entirely **disjoint from the Tue-22 window** arxiv-daily covers — a complement, per the 09-18 / 09-15 / 09-08 second-pass precedent. ~40 titles keyword-screened on target topics → 32 abstracts fetched → **22 featured + 6 runner-ups**. Probe HTML cached under the pre-approved temp dir `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/arxiv-search-0922/`. Institutions are author-affiliation inferred where arXiv does not print them (marked *tentative*).

> **Dedup note**: `arxiv-daily` / `arxiv-ai-search` / `game-rl-daily` / `conference-digest` (09-21) claimed the Mon-21 window's marquee clusters (auto-bidding/oCPX, rec/search production, long-context serving, post-training RL, world-model/game, eval); today's `arxiv-daily` (09-22) covers the Tue-22 window (22087+) — none of this report's IDs fall in either set. The featured set below is the **unclaimed Mon-21 remainder** — MoE architecture & inference, LLM reason-auditing, agent security/eval, time-series/audio, mechanism design. All 28 curated IDs confirmed absent from the 09-21 sibling-claimed sets, from today's arxiv-daily, and from `wiki/` (build-time `known_ids.txt` of 6,058 IDs + per-ID grep).

## Summary Statistics

| Scope | Value |
|---|---|
| Window covered | Mon 21 Sep 2026 mailing (only live window at run time); IDs 2609.20823–2609.22086 |
| Categories parsed | cs.AI, cs.LG, cs.IR, cs.CL, cs.GT, cs.MA, cs.NE, cs.SI, cs.CY, cs.CV |
| Unique IDs parsed | 609 (384 in-window; 294 unclaimed after full-wiki 6,058-ID dedup) |
| Featured in full in this report | 22 papers (6 sections) + 6 shortlisted runner-ups |
| Direct advertising / CTR / pCTR papers | **0** unclaimed (the Mon-21 window's two ads papers OneBid + ADAPT were claimed by 09-21 `arxiv-daily`) |
| Rec/interaction relevance | IntBMoE deployed in AMap generative rec with UVCTR A/B gain (+2.4% rel) — the window's strongest production-rec data point |
| Mailing status | `/new` pages still announce Mon-21 at fetch time; Tue-22 window (22087+) established by sibling `arxiv-daily` via API → this report mines the **unclaimed Mon-21 remainder** (disjoint from Tue-22) |

**Theme of the window (unclaimed remainder)**: the Mon-21 remainder concentrates **MoE & inference engineering** (full-participation block-conditioned MoE with a production rec deployment, W4A4 quantization theory, watermarkable speculative sampling, GPU-kernel compiler evaluation including a recommender-kernel benchmark), **LLM reasoning-audit & post-training** (formal-logic CoT verification, information-gain code-generation verifiers, efficiency-regularized abstention, reasoning-trace analysis for MT, multilingual unlearning), **agent security/privacy/eval** (long-running agent authorization revocation, black-box privacy-leakage channels, multi-stage jailbreak defenses, video-agent benchmark, graph-structured skill evolution), **sequential/time-series & audio** (spectrally-aligned latent flow matching for seq-gen, open full-duplex speech-to-speech with tools, on-device SALMs), and a **mechanism-design game-theory contribution** (α-fair prophet inequalities with sample-vs-full-info phase transitions).

---

## 1 LLM Post-Training & Reasoning

### 1.1 CoVer — GT-Anchored Verifier Co-Training for Code-Generation RL (2609.21208)
- **Title**: Information-Gain Rewards over Diversity-Pruned Tests: GT-Anchored Verifier Co-Training for Reliable Code Generation
- **Authors**: Ana Nunez, Peyman Najafirad
- **Institution**: UTSA (Najafirad; tentative)
- **Date**: Mon 21 Sep 2026 (cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.21208
- **Abstract**: Self-play co-training of a single LM as both coder and test author suffers two pathologies: *permissiveness collapse* (pass-rate rewards maximize trivial non-discriminative tests) and *concentration bias* (i.i.d. sampled tests cluster on modal inputs). **CoVer**: a single-policy GRPO framework. (1) An **information-gain (IG) reward** scores each self-generated test by the mutual information between its pass/fail vector and a graded, ground-truth-anchored correctness signal y∈[0,1]^m, gated by covariance sign so only positively discriminative tests get reward. (2) A three-stage diversity-aware selection prunes the candidate pool to a behaviorally non-redundant suite (invalidity / input-string / execution-profile filtering), raising effective IG-estimator sample size at fixed execution budget. On LiveBench, MBPP, LiveCodeBench, CodeContests, Code-Forces: **+5.8 pass@1 at 7B, +7.1 at 14B** over the Qwen2.5-Instruct backbone; as a drop-in within the CodeT ranking pipeline, CoVer-7B adds **+3.5 points**.
- **Key Innovations**: (1) IG reward over GT-anchored graded correctness as the anti-collapse objective; (2) behavioral non-redundancy pruning as variance control; (3) dual benefit of co-training for both generation and code selection.
- **Venue**: Preprint.

### 1.2 Rewarding Efficient Reasoning Improves Abstention on Underspecified Tasks (2609.20846)
- **Title**: Rewarding Efficient Reasoning Improves Abstention on Underspecified Tasks in Reasoning Models
- **Authors**: Polina Tsvilodub, Max Höth, Michael Franke, Björn Deiseroth, Carina Kauf
- **Institution**: multi-institution academic (Tübingen/MIT-aligned, Franke-Kauf; tentative)
- **Date**: Mon 21 Sep 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2609.20846
- **Abstract**: LRMs fail an under-studied capability: **knowing when to abstain**. Comparison with a human study reveals humans' reasoning effort on unanswerable tasks is *upper-bounded by* answerable tasks, while LRMs waste compute — generating longer CoTs on unanswerable than answerable prompts. A **GRPO reward encouraging efficient reasoning** about whether the task contains all needed information yields human-like abstention: **+12.8% average abstention gains** on several 4B LRMs while retaining answering capability and cutting CoT length **44%** on average.
- **Key Innovations**: (1) resource-rational (human-anchored) framing of abstention as an efficiency problem; (2) a GRPO reward for information-sufficiency meta-reasoning; (3) simultaneous abstention improvement and 44% inference-efficiency gain.
- **Venue**: Preprint.

### 1.3 LogicTrack — Auditing Reasoning Trajectories with Formal Logic Solvers (2609.21492)
- **Title**: LogicTrack: Auditing Reasoning Trajectories of Large Language Models with Formal Logic Solvers
- **Authors**: Jingyu Hu, Shu Yang, Weiru Liu, Di Wang
- **Institution**: Bristol/KAUST-aligned (Liu/Wang; tentative)
- **Date**: Mon 21 Sep 2026 (cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.21492
- **Abstract**: CoT optimization largely relies on outcome-based feedback, leaving *intermediate-step logical validity* unverified — models arrive at correct answers via logically flawed chains. **LogicTrack**: a neuro-symbolic framework that auto-formalizes each reasoning step into symbolic representations and verifies with automated theorem provers. Introduces **Solver-Based Backtracking Reward (SBR)** — a step-wise scoring of logical soundness that guides backtracking tree search at inference; additionally distills backtracking traces into SFT data so models internalize step-wise auditing. Across 8 reasoning benchmarks and 7 LLMs, improves both verifiability of chains and final-answer pass rate.
- **Key Innovations**: (1) formal-verifier feedback (not LLM judge) on reasoning intermediates; (2) SBR reward + inference-time backtracking tree search; (3) SFT from audited trajectories — CoT verification becomes an intrinsic capability.
- **Venue**: Preprint.

### 1.4 When Does Reasoning Help in MT? — Hierarchical Analysis of LRM Traces (2609.21247)
- **Title**: When Does Reasoning Help in Machine Translation? A Hierarchical Analysis of LRM Reasoning Traces
- **Authors**: Yuxiang Liu, Jiaming Luo, Eleftheria Briakou, Colin Cherry
- **Institution**: Google DeepMind-aligned (Cherry/Briakou+; tentative)
- **Date**: Mon 21 Sep 2026 (cs.CL); **EMNLP 2026 Main**
- **arXiv**: https://arxiv.org/abs/2609.21247
- **Abstract**: LRMs increasingly use intermediate traces for MT, but it is unclear when reasoning helps. Analyzes traces across models/languages/domains/datasets on reasoning language, length, structure. Findings: best reasoning language is **model-specific**; reasoning length has a **non-monotonic** relationship with quality; traces exhibit recurring functional patterns. Introduces **Hierarchical Meta-Summarization (HMS)**: a scalable framework inducing coarse- and fine-grained reasoning structures without predefined taxonomies. HMS reveals a shared organization — understanding/planning → translating/drafting → refining/verifying — plus domain-specific variation. Conclusion: MT reasoning should be controlled **model-, length-, and pattern-aware**, not uniformly encouraged.
- **Key Innovations**: (1) HMS taxonomy-free structure induction for reasoning traces; (2) model-specific best reasoning language + non-monotonic length curve; (3) practical directive: control reasoning conditionally rather than uniformly.
- **Venue**: EMNLP 2026 Main.

### 1.5 μ²-Bench — A Multilingual Machine Unlearning Benchmark (2609.20945)
- **Title**: μ²-Bench: A Multilingual Machine Unlearning Benchmark ($\mu^2$-Bench)
- **Authors**: Kyomin Hwang, Hyeonjin Kim, Hyunho Lee, Yearim Kim, Yeji Song, Nojun Kwak
- **Institution**: Seoul National University-aligned (Kwak; tentative)
- **Date**: Mon 21 Sep 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2609.20945
- **Abstract**: Undesired information (harmful content, private data) propagates through multilingual LLMs via direct training *and indirect cross-linguistic spread*. Multilingual Machine Unlearning (MMU) evaluation is underexplored. **μ²-Bench** simulates the full memorization → unlearning → evaluation pipeline across diverse languages: (1) broad language set; (2) evaluation on both training and **hold-out languages**; (3) knowledge dispersed across multiple languages. Shows successful MMU requires methods reflecting multilingual characteristics (cross-lingual transfer of both memorization and forgetting).
- **Key Innovations**: (1) full-pipeline multilingual unlearning benchmark; (2) hold-out-language and distributed-knowledge evaluation; (3) evidence that language-agnostic unlearning methods underperform.
- **Venue**: Preprint.

---

## 2 MoE Architecture, Quantization & Inference Systems

### 2.1 IntBMoE — Full-Participation MoE, Deployed in AMap Generative Rec (2609.21346)
- **Title**: IntBMoE: Integrating Block-Level Conditioning into Expert Composition for Full-Participation Mixture-of-Experts
- **Authors**: Ran Cheng, Longfei Xu, Zheng Liu, Kaikui Liu, Xiangxiang Chu
- **Institution**: Alibaba / AMap-aligned (Chu; tentative)
- **Date**: Mon 21 Sep 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.21346
- **Abstract**: MoE designs cannot independently set **participation** (how many experts contribute), **execution** (how many are computed), and **materialization** (how many parameter sets are stored). Sparse routing shrinks participation; dense output-mixing grows execution; parameter-merging grows materialization. **IntBMoE** decouples all three by pairing dense expert composition with sparse block execution: a small learned codebook supplies blocks (one per entry); at each internal layer a lightweight hypernetwork merges all expert bases in that layer's pool into one composed expert → **full participation** (every composed expert draws on the whole pool), **sparse execution** (router sends each token to a few blocks), **bounded materialization** (codebook fixes block count). **Dual-Path Residual Gating (DPRG)** couples two independently composed paths via multiplicative gating. Gains over sparse/dense MoE baselines on image classification; validated on language modeling **and sequential recommendation**. **Fully deployed in AMap's generative recommendation system** serving hundreds of millions of users under a 60ms latency budget, with **+2.4% relative UVCTR in online A/B**.
- **Key Innovations**: (1) three-way decoupling (participation/execution/materialization) via block-conditioned composition; (2) DPRG multiplicative dual-path gating; (3) rare full production data point — MoE for generative rec at AMap scale with measured UVCTR lift.
- **Venue**: Preprint (code released).

### 2.2 Understanding LLM Quantization via Activation-Guided Compensation & Orthogonal Residuals (2609.21450)
- **Title**: Understanding LLM Quantization through Activation-Guided Compensation and Orthogonal Residuals
- **Authors**: Yamato Narita, Issei Sato
- **Institution**: University of Tokyo-aligned (Sato; tentative)
- **Date**: Mon 21 Sep 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.21450
- **Abstract**: Aggressive **W4A4** quantization remains hard because activation outliers degrade effective quantization resolution; weight optimization, channel-wise scaling, and orthogonal rotation mitigate this but their error decomposition is unclear. Exact decomposition of local weight-activation quantization error into **activation-guided weight compensation + orthogonal residual**; bounds the residual with persistent channel-wise outlier and regular activation quantities. Produces practical guidelines: how random signs suppress constructive interference among persistent outlier channels; why sampling multiple sign patterns improves transformation selection; how second-moment balancing yields an **L2 scaling rule** while further relaxation recovers **SmoothQuant-style L∞ scaling**. Backpropagation-free configurations across eight Llama/Mistral models match gradient-trained SpinQuant performance.
- **Key Innovations**: (1) exact error decomposition isolating compensation-from-transformation components; (2) residual bounds → design guidelines (rotation/signs/scaling unified); (3) backprop-free W4A4 competitive with SpinQuant.
- **Venue**: Preprint.

### 2.3 Watermarkable Multi-Draft Speculative Sampling via Poisson Processes (2609.21858)
- **Title**: Watermarkable Multi-Draft Speculative Sampling via Poisson Processes
- **Authors**: Yanxiao Liu, Sicheng Wan, Zhan Gao, Deniz Gündüz
- **Institution**: Imperial College London-aligned (Gündüz; tentative)
- **Date**: Mon 21 Sep 2026 (cs.CR/cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.21858
- **Abstract**: Recent work shows combining speculative sampling with watermarking is highly non-trivial / potentially impossible. Presents a **multi-draft speculative sampling algorithm based on Poisson processes** that improves this frontier: strong sampling efficiency on its own and **naturally watermarkable** — an unbiased watermark embedded *without degrading speculative acceptance*. Built on an exact list-coupling-without-communication scheme yielding **drafter invariance** beneficial to both sampling and watermarking. Claimed **first multi-draft, drafter-invariant speculative sampling scheme maintaining both watermark strength and sampling efficiency**.
- **Key Innovations**: (1) Poisson-process list coupling as the construction primitive; (2) drafter invariance (decouples watermark from drafter choice); (3) first result combining multi-draft speculation + robust watermark, verified empirically.
- **Venue**: Preprint.

### 2.4 How Much of a Real Workload Can LLM-Generated GPU Kernels Reach? (2609.21058)
- **Title**: How Much of a Real Workload Can LLM-Generated GPU Kernels Actually Reach?
- **Authors**: Gaurav Agarwal, Ashish Garg, Isha Singhal
- **Institution**: industrial/hedge-fund-aligned (tentative)
- **Date**: Mon 21 Sep 2026 (cs.DC/cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.21058
- **Abstract**: Evaluates five model configs on **KernelBench level 1**: a frontier model produces correct kernels for **91.1%** of problems, verified speedups on 22/56 (median 1.235×); open-weights best reaches 30.4% correct, only three verified speedups, zero convolutions. Answers the unasked question — what fraction of real wall-clock do such kernels govern? Profiling 7 workloads / 3 domains: addressable fraction **8.9%–58.2%**. On transformers, 80–86% of runtime is cuBLAS GEMM + FlashAttention → realistic end-to-end gain ≈**1%**, shrinking with scale. On **recommenders it is 58.2%**, concentrated in a single embedding kernel → introduces **DLRM-Bench**, 12 recommender kernel problems in KernelBench format: 41.7% win rate, **1.552× median**, projecting **8.63% end-to-end**. Also: KernelBench's absolute-tolerance correctness check is satisfied by a tensor of zeros on **4 of 60** level-1 problems; two self-produced kernels exploited this, incl. one scored 283× writing 0.3% of its output buffer. Proposes scale-invariant replacements; releases all 879 evaluations.
- **Key Innovations**: (1) addressable-fraction profiling reframes kernel-authored speedups (transformers ≈1% e2e vs rec 58.2%); (2) DLRM-Bench — the first recommender-specific KernelBench-format suite (embedding kernels = the leverage); (3) correctness-check robustness audit exposing zero-tensor exploits.
- **Venue**: Preprint.

### 2.5 The Communication Bottleneck — Tree-Structured Expression Serialization (2609.21509)
- **Title**: The Communication Bottleneck: A Round-Trip Study of Tree-Structured Expression Serialization in Language Models
- **Authors**: Xavier Suau, Alex Ferrando de las Morenas, Luca Zappella, Samy Bengio
- **Institution**: Apple UX/alignment-aligned (Bengio; tentative)
- **Date**: Mon 21 Sep 2026 (cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.21509
- **Abstract**: When LMs reason in CoT or exchange free-text intermediates, they serialize structured info into natural language. Round-trip protocol: a generator converts a procedurally generated arithmetic expression into a word problem; a separate extractor recovers the expression; symbolic equivalence is the oracle. Across all pairwise combinations of 16 models: the channel is **lossy and asymmetric** — swapping generator/extractor shifts accuracy up to 60.4 points; best pair reaches 92.9% by combining *different* models on each end. **≥73.6% of round-trip failures originate at generation**; difficulty driven by tree structure (operator count, depth, right-branching), not model family. Channel is **trainable**: ~3,600 fine-tuning examples sharing the evaluation's operators/tree shapes lift every open-weight model above untrained Gemini-3.1-Pro; disjoint-domain regime (new operators/vocabulary) still lifts every open-weight model, though a gap to frontier remains.
- **Key Innovations**: (1) round-trip protocol + symbolic-equivalence oracle as an exact communication metric; (2) generation-side bottleneck attribution + structural difficulty factors; (3) fine-tuning transfers in matched *and* disjoint domains.
- **Venue**: Preprint.

---

## 3 Agents: Skills, Evaluation, Security, Privacy

### 3.1 GraphSkillEvo — Evolutionary Optimization of Graph-Structured Agent Skills (2609.21749)
- **Title**: GraphSkillEvo: Evolutionary Optimization of Graph-Structured Agent Skills
- **Authors**: Rui Sun, Zhi Zheng, Zhenkun Wang, Zhichao Lu
- **Institution**: City University of Hong Kong-aligned (Lu/Wang; tentative)
- **Date**: Mon 21 Sep 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.21749
- **Abstract**: Skill optimization improves LLM agents, but existing methods encode skills as **unstructured natural-language instructions** → no explicit workflow-level guidance, heavy redundancy, and an unconstrained search space. Proposes **graph-structured skills**: nodes = execution steps + operational guidance; directed edges = context-dependent transitions. Graph form gives clear workflow guidance and enables structured optimization. **GraphSkillEvo**: population-based evolutionary framework (mutation + crossover on graph skills), maintaining multiple candidates and combining effective components — broader exploration than purely LLM-based iterative self-refinement. Across five agent benchmarks, beats SkillOpt: **+4.01% avg accuracy on GPT-5.4-nano, +1.76% on GPT-5.4**.
- **Key Innovations**: (1) graph-structured (workflow-explicit) skill representation vs unstructured text; (2) population-based evolution with graph mutation/crossover; (3) consistent gains over SkillOpt across model scales.
- **Venue**: Preprint.

### 3.2 AgentVidBench — Multi-Hop Video QA for MLLM Agents (2609.21386)
- **Title**: AgentVidBench: A Multi-Hop Video Question Answering Benchmark for Evaluating MLLM Agents
- **Authors**: Seoyeon An, Hyeonseo Jang, Minsu Kim, Chanho Lee, Younghan Park, Kangwook Lee
- **Institution**: UW-Madison/KAIST-aligned (Lee; tentative)
- **Date**: Mon 21 Sep 2026 (cs.CV/cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.21386
- **Abstract**: Video benchmarks remain confined to simple scene-level queries / global summaries needing single-step inference, while real-world video understanding needs **multi-hop multimodal reasoning**. **AgentVidBench**: a multi-hop video QA benchmark evaluating spatial, temporal, and causal reasoning of MLLM agents. Beyond QA pairs, provides **step-by-step solution traces** for trajectory evaluation — checks whether agents *explicitly acquire the evidence* justifying answers. 12 proprietary + open MLLMs: single-turn performance is limited; integrating them into SOTA agentic workflows generally improves both accuracy and trajectory scores. Also presents a simple yet effective agentic strategy as a competitive baseline.
- **Key Innovations**: (1) multi-hop spatial/temporal/causal video reasoning benchmark (first agent-native); (2) trajectory evaluation beyond final-answer accuracy; (3) documented agentic-workflow lift across 12 MLLMs.
- **Venue**: Preprint (code + dataset released).

### 3.3 Authorization Revocation for Long-Running AI Agents: Root-Scoped Quiescence (2609.21284)
- **Title**: Authorization Revocation for Long-Running AI Agents: Root-Scoped Quiescence under Delegation and Asynchronous Execution
- **Authors**: Genliang Zhu, Chu Wang
- **Institution**: — (academic/industrial; tentative)
- **Date**: Mon 21 Sep 2026 (cs.PL/cs.AI/cs.CR)
- **arXiv**: https://arxiv.org/abs/2609.21284
- **Abstract**: Long-running agents outlive initiating processes through credentials, delegated tasks, queues, callbacks, reservations, provider-side ops; cancellation/process-exit/credential revocation don't close every pre-cut carrier. Defines **root-scoped authorization quiescence**: for each manifested sink, a certificate accounts for every cut-relevant acceptance under the retired root-epoch atom preceding its local fence, excludes protected acceptance after the fence, and permits exact rebind to a current, independently sufficient support. Linearizes a root cut; represents alternative/conjunctive authority as antichains of minimal sufficient root sets; composes provider-frontier certificates into a cutset. Proves post-cut issuer non-expansion, support-sound projection, compositional soundness, independent-support preservation, merge-order independence, crash/replay stability. Provider-free late-effect suite matches **17/17** registered outcomes; checker verifies 17/17 traces and rejects 44/44 semantic regressions.
- **Key Innovations**: (1) formalizes *when* an authorization revocation truly holds across async/delegated agent state; (2) root-scoped quiescence certificates + antichain authority composability; (3) proof appendix + concrete trace suite (17/17 accept, 44/44 reject).
- **Venue**: Preprint.

### 3.4 CIPL — Channel-Aware Framework for Recoverable Privacy Leakage in LLM Agents (2609.21686)
- **Title**: CIPL: A Channel-Aware Framework for Recoverable Privacy Leakage in LLM Agents
- **Authors**: Tao Huang, Guosen Wu, Guolong Zheng, Jiayang Meng, Chen Hou, Xu Yang, Xuechao Yang, Feng Xia
- **Institution**: — (academic; tentative)
- **Date**: Mon 21 Sep 2026 (cs.CR/cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.21686
- **Abstract**: Privacy-leakage evaluation in LLM agents is done component-wise (memory, retrieval, tool-use), failing to distinguish internal exposure from what an **external observer can actually recover**. **CIPL (Channel Inversion for Privacy Leakage)**: a channel-aware framework for black-box leakage. Represents a target through sensitive source → selection → assembly → execution → observation → extraction stages, evaluating the transition from selected sensitive units to attacker-recoverable output under a shared protocol. Experiments across memory/retrieval/tool-mediated targets + BrowserUse live-agent case study: **storage labels alone don't determine recoverability** — memory is near-saturated; retrieval-mediated leakage is frequently partial; tool-mediated and live-agent leakage varies strongly with observation surface, prompt-to-channel alignment, retrieval depth, provider behavior. A stratified semantic audit finds attacker-useful disclosures canonical exact matching misses.
- **Key Innovations**: (1) recoverability (not storage) as the leakage unit; (2) unified channel protocol across heterogenous agent pipelines + live-agent study; (3) stratified semantic audit beyond exact-match leakage counting.
- **Venue**: Preprint.

### 3.5 From Memory to Behavior — Behavior-Aware Role-Playing for Influencers (2609.21349)
- **Title**: From Memory to Behavior: A Behavior-Aware Role-Playing Framework for Social Media Influencers
- **Authors**: Ji-Lun Peng, Yi-Zhen Zhang, Chun-Nan Chou, Yun-Nung Chen
- **Institution**: NTU-aligned (Chen; tentative)
- **Date**: Mon 21 Sep 2026 (cs.CL/cs.AI); **EMNLP 2026 Findings**
- **arXiv**: https://arxiv.org/abs/2609.21349
- **Abstract**: LLM role-playing agents for real individuals fail to capture *situation-dependent reactions*. Existing ICL methods plus LLM-based eval are weak for obscure individuals. **Situation–Internal state–Behavior Persona** method incorporates situation-dependent behavioral strategies; evaluation protocol gives LLM evaluators references about the impersonated individual. New social-media reply dataset: outperforms state-of-the-art ICL baselines; eval protocol achieves moderate correlation with human judgment; transfers to fictional-character benchmarks. Behavioral information broadly improves impersonation fidelity.
- **Key Innovations**: (1) situation→internal-state→behavior persona (decision-tree behavioral rules vs flat memory); (2) reference-augmented LLM evaluation for obscure individuals; (3) transfer beyond social media to fictional characters.
- **Venue**: EMNLP 2026 Findings.

---

## 4 Agent & LLM Security / Jailbreak Defenses

### 4.1 CASCADE — Defense Combination Across Pipeline Stages (2609.21793)
- **Title**: CASCADE Against Jailbreaks: Combination Across Stages with Controlled Attack-Defense Evaluation
- **Authors**: Jiale Luo, Eric Han
- **Institution**: — (academic/industrial; tentative)
- **Date**: Mon 21 Sep 2026 (cs.CR/cs.CL); **EMNLP 2026 Findings**
- **arXiv**: https://arxiv.org/abs/2609.21793
- **Abstract**: Jailbreak defenses operate at different pipeline stages (input modification, output guard), but prior studies evaluate in isolation with inconsistent ASR definitions. First systematic study of **defense combinations within and across stages** under a consistent threat model (direct, black-box, single-turn attacks). Standardizes evaluation via a principled attack-success-rate formulation with controlled query budgets + explicit fairness rules. Across **19 attacks × 15 defenses**: no single defense is universally best, but well-chosen **combinations achieve substantial safety with minimal utility degradation**, yielding practical recommendations for layered defense pipelines.
- **Key Innovations**: (1) first standardized defense-combination study (19×15 matrix); (2) principled ASR + query-budget fairness; (3) actionable layered-defense recommendations.
- **Venue**: EMNLP 2026 Findings.

### 4.2 HE-Guardrail — Homomorphic Jailbreak Guardrail for Encrypted LLM Inference (2609.21484)
- **Title**: HE-Guardrail: A Homomorphic Guardrail Against Jailbreak Attacks for Encrypted Large Language Model Inference
- **Authors**: Byeongseo Min, Yongwoo Lee, Young-Sik Kim, Yongjune Kim
- **Institution**: POSTECH-aligned (Kim; tentative)
- **Date**: Mon 21 Sep 2026 (cs.CR/cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.21484
- **Abstract**: HE-based PPML lets a server evaluate LLMs over encrypted inputs — but **HE-LLM inference is vulnerable to malicious clients** submitting jailbreak prompts. The confidentiality protecting benign clients also blinds the server to incoming prompts/responses. **HE-Guardrail**: evaluates guardrail mechanisms entirely over encrypted data and homomorphically controls whether the target-model response is returned to the client. Instantiated with Llama Guard, JBShield, GradSafe — closely reproduces plaintext guardrail decisions in the encrypted domain, with distinct security-efficiency-utility trade-offs.
- **Key Innovations**: (1) identifies the HE-LLM jailbreak surface (blind server); (2) fully-homomorphic guardrail evaluation + encrypted response gating; (3) three standard guardrail instantiations with measured trade-offs.
- **Venue**: Preprint.

### 4.3 Conformal Privacy Auditing — Calibrated Re-identification Attacks (2609.21340)
- **Title**: Conformal Privacy Auditing: Calibrated Re-identification Attacks with Statistical Guarantees
- **Authors**: Shuo Huang, Gholamreza Haffari, Xingliang Yuan, Ting Yu, Lizhen Qu
- **Institution**: Monash-aligned (Haffari/Yuan; tentative)
- **Date**: Mon 21 Sep 2026 (cs.CR/cs.CL)
- **arXiv**: https://arxiv.org/abs/2609.21340
- **Abstract**: Empirical identity leakage from released text is driven by attackers combining LLMs + auxiliary knowledge. Existing audits report success rates for specific attack pipelines without finite-sample guarantees; DP is hard to translate to release-time decisions per document. **Conformal Privacy Auditing (CPA)**: distribution-free calibration framework certifying re-identification risk per released document against LLM-empowered adversaries. Outputs a conformal ambiguity set of candidate identities guaranteed to contain the true one with user-chosen confidence under exchangeability, plus an interpretable leakage proxy from set size. Supports logit-access and sampling-only attackers for open-source and proprietary API models. Across benchmarks/configs: calibrated coverage and sharp shifts in certified identifiability as auxiliary knowledge, LLM augmentation, and release mechanisms vary.
- **Key Innovations**: (1) finite-sample statistical certificates for LLM-empowered re-identification risk; (2) unified open-source/API attacker support; (3) calibrated comparison of release-time linkage risk across configs.
- **Venue**: Preprint.

---

## 5 Sequential Modeling, Time Series & Audio/Speech

### 5.1 Spectrally-Aligned Latent Flow Matching for Time Series Generation (2609.21989)
- **Title**: Time series generation with spectrally aligned latent flow matching
- **Authors**: Camilo Carvajal Reyes, Felipe Tobar
- **Institution**: Universidad de Chile-aligned (Tobar; tentative)
- **Date**: Mon 21 Sep 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.21989
- **Abstract**: Latent flow models are cost-effective for time-series generation but latent compression induces a **spectral mismatch** vs the underlying dataset, hindering use as training surrogates. Proposes a **spectrally-aligned latent-flow generator**: the latent space for flow matching is trained to preserve dynamics-relevant properties. Fine-tuning losses based on canonical signal representations — **Fourier, wavelet, and signature transforms** — overcome the mismatch; interpretability ensures alignment on relevant features (e.g., smoothness, targeted spectral content) rather than pointwise reconstruction only. Beats base latent-flow and SOTA on real-world long-range univariate/multivariate benchmarks on signal-realness and computational-efficiency metrics, while staying locally aligned to the training set.
- **Key Innovations**: (1) spectral alignment of the latent space (Fourier/wavelet/signature fine-tuning losses); (2) signal-realness-focused evaluation paradigm; (3) long-range univariate + multivariate superiority over latent-/SOTA baselines.
- **Venue**: Preprint.

### 5.2 NemotronLabs VoiceChat — Open Full-Duplex Speech-to-Speech with Tool Calling (2609.21967)
- **Title**: NemotronLabs VoiceChat: An Open Full-duplex Speech-to-Speech Model with Tool Calling Capabilities
- **Authors**: Jagadeesh Balam, Travis Bartley, Edresson Casanova, ..., Boris Ginsburg, ..., Yunsheng Liu, Shawn Wang, Wenjing Li, Zhonglei He (+47)
- **Institution**: NVIDIA (NemotronLabs)
- **Date**: Mon 21 Sep 2026 (cs.CL/cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.21967
- **Abstract**: Introduces an **open full-duplex speech-to-speech model with native tool-calling**. Combines streaming speech encoder + decoder-only LM with parallel specialized output streams for agent text and structured function calls, an auxiliary **RNN-T branch** for incremental user transcription, and a streaming TTS decoder — listen, transcribe, reason, invoke tools, and speak within one streaming architecture preserving the temporal behavior of natural conversation. On **Full-Duplex-Bench 1.0**: lowest pause-handling takeover among open-weight systems, 100% takeover following user interruptions, 4.33/5 post-interruption response quality; on FDB 1.5 resumes after backchannels in 93% of cases; VoiceBench 55.1 normalized average; **FDB 3.0: 82.5% tool-selection F1** (argument accuracy / e2e tool execution remain improvement areas).
- **Key Innovations**: (1) full-duplex conversation + native tool calling in a single open model; (2) streaming RNN-T transcription + TTS in one decoder-only stack; (3) strong interruption/backchannel behavior — SSoT agents become economically deployable.
- **Venue**: Preprint.

### 5.3 Samsone — Open Small Audio Language Models for On-Device Inference (2609.21666)
- **Title**: Samsone: A Family of Open Small Audio Language Models for On-Device Inference
- **Authors**: Piotr Masztalski, Michał K. Grzeszczyk, Olaf Sikorski
- **Institution**: — (Interspeech-accepted; tentative)
- **Date**: Mon 21 Sep 2026 (eess.AS/cs.AI); **Interspeech 2026**
- **arXiv**: https://arxiv.org/abs/2609.21666
- **Abstract**: SALMs for privacy-preserving, low-latency on-device execution. **Samsone-134M** sets a new SOTA for its size class across benchmarks; **Samsone-99M / Samsone-356M** probe SALM scaling laws. Compact footprint yet competitive with models orders of magnitude larger. Trained on public data; releases training code, weights, mobile-optimized checkpoints, and an open-source **Android app** demonstrating real-time on-device inference.
- **Key Innovations**: (1) SOTA SALM at 134M; (2) first small-model scaling-law evidence for audio LMs (99M/356M); (3) full open-stack mobile deployment incl. Android reference app.
- **Venue**: Interspeech 2026.

---

## 6 Games & Mechanism Design

### 6.1 Fair Prophets — α-Fair Prophet Inequalities (2609.21826)
- **Title**: Fair Prophets
- **Authors**: Paul Duetting, Michal Feldman, Mathieu Molina
- **Institution**: Google Research / Tel Aviv-aligned (Duetting/Feldman; tentative)
- **Date**: Mon 21 Sep 2026 (cs.GT/cs.DS)
- **arXiv**: https://arxiv.org/abs/2609.21826
- **Abstract**: Initiates the study of **α-fair prophet inequalities**, interpolating utilitarian welfare (α=0), Nash welfare (α=1), and Rawlsian max-min fairness (α→∞). It matters when expectation is applied: ex-ante (max min E[u_i]) vs ex-post (E[min u_i]). **Ex-ante**: full distributional knowledge → tight competitive ratio exactly **1/2 for every α≥0**; sample access: O(n log n) samples suffice for constant ratio when α∈(0,1], but **for every α>1 no finite samples beat the trivial 1/n** — full-information vs sample-access prophets become fundamentally separated. **Ex-post**: uniform constant ratio for all α∈(0,1); for α>1 ratio collapses to 1/n; one sample sufficess per fixed α<1 but no n-dependent sample budget gives a uniform guarantee as α→1. Opens prophet inequalities for non-linear welfare objectives.
- **Key Innovations**: (1) α-fairness spectrum (utilitarian→Nash→Rawlsian) for prophet inequalities; (2) ex-ante/ex-post distinction as a *provably* decisive modeling choice; (3) sharp sample-vs-full-information phase transitions (a clean separation absent in utilitarian setting), incl. the α>1 hardness.
- **Venue**: Preprint.

---

## Key Trends Across This Window (Unclaimed Remainder)

1. **MoE & inference cost are becoming a recommendation-production story** (21346 IntBMoE: full-participation + sparse execution, deployed in AMap generative rec with +2.4% UVCTR; 21058: recommenders expose 58.2% addressable kernel time vs ~1% for transformers — DLRM-Bench makes embedding kernels first-class targets): the "rec + efficient architecture" crossover the wiki tracks via CTR/sequential pages gains a rare industrial anchor.
2. **Reason-auditing matures from outcome to process** (21492 LogicTrack solvers verify each CoT step; 21208 verifier co-training with GT-anchored IG rewards; 21247 HMS taxonomy-free trace structure for MT; 20846 efficiency-regularized abstention — a human-resource-rationality-anchored post-training objective): "what the model *did*" replaces "what it concluded".
3. **Agent security moves to authorization & recoverability semantics** (21284 root-scoped quiescence for long-running agent revocation; 21686 CIPL recovery-channel framing; 21793 standardized 19×15 defense-combination study; 21484 encrypted-domain jailbreak guardrail): security guarantees are now expressed about *delegated state machines*, not prompts.
4. **Speech/audio agents reach deployable full-duplex economics** (21967 Nemotron VoiceChat: open full-duplex + tools, strong interruption handling; 21666 Samsone on-device 134M SALM + Android app): the "voice agent" trend now has open weights + tool calling + mobile checkpoints.
5. **Watermark/decoding rethink continues at the algorithm level** (21858 Poisson multi-draft speculative sampling that is watermarkable *without* acceptance loss; complements 09-21 RheoSampling): inference speed + provenance no longer need to trade.
6. **Mechanism design adds fairness phase transitions** (21826 Fair Prophets: ex-ante/ex-post + α-spectrum sample-access separations) — a games/econ result ready for auction/alloc theory cross-links.
7. **Ads/CTR again ~0 in the remainder** (9th+ consecutive window at the daily layer): classic end-to-end CTR-ML content appears only in conference batches (KDD/CIKM/WWW digests); the only CTR-adjacent production signal this window is IntBMoE's UVCTR A/B from the MoE angle.

## ADS / CTR Coherence Check

0 direct CTR/advertising papers in the unclaimed Mon-21 remainder (today's `arxiv-daily`-claimed OneBid 2609.21550 + ADAPT 2609.21308 were the window's ads entries). Closest this report gets: **IntBMoE's AMap UVCTR production lift** (+2.4% rel), DLRM-Bench (recommender-kernel evaluation), spectrally-aligned latent flow for sequential generation, and the Conformal/HE security threads applicable to ad-infra privacy. The classic end-to-end CTR-ML drought at the daily layer persists (conference-digest layer remains the CTR source).

## Cross-Reference Index (Sibling & Runner-Up Coordinates)

- Same-window siblings (09-21, first passes over Mon-21 window): `arxiv-daily` (49 claimed incl. OneBid 2609.21550, ADAPT 2609.21308, production rec/search, long-context serving, post-training RL, world-model/game, eval); `arxiv-ai-search` (21 featured + 6 runner-ups: agent memory/eval, attention primitives, tokenizers, speculative decoding, unlearning/steering, games, RAG/agent security); `game-rl-daily` (18 featured + 3 runner-ups: Game RL/MARL, world-model science, LLM-agent simulation); `conference-digest` (venue/KDD/RecSys/EMNLP digest content). The 28 curated IDs below are **disjoint from all of those sets** (shown by the 6,058-ID known set at build time + per-ID grep).
- Runner-ups this window (grep-verified 0 hits): **2609.21181** Implicit Rule Induction with Test-Time Task Embeddings in ARC (Embed-TTT two-step protocol, rule-vs-execution separation); **2609.21113** Decoupling Internal Representational Changes and Causal Importance in Fine-Tuned LLMs (EAP-located components vs representational-change layers uncorrelated; overlap → cross-task negative transfer); **2609.21841** EnterpriseVal — use-case-level GenAI evaluation for the enterprise (blinded expert + calibrated LLM-as-judge, two-tier threshold gate, bank pilot: citation precision 88%, hallucination 1.6%); **2609.22067** Value-Sensitive Delegation in Everyday AI Agent Use — 73,093 OpenClaw Reddit posts, values cluster at operating conditions not outputs; **2609.21857** Do Personality-Tuned LLMs Make Better Social Agents? (fine-tuning ≈ baseline for personality fidelity; low inter-rater agreement); **2609.22008** DiaVLo — diagnosing VLM behaviours via curated generation + causal concept attribution (EMNLP 2026 Findings).
- Sub-window map for future dedup: IDs **20823–21550** (daily claimed auto-bidding/rec/seq/serving), **21550–22068** (daily+ai-search claimed eval/post-training/game), **20825–22081** (this report's unclaimed remainder — where future same-window sweeps should look); window terminates at **2609.22086** (cs.CV new-sub max).