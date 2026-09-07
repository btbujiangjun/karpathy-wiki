---
title: arXiv AI Research Paper Search Report
type: synthesis
created: 2026-09-07
updated: 2026-09-07
sources: [arxiv.org]
tags: [arxiv, AI, LLM, CTR, recommendation, advertising, sequential-modeling, game-AI, agents, efficient-inference, MoE, KV-cache, game-theory]
---

# arXiv AI Research Paper Search Report

Generated: 2026-09-07 | Scope: AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games

**Methodology**: arXiv Atom API remained rate-limited (HTTP 429), so data was pulled directly from `arxiv.org/list/{cs.IR,cs.CL,cs.AI,cs.GT,cs.MA,cs.LG}/recent` listings for the **Mon 7 Sep 2026** mailing (papers submitted Fri 4 Sep – Mon 7 Sep). This report is **complementary** to [[arxiv-daily]] for 2026-09-07: the 23 papers featured there (Optimal Rates for Agentic Aggregation, Speculative Uncertainty, BeaconKV, Bayesian Unification, 1-shot OPD, RISE, ACE, DEX-Comp, Multi-Agent vs Single Agent, EvoHarnessBench, AlleCompanion, AtomRec, PTDG, LARK, MURAL, Trade-up Rec, AutoLR, SAM-D2Q, IGPO, Embedding Surgery, RCBNB-MB, Abstraction Agent, PPR) are not re-featured here. 24 new papers selected across 6 sections; every featured arXiv ID was grep-verified absent from `wiki/` (only 2609.05279 appears as a passing cross-reference in arxiv-daily, not as a featured entry). ~300+ entries screened across the six listings.

---

## 1. LLMs — Efficient Training & Inference

### 1.1 Don't Drop Dropout: Optimizing Layer Sparsity for Efficient LLM Training and Inference
- **Authors**: Mostafa Elhoushi, Alex Pretko, Nolan Dey, Bin Claire Zhang, Gavia Gray, Gurpreet Gosal, Abdulrahman Mahmoud, Shane Bergsma, Joel Hestness
- **Institution**: Cerebras Systems (tentative — author cluster matches Cerebras)
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.05275
- **Abstract**: Systematic rehabilitation of layer dropout (stochastic depth) for LLM pre-training, which has largely disappeared from modern recipes despite historical benefits. With optimal layer distribution, time schedule, and optimizer hyperparameters, layer dropout delivers lower loss at the same training FLOPs; at fixed step counts it saves up to 25% of training FLOPs. It also enables post-training optimizations — early exit, intermediate-layer skipping, and self-speculative decoding — for up to 1.5× inference speedup with negligible accuracy loss. Results span 2,400+ training experiments from 271M to 8.2B parameters, datasets up to 160B tokens.
- **Key Innovations**: Re-establishes layer dropout as a best practice at scale (quantifies and mitigates prior "dropout hurts accuracy" reports); explicit scaling analysis for training + post-training benefits; largest controlled sweep to date (271M–8.2B).
- **Venue**: Preprint

### 1.2 KVMem: Virtualizing Million-Token Agent Workspaces on a Consumer GPU
- **Authors**: Di Chai, Leye Wang, Zeshen Su, Zhiguo Xia, Zhihang Yu
- **Institution**: Peking University (tentative — Leye Wang affiliation)
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.04852
- **Abstract**: LLM agents accumulate persistent workspaces whose history exceeds both GPU KV capacity and native context windows. KVMem virtualizes overflowed history as paged KV state across GPU memory, host memory, and NVMe, using lightweight **model-native attention-space indexes** to select relevant historical blocks and materialize a query-dependent execution view bounded by the native context window. On long-context agent benchmarks up to 1M tokens (LongMemEval, MemoryAgentBench, AgentLongBench, DeepSWE), KVMem generally beats compaction-based context management (43.8% → 48.4% task success on DeepSWE with Qwen3.8-27B); it runs Qwen3.6/3.8-27B NVFP4 with MTP on a 24GB RTX 5090 Laptop GPU, virtualizing ~1M-token workspaces — 4× the native context.
- **Key Innovations**: KV-context virtualization as a memory-hierarchy paging problem (vs. summary/retrieval compaction that destroys fine-grained evidence); model-native attention indexes for block selection; consumer-hardware million-token agent workspaces.
- **Venue**: Preprint

