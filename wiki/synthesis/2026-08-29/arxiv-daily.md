---
title: "arXiv Daily — 2026-08-29: Continual-Learning Frontier Models for SovereignAI (Thomson), Visual Retrieval Heads in VLMs, LeVJEPA Collapse-Free Video Pretraining, SARA Action/Authorization Separation, Sparse Urban World Models (UrbanGround), Transduced LM Stochastic Estimation"
type: synthesis
created: 2026-08-29
updated: 2026-08-29
tags: [arxiv, daily, llm, continual-learning, soverign-ai, agents, agent-safety, tool-use, vlm, world-models, video-pretraining, spatial-models, gui-agents, retrieval, reranking, fair-division, game-theory, evaluation, accessibility, sequential-modeling, daily-digest]
---

# arXiv Daily — 2026-08-29

Complementary pass over the **Fri Aug 28 submission wave** (IDs ~2608.26410–2608.27456; no Sat Aug 29 mailing exists). Direct arXiv abs pages were retrievable in this environment; the wave listing was recovered from saved `list_cs.*` announcements (cs.AI / cs.CL / cs.CV / cs.GT / cs.HC / cs.LG / cs.MA / cs.NE / cs.SE, plus paper.cool category digests). Focus: LLMs (training / continual learning / theory), agents & agentic systems, world models & video pretraining, retrieval & IR, games & fair division. Every arXiv ID below is **grep-verified absent** from `wiki/` (checked against all prior digests through 08-30/08-31 incl. same-day `arxiv-ai-search`, `game-rl-daily`, `conference-digest`, `tech-report-digest`).

---

## 🧠 LLM Training & Continual Learning

