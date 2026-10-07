---
title: "Conference & arXiv Digest — 2026-10-07 (NeurIPS 2026 / EMNLP 2026 / KDD 2026 / SIGIR 2026 / RecSys 2026 / CIKM 2026 / ICML 2026 / CoRL 2026 + top-lab preprints)"
type: synthesis
created: 2026-10-07
updated: 2026-10-07
sources: [arxiv-export-api, arxiv-html, conference-announcements]
tags: [conference-digest, NeurIPS2026, EMNLP2026, KDD2026, SIGIR2026, RecSys2026, CIKM2026, ICML2026, CoRL2026, AAAI2026, SIGGRAPHAsia2026, recommendation, LLM, advertising, CTR, generative-IR, agents, world-models, games, code-reasoning, formal-verification, benchmarks, sequential-modeling, daily-digest]
---

# Conference & arXiv Digest — 2026-10-07

> **Scope.** Fresh papers in the window **2026-09-10 → 2026-10-07** that carry a *verified* venue tag (NeurIPS 2026, EMNLP 2026, KDD 2026, SIGIR 2026, RecSys 2026, CIKM 2026, ICML 2026, CoRL 2026, AAAI 2026, SIGGRAPH Asia 2026, ECCV 2026 workshops) **or** that come from a target industrial lab, across the wiki's core categories: recommendation / CTR / advertising, LLM training & reasoning, agent systems, games & world models, code & formal reasoning, and benchmarks. **34 papers** featured.

**Method (for reproducibility).** Harvest via the **arXiv export API** (`export.arxiv.org/api/query`, Atom XML): 5 category sweeps (`cs.IR`, `cs.LG`, `cs.CL`, `cs.AI`, `cs.CV`) bounded by `submittedDate:[202609150000 TO 202610072359]` (200 each) plus 16 topic/affiliation queries (`click-through rate`, `advertising`, `generative recommendation`, `sequential recommendation`, `Kuaishou`, `ByteDance`, `Alibaba`, `Tencent`, `NVIDIA`, `Baidu`, `Google DeepMind`, `Meta AI`, `OpenAI`, …) → **1,000 unique papers pooled**. Requests were **serialized and spaced ≥3 s**; the API's failure mode is a bare 14-byte `Rate exceeded.` body with **no HTTP error status** (a naive parser reads it as *zero results*). Venue tags were read from each entry's arXiv `comment` / `journal_ref` fields; affiliations were read **only** from the paper's own arXiv HTML author block, **never inferred from surnames or email domains** — unresolved items are marked *(affiliation not recovered)* rather than guessed.

**Dedup.** Baseline regex-extract of every `NNNN.NNNNN` id across `wiki/**/*.md` → **8,086 unique claimed arXiv IDs**; all 34 featured IDs re-verified **0-hit** immediately before writing. **No featured paper overlaps** the 2026-10-01 → 2026-10-06 sibling digests (`arxiv-daily`, `arxiv-ai-search`, `arxiv-paper-check`, `game-rl-daily`, `tech-report-digest`).

---

## 0. Executive Summary

