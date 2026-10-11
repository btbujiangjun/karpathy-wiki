---
title: arXiv Daily AI/LLM/RecSys/CTR/Games (2026-10-11)
type: synthesis
created: 2026-10-11
updated: 2026-10-11
sources: []
tags:
  - arxiv
  - ai
  - llm
  - recommendation
  - advertising
  - sequential-modeling
  - ctr
  - games
  - daily-digest
---

# arXiv Daily Report (2026-10-11)

Search scope: the arXiv export API's latest indexed announcement is still the **2026-10-08 (Thu) block** — queries for `submittedDate:[20261009 TO 20261012]` return zero entries, so no 2026-10-09/10/11 mailing is present. This run therefore re-harvests the wider window **2026-10-05 → 2026-10-08** with full category sweeps (`cs.AI`, `cs.LG`, `cs.CL`, `cs.IR`, `cs.GT`, `cs.MA`) plus 30 topical `all:` sweeps (recommendation, generic/sequential/generative rec, CTR, advertising/auctions, bandits, mechanism design, games, scaling, test-time, agents, GRPO, time-series). **1,330 unique papers** collected; **989 are new to the wiki** (grep-verified 0-hit against 8,517 repo-wide arXiv IDs). The **49 featured papers below are all new to the wiki**, drawn from the not-yet-reported tail of the window — the 2026-10-09 and 2026-10-10 digests had already claimed their own selections from the same block.

> ⚠️ Metadata note: the arXiv Atom API does **not** expose author affiliations. **Institution/company** is stated only where the abstract, comments, or code link name one; otherwise marked `not stated (arXiv metadata omits affiliations)`, with an author-list hint flagged `unconfirmed` where relevant. No HTTP 429/rate-limiting was observed on this run.

> ℹ️ Lane note: as in the two prior digests, the classical **CTR / ad-auction / recommender** lanes are effectively empty in this block — dedicated `abs:`-field sweeps for "click-through rate", `CTR`, "advertis*", "ad auction", "sponsored search", and "recommend*" surfaced no direct CTR/ads-serving paper. The closest material is personalization/memory (§4), retrieval/ranking (§5), and the auction/mechanism/fair-division theory in §7.

## Core AI / LLM / Agents

### 1. LLM-IDEA: Identifiability-Driven Experimental Agent for Autonomous Discovery of Mechanistic World Models
- **Authors**: Surya Shetty, Ulisses Braga-Neto
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI
- **Abstract**: LLM agents are increasingly deployed as autonomous scientists that design experiments and infer mechanistic world models, but **identifiability** is overlooked: on a plateau, the agent cannot tell whether it is under-powered or the model is simply unidentifiable from any such experiment.
- **Key innovations**: `LLM-IDEA` adds an **identifiability engine** returning a three-way plateau verdict — capability limit / resolvable-within-design-class / certified exhausted. On ODEBench, 60 of 62 free-constant systems are identifiable at round 0; a harvesting model is resolvable by one added initial condition; on DiscoverPhysics it finds two public worlds whose rubric rewards a distinction no legal experiment can make (every accurate-trajectory model there failed the explanation grade, 15/15 vs 5/9). On a proposed non-identifiable/identifiable "Alien Universe" testbed, it reaches discovery depth ≥3 on 8/8 seeds vs 1/8 without it.
- **arXiv**: https://arxiv.org/abs/2610.11253

### 2. TaReD: Tool-Aware Recursive Decomposition for Long-Horizon Tasks
- **Authors**: Wei-Xiang Mao, Zhi-Kai Chen, De-Chuan Zhan, Han-Jia Ye
- **Institution**: not stated (Nanjing University / LAMDA-adjacent author list; unconfirmed); code: github.com/WeiXiang-Mao/TaReD
- **Subjects**: cs.AI
- **Abstract**: Interleaving reasoning and actions along a single execution chain grows unreliable on complex tasks — long histories obscure intermediate dependencies and early planning errors propagate. Recursive decomposition helps, but decomposition must respect the system's actual tool capabilities, and large tool libraries cannot be exposed in full without blowing context.
- **Key innovations**: `TaReD` organizes tools by functional relationships into a **hierarchy of capabilities**; at execution time the agent discovers tools on demand and recursively decomposes the task into a subtask tree whose levels align with the capability required at each stage. Improves end-to-end task success by up to **40 points** over the compared baselines on complex real-world tasks.
- **arXiv**: https://arxiv.org/abs/2610.11268

### 3. SynCo: Data Synthesis Co-Training for Self-Evolving LLMs via Multi-Agent Reinforcement Learning
- **Authors**: Wei Yang, Shawn Li, Yuehan Qin, Yawei Wang, Mingxi Wang, Shixuan Li, Tiankai Yang, Jiate Li, Jesse Thomason, Xuezhe Ma, Yue Zhao
- **Institution**: not stated (USC-adjacent author list; unconfirmed)
- **Subjects**: cs.AI
- **Abstract**: Self-evolving LLM agents need to evolve not just the model but the **training experience** as capabilities change; static datasets or separately-updated synthesis models go stale, leaving previously useful tasks trivial and hard ones uninformative.
- **Key innovations**: `SynCo` co-trains two independently-parameterized agents with multi-agent RL — a **Synthesizer** that constructs tasks from the Reasoner's evolving capability state, and a **Reasoner** that learns from the resulting rollout outcomes. Multiple rollouts per task give complementary rewards to both agents (correctness → Reasoner; task quality, answer reliability, outcome-grounded teachability → Synthesizer); updates feed back into later synthesis rounds. Strongest overall performance across eight math-reasoning benchmarks, with most gains from previously unsolved problems.
- **arXiv**: https://arxiv.org/abs/2610.11345

### 4. Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks
- **Authors**: Haoyu Zhao, Zhengxu Yu, Zhiyuan He, Meng Fang, Rasul Tutunov, Haitham Bou-Ammar, Weilin Luo, Jun Wang
- **Institution**: not stated (UCL/Huawei-adjacent author list; unconfirmed)
- **Subjects**: cs.AI; cs.CL; cs.CV; cs.LG
- **Abstract**: In unfamiliar environments, limited observations support multiple world models that fit the past but predict different futures. Memento 3 lets a **frozen** LLM agent continually learn an explicit world model through external memory.
- **Key innovations**: The agent maintains a natural-language **rulebook** (persistent semantic memory of revisable dynamics hypotheses), compiles it into executable code for prediction/planning, and runs an observe → reflect → revise → compile → verify loop where updated code is accepted only if the LLM judges it faithful to the rulebook **and** cell-exact replay reproduces observed transitions. A population extension keeps multiple world models in parallel to share evidence. On **ARC-AGI-3** the single-model agent clears every level of all 25 public games at mean RHAE 100.0 using 44% of the human action count; an Atari Pong feedback controller wins 21:0 in three episodes without further LLM calls.
- **arXiv**: https://arxiv.org/abs/2610.11794

