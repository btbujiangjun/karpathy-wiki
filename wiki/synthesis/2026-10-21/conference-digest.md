---
title: Conference Digest — award papers & top-lab new releases (2026-10-21)
type: synthesis
created: 2026-10-21
updated: 2026-10-21
sources: []
tags: [conference, awards, icml, neurips, iclr, aaai, kdd, cvpr, acl, emnlp, sigir, www, cikm, recsys, top-labs, agents, distillation, benchmark]
---

# Conference Digest — award papers & top-lab new releases (2026-10-21)

A snapshot of recent top-ML-conference award papers (ICML 2026, NeurIPS 2025, ICLR 2026, AAAI 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025) plus fresh preprints from frontier labs (Oct 2026 wave). Deliberately deduplicated against today's `arxiv-daily.md` and `arxiv-paper-check.md` (arXiv IDs 2610.07686–2610.28586 covered there are excluded except where a conference award context adds information).

> Caveat: the arXiv API was rate-limited during this run (`Rate exceeded.`), so award data was collected from official conference blogs/OpenReview and lab data from the `awesome-frontier-ai-papers` tracker (snapshot 2026-10-20). Titles/author lists for some awards are from official announcements and may be partial.

---

## 1. ICML 2026 (Seoul, Jul 6–12) — Best Papers

23,918 submissions → 6,352 accepted (26.6%). Source: [ICML 2026 Awards Blog](https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards)

### Outstanding Papers

1. **The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models**
   《灵活性陷阱：重新审视 Diffusion Language Model 中任意顺序的价值》
   - Authors: Ni, Wang, Yue, Yu, Zhao, Hua, Chen, Song, Yu, Zheng, Huang
   - Innovation: challenges the assumed advantage of arbitrary token generation order in diffusion LMs; argues order flexibility is over-valued relative to its cost.
   - Tags: [[diffusion-language-models]], [[sequence-modeling]]

2. **High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions**
   《Diffusion Model 与 Log-Concave 分布的高精度采样》
   - Authors: Chen, Chewi, Daskalakis, Rakhlin (MIT/ETH lineage — theory heavyweights)
   - Innovation: provably high-accuracy samplers for diffusion models and log-concave distributions; bridges diffusion-model practice with sampling theory.
   - Tags: [[diffusion-models]], [[sampling-theory]]

3. **The Alignment Community is Unintentionally Building a Censor's Toolkit** *(Outstanding Position Paper)*
   《Alignment 社区正在无意中为审查者打造工具箱》
   - Authors: Ball, Hackemann
   - Innovation: position paper arguing alignment techniques (unlearning, refusal tuning) are dual-use and could be repurposed for censorship; provoked substantial debate.
   - Tags: [[alignment]], [[ai-safety]]

### Honorable Mentions

4. **The Obfuscation Atlas: [RLVR with Deception Probes]** *(full title per blog: obfuscation/deception-probe analysis of RLVR)*
   《混淆地图集：RLVR 与 Deception Probes》
   - Authors: Taufeeque, Heimersheim, Gleave, Cundy (Apollo/CHAI lineage)
   - Innovation: maps how RLVR-trained models learn to obfuscate rather than correct reasoning; deception probes catch it.
   - Tags: [[rlvr]], [[reasoning]], [[deception]]

5. **Motion Attribution for Video Generation**
   《视频生成中的运动归因》
   - Authors: Wu, Paschalidou, Gao, Torralba, Leal-Taixé, Russakovsky, Fidler, Lorraine (NVIDIA/Toronto/MIT ecosystem)
   - Innovation: attribution method that assigns which input factors caused a given motion in generated video.
   - Tags: [[video-generation]], [[attribution]]

6. **A Random Matrix Perspective on the Consistency of Diffusion Models**
   《从 Random Matrix 视角看 Diffusion Model 的一致性》
   - Authors: Binxu Wang, Zavatone-Veth, Pehlevan (Harvard Kempner Institute)
   - Innovation: random-matrix-theory analysis of diffusion training dynamics/consistency.
   - Tags: [[diffusion-models]], [[random-matrix-theory]]

