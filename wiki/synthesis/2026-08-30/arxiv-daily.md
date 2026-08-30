---
title: "arXiv Daily — 2026-08-30: DeepMind Co-Scientist Goes Into Real Labs, Task-Conditioned MoE Compression (MetaNet), Trajectory-Free RL for Diffusion (RVM), Process-Level Agentic Math Eval (EMNLP'26), Ordinal Multi-Answer Retrieval Metric, Confidence-Guided World Model Active Learning"
type: synthesis
created: 2026-08-30
updated: 2026-08-30
tags: [arxiv, daily, llm, agents, rl, diffusion, moe, compression, evaluation, world-models, retrieval, ranking, sequential-recommendation, scientific-discovery, agentic-rl, daily-digest]
---

# arXiv Daily — 2026-08-30

This is a complementary pass over the **Fri Aug 28 submission wave** (IDs ~2608.26xxx–2608.27xxx, top listed ID ~2608.27455). No weekend arXiv mailing exists, so the freshest verifiable live listing is **Fri 2026-08-28**. The [08-28 siblings (`arxiv-daily`, `arxiv-ai-search`, `arxiv-paper-check`)](../2026-08-28/) and the 08-29 / 08-30 `arxiv-ai-search` reports already mined that wave (claimed ~2608.26480–2608.27455). This digest re-screens the **under-covered** part of the same wave and pulls forward unclaimed IDs, focusing on LLMs, RL, games/world-models, agents, and retrieval/rec.

Focus: 6 papers across LLM agents + MoE architecture + RL training, process-level evaluation, world-models, and retrieval metrics. Every arXiv ID below is **grep-verified absent** from `wiki/` (checked against all prior digests, index, papers, and claims pages).

> Notes on method: direct arXiv API/web is blocked in this environment (curl exit 35; webfetch Transport error). Metadata recovered via targeted `websearch` against live arXiv abstract/HTML pages. Affiliations marked `(stated)` come from paper front matter; `(inferred)` = deduced from author identities / project pages; otherwise "not stated". Candidates that resolved to previously-covered IDs (e.g. REPREC = 2607.24845, already out-of-wave) were dropped.

---

## 🧠 LLM Agents & Scientific Discovery