### 5. Use and Disuse: Intent-Structured Experience Consolidation for Memory and Learning in LLM Agents (Hippocam)
- **Authors**: Xiangyi Zeng, Baihang Liu, Xutong Wang, Ze Jin, Yunpeng Li, Qixu Liu
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI
- **Abstract**: Turning continuous experience into reusable knowledge is the central challenge for long-term autonomous agents. Existing memories either dump full working details or lose recoverable context.
- **Key innovations**: `Hippocam` structures ongoing work as **nested intents**: the active context centers on the current intent, while completed intents consolidate to the outcomes/state needed downstream. A **recursive prefix-consolidation** mechanism makes long-unused experiences progressively more abstract while preserving original interactions for progressive detail recovery; recalled experiences are re-consolidated alongside new ones (reinforced, supplemented, updated). Connects working context, long-term memory, knowledge accumulation, and skill learning in one evolving process **without parameter updates**.
- **arXiv**: https://arxiv.org/abs/2610.12124

### 6. MemTrial: Learning When to Trust Memory in LLM Portfolio Agents
- **Authors**: Guanghao Wu, Zhuo Cai, Shoujin Wang
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI
- **Abstract**: Portfolio LLM agents credit each memory entry with the outcome of decisions that used it, but in markets that outcome mostly reflects the shared market move — credit tracks the market, not the experience — so agents often underperform a naive equal-weight portfolio.
- **Key innovations**: `MemTrial` **puts memory on trial**: it drafts each decision with eight combinations of retrieved experiences (fractional factorial design) so the shared market outcome cancels in differences, and credits each experience with its **Banzhaf value**. Noisy per-date credits are pooled across dates/similar experiences with a hierarchical Bayesian model and acted on only after they predict unseen dates, otherwise anchoring at a conservative reference (1/N). Best of 15 methods on a semi-synthetic benchmark with known experience quality; loses at most 2.2% vs 1/N on PortBench/InvestorBench (vs 15–38% for the best experience-learning agent); +21.2% utility over the best experience-learning agent averaged over five settings.
- **arXiv**: https://arxiv.org/abs/2610.11732

### 7. ReTeach: Building a Self-Teacher through Multi-Round Reflection and Retry
- **Authors**: Yafeng Tang, Hao Li, Hongsheng Yu, Qiang Fu
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI
- **Abstract**: Self-distillation improves reasoning without a stronger teacher, but the self-teacher needs an advantage over the student; conditioning on reference answers is not always possible, and reflection-based methods often smuggle in reference info, rich feedback, or persistent memory.
- **Key innovations**: `ReTeach` builds its self-teacher using **only self-generated attempts and outcome-level verification** — starting from a failed rollout, the teacher alternates explicit reflection with renewed attempts until success or budget exhaustion; each failed retry informs the next reflection. An outcome-aware selection/weighting splits initially-correct, reflection-corrected, and unresolved examples. On-policy distillation matches the teacher's context-conditioned token distributions at prefixes of the student's own rollouts, transferring correction while keeping single-pass inference. +1.39 pts average accuracy over GRPO across six benchmarks (math, science QA, tool use).
- **arXiv**: https://arxiv.org/abs/2610.11529

### 8. Structure Tax: How Structured Output affects LLMs Performance
- **Authors**: Vineet Kumar, Kanishka, Bhuvanesh Mandora
- **Institution**: not stated; venue: AACL-IJCNLP 2026 (Main)
- **Subjects**: cs.AI
- **Abstract**: Production LLMs are often constrained to JSON/XML, and prior work treats the resulting accuracy loss as an inherent "structure tax". This paper re-examines that claim across models, datasets, and schemas.
- **Key innovations**: Shows the tax depends on **schema design, not structure per se** — **reasoning-first field ordering** matches or exceeds free-form accuracy while answer-first ordering causes steep drops (especially in smaller models). Format sensitivity scales inversely with a task's own structural constraints, and reasoning-preserving schemas also improve calibration (CKA shows greater separability between correct/incorrect representations in middle layers). Reframes the question from "whether to structure" to "how to structure".
- **arXiv**: https://arxiv.org/abs/2610.12056

### 9. Internalizer: Portable Context-to-Parameter Mapping for Very Large Language Models
- **Authors**: Peter Devine, Nick Ryan, Benjamin Sirb, Alex Chiocchi
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI; cs.CL; cs.LG
- **Abstract**: Hypernetworks that map a context directly to a LoRA adapter let a model carry that context in weights, but prior work demonstrated them only up to 14B parameters.
- **Key innovations**: `Internalizer` generates document-specific LoRA adapters for the **frozen 284B DeepSeek v4 Flash** — two orders of magnitude larger than prior work — with most parameters in a **model-agnostic trunk** and only thin per-model entry/exit layers, so it trains cheaply on small models then ports to the large one. On unseen ≤4096-token documents, generated adapters reach **84.9% top-1 / 97.8% top-5** teacher-forced accuracy (base: 63.4% / 83.5%) with only a three-word instruction in the context window; a trained hypernetwork turns any document into an adapter in one forward pass.
- **arXiv**: https://arxiv.org/abs/2610.11715

### 10. Language Models as AI Research World Models
- **Authors**: Zijun Wang, Zewen Liu, Minhua Lin, Zhaotian Weng, Zhan Shi, Bing He, Yisi Sang, Dakuo Wang, Benoit Dumoulin, Wei Jin, Yuyin Zhou, Cihang Xie, Hanqing Lu
- **Institution**: not stated (industry+academic author list; unconfirmed)
- **Subjects**: cs.CL
- **Abstract**: AI research agents propose experiments faster than they can execute them, making **outcome prediction** the bottleneck for recursive self-improvement under limited experimental budgets.
- **Key innovations**: Studies LMs as **Research World Models (RWMs)** predicting intervention outcomes, using **2,600+ experimental records across nine research environments** (pretraining, post-training, inference; >171,000 H100 GPU-hours). Research knowledge from real experiments improves unseen-intervention prediction within an environment (Spearman +0.27) and transfers across environments — pretraining experience from OLMo3/Marin/Nanochat reduces selection regret in Qwen3 by **78%**; under a fixed Autoresearch budget, in-env/cross-env knowledge raises best gain by 15.8%/11.6%. Gains from added research knowledge exceed those from changing models or raising reasoning effort across 13 RWM backbones.
- **arXiv**: https://arxiv.org/abs/2610.12235

### 11. Verdict Without the Rule: Diagnosing and Auditing Regulatory Rule Sensitivity in LLM Compliance Systems
- **Authors**: Saisab Sadhu, Aadit Sengupta, Vinay Kumar Sankarapu, Pratinav Seth
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI; cs.CL; cs.CY
- **Abstract**: LLM compliance systems are deployed on the assumption that the verdict depends on the regulatory rule supplied. Holding the case fixed, the paper deletes, swaps, or negates the governing rule and checks whether the verdict changes (OCS) or the model's internal compliance representation shifts (ICS-delta).
- **Key innovations**: Across five models and 20 regulatory/platform-policy domains, neither signal moves much — verdicts are often **invariant to substantial rule perturbations**, and a purpose-built guard model is the least rule-sensitive and least accurate of the five, barely above chance (51% vs 90–92% for general models). The effect reflects **easy cases**: where deleting the rule flips a previously-correct prediction, models do track it. Neither better prompting nor internal-representation intervention closes the gap — accuracy alone does not establish that a compliance verdict is grounded in the supplied rule.
- **arXiv**: https://arxiv.org/abs/2610.12313

