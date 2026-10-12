---
title: "arXiv Paper Check — AI & CTR (October 12, 2026)"
type: synthesis
created: 2026-10-12
updated: 2026-10-12
sources: []
tags: [arxiv, arxiv-paper-check, daily-check, ai, ctr, recommendation, ads, ir, retrieval, memory, generative-recommendation, reasoning-rl, on-policy-distillation, agents, interpretability, safety, efficiency, state-space-models, daily-digest]
---

# arXiv Paper Check — AI & CTR (October 12, 2026)

**Search**: arXiv export API over HTTPS. Category sweeps (`cat:cs.AI`, `cat:cs.IR`, `cat:cs.LG`, 100 entries each, `sortBy=submittedDate desc`) plus topical `all:` passes (`"click-through rate"`, `"ctr prediction"`). The newest available block at run time is **2026-10-09** (Friday submission wave); the whole block is 187 `cs.AI` + 100 `cs.IR` + 100 `cs.LG` entries, of which the Oct-09 dated set is what is reported here.

⚠️ **Window framing, stated up front**: arXiv does not expose a rolling "last 24 hours". The newest block available at run time (2026-10-12 ~02:20 UTC) is the **2026-10-09 single-day block** — the previous `arxiv-paper-check` ([2026-10-10](synthesis/2026-10-10/arxiv-paper-check.md)) covered the 2026-10-08 block. This report therefore covers the **Oct-09 wave**, not a sliding 24 h.

⚠️ **CTR lane is back (barely).** The 2026-10-10 report recorded the **first fully-zero CTR yield** of the series. This block returns **one genuine CTR paper** (`2610.13066`, CTR-driven advertising image editing) plus a production recommender-systems paper (`2610.13806`, feature deprecation) and one generative-recommendation paper (`2610.12977`). LinkedIn/Meta/Kuaishou-scale CTR *architecture* (scaling laws, long-sequence modeling) is again absent.

**Dedup**: every featured ID was grep-verified **0-hit** against the entire `wiki/` tree immediately before writing (`rg -l -F "<id>" wiki/`). The only Oct-08 candidates seen in the sweeps that were already claimed by earlier digests (`2610.12300` learned-sparse indexes, `2610.11666` Autoregressive Retriever, each 5 wiki hits) were **excluded**.

**Scope note**: affiliations are **not** reliably available from the arXiv API metadata and were **not extracted this run — no affiliation is inferred**. Venue tags are only those self-reported via `comment`.

---

## ① CTR, Advertising & Recommendation (3)