### 1. Thomson: Continual Learning of Frontier Models for SovereignAI
| | |
|---|---|
| **Authors** | Shengzhuang Chen, Jerrod Parker, Yejin Bang, Andrew M. Bean, Nabeel Seedat, Stefan Winzeck, Dani Glazko, et al. |
| **Institution** | Thomson Reuters *(stated — open-weight model released under `thomsonreuters/Thomson-1.0-Small`)* |
| **arXiv** | [2608.27147](https://arxiv.org/abs/2608.27147) |

**Abstract:** The development of frontier models is commonly perceived to be the exclusive remit of a small number of heavily funded players, creating an information, economic and power asymmetry between developers and the diverse user base of modern AI. The authors argue that frontier performance is achievable by a wide range of institutions through Continual Learning on readily available open-weight models. Unlike limited approaches such as small-scale fine-tuning, prompt engineering, or tool-augmentation of a frozen model, their approach exploits a modern mid- & post-training stack while introducing safeguards that preserve both plasticity and stability at each stage. This yields gains comparable to those typically seen across multiple successive model generations, at compute and personnel budgets substantially lower than commonly thought. Demonstrated with **Thomson**, a general-purpose frontier model trained with an enhanced focus on high-stakes professional work, performing competitively with recent frontier models across agentic tasks, safety, legal, tax & multilingualism, and large-scale Deep Research.

**Key Innovations:**
- **SovereignAI thesis**: frontier performance achievable far beyond big-lab budgets via mid- & post-training continual learning on open-weight bases, preserving plasticity + stability at each stage
- **π-shaped capability pattern**: broad improvements across many capabilities (including non-targeted ones) while almost entirely eliminating the forgetting common to narrow domain adaptation
- Open-weights release validating the "far more actors can own the model stack" claim

### 2. Stochastic Estimation of Transduced Language Models
| | |
|---|---|
| **Authors** | Vésteinn Snæbjarnarson, Samuel Kiegeland, Manuel de Prada Corral, Ryan Cotterell, Tim Vieira |
| **Institution** | ETH Zürich / Johns Hopkins / University of Copenhagen *(inferred from author affiliations)* |
| **arXiv** | [2608.27428](https://arxiv.org/abs/2608.27428) |

**Abstract:** Transduced language models (TLMs) compose a pretrained source language model with a functional finite-state transducer to induce a language model over target strings. Computing the probability of a target prefix requires summing source-model probabilities of all source strings mapping to it — a set that can be exponentially large or infinite. Prior work uses a computational shortcut based on source prefix probabilities, then approximates with threshold-pruned beam summing, producing a lower bound with unknown error. The authors resample source prefixes without replacement and reweight each selected prefix by the inverse of its inclusion probability, giving an unbiased estimator of the target prefix probability and an estimate of the mass lost by threshold pruning.

**Key Innovations:**
- **Unbiased estimator** for TLM prefix probabilities (vs. threshold-pruned lower bounds with unknown error)
- Beam-summing algorithm that **reduces retained prefixes** as probability mass accumulates; halts with probability one
- Beats sequential Monte Carlo baselines on compute–variance tradeoff; on DNA-to-amino-acid transduction reduces runtime by several orders of magnitude; re-analysis leaves published conclusions unchanged but substantially lowers estimated surprisal

---

## 🤖 Agents & Agentic Systems

### 3. ASIL: Replacing Screenshot-and-Click with Structured State and Semantic Actions
| | |
|---|---|
| **Authors** | Rui Xie, Lu Chen |
| **Institution** | — |
| **arXiv** | [2608.26991](https://arxiv.org/abs/2608.26991) |

**Abstract:** Powerful code agents can execute scripts, call tools, and manage files, yet many important applications remain accessible primarily through graphical user interfaces. The authors argue that screenshot-and-click is an inefficient interface for software-operating agents: screenshots are state-incomplete, and GUI actions are brittle, semantically weak, and poorly matched to long-horizon planning. They introduce **ASIL (Agent-Software Interaction Layer)**, an agent-native interface that exposes software through structured JSON observations and code-executable semantic actions, realized through the deepest feasible access path for each application.

**Key Innovations:**
- **Structured-state JSON + semantic actions** replace pixel screenshots and brittle clicks for GUI agents
- ASIL reaches **>80 strict success** with closed models while executing fewer than five actions per task; the same tasks yield 6.6 / 26.6 under screenshot-and-click control and only 15.0 / 53.3 on an easier OSWorld-comparable band
- Scales with training: SFT raises Qwen3.5-2B 58.0→72.1 and Qwen3.5-9B 66.6→80.4; resource-limited on-policy RL further lifts to 74.4 / 82.2
- Instantiated across 15 applications, 300 single-app + 80 multi-app tasks

### 4. When Tool Outputs Become Commands: Separating Action Induction from Runtime Authorization (SARA)
| | |
|---|---|
| **Authors** | Xiaokun Guo, Zhen Xu, Dongdong Huo, Yanqiu Zhang, Wei Wang, Qinfu Yang, Dongjin Yu, Yu Wang |
| **Institution** | — |
| **arXiv** | [2608.27146](https://arxiv.org/abs/2608.27146) |

**Abstract:** Tool-augmented LLM agents must rely on untrusted runtime Observations to complete open-ended tasks; however, when tool outputs no longer merely provide data but begin to specify concrete actions, they effectively become "commands" that can drive real-world side effects beyond user intent. The authors argue this risk arises from conflating action induction with execution authorization, and propose **SARA**, which treats action induction and execution authorization as distinct runtime roles and separates action provenance from execution authority.

**Key Innovations:**
- **Context-isolated Action Probe** exposes action-inducing semantics and records action-origin provenance across steps
- Execution is authorized only against the user objective + audited evidence (goal / execution-chain / argument-level support); **No-History-Promotion** stops historical recurrence from laundering action origins into execution authority
- Limits ASR to ≤0.63% across four primary settings on AgentDojo + AgentDyn while maintaining competitive task utility

### 5. DSA: Evidence-Aware LLM-Agent Orchestration for Multi-Market Stock Research
| | |
|---|---|
| **Authors** | Linsen Zhu, Yi Shi |
| **Institution** | — |
| **arXiv** | [2608.26990](https://arxiv.org/abs/2608.26990) |

**Abstract:** LLMs can summarize financial information, but an operational stock-research system must first assemble heterogeneous evidence, expose unavailable data and model capabilities, and control how generated opinions affect a final report. The authors present **DSA**, an evidence-aware orchestration framework for multi-market stock research with LLM agents, organizing the workflow into evidence acquisition, structured context construction, model-routed analysis, optional role and Strategy Skill reasoning, and report generation with selected context and diagnostics.

**Key Innovations:**
- **Evidence-assembly-first** workflow with role-specific parsers and a signal-eligibility partition before synthesis; explicit disagreement supplied to the decision agent followed by a conservative risk override
- Reference implementation: six regional market paths, fifteen bundled Strategy Skills, hosted + local model routes
- Honest evaluation stance: 1,457 portable offline backend contract tests (596 mapped to six contract families) establish implementation conformance, *not* report quality or returns

### 6. TransMeme: A Multi-Agent Framework for Cross-Cultural Meme Transcreation
| | |
|---|---|
| **Authors** | Jingyi Zheng, Yule Liu, Zifan Peng, Tianyi Hu, Yuemeng Zhao, Xinhu Zheng, Xinlei He |
| **Institution** | — |
| **arXiv** | [2608.27127](https://arxiv.org/abs/2608.27127) |

**Abstract:** Internet memes are a pervasive form of multimodal online communication across diverse linguistic and cultural backgrounds; adapting them across cultures is a central challenge. Unlike ordinary translation or standalone text rewriting, cross-cultural meme transcreation must jointly preserve communicative intent, adapt culture-dependent meaning, and maintain coherence between text and image. **TransMeme** is a multi-agent framework with specialized agents coordinated to address cultural adaptation, target text rewriting, revision, and conditional visual adjustment.

**Key Innovations:**
- **Specialized agent + coordinated feedback** pipeline for intent/tone preservation and multimodal consistency (bidirectional Chinese–English)
- 33.1% average human-eval improvement over the strongest baseline; 60% Top-1 LLM-as-a-Judge ranking vs 26% for second-best
- Error analysis locates remaining bottlenecks in **humor reconstruction** and image-text alignment rather than cultural knowledge gaps

### 7. TraceBench: Controlled Evaluation of LLM Agents for Time-Series Root-Cause Attribution
| | |
|---|---|
| **Authors** | Tommaso Bendinelli, Artur Dox, Christian Holz |
| **Institution** | — |
| **arXiv** | [2608.27182](https://arxiv.org/abs/2608.27182) |

**Abstract:** LLM agents are increasingly applied to anomaly detection and root-cause analysis in time-series data from real-world systems, yet their performance has not been systematically evaluated under controlled conditions. **TraceBench** is a simulation-based framework generating controlled root-cause attribution tasks: an agent receives observations from a simulated physical dynamical system and must determine whether a system parameter was altered and, if so, which one.

**Key Innovations:**
- First **controlled/simulation-based benchmark** for time-series root-cause attribution by LLM agents (three interpretable mechanical systems, four agents)
- Agents benefit substantially from domain context and explore data primarily via **numerical console output rather than visualizations**
- Script-required evaluation (mapping each sample to a predicted root-cause label) hurts performance vs. direct prediction submission

---

## 🌍 World Models & Video Pretraining

### 8. LeVJEPA: Efficient & Scalable Video Pretraining without the Heuristics
| | |
|---|---|
| **Authors** | Lukas Kuhn, Lucas Maes, Giuseppe Serra, Quentin Le Lidec, Yann LeCun, Randall Balestriero, Florian Buettner, et al. |
| **Institution** | Meta FAIR *(inferred from author affiliations — Yann LeCun)* |
| **arXiv** | [2608.27395](https://arxiv.org/abs/2608.27395) |

**Abstract:** Video carries the temporal structure of the physical world, yet learning representations from it has remained computationally expensive: prevailing self-supervised methods either prevent representation collapse through architectural asymmetries (EMA target encoder, stop-gradient, capacity-limited predictor) or reconstruct masked content in pixel space. **LeVJEPA** is the first video encoder trained under LeJEPA's collapse-free objective, dispensing with both. A single encoder is trained with an invariance loss over global and local views of a clip, regularized by **SIGReg**, which excludes collapse with a provable guarantee.

**Key Innovations:**
- **Collapse-free single-encoder objective** (no EMA/stop-gradient/predictor asymmetry), reduced to encoder + projector and a single hyperparameter
- Uniform random token dropping both cuts cost and improves downstream accuracy: at matched epochs, 5.6–20.8× less pretraining compute than V-JEPA 2 (ViT-S/B/L); at matched FLOPs beats the strongest video baseline by 7.6pts on ImageNet-1K
- Encoder trainable with **block-causal attention at no measurable cost** — temporal ordering becomes an encoding property; nearly doubles motion-centric accuracy vs. compute-matched DINOv2 on the same frames

### 9. UrbanGround: From Local Perception to Spatial Agency in a Real-Scale City
| | |
|---|---|
| **Authors** | Tianjie Ju, Zheng Wu, Yueqing Sun, Yuhan Cui, Bobo Li, Shengqiong Wu, Pengzhou Cheng, Haodong Zhao, et al. |
| **Institution** | — |
| **arXiv** | [2608.27456](https://arxiv.org/abs/2608.27456) |

**Abstract:** Multimodal LLMs can interpret a street view, but urban agency depends on whether local evidence remains useful after the agent starts to move. The authors investigate how far current MLLM agents can turn local urban perception into reliable action in a real-scale city, proposing **UrbanGround**, the first sandbox to make this testable in a physically constrained replica of Hong Kong built from territory-wide 3D geospatial data, supporting closed-loop first-person interaction and an interactive map for navigation.

**Key Innovations:**
- **Real-scale, physically constrained urban sandbox** (Hong Kong replica) for closed-loop MLLM navigation — first of its kind
- Three-RQ protocol: local grounding → navigation to distant/less-explicit destinations → robustness to route/pedestrian changes
- Central finding: MLLM agents show useful atomic recognition + short-range spatial reasoning but **orientation and pedestrian-aware movement are unreliable**; local abilities do not compose into sustained goal-directed behavior and errors accumulate without correction

### 10. Retrieval Heads Meet Vision: Uncovering How VLMs Locate and Extract Visual Information
| | |
|---|---|
| **Authors** | Chanho Park, Daehyeon Choi, Jihyun Lee, Minhyuk Sung |
| **Institution** | KAIST *(inferred from author affiliations)* |
| **arXiv** | [2608.27417](https://arxiv.org/abs/2608.27417) |

**Abstract:** Vision-language models can locate an image region referred to by a text prompt and route the corresponding visual evidence to the output, yet the internal mechanism is not understood. Inspired by retrieval heads in LLMs, the authors introduce **Visual Retrieval Heads (VRHs)** — a small subset of attention heads (≈1.7–2.6%) causally responsible for grounding text descriptions to image regions. Scoring attention from output prediction tokens with a sum over the ground-truth referent region most reliably identifies causal heads.

**Key Innovations:**
- First identification of a **vision analog of retrieval heads**: masking only the top 20 VRHs cuts grounding accuracy by up to 80pp across eleven VLMs and five referring-expression benchmarks (random heads ≈ no effect)
- VRHs generalize beyond bounding-box grounding to attribute/spatial/counting/visual-math tasks; **functionally specific** (preserve output format, corrupt localization); **architecturally shared** — transfer causally across VLMs sharing an LLM backbone but differing in vision encoder, projector, and instruction tuning

---

## 🔍 Retrieval, IR & Benchmarks

### 11. STeReO: A Reranker for Orchestrating Heterogeneous Speech and Text Retrievers
| | |
|---|---|
| **Authors** | Inho Kim, Sumyeong Ahn |
| **Institution** | Seoul National University *(inferred from author affiliations)* |
| **arXiv** | [2608.26194](https://arxiv.org/abs/2608.26194) |

**Abstract:** RAG knowledge databases are increasingly diversifying to include various modalities such as speech and text, but research on handling such multi-modal database scenarios remains limited. **STeReO (Speech and Text Reranking Orchestrator)** is a reranker that aggregates disparate modality databases. To address the lack of specialized training data, the authors curate a dataset of queries, mixed-modality evidence, and relevance ranks, then train the reranker and evaluate it in single- and mixed-modality scenarios.

**Key Innovations:**
- First **mixed-modality (speech + text) reranking orchestrator** over heterogeneous retrievers
- Self-curated mixed-modality relevance training data
- Significant downstream QA gains from selecting the most relevant evidence across modalities

### 12. CorporateBench: Large-Scale Q&A Benchmarking with Temporal Knowledge Bases
| | |
|---|---|
| **Authors** | Sil Hamilton, Albert Yu Sun, Oscar J. Romero, Carl-Leander Henneking, David Mimno, Bishan Yang, Igor Labutov |
| **Institution** | Cornell University *(inferred from author affiliations — Mimno, Labutov)* |
| **arXiv** | [2608.27391](https://arxiv.org/abs/2608.27391) |

**Abstract:** LLMs increasingly answer complex questions about enterprise-scale document collections, but evaluation is hard: companies don't share internal communications and synthetic datasets are overly simple. **CorporateBench (CB)** is a human-validated multi-task Q&A benchmark whose corpora surpass 230,000 documents — four synthetically generated firms ranging from 12 to 10,000 employees, each sampled from a temporally evolving knowledge base guaranteeing cross-document logical consistency.

**Key Innovations:**
- **Company-scale eval corpus** (230K+ documents) with guaranteed cross-document consistency via temporally evolving KB sampling
- Two evaluation dimensions: information extraction and knowledge base querying
- Reveals **sharp degradation as input size approaches realistic scales** across five LLMs — a missing metric for corporate-communication reasoning

### 13. BrailleBench: Investigating Multi-Criteria Braille Comprehension in Large Language Models
| | |
|---|---|
| **Authors** | Jinghan Zhang, Fengran Mo, Zhiyu Chen, Xiaoyan Han, Kunpeng Liu, Chang-Tien Lu |
| **Institution** | Virginia Tech *(inferred from author affiliations)* |
| **arXiv** | [2608.27268](https://arxiv.org/abs/2608.27268) |

**Abstract:** Braille's indicators, contractions, and digital representations introduce distinct requirements for model comprehension, yet it is unclear whether AI systems are inclusive enough for blind and deafblind users. **BrailleBench** evaluates LLMs' Braille comprehension across criteria: 5,570 instances from five datasets (math, commonsense, multi-hop QA) across English and Braille Grades 1 and 2, built through a deterministic, expert-reviewed pipeline without LLM-generated data.

**Key Innovations:**
- **First multi-criteria Braille comprehension benchmark** (understand-authored, express-in-Braille, end-to-end interaction)
- LLM-generated instances excluded — deterministic expert-reviewed pipeline via a self-created Braille Toolkit
- Persistent gap between print-English capability and Braille accessibility; **Grade 2 fragile on the input side**, full-Braille requests further reduce performance; expression and understanding are asymmetric

### 14. Importance Scoring of Transformer Attention Heads in Learning Tabular Data
| | |
|---|---|
| **Authors** | Ahmad Jad Allah, Kazi F. Akhter, Md. Kamrozzaman Bhuiyan, Manar D. Samad |
| **Institution** | — |
| **arXiv** | [2608.27241](https://arxiv.org/abs/2608.27241) |

**Abstract:** Deep transformers are widely studied in vision and NLP, but their application to tabular data remains underexplored. This paper presents one of the first applications of an importance-scoring metric to interpret multi-head transformer models for tabular learning across 40 diverse datasets.

**Key Innovations:**
- **Head-importance interpretability for tabular transformers** — robustness to head drops in 72.5% of cases; removing the most important head first yields the greatest degradation
- Key heads are scattered across layers with no consistent layer-specific trend; importance varies considerably across datasets with different schemas/feature spaces (unlike image/language domains)
- Practical use for efficiency and redundancy within transformer architectures

---

## 🎮 Games, Fair Division & Governance

### 15. Simultaneous Envy and Equitability Guarantees
| | |
|---|---|
| **Authors** | Hadi Hosseini, Shraddha Pathak, Lirong Xia, Chengkai Zhang |
| **Institution** | Rensselaer Polytechnic Institute *(inferred from author affiliations)* |
| **arXiv** | [2608.26410](https://arxiv.org/abs/2608.26410) |

**Abstract:** The authors study the compatibility of two fundamentally different fairness notions in fair division — envy-freeness and equitability — for indivisible goods-only and chores-only settings, examining the existence and complexity of simultaneously satisfying their relaxations (EF1+EQ1 / EFX+EQX).

**Key Innovations:**
- **EF1+EQ1 may fail to exist** even for normalized additive valuations; algorithm computes EF1+EQ1 for normalized binary goods with at most seven agents
- Sharp contrast: **binary chores admit EFX+EQX for any number of agents, even without normalization**
- Initiates study of cross-notion ex-ante/ex-post guarantees — randomized allocations with ex-ante guarantees for one notion and ex-post guarantees for the other

### 16. Risks and Controls for Multi-Agent Systems
| | |
|---|---|
| **Authors** | Alistair Reid, Simon O'Callaghan, Dustin Venini, Liam Carroll, Tiberio Caetano |
| **Institution** | Australian AI Safety Institute *(stated)* |
| **arXiv** | [2608.26626](https://arxiv.org/abs/2608.26626) |

**Abstract:** This report presents a framework to reason about risks that emerge when AI agents interact with each other, how those risks change as interactions cross organisational boundaries, and the controls that may help address them. Failures can emerge from the interactions themselves, and once those interactions cross an organisation's perimeter, no single organisation can fully see, control, or govern them.

**Key Innovations:**
- **Three deployment tiers** by minimum common governance: singular governance (one org), federated governance (shared environment, agreed rules), open environments (no central authority)
- Per-tier risk-factor/failure-mode/control analysis; identifies who is positioned to apply controls and characterizes **collective-action gaps** where no actor can act alone

---

## 📌 Key Trends Today

1. **SovereignAI / continual learning goes mainstream** — Thomson validates frontier-quality capability building on open-weight bases at fractional budgets (π-shaped gains, near-zero forgetting), extending the wiki's open-model post-training line beyond low-cost pretraining (cf. Puro-2B, 08-28 digest).
2. **Agent-interface redesign** — ASIL (structured JSON state + semantic actions) and SARA (action-induction/authorization separation) both push past brittle screenshot/click and untrusted-tool-output modes, pointing to *interface* and *authorization-provenance* as first-class agent problems.
3. **Video pretraining cost collapse under collapse-free objectives** — LeVJEPA (SIGReg-regularized LeJEPA objective) achieves 5.6–20.8× compute savings and, unlike video-vs-image debates, makes block-causal video a viable general-purpose visual substrate.
4. **Spatial/embodied evaluation matures** — UrbanGround provides the first real-scale, physically constrained city sandbox for MLLM navigation and finds local abilities don't compose into sustained goal-directed behavior (orientation & pedestrian-awareness are the failure point).
5. **VLM mechanistic interpretability arrives** — Visual Retrieval Heads generalize the LLM retrieval-head triad (causal-sparse-universal) to vision and are architecturally shareable across backbones.
6. **Evaluation expands to accessibility and enterprise scale** — BrailleBench (Braille comprehension asymmetry) and CorporateBench (230K-doc temporal-KB QA, scale-limited performance) fill evaluation gaps for underrepresented users and corporate reasoning.
7. **Multi-agent governance theory emerging** — the Australian AI Safety Institute's deployment-tier framework formalizes collective-action gaps in cross-organizational agent interaction.