### 12. Why machines will still not rule the world
- **Authors**: Jobst Landgrebe, Barry Smith
- **Institution**: not stated (book-companion; unconfirmed)
- **Subjects**: cs.AI
- **Abstract**: A response essay defending the book's thesis that AGI is mathematically impossible because intelligent human processes are complex systems whose behaviour cannot be captured by models we can generate. It examines and rejects the two standard counter-arguments.
- **Key innovations**: Rejects the theoretical counter-argument grounded in universal approximation + Church–Turing–Deutsch (arguing serious issues in the physicalist premise) and the empirical counter-argument grounded in rising benchmark scores (**training-data contamination, flawed test construction, strategic optimization**). Position paper; not an empirical result.
- **arXiv**: https://arxiv.org/abs/2610.11424

## Reasoning / RL / Post-Training / Test-Time Compute

### 13. Environmental Feedback Modeling Matters: Rethinking Feedback Treatment in Agentic Hindsight Self-Distillation (SELF)
- **Authors**: Hangxi Guo, Fengyuan Liu, Yue Wang, Yuhua Qi, Haoyi Xiong, Fei Sun, Mengnan Du
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI
- **Abstract**: RL trains language agents in interactive environments but cannot be applied when rewards are unavailable; recent work uses environmental feedback as privileged context for hindsight self-distillation, yet simply conditioning the teacher on feedback is insufficient.
- **Key innovations**: `SELF` **jointly optimizes environmental-feedback modeling and hindsight self-distillation**: it learns to predict environmental responses while distilling guidance from a feedback-conditioned self-teacher into the policy, with a mutually-reinforcing mechanism (feedback modeling strengthens hindsight supervision; self-distillation improves feedback modeling). With Qwen3-8B, +6.4/+4.1 pts over SDPO/GRPO on τ-bench success, +10.71/+3.57 pts over SDPO/GRPO on AppWorld goal completion.
- **arXiv**: https://arxiv.org/abs/2610.11384

### 14. AdaptEvo: Adaptive Agent Learning with Evolving Supervision
- **Authors**: Shijun Wan, Jiancong Xie, Hang Xu, Jin Duan, Qixiong Wang, Xi Xiang, Maofei Que, Yahui Liu, Zhongyu Wei, Mu Chuan
- **Institution**: not stated (industry author list; unconfirmed); 21 pages
- **Subjects**: cs.CL
- **Abstract**: Rule-governed contextual decision tasks require applying specified rules to case-specific context; written rules leave gaps, and reference judgments vary in how well the rules/evidence support them.
- **Key innovations**: `AdaptEvo` couples **Confidence-Adaptive GRPO (CA-GRPO)** — balancing outcome vs process rewards by reference confidence — with an **Evolution module** that synthesizes reusable decision knowledge from recurring failures and refines process rubrics. Introduces an industrial multimodal content-moderation dataset with In-Period and **Out-of-Period** (changed-rule) test sets. With Qwen3.6-35B-A3B: 61.9% exact-label / 72.2% binary accuracy In-Period (+7.5/+3.7 pts over GRPO); CA-GRPO retains exact-label gains Out-of-Period where GRPO declines.
- **arXiv**: https://arxiv.org/abs/2610.11354

### 15. Where to Adapt Matters: Layer-Selective Fine-Tuning for Capability Retention (LS-LoRA)
- **Authors**: Zhiqiang Pang, Zihong Sun, Qi Xie, Jun Shu, Deyu Meng, Zongben Xu
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI
- **Abstract**: PEFT adapts LLMs to specialized tasks but degrades general capabilities; existing fixes rely on data replay or regularization. This work instead asks **where** adaptation should be applied.
- **Key innovations**: Shows fine-tuning different Transformer layers yields different target gains and degradation, and that layer-wise **empirical Fisher information** (target sensitivity) is high in layers with **low input–output cosine similarity** — a lightweight, forward-only proxy to rank layers without backprop. `LS-LoRA` places trainable LoRA adapters only in low-similarity layers, improving target-task performance while retaining substantially more commonsense reasoning than all-layer LoRA.
- **arXiv**: https://arxiv.org/abs/2610.11620

### 16. SFT-as-Context Mitigates Forgetting in Supervised Fine-Tuning
- **Authors**: Kenan Tang, Andong Hua, Chengxuan Qian, Saket Tiwari, Yao Qin
- **Institution**: not stated (UCSB-adjacent author list; unconfirmed); 37 pages
- **Subjects**: cs.CL; cs.AI; cs.LG
- **Abstract**: SFT equips LLMs with specialized capabilities but often forgets the parent model's general ones, which is especially limiting for queries needing both.
- **Key innovations**: `SFT-as-context` is a **training-free** method: the parent model uses the SFT model's response as context to answer the query, acquiring the fine-tuned capability via in-context learning while preserving its own general capabilities. Across 19 parent–SFT pairs and 11 benchmarks it stays within ~2 pts of the SFT model on fine-tuned capabilities and ~2.2 pts of the parent on general capabilities, and solves queries requiring both even when neither model succeeds alone; also lets a small open SFT model improve a strong closed LLM. Includes a Bayesian error bound and attention analysis showing selective attention to useful SFT responses.
- **arXiv**: https://arxiv.org/abs/2610.11132

### 17. Overcoming Prior Barriers: Supervised Fine-Tuning under Long-Tail Distribution (PASS)
- **Authors**: Haohui Wang, Jiahao Xu, Wangzhi Zhan, Tong Zeng, Dongqi Fu, Hong Li, Swastik Roy, Naren Ramakrishnan, Chris North, Jian Kang, Yujun Yan, Dawei Zhou
- **Institution**: not stated (Virginia Tech-adjacent author list; unconfirmed)
- **Subjects**: cs.AI; cs.CL; cs.LG
- **Abstract**: Concepts required by a downstream task receive different pretrained support — frequent concepts are well learned, rare ones weakly represented. SFT treats them alike.
- **Key innovations**: Introduces the **prior barrier** — how strongly the pretrained model supports competing concepts over the target — and shows barriers follow a **long-tail distribution** (head concepts start easier, tail concepts need extra instructions). Derives a predictive risk bound relating prior barrier and accumulated SFT evidence, then proposes `PASS`, an **adaptive SFT instruction selection** method that constructs reference-derived concepts, estimates each instruction's distinguishing evidence, and allocates budget toward under-covered concepts. Beats seven SOTA instruction-selection methods across four backbone-budget settings.
- **arXiv**: https://arxiv.org/abs/2610.12345

### 18. Open-ended Scientific Discovery with Possibilistic Reasoning
- **Authors**: Anita Yang, Siu Lun Chau, Tomoya Wakayama, Krikamol Muandet, Masaki Adachi
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI
- **Abstract**: Autonomous LLM discovery must generate and test hypotheses adaptively as evidence accumulates while keeping statistical validity. Anytime-valid methods handle data-dependent hypotheses, but open-ended discovery has a deeper problem: the best discovered hypothesis may still be best of a bad lot, and even background knowledge (physical laws) may need revision.
- **Key innovations**: Formalizes **Abductive Autonomous Scientific Discovery (AASD)** using possibility theory; introduces **abductive utility** as a computable measure of discovery progress and **possibility frontier search**, the first algorithm for AASD, which maintains anytime validity and achieves ε-optimal abductive utility asymptotically under suitable conditions. Strong performance on synthetic and real scientific-discovery tasks.
- **arXiv**: https://arxiv.org/abs/2610.11289