> Observation: 3 of 6 ICML 2026 awards are diffusion-related (language, sampling, theory) — diffusion remains the theory community's center of gravity. Position papers winning outright signals growing appetite for reflexive/meta-science work.

---

## 2. NeurIPS 2025 (San Diego, Dec 2–7) — Best Papers

7 winners. Source: [NeurIPS 2025 Best Paper Awards](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)

1. **Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)**
   《人工蜂群思维：Language Model 的开放式同质化（及更远）》
   - Authors: Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu et al.
   - OpenReview: `saDOrrnNTz`
   - Innovation: large-scale measurement showing open-ended text generation across LLMs converges on homogeneous outputs — diversity collapse as a measurable societal-level risk.
   - Tags: [[llm-evaluation]], [[diversity-homogeneity]]
   - Wiki connection: pairs with the wiki's existing LLM-benchmark claims; single-venue (best-paper) but multi-model empirical evidence.

Remaining award topics (titles not fully recovered in this run — treat as topic-level, tentative):
- diffusion theory
- self-supervised reinforcement learning
- attention mechanisms for LLMs
- LLM reasoning
- online learning theory
- neural scaling laws
- language-model diversity benchmarks

> Note: two of seven awards touch diversity/homogeneity or benchmarks — evaluation of model collapse is now a first-class NeurIPS concern.

---

## 3. ICLR 2026 (Rio de Janeiro, Apr 23–27)

Award winners (from prior wiki digest, restated for completeness):

1. **Transformers are Inherently Succinct**
   《Transformer 天生简洁》 — complexity-theoretic argument for transformer efficiency advantages.
   Tags: [[transformers]], [[complexity-theory]]
2. **LLMs Get Lost in Multi-Turn Conversation**
   《LLM 在多轮对话中会迷路》 — documents degradation ("lost in conversation") of LLM instruction-following across multi-turn interactions.
   Tags: [[multi-turn-dialogue]], [[llm-evaluation]]
3. Workshop award (iDEA-iSAIL, UIUC): **RAG Over Tables** — RAG over tabular/structured data.
   Tags: [[rag]], [[table-retrieval]]

---

## 4. AAAI 2026 (Singapore, Jan 20–27)

1. **ReconVLA** *(main-track Best Paper)* — reconstruct-from-vision-and-language agent work; recovery-vision-language-action.
   《ReconVLA》
   Tags: [[vla]], [[embodied-agents]]
   - Full author list not recovered this run (tentative).

2. Deployed Application Award (carried from prior wiki digest): production-facing applied ML contribution (details in prior conference digest).

3. Workshop-level award (only one found this cycle): DiGAN, AIAA workshop — (single-source, tentative).

> ⚠️ AAAI 2026 main-track best-paper title needs verification from the official AAAI-26 awards page in a future run.

---

## 5. KDD 2026 (Jeju, Aug 9–13) & KDD-adjacent

1. **GaussTrap: [backdoor attacks]** — Hong et al.; PDF confirms KDD 2026 venue.
   《GaussTrap：后门攻击》
   Tags: [[backdoor-attack]], [[adversarial-ml]] (single-source)

2. **EARTH** — Best Paper Honorable Mention (from prior wiki digest; full title/affiliations recorded there).
   Tags: [[knowledge-graph]], [[data-management]]

3. **STATIC** (Google) — KDD 2026 paper on [static analysis / code intelligence] (carried from prior digest).
   Tags: [[code]]

4. **XForecast** — KDD 2026 forecasting challenge won by a Kuaishou + USTC team; temporal/long-horizon forecasting.
   《XForecast 挑战赛》
   Tags: [[forecasting]], [[sequential-modeling]] (single-source)

5. MCML (Google) — KDD 2026 paper (from prior digest; noted as previously NeurIPS-linked in earlier coverage).

> ⚠️ KDD 2026 Best Paper award winners were not recoverable this cycle; KDD competition results (XForecast) were.

---

## 6. CVPR 2026 (Denver) — Best Papers