### 1.3 Cache-Aware Joint Router Adaptation for Memory-Efficient MoE Inference
- **Authors**: Zhenhe Wu, Yaping Jin, Qinghua Xing, Hang Zhou, Wei He, Xianjie Wu, Xianfu Cheng, Jian Yang, Hanting Chen
- **Institution**: Huawei Noah's Ark Lab-affiliated (tentative — Hanting Chen affiliation)
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.04895
- **Abstract**: In MoE decoding, the full expert set often exceeds GPU memory, causing repeated weight transfers. The authors formulate expert-cache management as a **model-side algorithmic problem**: a cache-aware post-training framework jointly adapts the MoE backbone and lightweight auxiliary cache routers while preserving the native Top-K expert-selection rule. Temporal Router predicts same-layer reuse to retain experts; the full Spatio-Temporal Router adds predecessor-hidden-state-based proactive loading. On Qwen3 and GPT-OSS across GSM8K/MATH/CommonsenseQA, Spatio-Temporal Router improves adjusted cache-hit rate by 1.15–18.03 pts and cuts expert-weight traffic 4.6–53.3% vs. the strongest prefetching baseline; joint (router + backbone) post-training matters — auxiliary-only adaptation yields modest cache gains.
- **Key Innovations**: Expert-cache management reframed as model-side (trainable) rather than pure runtime policy; joint backbone + router adaptation beats auxiliary-only; preserves standard Top-K at inference.
- **Venue**: Preprint