### 19. Probing for Long-Horizon Deductive Reasoning Capabilities in Language Models with Prolog (ProloNg)
- **Authors**: Hadeel Al-Negheimish, Jasna Ilieva, Yoon Kim
- **Institution**: not stated; venue: Findings of EMNLP 2026
- **Subjects**: cs.CL
- **Abstract**: Frontier LLMs can process 1M-token contexts, but how far can they go beyond retrieval into deep reasoning over long contexts?
- **Key innovations**: Builds `ProloNg`, a synthetic testbed probing **Prolog long-horizon deductive reasoning**, systematically varying reasoning depth (hardest case: depth 22, 62k context). Evaluating 8 reasoning models across 5 frontier families, performance **degrades substantially with depth, with most models approaching chance beyond depth 10** — a clean negative result on long-horizon deductive reasoning.
- **arXiv**: https://arxiv.org/abs/2610.11592

### 20. LEVER: Adaptive Cost-Aware Proof Search Over AND/OR Graphs
- **Authors**: Nihal Jain, Shuangjie Yao, Begum Cicekdag, Zhuo Zhang, Suman Jana
- **Institution**: not stated (Columbia-adjacent author list; unconfirmed)
- **Subjects**: cs.AI
- **Abstract**: LLM theorem provers largely search for *any* correct proof and improve quality only afterward, whereas mathematicians care about simplicity, purity, and search cost. LEVER makes the objective over correct proofs programmable and optimizes it **during** search.
- **Key innovations**: Scores partial proofs over an **AND/OR proof graph**, combining realized objective values with predictions for open subgoals so the objective guides search before completion; the same mechanism optimizes search cost, proof length, topical impurity, or weighted combinations, with the Lean kernel enforcing correctness. On PutnamBench (Lean 4), under matched budgets it costs **34% less** than a strong single-conversation agent while raising solve rate **80%→96%**; improves topical-impurity reduction to 42% (vs 33% for post-hoc refactoring) and traces a tunable quality–cost curve.
- **arXiv**: https://arxiv.org/abs/2610.11862

### 21. PIVOT: Perplexity-Informed KD-to-RL Transition Scheduling for Vertical-Domain Few-Shot Distillation
- **Authors**: Heng Li, Yong Zhang, Ning Cheng, Zhigen Li, Yun Zhu, Yanmeng Wang, Shaojun Wang, Jing Xiao
- **Institution**: not stated; venue: Findings of EMNLP 2026
- **Subjects**: cs.LG; cs.AI
- **Abstract**: Vertical-domain few-shot classification is hard for small LMs. On-Policy Distillation (OPD) then GRPO can help, but existing KD→RL pipelines use **globally fixed transition schedules**, ignoring that samples need different amounts of teacher-guided acquisition.
- **Key innovations**: `PIVOT` routes samples between OPD and GRPO according to **teacher-evaluated sequence perplexity** — low-perplexity samples move to GRPO for reward-driven refinement, high-perplexity ones stay in OPD for continued domain-knowledge acquisition. Beats continued-OPD and globally-synchronized OPD→GRPO baselines under equal post-warm-up student steps on Banking77 and HWU64, with more stable training dynamics.
- **arXiv**: https://arxiv.org/abs/2610.11167

### 22. Cost-Efficient Theorem Proving via Agent Orchestration in Program Verification (CoCo-Prover)
- **Authors**: Shuangjie Yao, Nikolaus Holzer, Mark Paul Santolucito, Baishakhi Ray, Suman Jana, Dongdong She
- **Institution**: not stated (Columbia/Barnard-adjacent author list; unconfirmed)
- **Subjects**: cs.AI; cs.LO; cs.PL; cs.SE
- **Abstract**: Program verification yields machine-checkable proofs — valuable for LLM-generated code, which is fluent but unverified. Most provers chase pass rates at any budget and ignore the success-vs-cost frontier, yet real software carries hundreds of interdependent obligations where the question is how many theorems can be proved **economically**.
- **Key innovations**: `CoCo-Prover` formalizes cost-efficient proving as **metalevel decision-making under cost** over two-level proof graphs — an AND/OR proof hypergraph within each declaration joined to a lemma-dependency graph across declarations. At each step it picks which open goals to select (symbolic topological pass) and which actions to purchase (an **agentic router** treating every bounded specialist invocation as separately-priced best-effort computation, under rules evolved as evidence accrues). On five Lean 4 program-verification benchmarks (function-level CLEVER/VERINA/AlgoVeri; repository-level NTP4VC/Vero) it gives the best success-vs-cost frontier, best solve rate on every benchmark (up to **100%** on two), and up to **30.9% less cost** than the strongest baseline with the strongest LLM.
- **arXiv**: https://arxiv.org/abs/2610.09681

## Efficiency / Inference / Serving / Quantization

### 23. DADP: Dynamic Activity-Dependent Pruning, A Reverse Hebbian-Inspired Structural Pruning Method
- **Authors**: Bhushan Deshpande
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.LG
- **Abstract**: Modern networks are heavily over-parameterized, but existing pruning relies on post-hoc magnitude thresholds or static initialization heuristics, needing manual per-layer sparsity targets or expensive retraining.
- **Key innovations**: `DADP` is a biologically-inspired **structural plasticity** mechanism that, during training, measures connection importance via the **accumulated product of pre-synaptic activations and post-synaptic error gradients**, then uses a **single global threshold** instead of fixed per-layer budgets — dynamically allocating sparsity across depth and naturally inducing neuron- and channel-level pruning. Across MLP, VGG-16, ResNet-18, BiLSTM-CRF, and MiniBERT it matches/beats Magnitude, SNIP, and RigL, retaining **73.67% accuracy at 99% sparsity** on ResNet-18 (dense: 76.06%); Shannon-entropy/effective-rank measurements confirm preserved latent feature diversity without representation collapse.
- **arXiv**: https://arxiv.org/abs/2610.11853

### 24. Quantize by Drift: Label-Free Mixed-Precision Post-Training Quantization for Text Embedders
- **Authors**: Hyojung Han, Jongmin Kim, Seung-Hun Jeon
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.IR; cs.CL; cs.LG
- **Abstract**: Mixed-precision PTQ needs a per-module sensitivity signal, but for a text embedder the obvious one (retrieval-quality cost when a module is quantized) needs relevance labels deployments rarely have.
- **Key innovations**: Uses a **label-free substitute — quantization-induced representation drift** (quantize one module, re-encode the corpus, measure how far output embeddings moved), where the observable is the deployed output representation a dense retriever ranks with. Drift orders sampled mixed-precision plans against held-out retrieval quality at macro Spearman 0.911 and transports across corpora/domains; the method is a single additive allocation under a packed-byte budget with no labels and no search. Pre-registered test: beats a LieQ steelman in 2/3 held-out embedders, but is **numerically below same-budget uniform precision** on all three — output drift is a robust coarse sensitivity signal, not a universally optimal objective.
- **arXiv**: https://arxiv.org/abs/2610.09227