### Evolving Creatives with Clicks (ECC): CTR-Driven Advertising Image Editing via Attribute Disentanglement and Preference Alignment
- **Authors**: Xu Zhang, Haohan Wang, Zheng Zhang, Yingjie Xia, Wei Feng, Honghe Zhu, Jingjing Lv, Changping Peng, Xuheng Qin, Zehua Zhang, Zheng Luo, Qicheng Li
- **arXiv**: [2610.13066](https://arxiv.org/abs/2610.13066) — cs.CV, cs.AI
- **Key contribution**: Reframes ad-creative optimization from whole-image *generation* to **fine-grained editing**: methods that build CTR reward and refine prompts via RL penalize *all* attributes of an underperforming image, even click-beneficial ones. ECC identifies **28 attributes significantly correlated with CTR** (ANOVA + Random Forest), instruction-tunes a prompt model to emit editing suggestions from attribute contrasts between high/low-CTR images, then refines it with **real click preferences**. Introduces **Consistent Preference Optimization (CPO)** — enforce consistency across semantically equivalent shuffled suggestions to reduce DPO overfitting — with an external (likely online/offline) evaluation of ad performance.
- **Why it matters**: The CTR signal is used as a **fine-grained causal-ish attribution** over creative attributes rather than a scalar reward — the ads-side counterpart to the wiki's feature-attribution / [[est]]-style efficiency themes.

### FORTE: A Production Framework for Feature Evaluation and Deprecation in Industrial Recommender Systems
- **Authors**: Vishnu Arun, Adam Obeng, Tianyou Wang, Zilin Ren, Mukuntha Narayanan Sundararaman, Han Wang, Shivin Thukral, Zhixiang Wang, Saurabh Vishwas Joshi, Darren Reger
- **arXiv**: [2610.13806](https://arxiv.org/abs/2610.13806) — cs.LG, cs.AI
- **Key contribution**: Names the **feature-lifecycle asymmetry** of production recsys — *adding* a feature must gain on some metric, but *removing* one must not regress *any* metric — and why deprecation is hard to prioritize (feature interactions, daily importance drift, A/B-test contention, multi-model consumers). FORTE is a model-agnostic framework with an **efficient perturbation implementation for daily feature evaluation**, **grouped ablation** over low-rank features to handle interactions, **lineage tracing** to find every downstream consumer, and offline results predictive enough of online A/B to green-light deprecations. Validated on **2 large-scale recommender systems**.
- **Why it matters**: The wiki tracks the *scale-up* side of industrial ranking; this is the rarely-published *tear-down* side — feature deprecation as a measurable cost-reduction program. Complements the CTR/rec scaling thread ([[understanding-scaling-laws-rec]], [[est]]).

### Beyond Semantic IDs: Finite-Beam Reachability and Continuous-Query Generation in Generative Recommendation
- **Authors**: Yu Sun, Renkai Xiang, Zuodong Xiang, Junwei Zhou, Yike Zhang, Jianxin Zhang, Zhihao Zhu, Xiaoyu Cao, Hailu Xu
- **arXiv**: [2610.12977](https://arxiv.org/abs/2610.12977) — cs.AI
- **Key contribution**: Diagnoses a **reachability constraint** in Semantic-ID (SID) generative recommendation: autoregressive decoding of discrete SIDs under **finite-width beam search** can render held-out targets *unreachable in the returned list* regardless of model quality. Proposes two **continuous-query** paradigms — **CQG-Single** (one retrieval query, single pass) and **CQG-AR** (autoregressive continuous residual updates) — removing the SID item-token vocabulary, code lookup, and discrete beam expansion so **every encoded item is directly scoreable** via dense/ANN retrieval. CQG-Single beats a TIGER-style baseline in **all seven runs** at **55.3%** of the trainable parameters.
- **Why it matters**: Attacks the interface, not the model — a "the output vocabulary is the ceiling" result for the generative-recommendation line (cf. [[hstu-generative-recommendation]], [[ge4rec-generative-ctr]]).

### AI-Mediation in Retail Markets: Revenue Effects and Assortment Optimization
- **Authors**: Omar El Housni, Marouane Ibn Brahim
- **arXiv**: [2610.12917](https://arxiv.org/abs/2610.12917) — cs.AI, econ.GN, math.OC
- **Key contribution**: Models assortment planning when an **AI shopping intermediary** forms a customer-facing shortlist (deterministic segment ranking, or stochastic Plackett-Luce) and customers choose via multinomial logit. Builds a dataset of **product rankings from leading AI models**, fits Plackett-Luce models, and shows that **ignoring AI mediation** costs **2.52%–11.37%** mean revenue at optimum, while a **simple deterministic plug-in using the fitted AI-utility ordering** loses at most **0.53%**. For deterministic mediation, characterizes complexity and gives an **FPTAS** for any fixed number of segments.
- **Why it matters**: Makes the LLM-as-recommender-intermediary channel an *assortment-optimization* problem with revenue bounds — an economics framing of the "AI mediates discovery" shift the wiki tracks via [[byoai]] / [[build-for-agents]].

---

## ② IR, Retrieval & Memory (3)

### Can Language Models Play the Wikipedia Game?
- **Authors**: Alexander Hickey, Joanna Knight, James Bishop
- **arXiv**: [2610.13948](https://arxiv.org/abs/2610.13948) — cs.AI, cs.IR
- **Key contribution**: Uses the **Wikipedia Game** (reach a target article using only links) as a controlled information-retrieval task. Compares sentence-embedding models and LLMs across **five Wikipedia languages** and **five academic-literature datasets**, building **local graphs of Wikipedia pages and OpenAlex paper citations** (no third-party APIs). Benchmarks against **human and TF-IDF** navigators: **no model significantly outperforms humans**, though the best (GPT-o3 mini, GPT-4o, QwQ:32B, DeepSeek-R1:70B) are comparable; rankings vary by language/topic.
- **Why it matters**: A rare *human-anchored* IR benchmark with an offline, reproducible graph harness — the navigation analogue of the benchmark-validity arc in [[dimensionality-barrier-retrieval]] and recent agentic-search audits.

### RATED: Reliability-Aware AI Agent Tool Retrieval via Execution Dynamics
- **Authors**: Weiliang Chen, Song Liao
- **arXiv**: [2610.13889](https://arxiv.org/abs/2610.13889) — cs.AI, cs.IR
- **Key contribution**: Existing tool retrieval optimizes **semantic relevance** and ignores **runtime availability**. RATED pairs a **frozen dual-encoder** (contrastive fine-tuned) for semantics with a **lightweight contextual bandit** that re-ranks by real-time execution feedback, adapting to tool failures without retraining. Releases **EcoAgent**, a benchmark of **5,172 real-world tools / >210k query-tool pairs** for offline retrieval + dynamic reliability. Reports **+52.2% relative MRR** over the ToolLLM API retriever and cuts fault selection rate from **86.2% → 2.9%** under a 30% API-outage scenario, at **<1 ms** overhead.
- **Why it matters**: Reframes tool selection as an **online reliability** problem — directly relevant to agent-harness work ([[skillopt-agent-skills]], [[longharness]]) where the tool set is noisy and changing.

### Memory Retrieval, Two Ways: NEAR (Neighborhood-Aware Residuals) & Beyond the Final Embedding (Token-Level Evidence)
- **Authors** (both): Han Luo, Zhan Zhuang, Xu He, Jujia Zhao, Yu Li, Suqin Yuan, Dong Li, Lei Feng
- **arXiv**: [2610.13314](https://arxiv.org/abs/2610.13314) (cs.IR) · [2610.13277](https://arxiv.org/abs/2610.13277) (cs.IR, cs.CL)
- **Key contribution**: Two **training-free** fixes for the same failure — single-vector query/memory similarity lets topically-overlapping but evidence-free records outrank the correct evidence. **NEAR** uses each memory's **neighbors** to derive a reference direction, builds **projection residuals** for queries and memories, and combines them with the originals for a **single ANN search** over a fixed index (gains on **8 long-context retrieval benchmarks × 9 embedding models**). **Beyond the Final Embedding** matches **contextual token representations** sparsely (each query token retrieves a few matching memory tokens), aggregating token matches with whole-memory similarity; an optional **low-rank query adapter** lifts average **Recall@10 / NDCG@10 by 13.3 / 14.3 points** (Qwen3-Embedding-4B).
- **Why it matters**: Both exploit structure already present in the embeddings — **neighborhood context** and **token-level evidence** — with no training, and both convert retrieval gains into **long-term memory QA** accuracy ([[mem1-agent]], [[memtrapbench]] thread).

---

## ③ LLM RL & Training (3)

### Generalized Proximal Policy Optimization (GPPO): Unifying LLM RL Algorithms from the Perspective of Divergence
- **Authors**: Zhicheng Cai, Xinyuan Guo, Hanlin Wu, Weinan Dai, Yuyan Zhou, Wei-Ying Ma, Ya-Qin Zhang, Hao Zhou
- **arXiv**: [2610.13015](https://arxiv.org/abs/2610.13015) — cs.LG, cs.AI
- **Key contribution**: Argues PPO's **clipping proxy is geometrically degenerate** — it cannot adapt resistance to policy shift, causing premature clipping and degraded exploration — and that variants (DAPO, DPPO, RIPO) are fragmented heuristics. GPPO gives a **generalized f-divergence trust-region theory** with a **monotonic-improvement guarantee**, shows different divergences induce distinct update geometries, and introduces **estimator topologies** beyond single-sample MC. Recasts PPO and its variants as special cases of a **two-dimensional {Divergence × Estimator} design space**; the best instantiation beats standard GRPO by up to **50% (math) / 14% (coding)** across eight competition-level benchmarks.
- **Why it matters**: A unification for the reasoning-RL zoo the wiki tracks ([[reinforcement-learning]], [[rlvr]]) — the axis is *which divergence and which estimator*, not another clipping tweak.

### Branching On-Policy Distillation (BranchOPD)
- **Authors**: Dongyang Chen, Shudong Liu, Shubo Li, Duoxun Tang, Jinwei Liang, Zehuan Wu, Lewei Lu
- **arXiv**: [2610.13481](https://arxiv.org/abs/2610.13481) — cs.AI
- **Key contribution**: On-policy distillation gives teacher supervision on student-generated trajectories, but a single trajectory realizes only **one continuation per decision**, limiting coverage under a fixed sampling budget. BranchOPD selects **informative decision points** via student uncertainty + teacher-student disagreement, **resamples continuations from shared prefixes**, and applies token-level teacher supervision to both the main trajectory and branches; **shared-prefix reuse** cuts student-generated token cost ~**19% (ALFWorld) / 31% (WebShop)** vs seven independent rollouts. Also adds **protocol-boundary repair** for repetition/wasted generation. Beats Vanilla OPD by **+18.55 pts avg@16 (math)** and **+13.8 pts ALFWorld ID/OOD success**.
- **Why it matters**: Extends the OPD thread's "which decisions/tokens carry signal" axis (cf. 10-08 DIAL-OPD, ReCal) from *token selection* to **branch selection at decision points**.

### Rollout-Time Intervention (RTI): Unlocking Agentic Reinforcement Learning Beyond Policy Limits
- **Authors**: Chen Xi, Ding Ruixue, Wang Zhigaoyuan, Zhang Fanrui, Zhang Qiang, Chen Boli, Wang Shihang, Wang Tianfu, Ren Ailin, Wang Pengyong, Xie Pengjun, Xiong Hui
- **arXiv**: [2610.13438](https://arxiv.org/abs/2610.13438) — cs.AI
- **Key contribution**: Agentic RL collapses when tasks exceed the policy's **capability boundary** and successful trajectories are too sparse. RTI uses **reward-side evidence (evaluation rubrics)** *during rollout* to convert erroneous trajectories into successful ones, manufacturing learning signal for tasks the policy rarely solves. The intervention trajectories are **off-policy**, so RTI **filters out excessive distributional shift** to keep them usable. Across five benchmarks RTI consistently beats RL baselines and lets the post-trained policy **transcend its original capability boundary** (Alibaba-NLP; code released).
- **Why it matters**: An explicit instance of the "**rubrics as a rollout-time oracle**" pattern — the same verifier/rubric economy that [[verifiable-rewards]] and [[rlvr]] depend on, pushed to *generate* rather than only *score*.

---

## ④ Agents & Memory (4)

### Humanize MLE Agents (HMA): Multi-Agent Session Alternation Beyond Single-Agent Limits
- **Authors**: Changye Li, Zijian Zhang, Muheng Li, Yiduo Pang, Tingjun Wu, Menghan Li, Yitong Liu, Hongkai Guo, Mengchi Chen, Chenyu He, Kaisheng Ma, Wei Xu, et al.
- **arXiv**: [2610.13494](https://arxiv.org/abs/2610.13494) — cs.AI
- **Key contribution**: Names two failure modes of long-horizon MLE agents: **long-horizon deceleration** (reasoning intensity drops as a single session lengthens) and **harness staleness** (custom tool/skill harnesses stop helping as the base model improves). Models **alternating agent sessions** as a **context-reset semi-Markov decision process (CR-SMDP)**, gives sufficient conditions for alternation to beat the single-agent reference limit plus an experiment-budget bound, and implements **HMA**: two agents alternate on a shared workspace, each session capped at **k experiments** with context reset. On **75 Kaggle tasks in MLE-bench** reaches SOTA **78.2% any-medal**, **+8.0 pts** over the strongest open-source baseline, with **no task-specific harness or prior knowledge**.
- **Why it matters**: A theory-backed argument that **restarting beats extending** — directly engages the wiki's harness/[[context-engineering]] and [[agentic-engineering]] threads.

### LongHarness: Advancing Agentic Reasoning over 100M-Token Corpora via Stateful Evidence Management
- **Authors**: Songtao Huang, Zhijie Zhong, Xiaohan He, Shuaiyu Zhang, Zhiyin Yu, Li Kang, Heng Zhou, Yutao Fan, Xiangchao Yan, Bo Zhang, Shiyang Feng
- **arXiv**: [2610.13075](https://arxiv.org/abs/2610.13075) — cs.AI
- **Key contribution**: Corpus-scale reasoning fails through **unbounded exploration** (retrieval grows history without closing information gaps) and **evidence-state drift** (acquired evidence/corrections stop informing the current conclusion). LongHarness is a **model-agnostic harness** that makes the evidence↔conclusion interaction explicit via **Evidence-Conclusion Coevolution** (unresolved conclusions steer search; new evidence revises the conclusions that directed it) plus **Evidence Lifecycle Management** for currency/traceability. Evaluated on OfficeQA Pro V1/V2, AA-LCR, LongBench v2 with two models.
- **Why it matters**: Pushes harness design from "better retrieval" to **explicit state management** over >context-window corpora — the same "memory is not just recall" theme as [[memtrapbench]].

### DREAM: Forgetting is Not Always Bad — A Neuro-Inspired Memory Repair Mechanism for Poisoned LLM Agents
- **Authors**: Lei Liu, Yunji Liang, Xiaowen Zhang, Jingqi Liu, Qi Li, Bin Guo, Zhiwen Yu
- **arXiv**: [2610.13267](https://arxiv.org/abs/2610.13267) — cs.AI
- **Key contribution**: Agent memory is vulnerable to **memory poisoning**; existing defenses pay for external isolation or continuous online auditing. DREAM is a **training-free, agent-intrinsic** repair framework inspired by destabilization-decay neuroscience: (i) perturbation-induced **implicit reactivation** exposes structural fragility of malicious memories, (ii) **adaptive anomaly diagnosis** finds topological anomalies, (iii) **dynamic memory repair** selectively suppresses harmful memories while reinforcing benign ones. Reduces attack success by **>95%** against backdoor poisoning at competitive benign utility, with up to **2.13× speedup** and **37.7% fewer tokens**.
- **Why it matters**: Recasts defense as **selective forgetting** rather than isolation/auditing — a cheap, in-agent primitive for the memory-safety thread ([[supply-chain-attacks]], prompt-injection defenses).

### JANUS: Enhancing Long-Horizon Autonomous Research with Co-Evolving World Models
- **Authors**: Mengdi Liu, Chenghao Jia, Hong Chang, Mingjie He, Shiguang Shan, Xilin Chen
- **arXiv**: [2610.13194](https://arxiv.org/abs/2610.13194) — cs.AI, cs.CL, cs.MA
- **Key contribution**: Long-horizon autonomous research via reactive Generate-Execute-Feedback suffers **feedback delays** under an exploding search space. JANUS adds a **co-evolving world model** around a **Predict-Verify-Evolve** loop: the research agent proposes candidates, the world model scores them by **forecast value improvement, information gain, and exploration utility**, and branches are selected/refined/pruned *before* execution. Ground-truth feedback is then distilled into **hierarchical research skills** and **exploration-strategy skills for the world model**, with coordination protocols driving continual co-evolution. Beats SOTA on MLS-Bench-Lite and real research tasks.
- **Why it matters**: The [[autoresearch]] / [[autoresearch-ai]] line's newest answer to "don't pay for bad experiments" — a learned simulator prunes the research tree.

---

## ⑤ Safety & Interpretability (3)

### AI Models Can Provably Hide Arbitrary Capabilities
- **Authors**: Andis Draguns, Sumeet Ramesh Motwani, Raymond Douglas, Christian Schroeder de Witt
- **arXiv**: [2610.13928](https://arxiv.org/abs/2610.13928) — cs.LG, cs.CR
- **Key contribution**: Capability evaluations assume hidden capabilities **can be elicited**; this paper breaks that assumption by constructing **backdoor attacks that embed encrypted neural networks inside host weights** (via *digital lockers*), decrypting and executing them only on a secret trigger. Unlike prior work hiding fixed strings, this hides **arbitrary computation**, and the circuits are **provably hard to elicit/interpret** under cryptographic assumptions even with full weight access. Demonstrates resistance to fine-tuning, weight noising, gradient-based trigger search, and latent adversarial training on a chemical-reaction (CBRN-proxy) task; releases the models.
- **Why it matters**: A hard limit on **elicitation-based auditing** — if dangerous capability can be cryptographically hidden, "we tried to elicit it and couldn't" is not evidence of absence. High-signal for the evals/safety-validity arc.

### Attention Sees, MLP Refuses: Tracing the Attention-to-MLP Safety Pathway in LLMs
- **Authors**: Zixuan Weng, Haoqi He, Weifei Jin, Yue Huang, Yang Bai
- **arXiv**: [2610.13078](https://arxiv.org/abs/2610.13078) — cs.AI
- **Key contribution**: Separates **harmfulness recognition** from **refusal writing** on residual-stream updates in decoder-only Transformers. Across **18 Base-Instruct pairs** (Qwen/Llama/Gemma): harmfulness decodes more readily from **attention** updates (esp. early layers), while **MLP** updates drive **harm-selective refusal writing** in aligned models; post-training strengthens MLP refusal writing in **all 18 pairs** without improving harmfulness decodability. Causal intervention — resetting downstream MLP updates to clean values — substantially cancels the refusal shift from upstream attention edits. Introduces **Sentinel**, an attention-derived detector.
- **Why it matters**: A clean **"recognition vs. action" pathway** decomposition for safety circuits — operationalizes how jailbreaks/over-refusal can share a substrate but diverge downstream.

### Defence Against the Dark Arts of Distillation: Unsupervised Discovery of Subliminal Learning
- **Authors**: Joseph Egan, Ciarán M. Gilligan-Lee, Michael O'Riordan, Yuchen Zhu
- **arXiv**: [2610.13536](https://arxiv.org/abs/2610.13536) — stat.ML, cs.AI, cs.LG
- **Key contribution**: When a student is distilled from a teacher sharing its base parameters, the student can inherit behavioural traits — **including misalignment** — even from semantically unrelated data (subliminal learning). All existing defenses require **knowing the trait**; this paper removes that requirement by **recovering a subliminally transferred trait from the parameter updates alone**, exploiting one asymmetry: the trait is expressed **consistently across diverse teacher-generated datasets** while task-specific/shared capabilities vary. The resulting weight-space direction can be **amplified to interpret** the trait or **projected out** to suppress it. Recovers animal-preference traits on the Cloud et al. benchmarks with **no trait labels** and almost no task-performance cost.
- **Why it matters**: Turns subliminal-transfer defense from a labeled problem into an **unsupervised signal-separation** problem — relevant to the [[model-collapse]] / distillation-safety thread and to [[strong-teacher-distillation]].

---

## ⑥ Efficiency & Architecture (1)

### ReplaySSM: Cache SSM Inputs, Not State
- **Authors**: Ze-Wei Liou, Harris Nover, Amey Naik, Andrii Skliar, Igor Shovkun, Ido Shahaf, Tri Dao
- **arXiv**: [2610.13778](https://arxiv.org/abs/2610.13778) — cs.LG, cs.AI
- **Key contribution**: Hybrid SSM models bottleneck on **eager recurrent-state read/write** at every decode step — large state I/O, low arithmetic intensity, no cheap speculative rollback, and quantization error fed back into later updates. ReplaySSM **unrolls the recurrence** into a **checkpoint + recent-input buffer**, separating output computation from checkpoint updates: state writes happen only periodically (~halves dominant state memory traffic), speculative rollback becomes a **buffer-pointer op**, and output-only verification needs no intermediate states. Implemented in **vLLM** for **Mamba-2** and **Gated DeltaNet**: **1.20–1.47×** faster standard decoding at batch 256 across four hybrids, ~**1.8×** the throughput of vLLM speculative decoding on two 120B-class models.
- **Why it matters**: A deployable serving win for the hybrid/SSM lane ([[mamba]] / linear-attention hybrids) with the reusable insight that **the recurrence itself can be reformulated so the expensive resource is never eagerly materialized**. Notable author (Tri Dao).

---

## Also worth recording (not detailed above)

- **`2610.12916`** — *DeFiRank: Federated Pairwise Ranking for Governance in Decentralized Financial Networks* (Zahra Batool, Michael Duchesne, Kaiwen Zhang, Ulrich Aivodji). Federated pairwise ranking so institutions train a ranking model without sharing private transaction data; NDCG@15 ≈ 0.87 vs ≈ 0.92 centralized, matching ranking stability (Kendall τ ≈ 0.70). Recommendation/ranking methodology in a governance setting.
- **`2610.13571`** — *Simultaneous Competitive and Regret Guarantees for TCP Acknowledgment* (Tsubasa Harada, Yasushi Kawase, Hanna Sumita). First algorithm achieving both a **(2+ε)** competitive ratio and **sublinear regret** against the best expert in an online-metric setting, with matching lower bounds; a neat theory datapoint for online algorithms / serving.
- **`2610.13653`** — *A Critical Look at Power Sampling when Test Time Sharpening LLMs* (Abiel Malkani Talwar, Christopher Nemeth, Henry Moss). Shows MCMC/SMC power-distribution samplers **fail to converge** under realistic budgets; their gains are largely recreated by **Best-of-N**, and fine-tuning to match π_α directly gives noisy, model-specific gains. Supports the "RLVR ≈ distribution sharpening" thesis (cf. [[rlvr]]).
- **`2610.13461`** — *SqueezeBench: Saturation-Resilient Evaluation of Mathematical Capability* (Pablo Manrique, Hai Xia, Stefan Szeider). A benchmark where success **raises the bar instead of removing the problem**: Lean-proved lower/upper records on integer functions, double-kernel checked, ten problems from extremal combinatorics. Directly relevant to the benchmark-saturation / [[galaxy-brain-reasoning]] threads.

---

## Cross-cutting observations

1. **CTR lane rebounds from zero, but at the *creative/creative-ops* edge, not the architecture edge.** ECC (`2610.13066`) uses CTR as an **attribute-level editing reward**; the Oct-09 block has **no new CTR-prediction architecture**. The production-scale signal is instead **FORTE** (`2610.13806`, tearing *down* features) — cost engineering, not scaling. The [[ctr-scaling-landscape]] thread gains no scaling entrant for the **fourth consecutive window**.
2. **Generative recommendation is being attacked at the interface.** `2610.12977` shows **finite-beam SID decoding** can make targets unreachable, and proposes continuous-query retrieval instead — the same "the discrete codebook/output vocabulary is the binding constraint" move now seen across [[hstu-generative-recommendation]] / [[ge24rec-generative-rec]]-style systems.
3. **Reasoning-RL is converging on the *supervision source*.** GPPO (`2610.13015`) unifies the update rule ({Divergence × Estimator}); BranchOPD (`2610.13481`) picks *where on the trajectory* to branch; RTI (`2610.13438`) manufactures on-boundary trajectories from **rubrics at rollout time**. Three levers on one bottleneck: effective signal per sample.
4. **Agent harnesses are being replaced by *state discipline*.** HMA (`2610.13494`) proves **alternation beats extension** and that harnesses go **stale**; LongHarness (`2610.13075`) makes evidence/conclusion state first-class; DREAM (`2610.13267`) treats poisoned memory as something to **forget**, not isolate. The through-line: the harness's job is **managing state and resets**, and its value decays as the model improves.
5. **Safety's hard limits get sharper.** Subtly: capability can be **cryptographically hidden** (`2610.13928`, breaking elicitation audits), refusal is **written by MLPs** while harmfulness is seen by **attention** (`2610.13078`), and misalignment can transfer **subliminally through distillation** yet be **recovered unsupervised** (`2610.13536`). Recognition, action, and transfer are now separable, measurable stages.
6. **Measurement honesty persists.** `2610.13653` (power sampling ≈ Best-of-N), `2610.13461` (saturation-resilient benchmark), and `2610.13889` (fault-selection rate as the real tool-retrieval metric) all replace headline metrics with harder ones — the series' standing finding that **reported ≠ verified** held again.

---

## Method disclosure, dedup, and cautions

**Harvest**: arXiv export API over HTTPS. Category sweeps `cat:cs.AI`, `cat:cs.IR`, `cat:cs.LG` (100 entries each, `sortBy=submittedDate desc`) plus topical `all:` passes (`"click-through rate"`, `"ctr prediction"`). Newest available block = **2026-10-09**; the Oct-08 entries returned by the sweeps were cross-checked and, where already claimed by earlier digests, excluded.

⚠️ **Window semantics**: "last 24 hours" is not exposed by arXiv. The newest available block at run time is the **2026-10-09 single day** (previous report covered 2026-10-08). Weekend submissions (Oct 10–11) are not yet announced.

⚠️ **Dedup**: ID-only (`rg -l -F`). Every featured ID verified **0-hit** against the live wiki immediately before writing. Excluded as already-claimed: `2610.12300` (5 hits), `2610.11666` (5 hits) — both Oct-08, covered by earlier `arxiv-daily`/`arxiv-paper-check` siblings.

⚠️ **CTR-lane caution**: exactly **one** genuine CTR paper (`2610.13066`) and **one** production recsys paper (`2610.13806`) in this block; no CTR-prediction architecture. Recorded explicitly so the thin yield is not read as omission.

⚠️ **Affiliation discipline**: affiliations are **not** reliably present in arXiv API metadata and were **not extracted this run**. **Nothing is inferred** from author names or topic. Venue tags are limited to those self-reported via the arXiv `comment` field.

⚠️ **No independent replication**: none of the results in this report were independently replicated, and none was reproduced by a second group. All metric values are as self-reported in the abstracts. The external/online evaluation referenced by ECC (`2610.13066`) is described only at a high level in the abstract.