### 1.4 Scale-QLoRA: Code-Invariant Adapter Merging for Native 4-bit Microscaling LLMs
- **Authors**: Tung-Ling Li, Jiale Huang, Lee-Chi Wang, Janaki Ram Gotei
- **Institution**: —
- **Date**: 2026-09-03
- **arXiv**: https://arxiv.org/abs/2609.04526
- **Abstract**: On native 4-bit microscaling checkpoints (NVFP4, MXFP4), merging a LoRA adapter back into the base model stops being free: merged weights must be written back through a quantizer that re-derives the E2M1 code plane (~90% of the artifact's bytes), coupling deployments to one quantization convention and — done naively — deleting the adaptation by up to 39 pp (the reconstruction optimum on an already-on-grid base is that base). **Scale-QLoRA** adapts only the per-block **scale** field, trains scales on the deployment grid, and freezes every E2M1 code: merging becomes a bit-exact identity, making the merged artifact code-invariant. Across four models and four tasks it is accuracy-lossless, matching merge-aware QAT-LoRA but preserving the code plane exactly (so lifecycle events never silently move the model).
- **Key Innovations**: Identifies code-plane re-quantization as the hidden failure point of LoRA merging on microscaling formats; scale-only adaptation → bit-exact, code-invariant merge; structural (lifecycle) advantage over QAT-LoRA.
- **Venue**: Preprint

### 1.5 Amortizing Scaling Law Construction Costs
- **Authors**: Abhash Kumar Jha, Diana Alexandra Onuţu, Neeratyoy Mallik, Swagatam Haldar, Sam Laing, Niccolò Ajroldi, Shiwei Liu, Joaquin Vanschoren, Aaron Klein
- **Institution**: Academic / LAION-affiliated (tentative — Vanschoren/Klein/Ajroldi cluster)
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.05016
- **Abstract**: Fitting scaling laws requires training an exhaustive grid over hyperparameters, token budgets, and parameter counts — but only the **best-loss frontier** is actually used. The authors formulate efficient scaling-law construction as a **Bayesian optimization data-collection problem** and introduce metrics for comparing fitting methods under constrained compute. Progressively expanding the compute budget during acquisition (mirroring compute-ordered evaluation in practice) substantially improves recovery efficiency; augmenting observed configurations with surrogate-fantasized evaluations recovers the broader grid, enabling accurate fits without training every configuration — closely matching full-dense-grid fits at **10–100× compute savings**.
- **Key Innovations**: Recasts scaling-law data collection as BO; compute-ordered budget expansion as acquisition policy; surrogate-fantasy augmentation recovers the discarded grid.
- **Venue**: Preprint

---

## 2. LLMs — Reasoning & Post-Training

### 2.1 GUT: Quantifying and Optimizing the Reasoning Uncertainty of LLMs via Graph Complexity
- **Authors**: Shuang Liang, Xin-Yu Hu, Xiang-Jun Ou, Shao-Qun Zhang
- **Institution**: —
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.05284
- **Abstract**: LLM reasoning often fans out into divergent branches at each step, some nonsensical, even under identical inputs. GUT characterizes the potential branches of a reasoning chain as a directed acyclic graph, covering all branches in graph space, then builds two modules: **GUT-Q** quantifies reasoning uncertainty by approximating reasoning-space complexity with graph complexity, and **GUT-O** reduces it by treating negative uncertainty as a reward in RL. Validated across four LLMs and five datasets.
- **Key Innovations**: Graph-complexity proxy for reasoning-space complexity (branching vs. textual entropy); uncertainty-grounded RL reward for reasoning optimization; unified quantize-then-optimize treatment.
- **Venue**: Preprint

---

## 3. Agents & Agentic AI

### 3.1 CUA-Universe: A Scalable and Dynamic Environment for Hybrid GUI+CLI Agents
- **Authors**: Haoting Shi, Wenhao Wang, Weicheng Fang, Yaozhong Liang, Tian Jin, Pengxiang Zhao, Guangyi Liu, Siheng Chen, Yanfeng Wang
- **Institution**: Shanghai Jiao Tong University (tentative — Siheng Chen/Yanfeng Wang affiliation)
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.05374
- **Abstract**: Computer-use agents mostly act via GUI alone, producing inefficient trajectories; real work is hybrid (visual-state inspection + precise CLI). The authors build an environment-to-data pipeline: **App-Forge** adapts real desktop software into reproducible VMs with discovered/wrapped/generated command-line surfaces (scales to 16 applications); **Task-Weave** synthesizes hybrid tasks of controllable difficulty from reusable operations over seed files; **Path-Steer** steers rollouts along efficient hybrid paths and harvests verified trajectories for post-training. Training on this data shifts behavior from inefficient GUI interaction and brittle CLI scripting toward complementary multimodal execution.
- **Key Innovations**: First scalable hybrid GUI+CLI environment pipeline (solves the manual-engineering bottleneck of hybrid envs); CLI surface discovery/wrapping/generation; verified-trajectory post-training harvest.
- **Venue**: Preprint

### 3.2 Testing Interchangeability in LLM Agent Teams
- **Authors**: Jianxin Gao, Tianyi Yu, Linna Deng, Runze Li, Zining Wang
- **Institution**: —
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.05279
- **Abstract**: Production multi-agent systems replace agents on the assumption that role-fillers are interchangeable. Against a placebo reproducing roster-change disruption without changing occupants, trading role-matched agents between eight independently-formed teams (each with private notebooks across ten formation episodes) costs little in task score but raises communication-per-unit-progress by **16–63%**; in Hanabi a swapped agent is *more* expensive than an inexperienced one (interference from conventions learned with its former partner), and in Collab-Overcooked most extra communication after an agenda-setter replacement comes from the agent that stayed. Greedy decoding and shorter formation history shrink the swap penalty alongside team drift.
- **Key Innovations**: Rigorous placebo-controlled test of agent interchangeability; separates task-outcome fungibility from coordination-efficiency cost; convention leakage as the mechanism — complements the same-mailing "equal inference cost" negative result (2609.04217).
- **Venue**: Preprint

### 3.3 TROVE: Adaptive Agent Skill Orchestration via Trace-Grounded Route Validation and Editing
- **Authors**: Tianxing Wang, Mingming Zhao, Shuai Huang, Huiyang Xu, Chaoyue Niu, Shengzhong Liu, Fan Wu
- **Institution**: Shanghai Jiao Tong University (tentative — Chaoyue Niu/Fan Wu affiliation)
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.05019
- **Abstract**: Agents commit to execution structures before decisive runtime outcomes, creating an orchestration bottleneck: invalidated plans force stale-step execution or broad replanning. TROVE **edits only what runtime evidence invalidates**. Offline, it distills evaluated workflow-search traces into atomic/composite skills plus an outcome-conditioned transition graph, preserving stable fragments while exposing outcome-dependent decisions. Online, a planned route is provisional: after committing one top-level skill, the controller keeps a valid continuation, inserts a trace-supported local response, or replaces only the invalid suffix. Across code-generation, QA, and math benchmarks with different backbones, TROVE beats dataset-level optimization, query-level architecture selection, and graph-constrained scheduling on the quality-efficiency frontier.
- **Key Innovations**: Local, trace-grounded plan repair (vs. broad replanning); skill + outcome-conditioned transition graph distillation from search traces; gains largest when outcomes change the appropriate continuation.
- **Venue**: Preprint

### 3.4 Does Your Agent's Memory Survive a Model Upgrade? A Controlled Study of Memory Portability
- **Authors**: Ankit Goyal, Jaideep Ray
- **Institution**: Sandia National Laboratories (tentative — Jaideep Ray affiliation)
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.05339
- **Abstract**: Model upgrades are routine; memory migrations are not. A new model may re-interpret old notes, mixed embedding versions may break retrieval, and repair may fail without original evidence. Four memory representations are compared on 48 synthetic histories with randomized answer codes and exact scoring (two sub-10B models): long-context raw, RAG chunks, compressed natural-language notes, and fixed-schema knowledge graphs. **Fixed-schema structures transfer reliably** (KG-fixed accuracy shift +0.0004±0.0020 after writer swap); compressed NOTES are highly model-coupled (accuracy shifts asymmetrically by +9.91/−13.28 pp by direction); 50/50 mixed-embedding partial RAG migration captures only a 4.96-pt gain of the 11.90-pt full re-embedding improvement. Diagnostic decomposition attributes 80% of the NOTES deficit to lossy construction, 81% of the RAG retrieval deficit to retrieval failures.
- **Key Innovations**: First controlled measurement of memory representations' portability across model upgrades; quantifies mixed-embedding retrieval collapse; evidence that schema-backed memory is the migration-safe choice.
- **Venue**: Preprint

### 3.5 Compact-Memory LLM Agents via Online Max-Member Clustering and Atom-Aware Packing
- **Authors**: Jiahe Geng, Jinpeng Wang, Kun Yuan
- **Institution**: Peking University (tentative — Kun Yuan affiliation)
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.04915
- **Abstract**: Long-horizon LLM deployments face tight prompt budgets; the question is which memory design gives the best quality–token trade-off in the compact regime. **RSM-full** combines a cosine-gated **max-member merge** write rule with an **atom-aware grouped context packer**. On AMA-Bench it reaches 83% of Full-Context quality at 32% of the token cost at a 4k budget, beating Online K-Means by +3.5–6.0 pp (p<.001) across the ~2.6k–5k regime; ablations attribute most of the gain to the merge rule (+5.7 pp) and grouped packer (+5.0 pp). On the independent RealMem persona-memory benchmark it improves on Budget-RAG (+0.69 pp) and Streaming-Proto (+2.97 pp) and matches BM25-RAG.
- **Key Innovations**: Merge-rule design (max-member vs. centroid) as the dominant quality lever in clustered memory; grouped atom-aware packing; strong compact-memory Pareto point at 4k budgets.
- **Venue**: Preprint

### 3.6 Reviewer Capability Governs Rejection Targeting, Not Repair Skill: Evidence from LLM Execute-Review-Revise Pipelines
- **Authors**: Faizan Tanveer
- **Institution**: —
- **Date**: 2026-09-02
- **arXiv**: https://arxiv.org/abs/2609.04270
- **Abstract**: Multi-agent LLM pipelines assign verification to cheaper models, but prior work holds reviewer capability roughly fixed. Varying the reviewer across capability tiers down to one that cannot solve the problems at all (constant set of 100 olympiad math problems; every rejection tracked): a **cross-family mid-tier reviewer improves final accuracy by 12 pp (52→64%, p=0.0005) with zero damaged answers**. Same-model self-review has the highest error-detection recall (0.85) yet yields no gain: it rejects 2.1× as often for a third the repair rate and falsely rejects 35% of its own correct answers (vs. 2% cross-family). The low self-review damage rate is an artifact of **revision inertia** — of 18 falsely rejected correct answers, the 3 the executor complied with all became wrong; the 15 ignored survived.
- **Key Innovations**: Reviewer capability (not repair capability) governs rejection targeting — mid-tier cross-family reviewer optimal; shows slack-compliance dynamics in self-review (revision inertia masks reviewer error).
- **Venue**: Preprint

---

## 4. Recommendation & Retrieval

### 4.1 Dynamic Heterogeneous Graph Representation Learning: A Survey
- **Authors**: Huan Liu, Pengfei Jiao, Jie Yin, Hongjiang Chen, Zhidong Zhao
- **Institution**: Tianjin University (tentative — Pengfei Jiao affiliation)
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.04779
- **Abstract**: First systematic survey of Dynamic Heterogeneous Graph (DHG) representation learning. Proposes a unified formal definition covering both discrete-time and continuous-time DHGs from the temporal-granularity perspective, then an algorithm-centric taxonomy: early embedding-based, GNN-based, and Transformer-based DHG methods — highlighting each class's intrinsic modeling bias w.r.t. dynamic granularity. Surveys applications (including recommendation), datasets/benchmarks, and open directions.
- **Key Innovations**: Unifying DHG formulation across DT/CT granularities; algorithm-centric taxonomy with explicit modeling-bias lens; consolidated app/dataset/benchmark enumeration.
- **Venue**: Preprint (survey)

### 4.2 RegionFed: Federated Learning for Personalized Query Understanding in Heterogeneous Retail Environments
- **Authors**: Quoc H. Nguyen, Ali Lafzi, Abhijeet Phatak, Siddharth Pratap Singh, Rohit Upadhyay, Yogananda Domlur Seetharama, Chittaranjan Tripathy
- **Institution**: Industry (retail tech — tentative)
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.05403
- **Abstract**: Retail search spans regions with distinct query patterns, vocabularies, and product preferences — data heterogeneity that challenges privacy-preserving training and personalization. Standard FL yields global models that sacrifice regional performance; existing **parameter-level** personalized FL catastrophically collapses on modern transformers (below 10% accuracy on T5) due to tied embeddings and LayerNorm interactions. **RegionFed** operates **entirely at the gradient level**: the ℓ₂ conflict between regional and global gradients serves as one signal that (i) diagnoses heterogeneity, (ii) routes each region to the cheapest sufficient personalization strategy, and (iii) controls personalization strength. It deploys on T5-Small/T5-3B/RoBERTa/CNN with zero code changes. RegionFed-Meta reaches 92.27% accuracy on Amazon ESCI, closing the gap to centralized training.
- **Key Innovations**: Gradient-level (architecture-robust) personalized FL that avoids parameter-mixture collapse in transformers; one unified heterogeneity signal for diagnosis + routing + strength control; retail query-understanding benchmark evidence.
- **Venue**: Preprint

### 4.3 SAGE: Semantic Attribute Graphs for Multi-Entity Visual Retrieval
- **Authors**: Yongjoo Kim, Mincheol Kwon, Seonga Choi, Minseung Lee, Kyeong-Jin Oh, Hyunyoung Lee, Yunsu Choi, Jungbeom Lee
- **Institution**: Academic (Korea — tentative)
- **Date**: 2026-09-01
- **arXiv**: https://arxiv.org/abs/2609.04255
- **Abstract**: Dense document images contain many fine-grained entities whose relevance depends on the query; single-vector cropping mixes distinct entity signals ("Semantic Dilution"), degrading entity-level retrieval with entity density. **SAGE** is a training-free framework that parses semantic entities, represents them as hierarchical graph nodes with **multi-vector embeddings**, and retrieves via iterative entity-level subgraph matching. Also introduces **DEAR**, a dataset of 1,055 query–image pairs from product detail pages with four question types of increasing complexity. SAGE substantially reduces semantic dilution and beats patch-level and OCR-based retrieval baselines, reaching Recall@3 0.849 and generation score 2.746 on multi-entity visual comparison queries.
- **Key Innovations**: First explicit identification + quantification of Semantic Dilution; training-free graph-structured multi-vector entity retrieval; product-page-grounding dataset (DEAR).
- **Venue**: Preprint

### 4.4 CAGE: Coherence-Aware Graph Encoding for Retrieval-Augmented Generation
- **Authors**: Tong Qi, Jingyu Wu, Youbing Yin, Spencer Hong, Daben Liu, Erin Babinsky
- **Institution**: —
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.04647
- **Abstract**: RAG scores passages independently against the query, assembling context sets that are individually relevant yet collectively incoherent. **CAGE** models "between-chunk coherence" across four dimensions — Intra-Domain Relevance, Noise Resistance, Informational Bonding, Factual Consistency — by transforming retrieved passages into directed heterogeneous entity graphs, amplifying factual anchors via min-out-degree reweighting, encoding structure with a Relational GCN, and fusing inter-chunk coherence with query relevance. On four multi-hop benchmarks CAGE matches/outperforms strong baselines including monoT5 at Recall@5 on bridge-dominated datasets and consistently improves downstream Exact Match even at comparable or lower retrieval recall.
- **Key Innovations**: Explicit four-dimension between-chunk coherence modeling (not just query-item relevance); graph-encoded relation as a reranking feature; coherence → downstream EM gains despite recall parity.
- **Venue**: Preprint

### 4.5 Repeated Queries Exhaust an LLM's Brand Recommendations but Not Its Sources
- **Authors**: Dmitrij Żatuchin
- **Institution**: —
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.05059
- **Abstract**: Whether repeated identical buying questions exhaust an LLM's brand recommendations depends on retrieval. Across 300 question-engine cells (50 questions × 6 engines × 15 runs, open extraction over 1,470 adjudicated organizations): the five non-retrieval engines were still adding never-seen brands at run 15 in 86–92% of cells (median repertoires 15–31 organizations), while the retrieval-enabled engine closed its list (median 8 organizations). Cited-domain accumulation keeps rising at every horizon tested (still adding domains at run 24, 59–84% of Chao2 estimate); a single run shows 62–77% of the five-run brand set; a parallel **fixed-roster extraction reproduces flat curves** on identical responses — roster-bounded tracking manufactures plateaus that open extraction removes.
- **Key Innovations**: Methodological warning that fixed-roster evaluation manufactures false saturation; distinguishes brand-repertoire exhaustion from source-exhaustion across engines; richness estimators (rarefaction/Chao2) applied to LLM recall.
- **Venue**: Preprint

---

## 5. Advertising, Forecasting & Sequential Modeling

### 5.1 How Faithful Is Attribution for Sales Forecasting? A Counterfactual Study
- **Authors**: Glib Kechyn
- **Institution**: —
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.04797
- **Abstract**: Deep sales forecasters (e.g., WaveNet-style dilational convnets) are accurate but opaque. An architecture-agnostic counterfactual interpretability layer is added to a multi-series WaveNet forecaster on the Corporacion Favorita grocery dataset (174,685 series × 1,688 days), decomposing each forecast into contributions summing **exactly** to the prediction (avoiding additive-SHAP artifacts). Faithfulness validated with deletion/insertion protocols (deletion gap 0.22 p<.001; insertion gap 0.27 p<.01, robust across five background seeds). Findings: promotion-signal reliance is heterogeneous (median ratio ≈1.0, ~20% of series show a strong effect) and the model captures weekly-cycle shape (day-of-week r=0.78) while under-predicting amplitude.
- **Key Innovations**: Exact-sum counterfactual attribution vs. SHAP-style artifacts; rigorous faithfulness evaluation (multi-seed deletion/insertion); candid characterization of where attribution is/ isn't informative.
- **Venue**: Preprint

### 5.2 PRICE: A Systematic Study of LLM Adaptation Choices for Bitcoin Price Forecasting
- **Authors**: Maryam Fakhari, Mehran Safayani
- **Institution**: Isfahan University of Technology (tentative)
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.05235
- **Abstract**: Systematic study of how LLM adaptation choices jointly affect short-term Bitcoin price forecasting on a 4-bit quantized LLaMA-3-8B: **LoRA** PEFT (efficient training on limited hardware), **recursive multi-step inference**, **integer-rounded numerical representation**, **Context-Task-Format (CTF) prompting** (outperforms CoT, iCoT, and few-shot), and **exact zero-temperature decoding** (stability in recursive forecasting). Ablations show each component contributes; PRICE achieves the lowest errors vs. eight transformer-based and time-series foundation models.
- **Key Innovations**: First joint study of fine-tuning + representation + prompting + inference + decoding choices for financial LLM forecasting; CTF prompting >> CoT for this task; strong results for a fully local quantized 8B setup.
- **Venue**: Preprint

### 5.3 MomentQuant: An Even More Minimalist Interval Method with Linear-Time Complexity for Time Series Classification
- **Authors**: Johann Faouzi
- **Institution**: —
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.05136
- **Abstract**: Two improvements to Quant, an interval-based time-series classifier extracting quantiles from recursive fixed dyadic intervals: (1) a highly optimized implementation of the same algorithm, and (2) approximate quantiles via the **Cornish–Fisher expansion**, eliminating the sort — strict linear-time complexity. MomentQuant is faster than Quant (and the optimized Quant faster than the original) at a small predictive-performance cost — relevant where inference outnumbers training.
- **Key Innovations**: Sort-free approximate quantiles (Cornish–Fisher) give linear-time interval classification; three-way efficiency evidence (original → optimized → MomentQuant).
- **Venue**: Preprint

---

## 6. Games & Game Theory

### 6.1 Game-Theoretic Drone Swarm Defense: A Case Study in Applied Differential Game Theory
- **Authors**: Ross E. Allen
- **Institution**: MIT Lincoln Laboratory (tentative)
- **Date**: 2026-09-03
- **arXiv**: https://arxiv.org/abs/2609.04394
- **Abstract**: Differential game (DG) theory applied to target-assignment and midcourse guidance for drone swarms defending high-value assets, treating the intruder swarm as a rational agent seeking a Nash equilibrium. Monte Carlo + Bayesian analysis show DG tactics raise defense success probability vs. unilateral-optimization baselines — from 94.6% to 96.8%, closing ~41% of the remaining gap to perfect defense — with the gain most pronounced against evasive intruders. A paired-trial Bayesian analysis assigns 99.9% posterior probability that DG tactics beat baselines in this scenario.
- **Key Innovations**: Applied Nash-equilibrium swarm defense vs. unilateral maneuver optimization; quantified closing of the gap-to-perfect under evasion; paired Bayesian credibility analysis over Monte Carlo.
- **Venue**: Technical report

### 6.2 A Numerical Approach to the Realizability Problems for Memoryless Nash and Epsilon Equilibria
- **Authors**: Senthil Rajasekaran, Jean-François Raskin, Moshe Y. Vardi
- **Institution**: University of Connecticut / ULB Brussels / Rice University (tentative)
- **Date**: 2026-09-03
- **arXiv**: https://arxiv.org/abs/2609.04396
- **Abstract**: Realizability (does an equilibrium exist?) is notoriously hard for probabilistic undiscounted state-based systems. This paper restricts to **memoryless, numerically constrained** equilibria in concurrent multiplayer reachability games. With bounded-size rational numbers (before/within rationals) and with radical-algebraic field extensions (given a basis), both exact and ε-ε-equilibrium realizability are **NP-complete**. In the unconstrained setting, it shows the celebrated ETR-completeness construction for exact Nash is flawed as presented, mends it to preserve the ETR upper bound, and notes the lower bound does not carry over to ε-equilibria.
- **Key Innovations**: New "numerically constrained equilibria" lens for realizability; NP-completeness results under two number-system constraints; correction of a celebrated ETR-completeness construction.
- **Venue**: Preprint

### 6.3 Strategic Facility Location in Euclidean Spaces
- **Authors**: Kim Thang Nguyen, Lucas Perotin, Bertrand Simon
- **Institution**: Université Gustave Eiffel / ENS Lyon (tentative)
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.05132
- **Abstract**: Strategic facility location: n agents report locations; a truthful mechanism locates a facility to minimize expected maximal agent-facility distance (egalitarian cost). Counter-intuitively, the problem is **easier for two agents on the plane than on the line** — the extra dimension lets mechanisms deter lies more efficiently. The paper devises lower bounds for ℝᵈ asymptotically matching the best known approximation factor of 2 as d grows, plus novel mechanisms improving over the best known plane algorithms, including a setting where the facility may be placed in an extra dimension.
- **Key Innovations**: Higher-dimension escape from the line's difficulty; matching lower bounds (~2) for large d; new truthful mechanisms beating prior plane algorithms.
- **Venue**: Preprint

### 6.4 Closing Gaps in Online Fair Division
- **Authors**: Tzeh Yuan Neoh, Nicholas Teh
- **Institution**: National University of Singapore (tentative — Nicholas Teh affiliation)
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.05310
- **Abstract**: Online fair division of indivisible items arriving one-at-a-time with irrevocable allocation. Three open questions closed: (1) no online algorithm can guarantee any positive multiplicative approximation to PROPk against an adaptive adversary — even knowing m in advance, values in [0,1], each good valued by ≤2 agents; extends to a broad range of envy/proportionality/share notions and to chores; (2) with predictions, a **deterministic 1/2-PROP1** algorithm against adaptive adversaries (removing the prior 1/n dependence), improving to n/(n+κ) with an upper bound κ on positively-valuing agents, robust to one-sided prediction error; (3) with known m ≥ n log n, a deterministic algorithm achieving fixed-β guarantees.
- **Key Innovations**: Impossibility theorems tightening online fair-division limits; prediction-aided deterministic PROP1 with constant (agent-count-free) guarantee; systematic extension to chores and broad share notions.
- **Venue**: Preprint

---

## Summary Statistics

| Category | Papers Count |
|---|---|
| LLMs — Efficient Training & Inference | 5 |
| LLMs — Reasoning & Post-Training | 1 |
| Agents & Agentic AI | 6 |
| Recommendation & Retrieval | 5 |
| Advertising, Forecasting & Sequential Modeling | 3 |
| Games & Game Theory | 4 |
| **Total (this report)** | **24** |
| Overlaps with [[arxiv-daily]] (2026-09-07) | 0 featured / 1 passing mention (2609.05279) |

## Key Trends

1. **Efficiency literature is consolidating around "structure-aware runtime + tiny model-side fixes"**: layer dropout's rehabilitation (2609.05275) shows the training-side sparsity opportunity; MoE cache routing (2609.04895), microscaling-safe LoRA merging (2609.04526), and KV-context virtualization (2609.04852) are all small, principled interventions that keep the served model identical — the same "don't change the architecture, fix the deployment path" pattern as today's BeaconKV/KV thread in [[arxiv-daily]].

2. **Agent evaluation is shifting from "can it do the task" to "does the system survive its own maintenance ops"**: model-upgrade memory portability (2609.05339), role-swap interchangeability (2609.05279), and salvage/revision dynamics (2609.04270) all treat agents as long-lived, replaceable parts of a fleet — not self-contained artifacts.

3. **Memory management is a recurring agent bottleneck**: three of the six agent papers (KVMem, Compact-Memory RS M-full, Memory Portability) attack context/prompt/workspace memory from different angles — virtualized KV, clustered compact prompting, schema-backed portability — reinforcing that memory is becoming the primary agent-scaling constraint.

4. **Hybrid interface + efficient execution is the computer-use frontier**: CUA-Universe explicitly builds GUI+CLI environments because GUI-only trajectories are inefficient; TROVE edits plan suffixes instead of replanning — both push "efficiency of action sequences" as a first-class eval axis.

5. **Personalization in FL/retail keeps hitting the transformer-collapse wall**: RegionFed's gradient-level FL is a direct response to parameter-level personalized FL collapsing on T5; the field is converging on gradient-space heterogeneity signals as the robust alternative.

6. **Forecasting/sequential work is dominated by "how" not "what"**: sales-forecast attribution faithfulness (2609.04797, exact-sum counterfactual), LLM adaptation choice studies (2609.05235), and sort-free linear-time classifiers (2609.05136) — the gains now come from measurement and attribution discipline, not new architectures.

7. **Game theory supplies both applied and foundational results**: drone-swarm differential-game defense (2609.04394) pairs with realizability corrections (2609.04396) and bias-free bounds in Euclidean facility location (2609.05132) and online fair division (2609.05310) — applied DG and theoretical GT both advancing this mailing.