### 25. DivMoE: Fine-Grained MoE Upcycling via Cross-Domain Expert Composition
- **Authors**: Yuxuan Lou, Kai Yang, Geng Zhang, Yong Liu, Yang You
- **Institution**: not stated (NUS-adjacent author list; unconfirmed); venue: NeurIPS 2026
- **Subjects**: cs.AI; cs.LG
- **Abstract**: Fine-grained MoE upcycling from a pre-trained dense model is attractive but has a structural pathology: when fine-grained experts derive from a single source model, naive routing collapses and accuracy drops to near-random.
- **Key innovations**: `DivMoE` achieves fine-grained upcycling with **structurally-balanced routing** via (i) **domain-specialized fine-grained expert initialization** (experts from domain-continually-pretrained dense models) and (ii) **diversity-constrained routing** — a hard constraint that each token activates experts from distinct domain groups. On Qwen3-1.7B, 55.6% vs 51.6% for the strongest baseline (naive fine-grained collapses to 23.2%); strictly improves over the dense base on every benchmark after Stage-2 continual pretraining; a 12B DivMoE matches 16B Moonlight-MoE at 64.5% after SFT.
- **arXiv**: https://arxiv.org/abs/2610.11317

### 26. QUILT: Rethinking Sparse-Attention Prefill through Shared Query Execution
- **Authors**: Zhenduo Zhao, Qihui Zhou, Mingcong Song, Zhiyi Chen, Chuangguan Ye, Fengfan Hou, Zequn Gong, Jing Li, Hongjie Si, Guoping Long
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.LG
- **Abstract**: Sparse-attention kernels process queries independently, repeatedly loading and dequantizing KV entries shared across neighboring queries — even though neighboring queries select largely overlapping KV.
- **Key innovations**: `QUILT` jointly processes neighboring queries and reuses shared KV. `Shift-and-Compare Set Decomposition (SCSD)` transforms irregular set operations into regular data-parallel primitives and is pipelined with attention to hide overhead; **cascaded sharing** captures reuse hierarchically, and a tile-aware strategy balances sharing granularity with hardware utilization (dropping low-importance query-specific tails). On LongBench with GLM-5.3 and DeepSeek-3.2: up to **55.1% lower kernel latency**, 55.9% less processed KV, and up to 36.8% lower TTFT with negligible accuracy loss.
- **arXiv**: https://arxiv.org/abs/2610.11134

### 27. Deflating the Hessian: Rank-4 W4A4 Quantization for Multimodal Diffusion Transformers
- **Authors**: Shiwen Wang, Pengxiang Zhao, Xiaoming Yuan
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.LG; cs.CV; math.OC
- **Abstract**: Low-rank branches mitigate 4-bit weight–activation (W4A4) PTQ loss for diffusion transformers, but existing methods optimize low-rank compensation and residual quantization separately (higher ranks) or use second-order updates without modeling activation-quantization error.
- **Key innovations**: Models low-rank-assisted W4A4 PTQ as a **coupled calibration problem** with solvers from the joint objective. Eliminating the output-side low-rank factor yields a **deflated Hessian** that discounts residual error already captured by the low-rank part, and an activation-noise surrogate suppresses activation-quantization error. Rank-4 beats rank-4 SVDQuant across five diffusion backbones and **surpasses rank-32 SVDQuant** on SANA-1.6B/FLUX with 8× smaller rank and up to 6.25× faster quantization; on Qwen3-8B it lifts MMLU 61.50% → 68.17%.
- **arXiv**: https://arxiv.org/abs/2610.11315

### 28. When Lower Reconstruction Loss Hurts: Distributionally Robust Refinement for Low-Bit LLM Quantization (DRQ)
- **Authors**: Yanlong Zhao, Xiaoyuan Cheng, Huihang Liu, Baihua He, Xinyu Zhang, Harrison Bo Hua Zhu, Wenlong Chen, Li Zeng, Zhuo Sun
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI; cs.LG; stat.ML
- **Abstract**: Weight-only PTQ leans on reconstruction-loss minimization, but the weights minimizing that loss need not perform better on new tasks — lower calibration reconstruction loss can even degrade same-calibration performance once input activations shift.
- **Key innovations**: `DRQ` is a post-hoc refinement minimizing **worst-case reconstruction loss over a constrained set of input activation distributions**; it refines the integer codes within the existing quantization grid, keeping quantization parameters and inference operators unchanged (no inference overhead). Improves models quantized by six representative PTQ methods (AWQ, GPTQ, ParoQuant, …) across dense and MoE LLMs.
- **arXiv**: https://arxiv.org/abs/2610.11226

### 29. APEX: Speculate smarter, not deeper
- **Authors**: Manvi Jha, Zach Zhang, Zhichao Xu, Linbo Liu, Sai Muralidhar Jayanthi, Vinayak Arannil
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.CL; cs.LG
- **Abstract**: Speculative decoding's effectiveness depends on both the proposal mechanism and draft depth, but fixed configurations cannot respond to changing predictability, repetition, and acceptance, so deeper drafting can waste compute without proportional speedup.
- **Key innovations**: `APEX` is a learned controller with **request-level expert selection** (APEX-Router: EAGLE-3 vs n-gram vs draft model) and **block-level depth adaptation** (APEX-Depth). It models accepted draft length as **censored survival feedback**, learning position-wise rejection hazards, block execution costs, and an action utility balancing throughput, accepted progress, and wasted tokens — all while retaining the target model's verification. Integrated into vLLM with Qwen3-8B: up to **5.24×** speedup over AR decoding; APEX-B cuts wasted-token percentage by 41.0% vs fixed n-gram speculation at k=16.
- **arXiv**: https://arxiv.org/abs/2610.07780

## Memory / Personalization / Conversation (Recommendation-adjacent)

### 30. Gated Memory: Admission-Controlled Memory Formation for Conversational AI
- **Authors**: Preeti Saraswat, Divya Neelagiri, Ajay Manoj
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.CL; cs.AI; cs.IR; cs.LG
- **Abstract**: Personalized conversational AI relies on long-term memory that extracts facts from utterances into vector stores; retrieval, dedup, and lifecycle management have advanced, but the **formation stage** (the moment a fact is first written) has received almost no principled attention — and critical context (permanent attribute vs transient situation) is irreversibly lost once extraction produces a triple.
- **Key innovations**: `Gated Memory` interposes two checkpoints between conversation and storage: an **admission gate** that evaluates each candidate fact against the full utterance context before extraction, and a **conditional enrichment** stage grounding admitted facts through an entity-scope taxonomy with privacy constraints. Admitted content is decomposed into atomic facts, each categorized, provenance-tagged (stated vs inferred), scoped to applicability, and grounded in context time/place. On LoCoMo-10 it improves LLM-judge accuracy +2.6% relative over a strong baseline with identical retrieval/generation.
- **arXiv**: https://arxiv.org/abs/2610.11270

### 31. Event-Centric Memory with Query-Aware Graph Augmentation for Long-Term Conversational Agents (QGMem)
- **Authors**: Yichen Liu, Chunfeng Yuan, Haowei Liu, Wenjuan Li, Zefeng Lin, Bing Li, Xu Chen, Weiming Hu
- **Institution**: not stated (CASIA-adjacent author list; unconfirmed); submitted to IEEE TPAMI
- **Subjects**: cs.CL
- **Abstract**: Long-term conversational memory follows two paradigms — flat (lightweight but leaves event relations and state updates implicit) or graph-based (explicit but costly and noisy over long histories).
- **Key innovations**: `QGMem` organizes experience into **events**: long dialogues are converted into event-indexed atomic memory units, consolidated into dynamic memory traces retaining state trajectories and current states. On a query, hybrid retrieval gathers candidates and **query-aware reranking** activates the most relevant units as compact working memory, which is organized as a **local graph** (`graph token` + textual working memory) for conflict-aware reasoning. Consistent gains across six benchmarks on retrieval, multi-hop evidence composition, conflict resolution, and ultra-long dialogue reasoning at moderate cost.
- **arXiv**: https://arxiv.org/abs/2610.11920