### 1. Accelerating Scientific Research with Gemini in the Real-World (Co-Scientist)
| | |
|---|---|
| **Authors** | Samuel Schmidgall, Xiaokai Zhu, Marian Shaw, Lin Yang, Valentin Liévin, Jingyun Yang, Yuchen Zhuang, Tim Strother, Alex Bijamov, Min Woo Sun, Anil Palepu, Justin Chen, David Steiner, Jacqueline Shreibati, Wei-Hung Weng, Yilin Zhao, Xingjian Hu, Nicholas Zahn, Sadhya Garg, Julia Kirby, Yuxiang Gan, Jiaoli Li, Divy Thakkar, Shekoofeh Azizi, David Racz, Juraj Gottweis, Vivek Natarajan, Chenglin Wu, Tal Danino, Keran Rong, Haozhe Wang, Benoit Schillings, Yong Cheng, Quoc V. Le, Tao Tu (et al.) |
| **Institution** | Google DeepMind, with Duke, Columbia, Google Research, Texas A&M *(stated)* |
| **arXiv** | [2608.26701](https://arxiv.org/abs/2608.26701) |

**Abstract:** The authors present an extension and comprehensive real-world validation of Co-Scientist, a Gemini-based multi-agent system designed to accelerate end-to-end scientific research across hypothesis generation, experimentation, and manuscript generation. Moving beyond in-silico hypothesis generation, this specialized configuration transitions Co-Scientist into an execution-grounded research partner advancing closed-loop scientific workflows across materials science, biology, and computer science. In materials science, Co-Scientist interfaced with a semi-automated chemical vapor deposition reactor to design a safe precursor route for MXenes; experimental execution produced a lamellar 2D material sharing key structural similarities with the Ti3C2Tx MXene lattice, though further experiments are needed to confirm the atomic structure. It also tailored growth recipes to laboratory constraints in minutes (via Gemini 3 Deep Think), enabling single-attempt growth of monolayer MoS2, MoSe2, and WS2 semiconductors. In biology, Co-Scientist predicted emergent swarming phenotypes of engineered E. coli across inducer (IPTG) gradients from sparse imaging data, quantitatively matching unpublished wet-lab morphological measurements. In computer science, Co-Scientist autonomously discovered an inference-time scaling architecture ("Agent_H") that outperformed six frontier models on HealthBench (Hard and Professional) while reducing potential clinical harm under blinded physician evaluation. A double-blind study of end-to-end generated papers with 30 domain experts across 450 reviews demonstrates that Co-Scientist's reliability modules reduce hallucination and plagiarism while improving research safety.

**Key Innovations:**
- Moves Co-Scientist from hypothesis generation to **execution-grounded** research — driving physical lab hardware (semi-automated CVD reactor) and closed-loop workflows
- Four distinct autonomy levels across workstreams (human-executed materials → expert-collaborative biology → fully autonomous CS architecture search → AI-generated manuscripts), showing autonomy is a per-task dial, not a system property
- Materials: proposes **C2Cl6** non-hazardous MXene precursor route + one-take growth of monolayer MoS2/MoSe2/WS2 in a lab with no prior experience
- CS: self-discovers **Agent_H**, an 8-phase inference-time scaling architecture (triage/compute allocation, task decomposition, ensemble judging) beating GPT-5 / Gemini 3.1 Pro on HealthBench, with lower clinical harm (p=0.0486)
- **Reliability layer**: hallucination clipping + log-grounded manuscript audit cut severe methodological errors from 100% (baseline) to 24%

---

## ⚙️ LLM Architecture & Efficiency

### 2. MetaNet: Meta-Learning Where to Allocate Experts — Task-Conditioned Layer-Wise Compression for MoEs
| | |
|---|---|
| **Authors** | Rongfeng Wang, Shichao Weng, Zhiqiang Wang, Xinyu Liu, Yang Yi, Peilong Zhou, Hongwei Tang |
| **Institution** | Nanjing Institute of Information Superbahn; University of Chinese Academy of Sciences (UCAS) *(stated)* |
| **arXiv** | [2608.26650](https://arxiv.org/abs/2608.26650) |

**Abstract:** Mixture-of-Experts (MoE) models route each token to a subset of expert networks, increasing capacity while keeping per-token computation sparse. In many deployed MoEs, the number of active experts is fixed across layers and tasks, although layer roles and expert redundancy vary with depth and demand varies with difficulty. Existing approaches address only part of this setting: layer-wise allocations are usually determined offline and reused for all tasks, while token-level methods vary expert activation using local routing signals without task-level context. The authors propose MetaNet, a support-set controller that predicts, for each layer, an expert-retention threshold and a bounded routing bias. The backbone, experts, and router remain frozen. On DeepSeek-MoE-16B-Chat, MetaNet provides a tunable accuracy-expert-activation trade-off. Relative to fixed k=6, a conservative setting activates 3.61 experts on average (40% fewer) and achieves comparable MMLU accuracy (0.489 vs. 0.474), whereas an aggressive setting activates 2.28 experts on average (62% fewer) with accuracy approximately 3.7 percentage points lower. The MMLU-trained controller also transfers to C-Eval without retraining, activating 2.90 experts on average (52% fewer than fixed k=6) at 0.386 accuracy.

**Key Innovations:**
- **Task-conditioned, meta-learned controller** (support-set) predicts per-layer expert-retention threshold + bounded routing bias — unlike fixed-offline layer allocation or token-only dynamic routing
- Keeps backbone, experts, and original router **frozen**; only a lightweight controller is added (complementary to runtime optimizations like DeepSpeed-MoE/Tutel/Lina)
- **Tunable accuracy–expert-activation trade-off**: 40–62% fewer active experts with bounded accuracy loss
- Cross-task generalization: MMLU-trained controller transfers to C-Eval without retraining

---

## 🧪 LLM Evaluation

### 3. From Atomic to Agentic: Towards Interpretable Evaluation of LLMs' Agentic Mathematical Capabilities
| | |
|---|---|
| **Authors** | Jiayi Kuang, Yinghui Li, Yunze Song, Keyu Chen, Zhifeng Shen, Yangning Li, Yidong Wang, Di Yin, Ruizhi Qiao, Xing Sun, Kai Jin, Ying Shen, Liang Lin, Philip S. Yu |
| **Institution** | Tencent Youtu Lab; Sun Yat-sen University *(stated — work done during internship at Tencent Youtu Lab)* |
| **arXiv** | [2608.26950](https://arxiv.org/abs/2608.26950) |

**Abstract:** Large Language Models (LLMs) are evolving from performing end-to-end mathematical reasoning to integrating agentic intelligence. However, most existing math benchmarks evaluate only final answers. This outcome-oriented evaluation provides limited diagnostic value for identifying process-level failures or rigorous logic, failing to guide the transformation of LLMs into robust agents. To bridge this gap, the authors present a process-level benchmark designed to evaluate the inherent agentic mathematical reasoning abilities of LLMs. Their framework aligns problem-solving agentic behaviors with a structured taxonomy of reusable mathematical atomic capabilities. It designs a comprehensive suite of planning, action, and feedback tasks across both textual and multimodal contexts, supported by an automated pipeline that synthesizes high-quality trajectories and produces fine-grained annotations via controlled LLM rewriting. Experiments reveal that models with similar end-to-end accuracy can exhibit markedly different agentic capability profiles. This demonstrates that process-level evaluation is crucial for interpreting the true potential of LLMs and guiding the development of next-generation mathematical agents.

**Key Innovations:**
- **Process-level (not just outcome) benchmark** for agentic mathematical reasoning, organizing capabilities into a reusable taxonomy of "atomic" math skills
- **plan–action–feedback** agent paradigm: models generate a global plan, execute sub-tasks with selected atomic capabilities, verify intermediates, and adapt on feedback
- Automated pipeline synthesizes high-quality trajectories + fine-grained annotations via controlled LLM rewriting
- Key finding: models with similar end-to-end accuracy can differ markedly in agentic capability profiles → outcome-only evals hide real capability gaps (EMNLP 2026)

---

## 🤖 Reinforcement Learning & Generative Models

### 4. Scaling Reinforcement Learning for Diffusion Models via Velocity Matching (RVM)
| | |
|---|---|
| **Authors** | Jaemoo Choi, Wei Guo, Yuchen Zhu, Arash Vahdat, Molei Tao, Julius Berner, Yongxin Chen |
| **Institution** | NVIDIA *(Vahdat)*; Georgia Institute of Technology *(Tao, Chen)*; others not stated |
| **arXiv** | [2608.23664](https://arxiv.org/abs/2608.23664) |

**Abstract:** Reward fine-tuning is becoming an important tool for adapting diffusion models to human preferences and task-specific objectives, but existing methods largely inherit policy-gradient machinery from large language models. Unlike autoregressive models, diffusion models do not provide tractable likelihoods for generated samples. As a result, current approaches either construct trajectory likelihoods from stochastic denoising transitions or approximate endpoint likelihoods with an evidence lower bound, introducing additional computation and algorithmic complexity. The authors demonstrate that this likelihood-based machinery is not necessary for effective diffusion reward fine-tuning. They propose reward-based velocity matching (RVM), a simple trajectory-free update that acts directly on the velocity field. RVM reinforces directions associated with high-reward generations, suppresses those with low reward, and involves an optional anchor term controlling drift from a reference velocity. It provides a general framework that recovers recent fine-tuning methods, including RAM and DiffusionNFT, as special cases. Across various large-scale diffusion model reward fine-tuning tasks, RVM is competitive with or outperforms trajectory-based policy-gradient methods under substantially reduced training cost. Once the velocity update is simplified, the particular loss variant matters less than reward and anchor design. For video generation, standard preference rewards can favor visually clean but nearly static outputs; introducing a new dynamic-tracking reward substantially improves motion while improving overall VBench performance.

**Key Innovations:**
- **Trajectory-free RL update** directly on the velocity field — obviates approximated/constructed likelihoods from stochastic denoising
- General framework that **recovers RAM (Reinforce Adjoint Matching) and DiffusionNFT as special cases**
- Competitive or better than trajectory-based policy-gradient methods at substantially lower training cost
- Finding: once the update is simplified, loss variant matters less than **reward + anchor design**
- Introduces a **dynamic-tracking reward** for video to counter preference-reward reward-hacking that favors clean-but-static outputs

---

## 🚀 World Models & Embodied AI

### 5. ConfAL-WM: Confidence-Guided Active Learning for Action-Conditioned World Models
| | |
|---|---|
| **Authors** | Xiang Liu, Sen Cui, Changshui Zhang |
| **Institution** | Tsinghua University *(inferred from author affiliation)* |
| **arXiv** | [2608.25572](https://arxiv.org/abs/2608.25572) |

**Abstract:** Action-conditioned world models have become an important foundation for embodied prediction, planning, and synthetic data generation, but their errors under new task and scene distributions are often concentrated in localized spatiotemporal regions such as robot arms, manipulated objects, contact areas, and occluded objects. The authors present ConfAL-WM, a confidence-guided active learning framework for post-training embodied world models. Built upon EVAC, it attaches a lightweight confidence probe to UNet decoder features and predicts dense confidence maps in the latent space. [Project page: ConfAL-WM.github.io]

**Key Innovations:**
- **Confidence-guided active learning** for post-training embodied/action-conditioned world models — targets error hot-spots (robot arms, objects, contacts, occlusions)
- Lightweight confidence probe on UNet decoder features → dense latent-space confidence maps (built on EVAC)
- Improves sample efficiency by concentrating post-training data collection where the world model is most uncertain

---

## 🔍 Retrieval & Ranking Metrics

### 6. Rank-Deviation Quality: A Distance-Aware Metric for Multi-Answer Retrieval and Ranking Evaluation (RDQ)
| | |
|---|---|
| **Authors** | Xiaokun Zhou, Alessandro Moschitti, Danielle Class |
| **Institution** | Amazon, USA *(stated)* |
| **arXiv** | [2608.25318](https://arxiv.org/abs/2608.25318) |

**Abstract:** The authors introduce Rank-Deviation Quality (RDQ), an evaluation metric for retrieval and ranking systems that adapts to queries with varying numbers of reference items, from a single correct answer to many valid results. RDQ scores a candidate ranking against an ordered reference list (ORL): each retrieved reference item contributes its output-position weight multiplied by a rank-deviation penalty, and items outside the ORL receive zero credit. Application-specific parameters control tolerance to misordering. Larger values emphasize retrieving valid reference items, whereas smaller values place more weight on matching their reference order. The output-position weights can reflect visibility in the application's interface, such as a vertical list or a carousel. Unlike metrics that require absolute relevance grades, RDQ operates on ordinal rankings, which annotators can produce through pairwise or listwise judgments. Unlike rank-correlation measures such as Kendall's tau, RDQ accounts for both which items are returned and how they are ordered. On a 5,000-query point-of-interest (POI) dataset with 12 systems, RDQ has the highest median empirical power@100 among the 13 evaluated metric configurations; it reaches mean tau >= 0.8 agreement with its own full-query ordering at 200 queries (RBP(0.9) requires 250). On TREC Deep Learning benchmarks, where NDCG uses native graded labels and RDQ uses ordinal tiers derived from them, RDQ reaches comparable median power at n=25 while NDCG is higher at n=100.

**Key Innovations:**
- **Ordinal, distance-aware metric** for multi-answer retrieval — requires no absolute relevance grades (only pairwise/listwise ordinal judgments) and no gain mapping
- Combines **which items are returned** *and* **how they are ordered** (vs. Kendall's tau which only measures order agreement)
- Output-position weights reflect UI visibility (vertical list, carousel); supports tied tiers, query-varying ORL sizes
- Empirical power@100 highest of 13 metric configurations on a 12-system POI dataset; comparable power to NDCG on TREC DL at low n

---

## 🧭 Scope & Dedup Note

- No weekend arXiv mailing exists for 08-30; freshest live listing is **Fri 2026-08-28** (top ID ~2608.27455), so this is a deeper second pass over that wave plus unclaimed IDs.
- **Dedup boundary:** highest ID covered by prior digests is **2608.27455** (08-28 siblings + 08-29/08-30 arxiv-ai-search). The six papers above fall in the **unclaimed 2608.23664–2608.26950** range and are all grep-verified absent from `wiki/`.
- **Dropped as KNOWN / out-of-wave:** LAMA (2608.27382), MaskRec (2608.27005), Stageboost (2608.27366), CoVeMem (2608.26895), WikiSkill (2608.27454), RLHEV (2608.25518, covered), HSR (2608.25755, covered), REPREC (resolves to 2607.24845, already covered in earlier wave); 2608.16957 excluded as pure math; 2608.26445 excluded (metadata not verifiable).
- Sibling 08-30 reports: `arxiv-ai-search` and `conference-digest` cover the conference/industry-centric wave; this `arxiv-daily` fills the previously-unproduced flagship daily digest for the date (no prior 08-30 arxiv-daily existed).