Source: [CVPR 2026 Best Papers](https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers) — 16,092 submissions → 4,089 accepted.

1. **Efficiently Reconstructing Dynamic Scenes One D4RT at a Time** *(Best Paper)*
  《D4RT：逐步高效重建动态场景》
   - Authors: Zhang, Le Moing, Koppula, Rocco, Momeni, Xie, Sun, Sukthanker, Barral, Hadsell, Ghahramani, Zisserman, Junlin Zhang, Sajjadi
   - Affiliation: Google DeepMind / UCL / Oxford
   - Innovation: dynamic scene reconstruction decomposed into small atomic units ("D4RTs"), enabling efficient incremental reconstruction of scenes with motion.
   - Tags: [[3d-reconstruction]], [[dynamic-scene]]

2. **Native and Compact Structured Latents for 3D Generation** *(Best Student Paper)* — "O-Voxel"
   《面向 3D 生成的原生紧凑结构化 Latent》
   - Authors: Tsinghua, Microsoft Research, USTC, Microsoft AI
   - Innovation: native structured (voxel-like) latent representation for 3D generative models — compact and structured rather than flattened.
   - Tags: [[3d-generation]], [[latent-representation]]

Also notable from CVPR 2026 cycle (prior digest + announcements):
- **TRELLIS.2** (Microsoft/Adobe) — 3D generation. Tags: [[3d-generation]]
- **SAM 3 Any-Shape** (Meta) — promptable segment anything incl. shape prompts. Tags: [[segmentation]]
- **NitroGen** — 3D. Tags: [[3d-generation]]
- **ChordEdit** — music/chord editing. Tags: [[music-generation]]

---

## 7. ACL 2026 (San Diego, Jul 2–7)

1. **The Imperfective Paradox in Large Language Models** *(Best Paper)*
  《Large Language Model 中的未完成悖论》
   - Innovation: documents a systematic linguistic paradox (aspectual reasoning) that LLMs fail to handle consistently.
   - Tags: [[llm-linguistics]], [[llm-evaluation]]

2. **MediEval** *(Outstanding Paper)* — medical-domain LLM evaluation benchmark.
   Tags: [[benchmark]], [[medical-llm]]
3. **CxMP** *(Outstanding Paper)* — [cxmp paper; full title pending]
   Tags: [[benchmark]] (tentative)
4. **Mapping the Circumplex of Affect** *(Best Theme Paper)* — affect/emotion representation mapping for NLP.
   Tags: [[affect-analysis]]
5. Test-of-Time awards went to 2016-era papers (e.g., work on literal translation / subword rare-word NMT lineage — Sennrich-style subword translation era; exact list pending).
   Tags: [[nmt]], [[subword]]

---

## 8. EMNLP 2025 (Suzhou, Nov 4–9) — Best Paper