### 32. When History Helps and Hurts: Selective History Use across Multimodal Turns (ReTurn)
- **Authors**: Shuoyang Sun, Kerui Gu, Hao Fang, Shaoli Huang, Bin Chen
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.CL
- **Abstract**: Reliable multimodal interaction depends on selective history use — an earlier question may stay relevant while its answer is outdated. Existing multi-turn evaluations rarely separate history-use demands from question difficulty.
- **Key innovations**: `ReTurn` is a benchmark of **7,000 base tasks** over visual and audio evidence with matched single-turn counterparts. Task-carrying history (Reconfirm/Reground) and evidence-carrying history (Retrieve/Rebind) each preserve target question/media/answer while varying agreement or competition. Across 13 omni-modal/VLM/audio-LM models, median open-ended accuracy falls from **93.7% (direct input) to 72.3% (in conversation)**; probes show high question recall can coexist with weak task application, and competing media can redirect answers away from historical targets. Supervised adaptation yields only partial gains.
- **arXiv**: https://arxiv.org/abs/2610.11948

### 33. UXBench Pro: Benchmarking Personalized User Experience in Multi-Turn Dialogue Interactions
- **Authors**: Mengze Hong, Zeyang Lei, Wenbo Shang, Xia Zeng, Xiying Zhao, Qi Zhu, Chen Jason Zhang, Di Jiang, Taiming Fu, Qiongyi Zhou, Qinghe Chang, Fubao Zhang, Chenxuan Ma, Minlong Peng, Jinfeng Huang, Zineng Zhou, Jindou Wu, Muge Qi, Sijun He, Xin Cui, Di Liang, Yuan Hua, Davey Chen
- **Institution**: not stated (major search/AI industry author list; unconfirmed)
- **Subjects**: cs.CL
- **Abstract**: Automated UX evaluation via binary preference prediction gives limited insight, and a single user-agnostic reward model ignores user heterogeneity.
- **Key innovations**: `UXBench Pro` provides **1,000 test instances** from real user interactions across 12 scenarios / 82 domains, each paired with a **FACTORS user profile** (seven interpretable behavioral facets). Introduces a **dual-perspective paradigm** — a personalized User Reward Model for third-person judgment plus **Sim4Eval**, a user simulator giving first-person multi-turn evaluation across four cognitive-state dimensions — and two meta-benchmarks (URMBench, USimBench) validating evaluator fidelity. Seven key findings motivate user-centric benchmarking and personalized optimization.
- **arXiv**: https://arxiv.org/abs/2610.11638

## Information Retrieval / Retrieval / Ranking

### 34. RECAST: Learning to Compute the Right Context through Adaptive Evidence Routing
- **Authors**: Yilun Hao, Krishna Sayana, Isabella Ye, James S Ren, Sukhdeep Sodhi, Craig Boutilier, Chuchu Fan
- **Institution**: not stated (MIT/Google-adjacent author list; unconfirmed)
- **Subjects**: cs.AI
- **Abstract**: RAG relies on fixed similarity-based retrieval, and agentic variants adapt queries/tools but stay retrieval-centric — yet much required evidence is **not present in any single source** and must be *derived* by filtering, aggregation, or computation across items.
- **Key innovations**: `RECAST` (Routing Evidence through Computation, Access, and Synthesized Tools) formulates **evidence construction as a sequential decision process** over heterogeneous retrieval + computation operations. A lightweight **RouterLM** iteratively selects/formulates primitive operations or specifies custom ones for a frozen **CompilerLM** to translate into executable code; once evidence is judged sufficient it is passed to a frozen **AnswerLM**. Trained with SFT then GRPO, RECAST reaches **75.6% mean success** across six benchmark families, **+15.9%** over the strongest large-model baseline; a trained Qwen3.5-9B router beats a training-free Gemini 3.5 Flash router by 5.0%, and +15.0% average on three held-out benchmarks.
- **arXiv**: https://arxiv.org/abs/2610.10507

### 35. RIT-RAG: Navigating Document Corpora with Retrieval-Induced Trees
- **Authors**: Meghanadh Pulivarthi, Swaraj Kumar Biswal, Kushagra Bhushan, Yatin Nandwani, Sachindra Joshi, Dinesh Raghu
- **Institution**: not stated (IBM Research-adjacent author list; unconfirmed)
- **Subjects**: cs.AI; cs.IR
- **Abstract**: Agentic RAG enables iterative search but exposes isolated chunks without document structure, making it hard to distinguish relevant evidence from chunks that merely resemble the query; structure-aware methods like PageIndex cannot scale to large corpora (they commit to one document and cannot recover from a wrong choice).
- **Key innovations**: `RIT-RAG` combines content retrieval with structural navigation: offline it builds a per-document tree from the table of contents or sitemap; at query time it retrieves a broad set of chunks and uses their positions to **induce manageable sub-trees, potentially across multiple documents**, which an LLM agent navigates — retrieval proposes *where to look*, the agent decides *what to read*. Highest answer accuracy across financial/scientific/customer-support benchmarks; on **EntQABench** (new, 2.84M technical-documentation pages) it improves accuracy by **6.8–11.4 points** over the strongest baseline across three LLMs.
- **arXiv**: https://arxiv.org/abs/2610.11370

### 36. Finding the Right Balance: Relevance and Diversity in LLM Retrieval
- **Authors**: Guillaume Brouillette, Faustin Kagabo, Usef Faghihi, Nadia Ghazzali
- **Institution**: not stated (arXiv metadata omits affiliations); code: github.com/GuillaumeBrouillette/finding-the-right-balance
- **Subjects**: cs.IR; cs.CL
- **Abstract**: Retrieval diversification is widely available in RAG frameworks, yet prior studies disagree on whether it helps. This work shows its effectiveness varies with **candidate-pool redundancy**, consistent with the number of distinct evidence pieces a query requires.
- **Key innovations**: Using controlled near-duplicate injection and production-style overlapping chunking, finds diversification **harms** relevance/coverage/answer quality on clean pools but **helps** multi-evidence tasks where redundancy makes nearest-neighbor retrieval return repeated passages. Proposes a **query-adaptive rule**: diversify only when the effective number of distinct documents in the top-k falls below the query's evidence requirement, computed from existing embeddings. Also introduces `RNG-Score`, a geometric reranker with nearest-neighbor fallback whose margin indicates duplicate structure.
- **arXiv**: https://arxiv.org/abs/2610.09412

### 37. RAGFlip: Measuring Query-Level Negative Flips in Retriever Upgrades
- **Authors**: Elyas Irankhah, Muhammad Arif
- **Institution**: not stated (arXiv metadata omits affiliations); code: github.com/Elyasirankhah/RAGFlip
- **Subjects**: cs.IR
- **Abstract**: Retriever upgrades are usually evaluated with aggregate metrics, which hide regressions on queries the previous retriever already served correctly.
- **Key innovations**: Studies these regressions as **negative flips** — queries where BM25 retrieved a judged-relevant passage and the replacement does not. Evaluates BGE-large, E5-large-v2, and SPLADE on NQ/HotpotQA/FiQA across five depths; all replacements improve overall coverage, yet negative flips occur everywhere — at k=1, **8.6–37.5% of BM25 successes are lost**; requiring all positive qrels raises HotpotQA@10 flips to 12.3–17.3%. Simple fixed-budget BM25 combinations reduce regressions. Motivates query-level compatibility alongside aggregate quality when evaluating retriever updates.
- **arXiv**: https://arxiv.org/abs/2610.07266