- **Recommendation / CTR / advertising / generative-IR is the strongest lane this window (8 papers).** It is dominated by a **semantic-ID construction debate**: FLASH (`2610.07402`, NeurIPS 2026) argues the "hashing is inferior" consensus is a *decoding* artifact, not a *representation* one, while two Artefact Research Center studies (`2610.08732`, `2610.08716`) build a unified PQ/RQ design space and show that generative retrieval **largely memorises query→identifier mappings** (random identifiers retain 83–90% of RQ Hit@1). These three papers jointly push against expensive learned tokenizers.
- **Industrial deployment evidence is present but narrow.** Airbnb's **SIFT** (`2610.07810`) reports a completed **online A/B** (+20.0% filter engagement, +0.72% overall filter usage). Most other papers are offline-only — the window is **academic-heavy**.
- **Agent systems (7 papers)** converge on *verification and memory structure*: SquidAgent (NeurIPS 2026) derives a token-budget criterion for when to parallelise, DAEDALUS bootstraps memory **without an oracle verifier**, and two negative/cautionary results — persistent memory adds cost with **no detectable accuracy gain** (`2610.07782`), and "bottling" (turning general capability into a cheap artifact) does **not** follow from strong zero-shot ability (`2610.08775`).
- **Games / world models (7 papers)** are unusually rich: a MOBA world-model Dyna loop (`2610.08033`) wins **70.2%** of real games with no real gradient, while two new *measurement* benchmarks (World Models' Last Exam in Physics; WorldSolver) show frontier video world models and LLM agents still **fail physical consistency**.
- **Code / formal reasoning (4 papers)** is defined by one loud result: *Lean-verified ≠ correct* (`2610.08144`) — semantically faithful autoformalisation is **harder than the Halting problem** (SCI = ∞), and the paper claims OpenAI's announced Navier–Stokes blown-up-solution Lean proof does **not** correspond to its natural-language claim.

---

## 1. Recommendation, CTR, Advertising & Generative Information Retrieval

### 1.1 FLASH — Rethinking Semantic ID Construction for Generative Recommendation: SimHash with Parallel Decoding and Semantic Alignment
- **中文标题**: 重新思考生成式推荐的 Semantic ID 构建：SimHash 结合并行解码与语义对齐
- **Authors**: Yuqing Liu, Huiyuan Chen, Yibo Wang, Wooseong Yang, Philip S. Yu
- **Affiliation**: University of Illinois Chicago; **Amazon**
- **Venue**: **NeurIPS 2026**
- **Problem background**: Semantic-ID generative recommendation represents each item as a sequence of discrete tokens and decodes the relevant item autoregressively. The field's default assumption is that *learned* quantization (RQ-VAE, RQ-KMeans) beats *training-free* hashing (SimHash) because it captures more semantics.
- **Key innovation**: The paper **challenges that consensus** and re-attributes the gap to two effects — (1) a **structural mismatch between hashing IDs and autoregressive decoding**, and (2) **information loss from rigid discretisation**. FLASH is a two-stage framework that **revitalises training-free SimHash** via **parallel decoding** plus **explicit semantic alignment**. No tokenizer training is required.
- **Results / comparison**: Reports **state-of-the-art performance across multiple datasets** against learned-tokenizer generative recommenders, with **stronger cold-start generalisation**, and shows **semantic alignment is a universally effective mechanism** across paradigms. ⚠️ Abstract names no datasets and gives no absolute numbers.
- **Significance**: If the result holds, an entire family of expensive tokenizer-training pipelines may be unnecessary — the contribution is as much a *reframing* as a method. Directly relevant to [[hstu-generative-recommendation]] and the wiki's Semantic-ID thread (GrIS `2610.01533`, FineSID, SPRIG).
- **Link**: https://arxiv.org/abs/2610.07402 · code: https://github.com/KevinC2015/Flash

### 1.2 SIFT — Search Intent-to-Filter Transformer for Multi-Task Personalized Filter Ranking at Airbnb
- **中文标题**: SIFT：面向 Airbnb 多任务个性化筛选器排序的搜索意图到筛选器 Transformer
- **Authors**: Shashank Dabriwal, Tanya Piplani, Hao Li, Yiwei Wang, Ashish Jain, Kedar Bellare, Stephanie Moyerman
- **Affiliation**: **Airbnb** (San Francisco)
- **Venue**: **GRAIL 2026 Workshop** (co-located, generative/retrieval-augmented/agentic personalization)
- **Problem background**: Search filters drive booking conversion in two-sided marketplaces, but production filter rankers rely on **hand-engineered, pre-aggregated ETL features**, making them costly to maintain and hard to extend to new filter types/contexts (trip length, group size).
- **Key innovation**: SIFT learns guest preference **directly from raw behavioural sequences** with a transformer, replacing manual feature engineering with a **unified guest representation** feeding multiple heads: booking likelihood, filter engagement, and **ordinal capacity thresholds** (e.g. 2+ bedrooms). Extending to a new filter requires **only a new head**. The guest representation is computed **offline daily**, not at request time, to keep serving fast.
- **Results / comparison**: Offline **+51.9% booking** and **+62.8% amenity-engagement PR-AUC** over the production baseline. **Online A/B**: **+20.0%** engagement with recommended filters, **+0.72%** overall filter usage among searchers, **+3.9%** usage of newly supported bedroom/bathroom/bed filters. ⭐ One of the few **completed online A/B** results in this window.
- **Link**: https://arxiv.org/abs/2610.07810

### 1.3 INTEGER — Adapting Generative Recommenders for Multi-Turn Interaction
- **中文标题**: 面向多轮交互的生成式推荐器适配
- **Authors**: Yu-Chen Den, Zhi Rui Tam, Yung-Yu Shih, Shih-Hsin Wang, Yun-Nung Chen, Pu-Jen Cheng, Eugene Yang
- **Affiliation**: National Taiwan University
- **Venue**: Preprint (cs.IR)
- **Problem background**: Generative recommenders decode items from interaction history but give users **no way to correct a recommendation that misses current intent**. Adding conversation is natural (items and words share an output space) but naive adaptation **overwrites the history→item mapping** the recommender depends on.
- **Key innovation**: **INTEGER** adds (a) a **learned routing token** that lets the model decide *when to recommend*, (b) **history re-anchoring** conditioning each item on both past behaviour and dialogue, and (c) **behavioural replay + instruction-data rehearsal** to prevent forgetting.
- **Results / comparison**: On Amazon Beauty and Toys, matches or beats the strongest baselines in accuracy with competitive conversation quality; **+13.3% Hit@10 on Amazon Beauty** and significantly outperforms the base generative recommender. Learns an **intent-agnostic item replacement** that suppresses rejected items.
- **Link**: https://arxiv.org/abs/2610.08136

### 1.4 A Systematic Study of Semantic ID Spaces for Generative Information Retrieval
- **中文标题**: 生成式信息检索 Semantic ID 空间的系统性研究
- **Authors**: Alexia Allal, Hicham Randrianarivo, Sylvain Lamprier
- **Affiliation**: **Artefact Research Center** (Paris); LERIA, Angers University
- **Venue**: Preprint (cs.IR/cs.CL)
- **Key innovation**: A **unified framework that subsumes Product Quantization (PQ) and Residual Quantization (RQ)** and their hybrids in one design space, enabling systematic study of **hierarchy vs. parallelism**, DocID length, and codebook size. Introduces **training-free intrinsic metrics** for DocID quality that avoid full downstream retraining.
- **Results**: Extensive experiments on **MS MARCO 300K** and **NQ320K** characterising how structural DocID properties influence retrieval effectiveness.
- **Link**: https://arxiv.org/abs/2610.08732

### 1.5 Disentangling Paradigm, Identifier, and Decoding in Generative Retrieval
- **中文标题**: 解耦生成式检索中的范式、标识符与解码
- **Authors**: Hicham Randrianarivo, Logan Renaud, Alexia Allal
- **Affiliation**: **Artefact Research Center**
- **Venue**: Preprint (cs.IR/cs.CL)
- **Problem**: Recent generative-retrieval work swaps the AR decoder for **diffusion** while changing **identifiers, training recipe, and decoding at once**, so gains cannot be attributed to any single factor.
- **Key innovation**: Controlled comparison on NQ320K/MS300K training **AR, masked-diffusion, and block-diffusion** models with **RQ, PQ, and random identifiers**, holding identifier length and budget fixed and decoding each model several ways. Introduces **one-pass scoring** to decode diffusion retrievers (read the fully masked identifier once; score each document by its codes' probabilities).
- **Results / comparison**: **Decoding alone moves a diffusion model's Hit@1 by 6.6–13.7 points.** One-pass scoring matches/beats generate-and-match in **11 of 12 settings**. AR still leads in Hit@1 — **the lead comes from the model, not beam search**. ⚠️ **Every paradigm largely memorises query→identifier mappings**: **random identifiers retain 83–90%** of RQ Hit@1; PQ leads RQ by **3.4 points**.
- **Significance**: A rare *ablation-first* paper; its memorisation finding is the strongest caution this window for the "semantic IDs encode meaning" narrative, and pairs directly with FLASH §1.1.
- **Link**: https://arxiv.org/abs/2610.08716

### 1.6 Seeing the Context — Enhancing Recommender Systems with Image-Derived Contextual Signals
- **中文标题**: 看见上下文：利用图像衍生的上下文信号增强推荐系统
- **Authors**: Tal Cordova, Tomer Geva, Moshe Unger
- **Affiliation**: Coller School of Management, **Tel Aviv University**
- **Venue**: **CARS Workshop @ RecSys 2026**
- **Key innovation**: Proposes a **new representation of context derived from images** (physical, social, modal categories learned via a VLM) and **ICE-Fuse**, a pipeline that fuses the categories into a context-aware recommender (TripAdvisor data; Review-aware Graph Contrastive Learning as the base algorithm).
- **Results**: Image context **does not win standalone** but **improves established signals when combined**; semantic analysis shows image- and review-derived context capture **distinct** aspects — images are **complementary**, not replacement.
- **Link**: https://arxiv.org/abs/2610.08407

### 1.7 A Systematic Investigation of Bias in Large Language Models for Advertising Relevance
- **中文标题**: 大语言模型广告相关性判断中偏差的系统性研究
- **Authors**: Weiwei Wang, Yinchuan Xu, Jialu Gao, Youkow Homma, Jian Jiao
- **Affiliation**: **Microsoft**
- **Venue**: Preprint (cs.AI)
- **Problem**: LLMs increasingly judge ad–query relevance, but the **fairness** of these judgments is under-studied.
- **Key innovation**: A **counterfactual framework** varying **advertiser identity, popularity, input language, and demographic wording**, over GPT-4o (categorical relevance judge) and a Qwen-7B relevance model. Advertiser/language experiments use **real advertising logs**; demographic experiments use controlled synthetic queries in employment/housing/credit.
- **Results**: For **both models**, changing advertiser identity or language **can alter relevance assessment**; selected demographic comparisons show **stereotype-consistent patterns** (gender × occupation). Mitigation effectiveness **depends on whether advertiser info is relevant to the query** and on label distribution in training data.
- **Link**: https://arxiv.org/abs/2610.07544

### 1.8 DyPAM — Dynamic Positional Attention Modulation for Parameter-Efficient Fine-Tuning
- **中文标题**: 面向大语言模型参数高效微调的动态位置注意力调制
- **Authors**: Dayan Pan, Jingyuan Wang, Xie Yu
- **Affiliation**: Beihang University (School of Computer Science and Engineering; School of Economics and Management)
- **Venue**: **KDD 2026**
- **Problem**: Most PEFT methods apply **uniform, static** adaptations, ignoring structured heterogeneity of attention across dimensions/heads/layers/tokens; **RoPE induces dimension-dependent positional structure** that uniform adaptation cannot match.
- **Key innovation**: DyPAM modulates how positional information contributes to attention by operating **directly on query/key representations** — input-conditioned **dimension-wise** modulation plus **head-wise and layer-wise** structural modulation — **without modifying the pretrained backbone**.
- **Results**: Consistently outperforms strong PEFT baselines on **math and commonsense reasoning** across multiple backbones. ⚠️ No numbers in the abstract.
- **Link**: https://arxiv.org/abs/2610.07848

---

## 2. LLM Training, Efficiency & Reasoning

### 2.1 Behavior-Preserving KV Cache Compression
- **中文标题**: 保持行为的 KV Cache 压缩
- **Authors**: Doo Hwan Hwang, Junyoung Jang, Junho Na, Hosung Lim, Kee-Eung Kim
- **Affiliation**: *(affiliation not recovered from HTML author block)*
- **Venue**: **EMNLP 2026 Main Conference**
- **Problem**: KV caches bottleneck long-context inference; existing **training-free eviction policies** use **proxy importance signals** (e.g. attention mass) rather than the model's actual behaviour.
- **Key innovation**: Reframes compression as **preserving the full-cache predictive distribution** — score candidate evictions by estimating the compressed-cache logits they induce and measuring **KL to the full-cache next-token distribution**; uses **pre-eviction forward statistics** to avoid a separate masked forward pass per candidate.
- **Results**: Substantial downstream-quality gains over lightweight attention heuristics at **matched retained-KV budgets**, largest under **aggressive compression**, while retaining end-to-end speedup over full-cache inference.
- **Link**: https://arxiv.org/abs/2610.06479

### 2.2 Foresight-over-Graph (FoG) — Reasoning Beyond Local Horizons for KBQA
- **中文标题**: 图前瞻：知识库问答中超越局部视野的推理
- **Authors**: Yang Hong, Yajun Yang, Xin Wang, Liping Jing, Qinghua Hu
- **Affiliation**: Tianjin University; Beijing Jiaotong University
- **Venue**: **NeurIPS 2026**
- **Problem**: LLM-guided graph reasoning uses **hop-wise greedy/beam pruning**, which is **myopic**: evidence weak near the source may become crucial after deeper context, so answer-critical branches are discarded prematurely.
- **Key innovation**: **Foresight-aware evidence retrieval** that iteratively builds a question-relevant subgraph and uses **far-to-near feedback** to guide path exploration, plus a compact **memory subgraph**.
- **Results**: SOTA on KBQA benchmarks, with **+16.58% Hit on CWQ** (i.e. +16.58 pts), while **reducing LLM calls and token usage**.
- **Link**: https://arxiv.org/abs/2610.08388 · code: https://github.com/yhong7/FoG

### 2.3 Feature Information Dynamics in Diffusion
- **中文标题**: 扩散模型中的特征信息动力学
- **Authors**: Jia-Shu Pan, Tao Zhang, Yufei Huang, Yanjun Sheng, Tailin Wu
- **Affiliation**: *(affiliation not recovered from HTML; code hosted at AI4Science-WestlakeU)*
- **Venue**: **NeurIPS 2026 (poster)**
- **Problem**: The intuition that diffusion "reveals coarse structure before fine detail" is **empirical and qualitative**.
- **Key innovation**: An information-theoretic framework — using the **I-MMSE identity**, it links the rate of feature mutual-information change to the **gap between optimal unconditional and feature-conditional denoising losses**, yielding practical **feature-information-density estimators**; a **chained decomposition** separates shared from incremental information in a feature hierarchy.
- **Results**: Quantitatively confirms **spectral autoregression in pixel diffusion**; across a **class → mask → Canny** conditioning chain, per-feature information densities **differ across pixel, SD-VAE, VA-VAE, and RAE**, suggesting **ordered generation** may help diffusion training.
- **Link**: https://arxiv.org/abs/2610.08626 · code: https://github.com/AI4Science-WestlakeU/feature-information-dynamics

### 2.4 Differentiable Bit-Widths (DBW) — Co-optimizing Pruning and Quantization via SVD
- **中文标题**: 可微位宽：基于 SVD 联合优化剪枝与量化实现超高效 LLM 压缩
- **Authors**: Hankyul Kang, Jongbin Ryu
- **Affiliation**: **Ajou University**
- **Venue**: **NeurIPS 2026**
- **Problem**: SVD-based compression runs **two decoupled stages** (truncate, then quantise), requiring separate optimisation and failing to exploit their balance under aggressive compression.
- **Key innovation**: A **differentiable method for learning component-wise bit-widths**, so unimportant components are assigned **0-bit** precision and pruned away — pruning and quantization co-optimised in one framework.
- **Results**: Beats two-stage baselines even at **1.61-bit** extreme quantization.
- **Link**: https://arxiv.org/abs/2610.06026 · code: https://github.com/MMAI-Laboratory/DBW

### 2.5 Base Models Can Reason By Taking a Cue From Training Data
- **中文标题**: 基座模型可借训练数据中的线索进行推理
- **Authors**: Sophie L. Wang, Amil Dravid, Rulin Shao, Kevin Farhat, Sewon Min, Alexei A. Efros
- **Affiliation**: *(affiliation not recovered from HTML author block)*
- **Venue**: Preprint (cs.LG/cs.AI/cs.CL)
- **Key innovation**: Studies how **starting-token cues** associate with reasoning behaviour. Fixing a cue makes a *base* model competitive with its **RL-trained counterpart**: `".\n\nOkay"` raises **Olmo-3-7B** MATH-500 pass@1 from **42% → 78%**; `"Alright,"` raises **Qwen3-14B** from **72% → 87%**. RL mainly makes these cues **more likely**; fixing them recovers much of RL's gain. **Causal data interventions** turn an arbitrary word ("chicken") into an effective reasoning cue, and make "Think duck duck goose" as effective as "Think step by step".
- **Significance**: Reframes part of RLVR's benefit as a **token-distribution/format effect**; relevant to [[rlvr]] and [[verifiable-rewards]].
- **Link**: https://arxiv.org/abs/2610.06851 · code: https://github.com/sophicle/cues

---

## 3. Agent Systems & Agentic Reasoning

### 3.1 SquidAgent — Parallelize Wisely, Coordinate Efficiently
- **中文标题**: SquidAgent：明智并行，高效协调
- **Authors**: Yexiong Lin, Shanshan Ye, Yu Yao, Zhen Fang, Bo Han, Tongliang Liu
- **Affiliation**: The University of Sydney; **MBZUAI**; University of Technology Sydney; Hong Kong Baptist University
- **Venue**: **NeurIPS 2026**
- **Problem**: Parallel multi-agent systems *should* give near-linear speedups but often run **slower than a single agent**, due to two hidden costs: **re-exploration cost** (workers rebuilding context the orchestrator already has) and **alignment cost** (reconciling inconsistent outputs).
- **Key innovation**: A principled criterion — parallelise a layer only if **critical-path cost + re-exploration + alignment < serial cost**. Since LLMs are **poorly calibrated at wall-clock estimation**, cost is measured in **predicted output tokens** (which LLMs estimate more reliably). SquidAgent estimates all token budgets in **one planning step**, **forks workers directly from the orchestrator's session** (eliminating re-exploration), and replaces post-hoc reconciliation.
- **Link**: https://arxiv.org/abs/2610.08647

### 3.2 AdvSim2Real — Training Web Agents Against Adaptive Prompt Injection in a Web World Model
- **中文标题**: AdvSim2Real：在 Web 世界模型中训练 Web Agent 抵御自适应提示注入
- **Authors**: Sarim Hashmi, Mukul Ranjan, Kshitij Mishra, Mikhail Kuznetsov, Praneeth Vepakomma, Nils Lukas
- **Affiliation**: *(author block not recovered; code repository and author affiliation indicate MBZUAI)*
- **Venue**: Preprint (cs.CL/cs.AI/cs.LG)
- **Problem**: Web agents must read third-party pages, so **planted instructions can redirect them**; they cannot ignore the page because it holds the values/controls the task needs. Existing defences fine-tune on **fixed** injections (bypassed by adaptive attackers); adversarial training keeps **tasks fixed** (a task stops teaching once solved).
- **Key innovation**: **Co-evolves a task curriculum, an injection adversary, and the agent inside a frozen web world model.** The curriculum is rewarded for tasks solved **~half the time**; the adversary **only for a success flip**.
- **Results**: A **4B agent** becomes both more capable and more robust; completion rises with and without attacks, holds against a **frontier-model adversary it never trained against**, and the capability gain **carries over to a real browser** — **+33.6% relative completion** on 150 web tasks under the unseen adversary.
- **Significance**: Directly relevant to [[prompt-injection]]. Methodological innovation: **rewarding the adversary only for flipping a judged success**, avoiding reward-hacking by trivial injections.
- **Link**: https://arxiv.org/abs/2610.08773 · code: https://github.com/Sarim-MBZUAI/advsim2real

### 3.3 DAEDALUS — Bootstrapping Agent Memory from Self-Generated Tasks
- **中文标题**: DAEDALUS：从自生成任务中自举 Agent 记忆
- **Authors**: Antoine Edy, Max Conti, Victor Xing, Marc-Antoine Allard, Nawfal Benhamdane, Gautier Viaud
- **Affiliation**: **Illuin Technology**
- **Venue**: Preprint (cs.AI/cs.CL/cs.LG)
- **Problem**: Agents lack operational knowledge of new environments and repeat mistakes. Existing procedural-memory approaches need **human-written guidelines or training tasks + an oracle verifier** — i.e. prior environment knowledge.
- **Key innovation**: Bootstraps memory **without existing tasks or oracle verifiers**: an **explorer** generates challenging-but-solvable tasks, a **solver** attempts them; a **heuristic derived from each failure** is accepted only after repeated in-context success; outcomes feed back to tune task difficulty; accepted heuristics are consolidated into a **memory bank**.
- **Results**: Across **AppWorld, τ²-bench, AutomationBench**: **up to +15.9 points mean success** and **up to 2.2× pass^5** over no-memory, competitive with methods using training tasks at **lower inference cost**; gains emerge with a small exploration budget and transfer to other agents.
- **Link**: https://arxiv.org/abs/2610.08048

### 3.4 When Tools Lie — Reliability of Mathematical Agents Under Corrupted Tool Feedback
- **中文标题**: 当工具说谎：工具反馈被污染时数学 Agent 的可靠性
- **Authors**: Kavienan Jegatheesan, Gayathri Lihinikaduarachchi
- **Affiliation**: University of Moratuwa, Sri Lanka
- **Venue**: **MathAI Workshop @ NeurIPS 2026**
- **Key innovation**: A **controlled corruption framework** where a hidden interceptor replaces tool outputs with plausible-but-wrong results, evaluated across **31 problems and four verification designs** (none / mandatory same-context reflection / optional fresh-context verification / optional structural verification).
- **Results**: Without verification, corruption drops accuracy **100% → 72.4%**; **mandatory reflection fully recovers to 100%**. Optional verification helps **only when models actively invoke it**. Full problem restart succeeds **100%** after explicit detection. Core claim: **verifier availability and verification policy are separate components** of reliability.
- **Link**: https://arxiv.org/abs/2610.08097

### 3.5 Persistent Memory in Multi-Agent LLM Inference — What It Costs, What It Buys, and When You Can Tell
- **中文标题**: 多 Agent LLM 推理中的持久记忆：代价几何、收益几何、何时可辨识
- **Authors**: Hochan Son, Kyungdoe Han, Jaehan Koh, Xiaowu Dai, Wenlu Xu, Guang Cheng
- **Affiliation**: University of California, Los Angeles; University of Wisconsin; HCLTech America
- **Venue**: **ML for Systems Workshop @ NeurIPS 2026 (poster)**
- **Finding**: On one three-tier agent architecture, **decomposition** delivers — peak KV working set **14.3 MiB/query vs 35.5 and 35.3 MiB** for single-pass and retrieval-augmented baselines. But the **persistent tier does not**: across eight controlled dataset pairs (n=100/arm) it costs **+0.368 MiB** peak cache and produces **no detectable accuracy change** (+0.015, 95% CI [−0.011, +0.046]).
- **Significance**: ⚠️ A **structural null** (single-question benchmarks give each item its own evidence, so recall has nothing informative to retrieve) and a **methodology caution**: reaching the null required **four measurement corrections — three inflating the apparent benefit**. Gives the conditions an agent-memory ablation must satisfy. Directly relevant to the wiki's memory-agent thread.
- **Link**: https://arxiv.org/abs/2610.07782

### 3.6 Agent in a Bottle — Can LLM Agents Turn Their Capabilities Into Cheap, Scalable Artifacts?
- **中文标题**: 瓶中 Agent：LLM Agent 能否将能力转化为廉价、可扩展的产物？
- **Authors**: Ankit Sonthalia, Haritz Puerto, Alexander Rubinstein, Martin Gubri, Seong Joon Oh
- **Affiliation**: *(affiliation not recovered from HTML author block)*
- **Venue**: Preprint (cs.AI)
- **Key innovation**: Defines **"bottling"** — turning general capability into task-specific solutions balancing quality and amortised cost — and introduces **BOTTLED**, a benchmark where agents receive an unlabelled workload under fixed time/compute/API budgets.
- **Results (cautionary)**: Across **ten models, three tasks**, strong zero-shot ability **does not reliably translate** into bottling ability — **48 of 60 runs** score below the 95% CI lower bound of their own zero-shot performance; **31 of 60** underperform the stronger of two small-model distillation baselines at equal token budget. Upside: Opus 5 on query–product relevance retains **~82% zero-shot macro-F1 at ~657× lower cost**, and ~**94% of Jev's macro-F1 at a quarter** of Jev's projected cost.
- **Link**: https://arxiv.org/abs/2610.08775

### 3.7 ScienceClaw — Benchmarking Continual Self-Evolution of AI-for-Science Agents
- **中文标题**: ScienceClaw：跨自然科学与社会科学的 AI-for-Science Agent 持续自演化基准
- **Authors**: Mingda Zhang, Wenjin Liu, Tiesunlong Shen, Zikai Xiao, Zhenghong Lin, Qing Xu, Erik Cambria, Xiaoying Tang, Haoran Luo
- **Affiliation**: CUHK-Shenzhen; Nanyang Technological University; Duke-NUS Medical School (Centre for Biomedical Data Science); Zhejiang University; Jurisprudence Research Association, China Law Society
- **Venue**: Preprint (cs.AI)
- **Key innovation**: Formalises **fixed-parameter program self-evolution** unifying task solving, scientific verification, and program updates. **ScienceClaw-Eval spans 23 disciplines** and measures scientific correctness, evolutionary gain, retention, cross-dataset transfer, and evolution cost via sequential streams + independent reset evaluation. Converts re-execution-verified failure→success trajectories into **Skill and Operator candidates**, retaining an update only when **source-task replay reproduces the repair and independent tasks improve**.
- **Link**: https://arxiv.org/abs/2610.08691 · code: https://github.com/beita6969/ScienceClaw

---

## 4. Games, World Models & Sequential Decision-Making

### 4.1 SpeedrunBench — Challenging LLM Agents with Video Game Speedrunning
- **中文标题**: SpeedrunBench：以电子游戏速通挑战 LLM Agent
- **Authors**: Yoshinari Fujinuma, Keisuke Kamahori, Ryuto Koike, Abdelrahman Madkour, Varun Prashant Gangal, Monty Bichouna, Martyna Markiewicz, Shivani Jain, Duncan Curtis, Rebecca Qian, Anand Kannappan
- **Affiliation**: **Patronus AI**; University of Washington; Institute of Science Tokyo
- **Venue**: Preprint (cs.AI)
- **Key innovation**: A benchmark evaluating frontier LLM agents across **9 games** on **strategy formation** — repeatedly improving strategy, reflecting, exploiting gained knowledge, and reasoning over long horizons to beat one's own (and others') records.
- **Results**: Frontier agents **approach human world records in simple platformers** but remain **behind humans on longer, more complex games** under practical budgets.
- **Link**: https://arxiv.org/abs/2610.08076

### 4.2 Recursive Game Creator — An Agentic Product-Level Experience-Oriented Game Harness
- **中文标题**: 递归游戏创造者：面向产品级体验的 Agentic 游戏 Harness
- **Authors**: Jiajun Chen, Haoyu Wu, Mingda Jia, Xihui Liu
- **Affiliation**: **HKU MMLab**; Shenzhen Loop Area Institute
- **Venue**: Preprint (cs.AI/cs.MA/cs.SE)
- **Problem**: Program correctness does **not** ensure a good player experience; prior game-design agents stop at "playable prototypes".
- **Key innovation**: An **experience-oriented harness** with four agents — **Designer, Builder, Player, Reviewer** — in a recursive loop. The **coding-native Player** creates/executes reusable policies via programmatic interfaces to collect diverse trajectories (avoiding slow, biased GUI collection); the **Reviewer** uses trajectory-based metrics + visual evidence + textual preferences.
- **Results**: SOTA **77.89 on GameCraft-Bench**; on **GameASG-Bench** strict task success **53.2%** (+34.1% over same-model baseline) and **highest runtime-check pass rate 93.4%**; user study shows longer playtime and higher ratings.
- **Link**: https://arxiv.org/abs/2610.08621

### 4.3 Learning in Dreams, Winning in Reality — A Continuous Dyna Loop for a Ten-Hero MOBA
- **中文标题**: 梦中学习，现实取胜：十英雄 MOBA 的连续 Dyna 循环
- **Authors**: Jordy Kieto (independent)
- **Affiliation**: Independent (code: `JordyKieto/puffermoba-dyna`)
- **Venue**: Preprint (cs.AI)
- **Key innovation**: Learns a **structured multi-agent world model** of a complete **ten-hero MOBA** (206 units, up to 6,000 ticks), trains a policy **only inside it** (1,400-tick free-running imagined episodes), and measures it in the **real game** against the shipped opponent — as a **continuous asynchronous Dyna loop** where the real game provides **no gradient, only its own games as world-model training data**.
- **Results**: Policy wins **70.2% of real games as radiant** (421/600; 95% CI 66.4–73.7) on unseen seeds, **up from 0% for dream-only and 33.7% before the loop**. Key finding: **model exploitation is invisible from inside the dream** (every unanchored run collapsed while no in-dream metric tracked it); a world model accurate on its training corpus is **badly wrong on the policy's own games**, and Dyna repairs it there (**+9.2 pts** real win rate).
- **Significance**: A strong "judge world models from the outside" result; relevant to the game-RL and world-model threads.
- **Link**: https://arxiv.org/abs/2610.08033

### 4.4 World Models' Last Exam in Physics
- **中文标题**: 世界模型的物理"最后一次考试"
- **Authors**: Mingju Gao, Qingle Liu, Yuzhao Peng, Xinjie Lin, Ziming Qin, Zheng Jiang, Wenyi Li, Calvin Xiao, Youjie Zheng, Kaisen Yang, Qinhuai Na
- **Affiliation**: **Navers Lab / Einsia.AI**; Peking University; Tsinghua University
- **Venue**: Preprint (cs.CV)
- **Key innovation**: A **measurement-based benchmark** for physical consistency in video world models — **40 controlled tasks** spanning mechanics, optics, fluids, thermal/phase-change, electromagnetism, surface tension. Each task pairs an initial image + prompt with predefined physical criteria, enabling **interpretable tests without reference videos**; the evaluator combines **task-observability screening** with **task-specific quantitative measurements**.
- **Results**: Across **8 video generation models, 1,280 videos**, persistent physical inconsistencies; best model scores **57.76/100**. Evaluator agrees with human judgments **better than a direct VLM baseline**.
- **Link**: https://arxiv.org/abs/2610.08791

### 4.5 How Much Planning Is Enough? Reducing Search and Computation in World-Model Planning
- **中文标题**: 规划多少才够？减少世界模型规划中的搜索与计算
- **Authors**: Changbai Li, Sirui Li, Yichen Yang, Tongfei Chen, Zichao Feng, Shuwei Shao, Huobin Tan
- **Affiliation**: Beihang University; Nanyang Technological University; Chengdu University of Technology
- **Venue**: Preprint (cs.RO/cs.AI)
- **Key innovation**: **SufficientPlan**, a deployment framework requiring **no modification** to pretrained world models or planners: **Paired Sequential Budget Certification (PSBC)** uses paired closed-loop evidence to certify a reduced **model–task-specific** search budget within a tolerance; **Static-Context Reuse (SCR)** caches observation/goal representations across search iterations while preserving candidate-dependent planning.
- **Key finding**: Competitive performance is achievable **without agreeing with the full-budget action**; sufficient budgets **vary across model–task pairs**; iterative planners repeatedly re-encode **solve-invariant context**.
- **Link**: https://arxiv.org/abs/2610.08350

### 4.6 WorldSolver — Can LLM Agents Simulate Physical Dynamics via Solver Generation?
- **中文标题**: WorldSolver：LLM Agent 能否通过生成求解器来模拟物理动力学？
- **Authors**: Siru Jiang, Yongzhe Lyu, Shuo Lu, Yubin Wang, Yuxiang Zhang, Yue Liao, Bin Wang, Jian Liang, Tieniu Tan
- **Affiliation**: NLPR & MAIS, **CASIA**; Peking University; **Huawei Noah's Ark Lab**
- **Venue**: Preprint (cs.AI)
- **Key innovation**: **WorldSolver**, a benchmark of **168 simulation tasks** derived from physical phenomena in **61 classic computer graphics papers**, spanning **7 physical domains**. Each task provides a fixed code scaffold and leaves the **solver implementation** to the agent; evaluated on **Execution Checks**, **Visual Fidelity**, and **Physical Plausibility**.
- **Results**: Producing executable solvers is hard; satisfying visual + physical correctness is harder. **GPT-5.6-Sol** and **Claude-Opus-5** perform comparatively better but still achieve overall low scores.
- **Link**: https://arxiv.org/abs/2610.08720

### 4.7 Towards the Automatic Synthesis of Interpretable Chess Tactics
- **中文标题**: 面向可解释国际象棋战术的自动合成
- **Authors**: Abhijeet Krishnan, Chris Martens
- **Affiliation**: *(affiliation not recovered from HTML author block)*
- **Venue**: **Explainable Agency in AI Workshop, AAAI 2026**
- **Key innovation**: A **symbolic sub-policy model for chess** inspired by human tactics, adapting patterns learned by the inductive logic programming system **PAL**. Contributes a **divergence metric** vs a random baseline, and a computational evaluation scheme augmenting an off-the-shelf engine.
- **Results**: Learns a set of tactics suggesting moves of **similar playing strength to a human beginner**.
- **Link**: https://arxiv.org/abs/2610.07640

---

## 5. Code, Formal Reasoning & Verification

### 5.1 SCOPE — Certified Theorem Proving with a Language Model as the Policy Planner
- **中文标题**: SCOPE：以语言模型作为策略规划器的可验证定理证明
- **Authors**: Hanchao Zhou, Jialei Li
- **Affiliation**: *(affiliation not recovered from HTML author block)*
- **Venue**: Preprint (cs.AI)
- **Problem**: In Lean, direct generation fails on multi-step numeric propositions: a proof is valid only if **every content integer is correct**, so pass rate is bounded by the **k-th power of per-integer accuracy**. Controlled corruption across **2,617 reference proofs** confirms this power law.
- **Key innovation**: **SCOPE (State-Conditioned Operator Planning and Execution)** enforces a division of labour — the model **plans over an operator vocabulary**, a **symbolic engine executes the numerics**, and a **compiler renders the proof**.
- **Results**: Certifies **191/218 (87.6%)** with a **135M backbone**; the 7B DeepSeek-Prover-V1.5-RL certifies **18/218 at 27.5× tokens and 37.5× wall-clock**; DeepSeek-Prover-V2-7B certifies **zero** on a bidirectional dual suite. On the public **Lean-Workbook**, **2,132/3,536 (60.29%)** certify with zero regression.
- **Link**: https://arxiv.org/abs/2610.08319

### 5.2 An AI-Assisted Formalization of the Poincaré Conjecture
- **中文标题**: AI 辅助的庞加莱猜想形式化
- **Authors**: Zhiyuan Zhang, Axel Delaval, Leheng Chen, Jinxuan Chen, Jie Xu, Yuxuan Liao, Jiedong Jiang, Chunlei Liu, Bin Dong
- **Affiliation**: *(affiliation not recovered from HTML author block; code at `frenzymath`)*
- **Venue**: Preprint (cs.AI/math.GT)
- **Key innovation**: A **Lean 4 formalization of the Poincaré conjecture** built from a **mathematician-prepared proof blueprint** + **explicit milestone statements**, enabling **parallel agent work** and clear blocker localisation. The contribution is as much **organisational** (which human interventions mattered) as technical.
- **Link**: https://arxiv.org/abs/2610.08329 · code: https://github.com/frenzymath/PoincareConjecture

### 5.3 Navier–Stokes lost in translation — Why Lean verification of AI autoformalisation does not guarantee correct natural language proofs
- **中文标题**: 迷失在翻译中的 Navier–Stokes：为何 Lean 验证 AI 自动形式化不能保证自然语言证明正确
- **Authors**: Alexander Bastounis, Fabian Circelli, Anders C. Hansen
- **Affiliation**: *(affiliation not recovered from HTML author block)*
- **Venue**: Preprint (math.AP/cs.AI/math.LO)
- **Thesis**: **Lean-verified ≠ correct.** Resolving ambiguities in mathematical natural-language text to give a **semantically faithful** translation is **arbitrarily high in the Solvability Complexity Index hierarchy (SCI = ∞)** — informally **harder than the Halting problem** (SCI = 1).
- **Evidence**: Several real **AI mistranslations of NL statements/proofs into Lean**, including **OpenAI's announced Navier–Stokes proof** — the paper claims the formalised Lean proof **does not correspond** to the stated NL claim of blow-up.
- **Significance**: A foundational caution for the entire autoformalisation-verification narrative (cf. [[anthropic-riemann-zeta]]); pairs with §5.1 and §5.2 as the "trust boundary" triad.
- **Link**: https://arxiv.org/abs/2610.08144

### 5.4 NeMo-DCR — Bit-Exact Delta-Compressed Refit for Scalable Agentic RL at Trillion-Parameter Scale
- **中文标题**: NeMo-DCR：面向万亿参数规模可扩展 Agentic RL 的位精确增量压缩重配
- **Authors**: Songlin Jiang, Zhiyu Li, Terry Kong, Yu Yao, Youngeun Kwon, Bernard Nguyen, Ashwath Aithal, Mario Di Francesco
- **Affiliation**: **NVIDIA**; Aalto University
- **Venue**: Preprint (cs.DC/cs.AI) — code open-sourced in **NVIDIA NeMo RL PR #2444**
- **Problem**: Agentic RL disaggregates training from rollout, so each policy update must reach rollout clusters; transferring a full **1T** checkpoint takes **87.5 min** between two AWS regions. BF16 training changes only **~1% of stored weights per step**, but prior sparse systems fall short on **placement, exactness, or efficiency** and none fully recovers from **mid-refit failures**.
- **Key innovation**: Sends **only changes yet is bit-exact**: fixed **affine mappings** project changes into the checkpoint's canonical coordinates; **XOR masks** carry affine changes (bit-preserving), overwrites carry the rest; **in-place application**, retry-overwrite, and a **joint commit** binding policy to baseline; streaming via object storage/relay tree **without a cross-cluster collective**.
- **Results**: Refits of **30B–1T** models even at **3% and 5%** change rates (full numbers truncated in abstract).
- **Link**: https://arxiv.org/abs/2610.08430 · code: https://github.com/NVIDIA-NeMo/RL/pull/2444

---

## 6. Benchmarks & Evaluation

### 6.1 The Labeling Problem in Hallucination Detection Benchmarks — An Empirical Evaluation
- **中文标题**: 幻觉检测基准中的标注问题：一项实证评估
- **Authors**: Jorma Valjakka, Juhani Kivimäki, Juha Mylläri, Jukka K. Nurminen
- **Affiliation**: University of Helsinki (Department of Computer Science)
- **Venue**: **NeurIPS 2026 Evaluations & Datasets Track**
- **Problem**: Hallucination-detection methods are benchmarked with open-domain QA, then **automated labelers** compare answers to reference answers. This creates ambiguity between **reference faithfulness** (fully supported by the reference) and **factual correctness** (free from false specific claims).
- **Key innovation**: **900 human-labeled** QA pairs across **3 QA datasets × 3 generator models**, labels targeting answer-level **factual correctness**; evaluates lexical metrics, a reference-entailment NLI baseline, and **seven LLM judges** under controlled prompt variants.
- **Results**: Substantial disagreement **among** automated labelers and **between** them and human annotations; many exhibit **strong directional error biases**; replacing a faithfulness judge with a correctness-targeted one often does not help.
- **Significance**: A direct hit on the wiki's benchmark-validity thread (cf. `benchmark-rigging-analysis`, `Holdout Best-of-N`).
- **Link**: https://arxiv.org/abs/2610.08026 · code: https://github.com/jova486/LPHB

### 6.2 OTel — Open Telco AI Datasets, Benchmarks, and Models
- **中文标题**: OTel：开放的电信 AI 数据集、基准与模型
- **Authors**: Farbod Tavakkoli, Gregory Diamos, Kenneth Church, David Kanter, Mark Austin, Imtiaz Karim, Mirza Masfiqur Rahman, Merouane Abdelkader Debbah, Zeinab Nezami, Ali Maatouk, Leandros Tassiulas, Rex Ying, Nick Sorros, Louis Powell, …
- **Affiliation**: **AT&T Chief Data Office**, RelationalAI, MLCommons, UT Dallas, Purdue, Khalifa University, University of Leeds, Yale University, Mantis NLP, GSMA, Essential AI (and others)
- **Venue**: **NeurIPS 2026, Evaluations & Datasets Track (Spotlight)**
- **Key innovation**: An open telecom AI resource — derived datasets for retrieval, reranking, instruction tuning and safety/abstention, plus **30 full-parameter post-trained baselines** (10 embedding models, 3 rerankers, 17 LLMs).
- **Results**: Released models downloaded **>16 million times** (as of 2026-05-03). Post-training improves all three families: embedding retrieval **93.1% NDCG@10**, reranking **0.947 MRR@10**, LM correctness **87.8%**.
- **Link**: https://arxiv.org/abs/2610.07766

### 6.3 PolarScale — A Physics-Grounded Benchmark for Radiometrically Consistent RGB-to-Stokes Estimation
- **中文标题**: PolarScale：面向辐射一致 RGB-to-Stokes 估计的物理基准
- **Authors**: Beibei Lin, Tingting Chen, Xin Zhang, Wenhao Zhao, Dongjun Li, Zifeng Yuan
- **Affiliation**: National University of Singapore; University of Michigan, Ann Arbor
- **Venue**: **NeurIPS 2026**
- **Key innovation**: Prior RGB→polarization methods predict only **normalized** Stokes components, dividing out the **radiometric scale** needed for full Stokes reconstruction. PolarScale makes the **scale an explicit prediction/evaluation target**, with angular, self-consistency, and physical-bound metrics.
- **Results**: Across **7 restoration/generative backbones**: strongest restoration models estimate the scale with **3.6–4.3% mean relative error** vs **5.7%** for a constant-scale control and violate physical bounds on **<0.25%** of pixels; **two generative baselines collapse to near-zero scale**; explicit descriptor supervision improves descriptor accuracy (**23.66 vs 18.88 dB PSNR**).
- **Link**: https://arxiv.org/abs/2610.08346

---

## 7. Cross-Cutting Observations

1. **★ The Semantic-ID "learned vs hashing" consensus is being challenged from three directions in one window.** FLASH (`2610.07402`, NeurIPS 2026) says the gap is a **decoding/alignment** artifact; the Artefact pair (`2610.08732`, `2610.08716`) provides a **unified PQ/RQ design space** and shows generative retrieval **largely memorises identifier mappings** (random IDs keep 83–90% of RQ Hit@1). Taken together this is a stronger statement than the wiki's earlier "semantic IDs encode meaning" framing — the **identifier scheme may matter less than the decoder**. ⚠️ All three are offline; none reports a production A/B.
2. **★ Verification is the organising theme of the agent/code lanes — and the window labels it a policy problem, not just a capability one.** When Tools Lie shows **mandatory** reflection recovers 100% while **optional** verification only helps when invoked; AdvSim2Real shows adversarial hardening must **co-evolve** with the task curriculum; SquidAgent derives a **token-budget decision rule**; DAEDALUS accepts a heuristic only after **repeated in-context success**. The cross-cutting claim — *"who verifies, and is it mandatory?"* — connects to [[verifiable-rewards]] and the wiki's [[verification-gap]].
3. **★ World models are being judged "from the outside," and they fail.** The MOBA Dyna loop (`2610.08033`) explicitly measures the **real game** (70.2% win rate) rather than in-dream return; World Models' Last Exam (`2610.08791`, best **57.76/100**) and WorldSolver (`2610.08720`) are **measurement-first** benchmarks. The shared, now-well-evidenced finding: **in-dream / visual metrics do not track real task success**.
4. **★ Industrial evidence is scarce this window.** Of 34 featured papers, only **SIFT/Airbnb** (`2610.07810`) reports a **completed online A/B**; **Microsoft** (§1.7), **NVIDIA** (§5.4), **Amazon** (§1.1) and **Ant Group** (§2.x) contribute alongside universities. The window is **academically dominated** — unlike the industrial burst the 2026-10-05/06 digests recorded — so business-impact claims should not be read as widespread.
5. **Formal verification's trust boundary is now a formal impossibility result.** §5.3's SCI = ∞ argument (autoformalisation is harder than Halting) is the **strongest theoretical caution** this wiki has recorded against treating Lean-checked output as ground truth, and it directly implicates a frontier-lab announcement. It should be cross-referenced wherever the wiki cites "machine-checkable proof" as evidence.
6. **Two methodological negatives worth preserving as claims candidates:** persistent memory as an **ablation artifact** (`2610.07782`, four measurement corrections, three inflating the benefit) and **bottling ≠ zero-shot ability** (`2610.08775`, 48/60 runs below their own zero-shot CI). Both are **reproducible cautionary** results rather than capability claims.

---

## 8. Venue Index

| Venue | Papers in this digest |
|-------|-----------------------|
| **NeurIPS 2026** (main) | FLASH `2610.07402`; FoG `2610.08388`; Feature Information Dynamics `2610.08626`; DBW `2610.06026`; SquidAgent `2610.08647`; PolarScale `2610.08346` |
| **NeurIPS 2026** (ED Track) | Labeling Problem in Hallucination Detection `2610.08026`; OTel `2610.07766` (Spotlight) |
| **NeurIPS 2026** (workshops) | When Tools Lie `2610.08097` (MathAI); Persistent Memory `2610.07782` (MLSys) |
| **EMNLP 2026** (main) | Behavior-Preserving KV Cache Compression `2610.06479` |
| **ICML 2026** | *(only tangential CV papers surfaced this window — none featured)* |
| **KDD 2026** | DyPAM `2610.07848` |
| **SIGIR 2026** | *(no new main-track paper in-window)* |
| **RecSys 2026** | Seeing the Context `2610.08407` (CARS workshop) |
| **CIKM 2026** | *(new in-window CIKM papers were already claimed by sibling digests)* |
| **AAAI 2026** (workshop) | Interpretable Chess Tactics `2610.07640` (Explainable Agency) |
| **CoRL 2026** | DepthWorld `2610.08780` *(not featured — robotics)* |
| **SIGGRAPH Asia 2026** | *(technical-communication graphics papers; not in scope)* |
| **GRAIL 2026** (RecSys workshop) | SIFT/Airbnb `2610.07810` |
| **No venue (preprint)** | INTEGER `2610.08136`; Semantic ID Spaces `2610.08732`; Disentangling GR `2610.08716`; Ad Bias `2610.07544`; Base-Model Cues `2610.06851`; AdvSim2Real `2610.08773`; DAEDALUS `2610.08048`; Agent in a Bottle `2610.08775`; ScienceClaw `2610.08691`; SpeedrunBench `2610.08076`; Recursive Game Creator `2610.08621`; MOBA Dyna `2610.08033`; World Models' Last Exam `2610.08791`; SufficientPlan `2610.08350`; WorldSolver `2610.08720`; SCOPE `2610.08319`; Poincaré `2610.08329`; Navier–Stokes `2610.08144`; NeMo-DCR `2610.08430` |

## 9. Method Notes & Caveats

- **Coverage is topic-complete, not month-exhaustive.** The `submittedDate` range (2026-09-10 → 2026-10-07) with `max_results=200` per category returns the **newest ~200 per category**, which (because arXiv batches are back-loaded) over-represents the **last two days**. Early-window coverage relies on the 16 topic/affiliation queries.
- **Venue tags are self-reported** in the arXiv `comment`/`journal_ref` fields and were **not independently verified against conference proceedings**; a "NeurIPS 2026" tag may denote main track, an oral/poster, or a workshop where the comment is ambiguous — where the distinction was recoverable it is stated.
- **Affiliation discipline.** All affiliations were read from the paper's own **arXiv HTML author block**; those with no HTML render or no affiliation markup are marked *(affiliation not recovered)* and **not inferred**. Seven entries are so marked.
- **Temp files** (Atom XML, HTML renders, parser scripts) were written to `/var/folders/…/T/opencode/confdig/` (pre-authorized scratch) and are not part of the wiki.
- **Dedup**: 34/34 featured IDs re-verified absent from the 8,086-ID whole-wiki baseline immediately before writing; no overlap with sibling 2026-10-01→06 digests.

## References

- arXiv export API: https://export.arxiv.org/api/query
- NeurIPS 2026: https://neurips.cc/virtual/2026/
- EMNLP 2026: https://2026.emnlp.org/
- KDD 2026: https://kdd2026.kdd.org/
- RecSys 2026: https://recsys.acm.org/recsys26/
- ICML 2026: https://icml.cc/virtual/2026/
- AAAI 2026: https://aaai.org/conference/aaai/aaai-26/