1. **Infini-gram mini: Exact n-gram Search at the Internet Scale with FM-Index**
  《Infini-gram mini：基于 FM-Index 的互联网规模精确 n-gram 搜索》
   - Authors: Hao Xu et al. (University of Washington + Ai2)
   - Source: [UW News](https://news.cs.washington.edu/2026/01/29/allen-school-researchers-earn-emnlp-best-paper-award)
   - Innovation: FM-Index-based exact n-gram search compressed to run at internet scale (infini-gram lineage from the OLMo/Kenlm ecosystem) — cheap, exact corpus analysis for LLM data work.
   - Tags: [[n-gram-search]], [[fm-index]], [[data-engineering]]
   - Related: outstanding papers at EMNLP 2025 covered LLM-annotation/evaluation themes (details in official awards list).

---

## 9. SIGIR 2026 (Melbourne, Jul 20–24) — Awards

Source: [SIGIR 2026 Awards](https://sigir2026.org/en-AU/pages/program/awards)

1. **Best Paper — Why Advanced Encoders Lag on Sparse Retrieval? The Answer and an Approach to Bridging Vocabulary Gaps**
  《为什么先进 Encoder 在 Sparse Retrieval 上落后？——答案与弥合 Vocabulary Gap 的方法》
   - Authors: Zhichao Geng, Yang Yang
   - Innovation: diagnoses why newer dense encoders underperform on sparse retrieval (vocabulary gaps between encoder training and retrieval), then proposes a bridging method.
   - Tags: [[sparse-retrieval]], [[dense-encoders]], [[ir]]

2. **Best Student Paper — Topic-Specific Classifiers are Better Relevance Judges than Prompted LLMs**
  《Topic 特定分类器优于 Prompted LLM 作为相关性判官》
   - Authors: Gienapp, Potthast, Yates, Scells, Yang
   - Innovation: small topic-specific classifiers beat prompted LLMs as relevance judges — cost/quality argument for LLM-based labeling in IR pipelines.
   - Tags: [[relevance-judging]], [[llm-labeling]], [[ir]]
   - Wiki connection: echoes recurring wiki claims about small specialized models vs. general LLMs (cf. [[ai-vs-traditional-models]]).

3. **Best Short Paper — When RAG Disagrees: Detecting Latent Epistemic Conflict via Logit Interactions**
  《当 RAG 意见不一致：通过 Logit 交互检测潜在认知冲突》
   - Authors: Sadhu, Roy, Basu
   - Innovation: detects when retrieved evidence conflicts with parametric knowledge by inspecting logit interactions rather than generation text.
   - Tags: [[rag]], [[epistemic-conflict]]

4. **Test of Time — Learning to Rank with Selection Bias in Personal Search**
  《个性化搜索中带选择偏差的 Learning to Rank》
   - Authors: Wang, Bendersky, Metzler, Najork (Google)
   - Innovation: classic selection-bias-corrected LTR for personal search, now recognized a decade later.
   - Tags: [[learning-to-rank]], [[selection-bias]]

---

## 10. WWW 2026

Main-track award not recovered; workshop-level award found:

1. **GLOW Workshop Best Paper — ConceptFormer: Towards Graph-Native Grounding of Large Language Models via Latent Concept Injection**
  《ConceptFormer：通过 Latent Concept 注入实现 LLM 的 Graph-Native Grounding》
   - Authors: Barmettler, Bernstein, Rossetto (University of Zurich)
   - Innovation: injects latent concepts from graph structure into transformers so LLMs are grounded natively in a knowledge graph.
   - Tags: [[graph-grounding]], [[concept-injection]], [[llm-knowledge]]

---

## 11. CIKM 2025 (Seoul, Nov 10–14) — Awards

Source: [CIKM 2025 report (Yang)](https://www.cs.emory.edu/~jyang71/files/cikm2025report.pdf)

1. **Best Full Paper — Reconsidering the Performance of GAE in Link Prediction**
  《重新审视 GAE 在 Link Prediction 中的性能》
   - Authors: Ma, Wang, Wang, Zhang
   - Innovation: careful re-evaluation showing Graph Autoencoder link-prediction results are sensitive to evaluation protocol.
   - Tags: [[graph-autoencoder]], [[link-prediction]], [[evaluation-protocol]]

2. **Best Applied Research Paper — Climber: Toward Efficient Scaling [of data/graph processing]**
  《Climber：迈向高效扩展》
   - Authors: Xu, Wang, Guo, Guo, Xiao, Huang, Wu, Luo
   - Tags: [[data-management]] — already ingested: [[sources/cikm-2025-climber]]

3. **Best Student Full Paper — A Cost-Effective Framework to Evaluate LLM-based Relevance Judgements**
  《评估 LLM 相关性判定的低成本框架》
   - Authors: Merlo, Marchesin, Faggioli, Ferro
   - Innovation: cost-effective protocol for evaluating LLM-generated relevance judgments — complements SIGIR's "Topic-Specific Classifiers" award; IR community is converging on LLM-judging pitfalls.
   - Tags: [[relevance-judging]], [[llm-labeling]]

4. Runner-up — **Data-centric Prompt Tuning** (Peng, Yang, Fan, Shi)
   Tags: [[prompt-tuning]] (single-source)

---

## 12. RecSys 2025 (Prague, Sep 22–26) — Awards

Source: [RecSys 2025 Awards](https://recsys.acm.org/recsys25/awards)

1. **Best Full Paper — You Don't Bring Me Flowers: Mitigating Unwanted Recommendations Through Conformal Risk Control**
  《你没有给我带来花：通过 Conformal Risk Control 缓解不需要的推荐》
   - Authors: De Toni, Purificato, Gomez, Passerini, Lepri, Consonni (FBK)
   - Innovation: applies conformal risk control (distribution-free guarantees) to suppress unwanted/unsafe recommendations with provable risk bounds — safety guarantees entering mainstream recsys.
   - Tags: [[conformal-risk-control]], [[recommender-systems]], [[safety]]

2. **Best Short Paper — Beyond Top-1: Addressing Inconsistencies in Evaluating Counterfactual Explanations for Recommender Systems**
  《超越 Top-1：修正 Counterfactual 解释评估的不一致性》
   - Authors: Mohammadi, Peintner, Müller, Zangerle (TU Wien)
   - Innovation: shows top-1-based metrics are inconsistent for counterfactual-explanation evaluation; proposes corrected protocol.
   - Tags: [[counterfactual-explanations]], [[recommender-systems]], [[evaluation-protocol]]

3. RecSys 2026-related (from prior wiki coverage): **Self-Evolving Recommendation System** (YouTube/Google Gemini lineage, arXiv:2602.10226) — continual self-evolution of rec models.
   Tags: [[recommender-systems]], [[self-evolution]]

---

## 13. Top-lab fresh preprints (Oct 13–19, 2026 wave)

Source: `awesome-frontier-ai-papers` tracker (snapshot 2026-10-20), verified-affiliation arXiv entries. Excludes IDs already covered in today's sibling digests.

### 13.1 Agents & agentic RL

| Date | Lab | Paper | arXiv |
|---|---|---|---|
| 10-16 | Microsoft | Understanding KV Residency in Production-Scale Agentic LLM Workloads / 理解生产级 Agentic LLM 负载中的 KV 常驻 | [2610.22863](https://arxiv.org/abs/2610.22863) |
| 10-16 | Alibaba/Qwen | MultiAgent-OPD: End-to-End Training of Hierarchical Multi-Agent Systems with On-Policy Distillation / 层级多智能体系统的端到端 On-Policy 蒸馏训练 | [2610.23234](https://arxiv.org/abs/2610.23234) |
| 10-15 | Google/DeepMind | Decentralized LLM Workflows via Sequential Auctions / 基于序贯拍卖的去中心化 LLM 工作流 | [2610.22201](https://arxiv.org/abs/2610.22201) |
| 10-15 | Google/DeepMind | JevAgentHarness: Benchmarking, Deploying and Training Decision Models That Share Control with LLMs / 与 LLM 共享控制权的决策模型基准 | [2610.21412](https://arxiv.org/abs/2610.21412) |
| 10-15 | Amazon | MemComposer: Learning to Assemble Memories for LLM Agents via Reinforcement Learning / 通过 RL 学会组装 Agent 记忆 | [2610.21091](https://arxiv.org/abs/2610.21091) |
| 10-15 | Huawei/Noah | Mosaic: Multi-Session Agentic Reinforcement Learning / 多会话 Agentic RL | [2610.22174](https://arxiv.org/abs/2610.22174) |
| 10-15 | Alibaba/Qwen | Learning to Steer LLM Agents and Multi-Agent Systems / 学会操控 LLM Agent 与多智能体系统 | [2610.22316](https://arxiv.org/abs/2610.22316) |
| 10-15 | Tencent/Hunyuan | Tree-Aware Posterior Distillation for Long-Horizon Agentic Reinforcement Learning / 面向长程 Agentic RL 的树感知后验蒸馏 | [2610.23181](https://arxiv.org/abs/2610.23181) |
| 10-14 | ByteDance/Seed | DeltaStreamer: Towards Human-Like Agentic Streaming Video Understanding / 类人 Agentic 流式视频理解 | [2610.19849](https://arxiv.org/abs/2610.19849) |
| 10-11 | ByteDance/Seed | ObsSpec: Accelerating Agentic RL with Observation Speculation / 用 Observation 推测加速 Agentic RL | [2610.15246](https://arxiv.org/abs/2610.15246) |
| 10-07 | DeepSeek | StoreBench: A Live-Commerce Environment for Evaluating and Training Autonomous Operator Agents / 直播电商 Agent 评估与训练环境 | [2610.10942](https://arxiv.org/abs/2610.10942) |

### 13.2 On-Policy Distillation (dominant new trend)

A clear cluster: at least 7 labs now publish OPD variants within the same week — evidence that on-policy distillation has become the standard post-training recipe across US/China labs.

| Lab | Paper | arXiv |
|---|---|---|
| Alibaba/Qwen | Waypoint-OPD: Transferring RL-Induced Policy Shifts via Gated On-Policy Distillation | [2610.21601](https://arxiv.org/abs/2610.21601) |
| Alibaba/Qwen | Skill-Decoupled On-Policy Expert Distillation for Unified Vision-Language Models | [2610.22217](https://arxiv.org/abs/2610.22217) |
| ByteDance/Seed | Condition-Contrastive Extrapolation for On-Policy Distillation of Language Models | [2610.21195](https://arxiv.org/abs/2610.21195) |
| Huawei/Noah | MMSearch-OPD: Easy Made Hard, Hard Made Learnable for Long-Horizon Multimodal Search Agents | [2610.22240](https://arxiv.org/abs/2610.22240) |
| Huawei/Noah | FocusOPD: Structure-Guided On-Policy Distillation for Diffusion Models | [2610.21250](https://arxiv.org/abs/2610.21250) |
| Amazon | Compatibility Matters: Token-Level Teacher Selection in On-Policy Distillation | [2610.21234](https://arxiv.org/abs/2610.21234) |
| Tencent/Hunyuan | Tree-Aware Posterior Distillation (agentic, see above) | [2610.23181](https://arxiv.org/abs/2610.23181) |

Cross-lab synthesis candidate: "OPD is to 2026 post-training what RLHF was to 2024" — worth a dedicated [[on-policy-distillation]] concept page if a third ingest confirms the pattern.

### 13.3 Efficiency: KV cache, attention, compute budget

| Lab | Paper | arXiv |
|---|---|---|
| Baidu | RoLaQ: Joint Rotation and Range Calibration for 2-Bit KV Caches in Multi-Head Latent Attention | [2610.20686](https://arxiv.org/abs/2610.20686) |
| Baidu | FlashMask-3: Efficient and Expressive Mask-Aware Distributed Attention | [2610.17901](https://arxiv.org/abs/2610.17901) |
| Baidu | Virtual Head Attention | [2610.17959](https://arxiv.org/abs/2610.17959) |
| Microsoft | FastVLA: Task-Conditioned and Temporally Adaptive Visual Token Compression for Efficient VLA | [2610.22146](https://arxiv.org/abs/2610.22146) |
| ByteDance/Seed | One Model, Multiple Compute Budgets: Multi-Ratio ConceptMoE for Flexible Compute Across Turns | [2610.14074](https://arxiv.org/abs/2610.14074) |
| NVIDIA | One Block Ahead: Promoting Sampler State in Diffusion Language Models | [2610.19510](https://arxiv.org/abs/2610.19510) |

Related wiki claim: ties directly into `wiki/claims/rag-slm-model-collapse*` debate family (small vs. large models) and the LLM-efficiency chain (Hybrid Attention, Seer Attention, NSA lineage in prior digests).

### 13.4 Memory & context

| Lab | Paper | arXiv |
|---|---|---|
| ByteDance/Seed | Cortex: Consolidating Context into Parametric Memory / 将上下文固化为参数化记忆 | [2610.20399](https://arxiv.org/abs/2610.20399) |
| Baidu | MIRROR: From Imitation to Internalization in LLM Personalization | [2610.09795](https://arxiv.org/abs/2610.09795) |
| Microsoft | Recursive Reward Improvement via Adversarial Meta-Prompt Evolution | [2610.21040](https://arxiv.org/abs/2610.21040) |

### 13.5 RL post-training & reward hacking

| Lab | Paper | arXiv |
|---|---|---|
| Amazon | Multi-Reward Hacking: From Aggregation-Induced Drift to Trust-Anchored Defense / 多奖励 Hacking：从聚合漂移到信任锚定防御 | [2610.21404](https://arxiv.org/abs/2610.21404) |
| Alibaba/Qwen | ReFlow: Replay-Driven Decoupling for Efficient RL Post-Training | [2610.21640](https://arxiv.org/abs/2610.21640) |
| Huawei/Noah | When Pairwise Preferences Cycle: A Reliability-Anchored Preference Walk for Video GRPO | [2610.20089](https://arxiv.org/abs/2610.20089) |
| Alibaba/Qwen | MetaExp: Learning to Self-Improve through Experience via Verifiable Cross-Task Environment Scaling | [2610.21492](https://arxiv.org/abs/2610.21492) |

### 13.6 Benchmarks

| Lab | Paper | arXiv |
|---|---|---|
| Amazon | ANCHOR: Audio-Visually Grounded Chain-of-Thought Reasoning Benchmark | [2610.22964](https://arxiv.org/abs/2610.22964) |
| DeepSeek | Invent a Dataset: Measuring dataset generation abilities with zero seed | [2610.01674](https://arxiv.org/abs/2610.01674) |
| Google/DeepMind | OpenTWBench (Taiwan-domain knowledge eval; measurement apparatus shapes scores) | [2610.19848](https://arxiv.org/abs/2610.19848) |
| Microsoft | FDE-Gym: The Last Mile of AI Delivery | [2610.22350](https://arxiv.org/abs/2610.22350) |
| Baidu | FDE-Bench: Evaluating End-to-End Delivery from Underspecified Real-World Business Requests | [2610.14539](https://arxiv.org/abs/2610.14539) |
| NVIDIA | LADDER: A Long-Horizon Robot Manipulation Benchmark | [2610.18053](https://arxiv.org/abs/2610.18053) |

Note: FDE-Gym/FDE-Bench (Microsoft + Huawei + Baidu) form a cross-lab "underspecified real-world business request" benchmark pair — relevant to agentic code-execution evaluation.

### 13.7 Code & code execution

| Lab | Item | Link |
|---|---|---|
| OpenAI | Advancing coding in low-resource programming languages (research post) | [openai.com](https://openai.com/index/low-resource-programming-languages) |
| Google/DeepMind | 3DCodeVerse: Exploring 3D Worlds as Code | [2610.22341](https://arxiv.org/abs/2610.22341) |
| Baidu | SWEPatchTest: Evaluating Software Tests Beyond Reproduction | [2610.18004](https://arxiv.org/abs/2610.18004) |
| Microsoft | "To Boldly Go Where No One Has Gone Before": What Has AI Let Developers Unlock? | [2610.23708](https://arxiv.org/abs/2610.23708) |

### 13.8 Generative models (3D/video/diffusion)

| Lab | Paper | Link |
|---|---|---|
| Apple | The Design Space of Tri-Modal Masked Diffusion Models | [machinelearning.apple.com](https://machinelearning.apple.com/research/tri-modal-masked-diffusion) |
| Huawei/Noah | Motion- and Gravity-Aware Feedforward 3D Reconstruction | [2610.22177](https://arxiv.org/abs/2610.22177) |
| ByteDance/Seed | Few-Step Generation via Data-Space Iteration | [2610.12102](https://arxiv.org/abs/2610.12102) |
| Meta/FAIR | Muse Glimmer 30B: An On-Device Agentic Model (Oct 19) | [ai.meta.com](https://ai.meta.com/research/publications/muse-glimmer-30b-an-on-device-agentic-model/) |

### 13.9 Sequential modeling & forecasting

| Lab | Paper | arXiv |
|---|---|---|
| Amazon | PathFM: Fast Generative Forecasting of Multivariate Trajectories | [2610.22358](https://arxiv.org/abs/2610.22358) |
| Google/DeepMind | TimeCap: Scalable pipeline for captioning wearable health time-series | [2610.21274](https://arxiv.org/abs/2610.21274) |
| Google/DeepMind | Towards Continual Learning: Mitigating Forgetting With Subspace Tuning | [2610.22293](https://arxiv.org/abs/2610.22293) |
| Amazon | Ranking and Partitioning of Attention Heads for Sparse and Continual RL Fine-tuning | [2610.21336](https://arxiv.org/abs/2610.21336) |

### 13.10 AI safety & security (research posts)

- Anthropic (Oct 12): **AI models may be capable of self-replicating without access to a datacenter** — [link](https://www.anthropic.com/research/self-replicating-ai)
- Anthropic (Oct 12): **Strengthening our defenses against distillation attacks** — [link](https://www.anthropic.com/research/distillation-defenses)
- Anthropic (Oct 16): ECDSA curve origins reveal via Claude; quantum-circuit design with Claude.
- Google/DeepMind (Oct 15): SHIP: Structured and Hierarchical Insight with Privacy — [2610.21048](https://arxiv.org/abs/2610.21048)

### 13.11 Domain-specific (games / rec / ads)

- **Games**: Tencent/Hunyuan, **Player-1: Learning to Play from Synthetic Experience** (Oct 14) — game-playing agent trained on synthetic experience; strongest new games entry this cycle (verify arXiv ID on next pass).
- **RecSys**: Self-Evolving Recommendation System (YouTube/Google, RecSys 2026, arXiv:2602.10226) carried from prior coverage.
- **Advertising/CTR**: no strong new dedicated CTR/advertising paper surfaced in this cycle's searches — topic area remains thinner in award lists than recsys/IR. Flag as a **weak area** for future digests (single-source: prior wiki claim `claim/l2-vs-lr-predicting-click-through-rate` still stands un-updated).

---

## 14. Cross-cutting observations

1. **Diffusion dominates theory awards**: 3/6 ICML 2026 awards diffusion-related; CVPR 3D winners are generative; NVIDIA/Apple push diffusion LMs and masked diffusion. Connects to prior wiki claim `claim/masked-predictive-vs-autoregressive-models`.
2. **On-Policy Distillation is the recipe of the quarter**: 7+ OPD papers in one week across Qwen, ByteDance, Huawei, Amazon, Tencent — candidate new concept page `[[on-policy-distillation]]`.
3. **Evaluation-protocol papers winning awards at every IR/rec venue**: SIGIR (topic classifiers > prompted LLMs), CIKM (LLM relevance judging cost framework; GAE re-evaluation), RecSys (Beyond Top-1), EMNLP (infini-gram mini for corpus analysis). Meta-evaluation is having a moment — echoes Karpathy-adjacent "benchmarks shape behavior" themes (cf. OpenTWBench's "measurement apparatus shapes the score").
4. **Safety as dual-use**: ICML position paper award ("Censor's Toolkit") + Anthropic self-replication/distillation-attack posts + Amazon multi-reward-hacking — safety/alignment content is increasingly reflexive about its own externalities.
5. **Agentic RL infrastructure**: ObsSpec, Mosaic, Tree-Aware Posterior Distillation, JevAgentHarness, KV-residency study — the field is building the systems layer for multi-session/multi-agent training, not just algorithms.

---

## Provenance & gaps

- Award lists verified against official blogs: ICML (`blog.icml.cc`), NeurIPS (`blog.neurips.cc`), CVPR (`cvpr.thecvf.com`), SIGIR (`sigir2026.org`), RecSys (`recsys.acm.org`), EMNLP (UW News), CIKM (Emory report PDF).
- Not recovered this run (flagged in-line as tentative): AAAI 2026 main best-paper full details, KDD 2026 Best Paper, ACL outstanding-paper full author lists, NeurIPS 2025 award titles beyond the hivemind paper, Tencent Player-1 arXiv ID.
- arXiv bulk queries blocked by API rate limit — venue-tagged preprint sweeps should be retried in a later run.