## Sequential Modeling / Time Series

### 38. SteerCast: Retrieval-Based Latent Steering for Decoder-Only Time Series Forecasting
- **Authors**: Van Dai Do, Huu Hiep Nguyen, Minh Hoang Nguyen, Hung Le
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.LG
- **Abstract**: A retrieval-based latent steering method improves decoder-only forecasters at inference time **without updating parameters**.
- **Key innovations**: `SteerCast` builds a database storing each training history window's representation together with a **steering vector** in the forecaster's latent space — the difference between representations induced by the ground-truth continuation and by the model's own prediction. At test time it retrieves nearest neighbors for a query history, aggregates their steering vectors, and injects the signal into hidden states at every autoregressive step, steering predictions toward trajectories consistent with similar training cases. Consistently improves accuracy across multivariate benchmarks/horizons over the fine-tuned backbone and retrieval baselines, using only the training set and no extra training.
- **arXiv**: https://arxiv.org/abs/2610.11229

### 39. CARE: A Lightweight Plug-in Gated Correction and Uncertainty-aware Module for Long-term Time Series Forecasting
- **Authors**: Guo Cheng, Changlong Lv, Jingyi Hou
- **Institution**: not stated (arXiv metadata omits affiliations); code: github.com/CG-BNYC/CARE
- **Subjects**: cs.LG
- **Abstract**: Deterministic long-horizon forecasters emit a single trajectory, masking heterogeneous difficulty across horizons/channels and offering no localized reliability signal.
- **Key innovations**: `CARE` is a **lightweight plug-in** operating in parallel with any deterministic forecaster: it resamples historical context to match the forecast horizon, learns residual-correction patterns from this aligned history, and applies **scale-aware bounded updates modulated by per-coordinate sigmoid risk gates**. A multi-objective loss jointly optimizes forecast accuracy, residual tracking, risk alignment, and base-model anchoring. Across eight benchmarks and three backbones it improves accuracy at marginal cost and — on Weather — the highest-risk-gate tertile shows ~4× the error of the lowest, giving planners an interpretable per-step trust signal.
- **arXiv**: https://arxiv.org/abs/2610.11165

### 40. SACQ: Structured Decoding with Memory-Conditioned Refinement for Long-Horizon Forecasting
- **Authors**: Guo Cheng, Zhengzhuo Xu, Chenchen Jing, Jingyi Hou
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.LG
- **Abstract**: LTSF models use patch encoders with a flatten readout that maps the whole encoded memory to all future steps through one shared projection, implicitly coupling future positions and amplifying sensitivity to corrupted inputs / noisy labels.
- **Key innovations**: `SACQ` is a **plug-in structured prediction head** replacing flatten readout while keeping the encoder: it first establishes a coarse patch-grid forecast scaffold, then refines each future position by cross-attention over historical memory, merging the attention correction with the scaffold via a learned per-patch gate. A **batch-adaptive scaled log-cosh loss** calibrates robustness to the current residual scale. Top-tier MSE/MAE across PatchTST, DLinear, and patch-Mamba backbones, and substantially more robust under input corruption and label-noise stress tests.
- **arXiv**: https://arxiv.org/abs/2610.11170

### 41. Temporal Predictive Multiplicity: Equally Accurate Time Series Models Yield Different Forecast Trajectories
- **Authors**: Emanuele Albini, Francesca Toni, Saumitra Mishra, Francesco Leofante
- **Institution**: not stated (Imperial College London-adjacent author list; unconfirmed)
- **Subjects**: cs.LG; cs.AI
- **Abstract**: Models with near-identical predictive performance can yield substantially different predictions (predictive multiplicity), but prior work studied this for individual scalar outputs. In forecasting, predictions across horizons jointly define a **trajectory**, and horizon-wise comparison hides differences.
- **Key innovations**: Introduces **temporal predictive multiplicity** — disagreement over **complete forecast trajectories** among models with near-identical performance. Shows that constraining predictive performance alone still admits a broad range of trajectories, and that constraining horizon-wise multiplicity only **partially** reduces trajectory-level multiplicity. Experiments with **19 neural forecasting architectures on 11 datasets** confirm near-optimal models produce substantially variable trajectories, and trajectory-level disagreement is **largely unrelated to horizon-wise disagreement** — a gap with consequential downstream effects.
- **arXiv**: https://arxiv.org/abs/2610.09994

### 42. Training on the Future: A Delay-Aware Audit of Test-Time Adaptation for Time-Series Forecasting
- **Authors**: Mohamed Readh Fentazi, Mazene Ameur, Adlen Ksentini
- **Institution**: not stated (arXiv metadata omits affiliations); code: github.com/Xodios/... (full repo linked in paper)
- **Subjects**: cs.LG
- **Abstract**: TTA for forecasting updates a deployed model from incoming ground truth, but an H-step forecast's label exists only H steps later and real pipelines add further delay — prior TTA evaluations can leak the future.
- **Key innovations**: Builds a **leakage-free harness** releasing forecast-origin labels only at step s+d with d ≥ H, and enforces it inside the released code of four recent TTA methods (TAFAS, COSA, PETSA, DynaTTA) across five benchmarks. Under causal delayed labels the picture is asymmetric: on ETTm1 all audited methods adapt but a hyperparameter-free **RLS filter bank** beats three of four at a fraction of cost; on the other datasets the largest significant gain over a frozen checkpoint is 0.5%, and longer delays make adapters harmful on drift-heavy ETTh2. **Leaky next-step updates inflate apparent gains by up to 110%**, and the backbone training recipe moves frozen error by up to 25×.
- **arXiv**: https://arxiv.org/abs/2610.12232

## Auctions / Mechanism Design / Games / Fair Allocation

*Lane note: no game-playing/board-game RL paper appeared in the window; the nearest content is auction/mechanism/fair-division theory (the layer under ad delivery and marketplace pricing) plus two LLM-agent-commerce/game-theoretic decoding items.*

### 43. Optimal Regret for Online Market Making with Limit Order Book
- **Authors**: Maria Elena Vischi, Francesco Emanuele Stradi, Alberto Marchesi
- **Institution**: not stated (Politecnico di Milano-adjacent author list; unconfirmed)
- **Subjects**: cs.GT; cs.LG
- **Abstract**: In online market making a maker posts bid/ask prices before observing the market price and the incoming trader's private valuation, revealed (in the limit-order-book feedback model) only if no transaction occurs.
- **Key innovations**: Under i.i.d. trader valuations and adversarial market prices, improves the prior expected-regret bound of Õ(T^{2/3}) to a **high-probability Õ(√T)**. The algorithm discretizes the bid-ask space with **two coupled grids** combined with Hedge (warm-up: full feedback; then the weaker LOB feedback). Also shows sublinear regret is **impossible** in fully adversarial environments even under full feedback, motivating the stochastic-valuation assumption.
- **arXiv**: https://arxiv.org/abs/2610.09691

### 44. Online Fair Division under Eligibility Constraints
- **Authors**: Joes Biburger, Nicole Megow, Golnoosh Shahkarami
- **Institution**: not stated (University of Bremen-adjacent author list; unconfirmed)
- **Subjects**: cs.GT
- **Abstract**: Fair division of indivisible items where each item may go only to a subset of eligible agents — equivalent to restricted assignment in scheduling. Eligibility makes standard fairness benchmarks inadequate, so the paper uses eligibility-aware proportionality and envy-freeness.
- **Key innovations**: Proves a sharp **chore–goods separation for proportionality** under identical valuations: no online algorithm beats an o(m) approximation for chores; for chores the optimal online Prop1 approximation is Θ(√m) (lower bound even for unit-size jobs), while for goods it drops to Θ(log m). For envy, goods and chores are equivalent under eligibility-aware notions but the choice of notion is decisive: strong EF1 may fail to exist even offline, while weak EF1 is maintainable online and weak EFX separates offline from online.
- **arXiv**: https://arxiv.org/abs/2610.08064

### 45. Envy-free Allocations with Individual Payments
- **Authors**: Robert Bredereck, Eva Deltl, Tanmay Inamdar, Pallavi Jain, Pranjal Pandey
- **Institution**: not stated (TU Berlin/University of Glasgow-adjacent author list; unconfirmed)
- **Subjects**: cs.GT; cs.DS
- **Abstract**: When an envy-free allocation of indivisible goods does not exist, monetary transfers can restore it, but prior work assumes subsidies come from an external source. This paper allows only transfers **between agents**, each constrained by an individual budget.
- **Key innovations**: Verifying whether a given allocation can be made envy-free by budget-constrained payments is **polynomial-time tractable**, but computing such an allocation from scratch is **NP-hard even with large budgets**. A parameterized-complexity analysis gives FPT (in number of goods, or agents + good types) and efficient special-case algorithms; a type-based algorithm settles the envy-freeness part of an open question of T. T. Nguyen and J. Rothe.
- **arXiv**: https://arxiv.org/abs/2610.09610

### 46. Support-Dependent Regret Rates for Profit Maximization in Multilateral Trade
- **Authors**: Francesco Bacchiocchi, Matteo Castiglioni, Anna Lunghi, Alberto Marchesi
- **Institution**: not stated (Politecnico di Milano-adjacent author list; unconfirmed)
- **Subjects**: cs.GT
- **Abstract**: Online profit maximization in multilateral trade generalizes dynamic pricing and bilateral trade: an intermediary posts prices to buyers and payments to sellers, and trade occurs only if every agent accepts.
- **Key innovations**: With valuations from an unknown joint distribution (arbitrary correlation) where each marginal has support of size ≤ K, designs an algorithm with regret **Õ(√(K^d T))** for constant dimension d — extending optimal support-dependent guarantees from 1-D dynamic pricing to multidimensional multilateral trade. Core ingredient: a **normalized zooming procedure** adapting to the local probability of trade, avoiding excessive refinement of nearly flat regions.
- **arXiv**: https://arxiv.org/abs/2610.08611

### 47. A Constant-Factor Approximation to Multidimensional Consumer Utility
- **Authors**: Kira Goldner, Taylor Lundy, Thodoris Tsilivis
- **Institution**: not stated (Boston University/UBC-adjacent author list; unconfirmed)
- **Subjects**: cs.GT
- **Abstract**: Motivated by social services where consumers pay with non-transferable "ordeals", the paper studies mechanisms maximizing **consumer utility** for multiple unit-demand buyers and heterogeneous items with independent known priors — prior work only had a logarithmic gap between optimal utility and social welfare.
- **Key innovations**: Resolves whether simple mechanisms can get a **constant-factor approximation to optimal utility itself**: gives a **(5.67+ε)-approximation** for general independent values, improving to **2e/(e−1) < 3.164** for i.i.d. values. Each buyer chooses between posted item prices and free item lotteries, with contention resolution deciding service; the mechanism is BIC, ex-post IR, and polynomial-time. The key technical tool is a general upper bound on optimal ex-ante-constrained utility separating posted-price and lottery contributions.
- **arXiv**: https://arxiv.org/abs/2610.10516

### 48. Parallelism or Concession? Concurrency-Aware Procurement Negotiation for Agentic Commerce (CANO)
- **Authors**: Xiaolin Xu, Donghao Zhu
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.GT; cs.AI; cs.MA
- **Abstract**: Agentic buyers can cheaply fork a procurement task into many parallel negotiations, but concurrency is not free — each thread consumes resources and simultaneous agreements create cancellation/commitment risk. The paper studies a one-unit post-order sourcing problem with a single hard-deadline negotiation window.
- **Key innovations**: Models joint choice of **number of seller-facing negotiators** and a **common procurement price cap** (acceptance curve + fulfillment loss + per-thread cost + excess-commitment cost), proving three structural results: geometric marginal value of an extra negotiator (conditional concurrency threshold); **parallelism substitutes for concession** under a convex quantile curve; and dispersed prices reward harder bargains but punish price-raising guarantees. Operationalized as `CANO`, a deterministic concurrency+price-cap optimizer that beats common heuristics across analytic and Monte-Carlo/finite-data/correlated-seller stress tests. Relevant to agentic commerce / ad-market negotiation.
- **arXiv**: https://arxiv.org/abs/2610.06017

### 49. Nash Equilibrium Text: A Game-Theoretic Decoding Framework for Text Generation
- **Authors**: Alireza Jafari, Arman Adibi, Mohammad Ghavamzadeh, Hadi Daneshmand
- **Institution**: not stated (arXiv metadata omits affiliations); code: github.com/alireza-jafari/Nash-Decoding
- **Subjects**: cs.AI; cs.CL
- **Abstract**: Reframes text revision as a game that admits a **Nash equilibrium**: token positions are players, vocabulary items are actions, and each player's utility is the LM's log conditional probability.
- **Key innovations**: Shows Nash equilibria can have **exponentially higher likelihood than autoregressive outputs** as sequence length grows, and proposes `Nash decoding`, which reaches an ε-Nash equilibrium in **O(1/ε)** time given the joint token-conditional probability. Run with conditional-probability estimates from LMs, on CLAPNQ/PubMedQA/CoQA the resulting equilibria from masked LMs achieve higher F1 and ROUGE than autoregressive models **up to 18× larger**, with no fine-tuning or retraining, at extra test-time computation.
- **arXiv**: https://arxiv.org/abs/2610.05817

## Notes
- **Harvest window**: latest API-indexed announcement = **2026-10-08** (no 10-09/10/11 mailing present); category + topical sweep over **2026-10-05 → 2026-10-08** → 1,330 unique papers, **1,059 new to the wiki** (0-hit against 7,181 repo-wide arXiv IDs). **49 featured, all new to the wiki.**
- **CTR/ads-rec lane empty**: dedicated click-through/advertis*/ad-auction/sponsored-search/recommend* sweeps returned no direct CTR or ads-serving paper in this block — disclosed, not omitted; the nearest material is in §4 (personalization/memory), §5 (retrieval/ranking), and §7 (auction/mechanism theory).
- **Affiliations**: arXiv metadata omits them; only where an abstract/comment/code link names one is an institution shown, else `not stated` with `unconfirmed` author-list hints. No result independently replicated; venue tags are self-reported (NeurIPS 2025/2026, EMNLP 2026 Findings, AACL-IJCNLP 2026, IEEE TPAMI submission).
