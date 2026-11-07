---
title: arXiv AI Search — Recent Papers (AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games)
type: synthesis
created: 2026-11-07
updated: 2026-11-07
sources:
  - https://arxiv.org/
  - http://export.arxiv.org/api/query
tags:
  - arxiv
  - ai
  - llm
  - agents
  - recommendation
  - sequential-modeling
  - reranking
  - ctr
  - advertising
  - generative-recommendation
  - game-ai
  - reinforcement-learning
  - retrieval
  - daily-digest
---

# arXiv AI Search — Recent Papers

**Date:** 2026-11-07  
**Scope:** Recent arXiv submissions (primarily 2026-10-29 to 2026-11-05) across AI, LLMs, recommendation, advertising, sequential modeling, CTR/ranking, and game AI.  
**Method:** Targeted arXiv API queries (`cs.AI`, `cs.CL`, `cs.LG`, `cs.IR`, `cs.MA`) sorted by submission date; deduplicated across query groups.  
**Note on affiliations:** arXiv metadata often omits structured institution/company fields for very recent submissions. Affiliations below are listed when explicitly available in arXiv metadata/author strings or clearly stated in the submission; otherwise marked as *not specified in arXiv metadata*.

---

## 1) LLMs, Agents & Reasoning

### 1. SwarmEvolve: Latent Agent Swarms for Evolutionary Discovery and Optimization
- **Authors:** Qile Jiang, George Em Karniadakis
- **Institution/Company:** Not specified in arXiv metadata
- **arXiv:** [2611.08483](https://arxiv.org/abs/2611.08483) (submitted 2026-11-05)
- **Categories:** cs.AI, cs.NE
- **Abstract:** LLM-guided evolutionary search uses AI agents to improve programs for mathematical and computational problems by iteratively refining solutions and combining high-scoring methods. However, the process is often slow because the LLM generates a long textual chain of thought for each round and must repeat this generation many times to maintain population diversity. We present SwarmEvolve, a framework in which hundreds of low-cost agents per round work in swarms, reason in latent space without decoding to text, and share information by passing KV caches. Each swarm studies the problem from a different angle. A novelty filter keeps the most distinct agent ideas by directly measuring the distances between the agents' hidden state vectors. Crossover of ideas happens naturally in latent space, as a summarizer agent receives the combined KV caches of all swarm members. On 21 problems in mathematical discovery and scientific computing, SwarmEvolve gets the highest average score and needs a median of only 3 to 8 minutes to reach the best scores that other state-of-the-art frameworks reach in 60 minutes. On several problems, SwarmEvolve with Qwen3 8B improves on the solutions that AlphaEvolve first found with frontier LLMs.
- **Key innovations:**
  - **Latent-space agent swarms:** hundreds of low-cost agents reason without text decoding, reducing generation overhead.
  - **KV-cache communication/crossover:** swarm members share information by passing KV caches; a summarizer combines caches for latent crossover.
  - **Novelty filtering in hidden-state space:** keeps diverse ideas by measuring distances between agent hidden vectors.
  - **Efficiency claim:** median 3–8 minutes to reach best scores that other SOTA frameworks reach in ~60 minutes (on 21 problems); reported improvements over AlphaEvolve-found solutions on some tasks using Qwen3 8B.

### 2. MedGraph: Maintaining Patient State with Graph Memory for Long-Term Medical Dialogue
- **Authors:** Donghua Zhang, Zizheng Wang, Ze Dong, Yiding Feng, Siyu Qian
- **Institution/Company:** Not specified in arXiv metadata
- **arXiv:** [2611.08433](https://arxiv.org/abs/2611.08433) (submitted 2026-11-05)
- **Categories:** cs.CL, cs.AI
- **Abstract:** LLM-based medical assistants that follow a patient across visits need a memory that keeps the patient's clinical state correct as it changes. We examine the errors of five memory systems on longitudinal medical dialogue and find three recurring causes: the retrieved evidence gives an outdated state, includes another person's health facts, or lacks a safety fact the answer depends on. We present MedGraph, a graph memory built for these three cases. Construction extracts dated facts from each session, attributes each fact to the person it describes, and links medication, diagnosis, and measurement records into chains that keep earlier states. Retrieval ranks the patient's chains as units, reads each chain at the time the question asks about, and adds the original dialogue text; a patient profile lists every recorded safety fact with every question. On MedMemoryBench, MedGraph has the highest overall accuracy with both a GPT and a Qwen backbone, 10.5 and 10.4 points above the strongest of five baselines, with efficient memory construction and answering in the GPT setting.
- **Key innovations:**
  - **Error taxonomy for longitudinal medical memory:** outdated state, cross-person fact leakage, missing safety facts.
  - **Graph memory with attribution and temporal chains:** dated facts, person attribution, and linked medication/diagnosis/measurement chains preserving history.
  - **Time-aware chain retrieval + safety profile:** ranks patient chains, reads state at queried time, adds original dialogue, and injects all recorded safety facts.
  - **Reported gains:** +10.5/+10.4 points over strongest baseline on MedMemoryBench (GPT/Qwen backbones).

### 3. StepBack: Step-Level Error-Localized Resampling for Efficient Test-Time Reasoning
- **Authors:** Yang Ouyang, Jung-Eun Kim
- **Institution/Company:** Not specified in arXiv metadata
- **arXiv:** [2611.08403](https://arxiv.org/abs/2611.08403) (submitted 2026-11-05)
- **Categories:** cs.AI, cs.CL, cs.LG
- **Comment:** NeurIPS 2026 (per arXiv comment)
- **Abstract:** Self-consistency (SC) is a widely used decoding strategy for improving chain-of-thought reasoning, but it requires sampling many complete reasoning trajectories with a preset budget. Its efficient variants reduce the cost mainly by stopping full-trajectory sampling early or distributing the number of samples across questions. In this paper, we propose StepBack, a step-level error-localized resampling method for efficient test-time reasoning. Given a small set of draft trajectories, StepBack localizes likely first error positions using lightweight signals and then resamples the detected error step and its suffix, followed by majority answer voting. Empirically, StepBack matches the accuracy of SC on average across seven mathematical reasoning and multi-hop QA benchmarks, while reducing token usage by up to 41.26%. In addition, by nature, StepBack can be combined with adaptive inference methods such as Adaptive Consistency, further improving their inference-time efficiency.
- **Key innovations:**
  - **Step-level error localization:** identifies likely first error positions in draft CoT trajectories using lightweight signals.
  - **Suffix resampling:** resamples only from the detected error step onward instead of regenerating full trajectories.
  - **Efficiency/accuracy tradeoff:** matches self-consistency accuracy on average across 7 math/multi-hop QA benchmarks with up to 41.26% token reduction; composable with Adaptive Consistency.

### 4. FedReason: Large Language Models as Weight-Space Meta-Aggregators for Heterogeneous Federated Learning
- **Authors:** Ali Mohammadi Ruzbahani, Abbas Yazdinejad, Hadis Karimipour
- **Institution/Company:** Not specified in arXiv metadata (corresponding author noted in arXiv comment)
- **arXiv:** [2611.08383](https://arxiv.org/abs/2611.08383) (submitted 2026-11-05)
- **Categories:** cs.CR, cs.AI
- **Abstract:** Federated learning servers combine client models with a fixed aggregation rule, and each rule in common use is designed for one kind of heterogeneity. We study whether a large language model (LLM) that inspects the client models can choose the rule itself, without any training on the server. In FedReason, the LLM is called every ten rounds. It analyses the weights by running code in a restricted server-side sandbox, sees only the printed results, may score a few candidates on a 500-image proxy set, and submits a short Python aggregation program. The server applies the program until the next call and falls back to FedAvg whenever its output is invalid. Full weight tensors never leave the server. We evaluated FedReason with Claude Opus 5.5 on CIFAR-10 and CIFAR-100 with ResNet-18 under Dirichlet label skew, width-heterogeneous sub-models and Byzantine clients, in 168 runs against 14 baselines. Across 12 paired label-skew runs it beat FedAvg by 1.26 percentage points on average (10 wins), and a control that spends the same per-round proxy budget on choosing among standard rules by 1.08 points. It was the strongest server-side rule on CIFAR-100 but did not beat SCAFFOLD, which changes client training. With three of ten clients malicious, it excluded all sign-flipping clients from the first round and stayed about one point below FLTrust without training a root model. Without proxy feedback, accuracy fell from 73.8% to 38.8% in one seed. A 60-round run cost 0.79 USD in API fees on average.
- **Key innovations:**
  - **LLM as meta-aggregator:** uses an LLM to inspect client model statistics and synthesize aggregation code, rather than using a fixed rule.
  - **Restricted sandbox + privacy boundary:** LLM runs analysis code server-side, sees only printed results, and submits Python aggregation programs; full tensors stay on server.
  - **Proxy-guided selection with fallback:** optional 500-image proxy scoring; server falls back to FedAvg on invalid programs.
  - **Empirical findings:** gains over FedAvg under label skew; strong Byzantine exclusion in sign-flip setting; proxy feedback is critical (73.8% → 38.8% without it in one seed).

### 5. Agent-R²: Scaling Agents for Realistic Productivity Work via Real-Source Data Synthesis
- **Authors:** Teng Pan, Zixuan Wang, Yuchen Yan, Qifei Wu, Yao Chen, Yingqi Qu, Ruiqing Zhang, Yongliang Shen
- **Institution/Company:** Not specified in arXiv metadata
- **arXiv:** [2611.08219](https://arxiv.org/abs/2611.08219) (submitted 2026-11-05)
- **Categories:** cs.CL
- **Abstract:** Large language models have made rapid progress in agentic reasoning and tool use, raising expectations for agents that can take over realistic productivity work from humans. However, current agents still struggle to finish such tasks, where success requires following long-horizon professional workflows, understanding heterogeneous file contexts, and producing usable deliverables under fine-grained requirements. A key bottleneck is the lack of scalable post-training data that reflects real work intent, authentic file environments, and deliverable-level evaluation. To close this gap, we introduce Agent-R², a real-source data synthesis framework that scales training data for realistic productivity work. Instead of relying on manually specified workflows or LLM-generated files, Agent-R² grounds synthesis throughout the pipeline in real occupational seeds, corpus-derived workflow evidence, and authentic web-sourced files. From 10k web-corpus candidates, Agent-R² distills 4k task instances that pair real multi-format attachments with fine-grained, deliverable-level rubrics. On this data, we train Agent-R²-4B via supervised fine-tuning and rubric-based reinforcement learning, improving both end-to-end productivity performance and file-grounded reasoning. Trained on only 4k instances, Agent-R²-4B surpasses Qwen3-235B-A22B-Thinking-2507 on both GDPval (51.0% vs. 48.0%) and OfficeQA (14.8% vs. 13.8%). Further analysis shows that Agent-R² mitigates shortcut behavior, where agents produce superficially plausible deliverables before sufficiently grounding, constructing, or verifying them, while promoting sustained exploration.
- **Key innovations:**
  - **Real-source synthesis pipeline:** grounds tasks in occupational seeds, corpus-derived workflow evidence, and authentic web-sourced multi-format files (not LLM-fabricated files/workflows).
  - **Deliverable-level rubrics:** 4k distilled instances with fine-grained evaluation criteria for realistic productivity outputs.
  - **Rubric-based RL post-training:** SFT + rubric-based RL improves file-grounded reasoning and end-to-end task completion.
  - **Efficiency claim:** Agent-R²-4B trained on 4k instances outperforms a much larger model on GDPval (51.0% vs 48.0%) and OfficeQA (14.8% vs 13.8%); reduces shortcut/plausible-but-unverified behavior.

### 6. Don't Prompt Your Agents. Equip Them: Skillware as a Modular Standard for Sovereign, Auditable, and Deterministic Capability Execution for Logical Systems
- **Authors:** Vladimiros Peilivanidis
- **Institution/Company:** ARPA Hellenic Logical Systems (per arXiv metadata from earlier query)
- **arXiv:** [2611.07652](https://arxiv.org/abs/2611.07652) (submitted 2026-11-05)
- **Categories:** cs.AI, cs.SE
- **Abstract:** Current autonomous logical systems rely on a fragile assumption: that language models should dynamically write code, guess API payloads, and memorize operational constraints through prompt engineering. In practice, this burns massive context windows, inflates API bills, and produces brittle agents that fail unpredictably in production. In this work, we present Skillware, an open architectural framework and capability registry that formally separates what an agent wants to do from how that task is executed. Instead of prompting models with loose text instructions or markdown files baptized as 'skills', Skillware equips them with modular, versioned software capability bundles. Much like skill hotkeys in video games that execute deterministically under fixed world rules, each bundle combines a typed JSON input contract, deterministic Python code, task directives, bundled datasets, and automated unit tests. In-process adapters translate these capabilities into native tool declarations for any model, from frontier cloud APIs to local open-weight runtimes with zero network latency. Evaluating 23 frontier and open-weight models across 368 benchmark conditions, we show that small local models (3B to 8B parameters) equipped with Skillware consistently outperform unequipped frontier models on complex multi-step workflows. They cut token usage by up to 84.8%, slash inference costs by up to 97.3%, and eliminate parameter errors entirely. True agent reliability does not come from larger models or longer prompts, but from equipping logical systems with verified, deterministic software.
- **Key innovations:**
  - **Skillware capability bundles:** modular, versioned bundles with typed JSON contracts, deterministic Python execution, directives, datasets, and tests.
  - **Intent/execution separation:** decouples *what* the agent wants from *how* it is executed; reduces prompt memorization and dynamic code guessing.
  - **Model-agnostic adapters:** translates bundles into native tool declarations for cloud/local models.
  - **Reported results:** 23 models / 368 conditions; equipped 3B–8B models outperform unequipped frontier models on complex workflows; up to 84.8% token reduction, 97.3% inference-cost reduction, and elimination of parameter errors (as reported).

---

## 2) Recommendation & Sequential Modeling

### 7. User Embeddings are Superpositions of Interpretable Behavioral Modes
- **Authors:** Jonathan Kozaczuk, Zheng Dong, Noyan Evirgen, Keivan Majidi, Eddie K. H. Ng, Chris Porter, Qi Zhao, Jia Geng, Changmao Li, Brandon R. Feng
- **Institution/Company:** Not specified in arXiv metadata
- **arXiv:** [2611.08487](https://arxiv.org/abs/2611.08487) (submitted 2026-11-05)
- **Categories:** cs.LG
- **Comment:** Accepted to NeurIPS 2026 (per arXiv comment)
- **Abstract:** User embeddings are central components of modern recommendation, personalization, and behavioral modeling systems. Though these embeddings can compactly encode rich behavioral information, they are inherently dense and opaque, limiting interpretability. To address this gap, we argue that user embeddings can be understood as sparse superpositions of interpretable behavioral modes. This structure is directly predicted by generative models of user behavior for linear embeddings and extends approximately to deep-learning representations by the superposition hypothesis. Superimposed modes can naturally be recovered by sparse dictionary learning methods, such as sparse autoencoders (SAEs), and recovered modes can be automatically named and queried in natural language. We validate mode recovery against known ground truth on synthetic data, where SAEs recover modes better than classical sparse baselines, including on transformer-encoded embeddings. We then apply the method to classical and transformer-based user embeddings from two real-world datasets. We also show how the corresponding natural-language labels enable zero-shot audience retrieval and characterization over embeddings never trained on text. The framework is post-hoc and model-agnostic, requiring no modification to the upstream embedding system.
- **Key innovations:**
  - **Superposition view of user embeddings:** interprets dense user vectors as sparse combinations of interpretable behavioral modes.
  - **SAE-based mode recovery:** applies sparse dictionary learning/SAEs post-hoc to linear and deep user embeddings.
  - **Natural-language labeling and querying:** recovered modes can be named and used for zero-shot audience retrieval/characterization over text-untrained embeddings.
  - **Model-agnostic interpretability:** no changes required to upstream embedding models; validated on synthetic and two real-world datasets.

### 8. Beyond Independent Predictions: Learning the Browsing Journey for Sequence-Level Re-ranking
- **Authors:** Jiayi Zhang, Jingxin Hai, Zhenjia Ma, Hongbin Pei, Dagui Chen, Han Zhu, Jian Xu
- **Institution/Company:** Not specified in arXiv metadata
- **arXiv:** [2611.07591](https://arxiv.org/abs/2611.07591) (submitted 2026-11-05)
- **Categories:** cs.IR
- **Abstract:** Re-ranking aims to present users with an ordered list that maximizes sequence-level utility. Industrial deployments widely adopt the Generator--Evaluator framework, where the generator proposes candidate sequences, and the evaluator scores them to select the best one for display. The fidelity of the evaluator's utility estimates thus directly governs recommendation quality. However, existing evaluators predominantly follow the Independent Behavior Modeling (IBM) paradigm, which simplifies the continuous user browsing journey into independent per-item predictions (e.g., CTR). This oversimplification ignores two physical realities: (i) a click can occur only after the item has been reached and impressed, and (ii) items compete for finite user attention. As a result, IBM produces systematically biased evaluations and suboptimal sequence selection. To address this, we propose a Joint Behavior Modeling (JBM) perspective that explicitly models the display → impression → click process to capture causal and competitive dependencies within a sequence. Building on JBM, we develop the Impression-Click Evaluator (ICE), a plug-and-play framework that (i) predicts a browsing-depth distribution to estimate per-position impression probabilities, (ii) leverages predicted impressions to suppress spurious context from unexposed items during click modeling, and (iii) introduces a click distribution matching objective to capture intra-sequence dependencies. Extensive offline experiments across diverse backbones, together with a 14-day online A/B test in the Taobao App (+0.70% clicks, +3.67% revenue) and full-traffic deployment, validate the effectiveness and robustness of our approach.
- **Key innovations:**
  - **Joint Behavior Modeling (JBM):** models display → impression → click as a causal browsing journey rather than independent per-item CTR predictions.
  - **Impression-Click Evaluator (ICE):** predicts browsing-depth/impression probabilities and conditions click modeling on likely exposure.
  - **Spurious-context suppression + distribution matching:** downweights unexposed items and adds click-distribution matching to capture intra-sequence dependencies.
  - **Industrial validation:** Taobao App 14-day A/B test reported +0.70% clicks, +3.67% revenue, plus full-traffic deployment (as reported).

### 9. Tasteply: Externalizing Stable and Situational Preference as Manipulable Spatial Objects
- **Authors:** DaEun Choi, Daniel Lee
- **Institution/Company:** Not specified in arXiv metadata
- **arXiv:** [2611.07851](https://arxiv.org/abs/2611.07851) (submitted 2026-11-05)
- **Categories:** cs.HC, cs.IR
- **Abstract:** Most recommender systems treat user preferences as a single signal to infer and optimize, yet human preferences are a mix of a stable preference and situational preferences that turn on and off depending on context. Through Tasteply, we externalize this preference structure as manipulable spatial objects. Tasteply represents each situational preference as an attractor and the stable preference as an underlying global field. Users can adjust their feed by moving around the space and adjusting the strength of the global field, turning the preference structure that remains latent within the model into something they can see and act on directly to steer the recommendation algorithm. Through an exploratory study (N=5), we found that this spatial control was effective, along with its limits and future direction as a means of manipulating preference-based recommendations.
- **Key innovations:**
  - **Stable + situational preference decomposition:** separates persistent taste from context-dependent preferences.
  - **Spatial externalization for user control:** situational preferences become attractors; stable preference becomes a global field users can manipulate.
  - **Direct steering interface:** turns latent preference structure into an interactive control surface for recommendation feeds (exploratory N=5 study).

---

## 3) CTR, Advertising & Generative Recommendation

### 10. BRIDGE: Bridging the Semantic Quantization Gap for Generative Recommendation
- **Authors:** Yatong Xiao, Mingjie Sun, Peng Wang, Wenjin Wu, Peng Jiang
- **Institution/Company:** Not specified in arXiv metadata
- **arXiv:** [2611.07425](https://arxiv.org/abs/2611.07425) (submitted 2026-11-05)
- **Categories:** cs.IR
- **Abstract:** Generative recommendation retrieves items by autoregressively generating Semantic IDs (SIDs), where an RQ-VAE quantizes each item into a hierarchical SID sequence that the decoder generates level by level. We identify an overlooked bottleneck in this paradigm: the Semantic Quantization Gap (SQG). Quantization derives SIDs from rich continuous signals, including codebook centroids, local neighborhood geometry, and level-wise entropy. However, the decoder receives only discrete identifiers and loses the semantic structure that shaped them. This mismatch manifests in three ways: a grounding gap, where the decoder lacks semantic anchors when target-side information is limited; a neighborhood gap, where token-level supervision discards inter-item similarity and exacerbates exposure bias; and a difficulty gap, where computation is allocated uniformly despite generation difficulty diminishing with depth. To bridge the SQG, we propose BRIDGE. Codebook-grounded latent reasoning injects frozen quantizer centroids as semantic anchors before SID generation. Privileged EMA self-distillation transfers neighborhood-aware knowledge from a teacher to an on-policy student, preserving inter-item geometry while mitigating exposure bias. Effort-aware recurrence allocates more computation to the challenging early levels and progressively reduces it with depth. Across three Amazon benchmarks, BRIDGE improves Recall@10 and NDCG@10 by 10.9% and 9.7% on average over the strongest baseline (up to 12.6% and 10.7%). In a one-week online A/B experiment on a large-scale e-commerce advertising platform with 5% traffic, BRIDGE improves eCPM by 0.65%.
- **Key innovations:**
  - **Semantic Quantization Gap (SQG):** diagnoses grounding, neighborhood, and difficulty gaps in SID-based generative recommendation.
  - **Codebook-grounded latent reasoning:** injects frozen RQ-VAE centroids as semantic anchors before discrete SID generation.
  - **Privileged EMA self-distillation:** transfers neighborhood-aware knowledge to an on-policy student to preserve geometry and reduce exposure bias.
  - **Effort-aware recurrence:** allocates more compute to early/harder SID levels and less later; reported offline gains (avg +10.9% Recall@10, +9.7% NDCG@10) and online eCPM +0.65% (5% traffic, 1 week).

### 11. OneTrans-GSR: A Generative Slate Ranking Paradigm Unifying Reranking and Mix-Ranking with One Autoregressive Transformer
- **Authors:** Feng Cheng, Yu-Hsuan Huang, Fengyi Wang, Chaofan Zhou, Zhennan Zhu, Huan He, Bo Zhang, Ruoqi Zhang, Zhanfeng Mo, Ziwei Liu, Lanyi Li, Yifeng Pan, Junhua Long, Ziqiu Zhou, Yue Lin, Shaowei Liu
- **Institution/Company:** Not specified in arXiv metadata
- **arXiv:** [2611.04720](https://arxiv.org/abs/2611.04720) (submitted 2026-11-03)
- **Categories:** cs.IR
- **Abstract:** Industrial recommender systems allocate substantial computation to pointwise candidate scoring, yet separate reranking and mix-ranking stages still assemble the final exposure slate using hand-crafted rules and specialized low-capacity models. Mix-ranking combines product cards, short videos, livestreams, and advertising cards supplied by distinct upstream business channels. Although these rules and models encode valuable domain knowledge, they are inherently limited in leveraging additional data and computation. They constrain the combinatorial space of candidate slates and determine objective trade-offs through manual tuning. To enable scalable and effective slate generation, we reformulate reranking and mix-ranking as a unified learning problem whose performance can improve with computation. Specifically, we instantiate this formulation across the reranking and mix-ranking stages and propose OneTrans-GSR, a single decoder-only policy that extends our deployed OneTrans backbone to generate the exposure slate end-to-end. During training, a reward model evaluates complete slates and guides reinforcement learning toward slate-level and long-term objectives. During decoding, business constraints are explicitly enforced. Offline evaluation shows that slate quality consistently improves as reward-model and policy compute increase. Deployed in a large-scale industrial recommendation system, OneTrans-GSR mixes heterogeneous content types within a unified slate. In online A/B tests, it improves GMV/u by 2.63%, advertiser value by 2.06%, and repurchase rate by 2.03%, while reducing end-to-end latency across the reranking and mix-ranking stages by 13%.
- **Key innovations:**
  - **Unified reranking + mix-ranking:** replaces separate rule/model stages with one decoder-only autoregressive slate-generation policy.
  - **Slate-level reward modeling + RL:** evaluates complete heterogeneous slates (products, videos, livestreams, ads) and optimizes long-term/slate-level objectives.
  - **Constraint-aware decoding:** enforces business constraints at generation time.
  - **Compute-scaling and deployment results:** slate quality improves with reward/policy compute; online A/B reported GMV/u +2.63%, advertiser value +2.06%, repurchase +2.03%, and 13% latency reduction.

### 12. SPADE: Spatiotemporal Preference Alignment and Diversity Enhancement for Local Search
- **Authors:** Chenxu Wang, Wenxuan Yang, Yueqi Mou, Shuxian Bi, Biao Tang, Peng Yan
- **Institution/Company:** Not specified in arXiv metadata
- **arXiv:** [2611.04662](https://arxiv.org/abs/2611.04662) (submitted 2026-11-03)
- **Categories:** cs.IR
- **Abstract:** Proactive query recommendation aims to suggest relevant search queries to users on the homepage of local service apps. Unlike conventional recommendation over a fixed item set, this requires open-set generation from a vocabulary of millions, where outputs must simultaneously align with user preference, match fine-grained spatiotemporal context, cover long-tail intents, and provide diverse alternatives within a few candidate slots. Existing approaches address these axes in isolation: standard tokenization suppresses long-tail queries, coarse location encoding misses fine-grained geographic demand, generic preference optimization fails to align with production impression-click distributions, and standard beam search collapses to near-duplicate outputs. We present SPADE (Spatiotemporal Preference Alignment and Diversity Enhancement), an end-to-end generative framework that jointly optimizes the generation space, contextual representation, preference distribution, and output slate quality through four components: Objective-Aligned BPE (OA-BPE) aligns subword merging with business value signals to boost long-tail query generation probability; Spatio-Temporal Adaptive Representation (STAR) replaces coarse location tokens with continuous multi-scale encodings and soft gating for precise spatiotemporal grounding; MARS-DPO (Multi-dimensional Adaptive Reward Sampling DPO) combines cross-domain pre-training with preference alignment on production impression-click data via composite rewards and adaptive hard negative sampling; and Sigmoid Diversity Beam Search (SDBS) improves intent coverage without sacrificing recall. Offline experiments on large-scale production data show that SPADE outperforms the strongest generative baseline by +5.6% HR@5, -40.3% GeoC@5, and +1.9% Exec@5. A one-week online A/B test confirms production impact: +1.88% Module CTR, +0.177% Search Volume, and +0.105% Search DAU.
- **Key innovations:**
  - **OA-BPE tokenization:** aligns subword merges with business-value signals to improve long-tail query generation.
  - **STAR spatiotemporal encoding:** continuous multi-scale location/time representations with soft gating for fine-grained local intent.
  - **MARS-DPO:** preference alignment on production impression-click data using composite rewards and adaptive hard negatives.
  - **SDBS decoding:** diversity-aware beam search to improve intent coverage; reported offline/online gains including +1.88% module CTR in A/B test.

### 13. Probabilistic Relevance Decisions for Semantic Retrieval
- **Authors:** Bahadır Tatar, Cevat Şener
- **Institution/Company:** Recruspace LLC (per author string in arXiv metadata)
- **arXiv:** [2611.08014](https://arxiv.org/abs/2611.08014) (submitted 2026-11-05)
- **Categories:** cs.IR
- **Abstract:** Dense similarity supplies reusable corpus representations, while probabilistic relevance decisions offer query-dependent document scoring. We compare dense-only BGE-M3 with TypeSafe Jev Noul and OpenAI Decisions Predicate scores on the official BEIR SciFact test benchmark. The study evaluates 300 official test queries using identical positive-enriched 100-document pools and full-corpus dense retrieval followed by reranking at candidate depths of 50 and 100. Unlike the controlled pools, neither dense prefix receives positive injection. Jev has the highest observed Recall@5 and nDCG@10 under the evaluated conditions. At depth 50, full-corpus nDCG@10 is 0.6413 for BGE-M3, 0.7545 with OpenAI and 0.7805 with Jev. Extending depth from 50 to 100 increases known-positive candidate recall but produces small, uncertain final-effectiveness changes. All four paired-bootstrap depth intervals include zero. Unique-condition API scoring cost approximately doubles, while compatible cached decisions reduce incremental expenditure. OpenAI returns many exact-zero scores, and secondary exact-tie randomization reveals ranking sensitivity without replacing deterministic primary results. These exploratory, unadjusted analyses support relevance decisions as a complement to dense retrieval within this protocol, without establishing general superiority, probability calibration or equivalence between depths.
- **Key innovations:**
  - **Probabilistic relevance decisions vs dense similarity:** frames reranking as query-dependent relevance decisions complementing reusable dense representations.
  - **Controlled BEIR SciFact comparison:** evaluates dense-only BGE-M3 against TypeSafe Jev Noul and OpenAI Decisions Predicate under matched pools and full-corpus reranking (depth 50/100).
  - **Cost/behavior analysis:** reports API cost doubling for unique-condition scoring, cache benefits, exact-zero/tie behavior, and bootstrap uncertainty (depth effects include zero).
  - **Measured effectiveness (reported):** depth-50 full-corpus nDCG@10 — BGE-M3 0.6413, OpenAI 0.7545, Jev 0.7805.

---

## 4) Games & Interactive AI

### 14. Discovering Learning Rules that Shape Others (DUOS)
- **Authors:** Hong Jun Lee, Ziyan Wang, Jun Wang, Stefanos Leonardos, Yali Du
- **Institution/Company:** Not specified in arXiv metadata
- **arXiv:** [2611.08335](https://arxiv.org/abs/2611.08335) (submitted 2026-11-05)
- **Categories:** cs.LG
- **Abstract:** In general-sum games, self-interested learners can reach outcomes that are poor for everyone, which has motivated methods that shape the opponent's learning. Methods like Learning with Opponent-Learning Awareness (LOLA), which differentiates through the opponent's learning process, and Model-Free Opponent Shaping (M-FOS), which uses model-free optimisation methods for long-horizon opponent shaping, have enabled mutual cooperation and exploitation of learners. However, these methods require access to the opponent's parameters, policy, rewards or learning rule during deployment. In single-agent reinforcement learning, update rules discovered by meta-learning have achieved state-of-the-art results (e.g. DiscoRL). These rules are separate from the policy they train and read only the agent's own experience. We hereby extend this framework to general-sum settings by introducing Discovered Update Rule for Opponent Shaping (DUOS). To the best of our knowledge, this is the first method to discover an update rule for an agent in general-sum games. DUOS meta-trains the rule to maximise the agent's expected return over its lifetime, and updates an inner network using the agent's own experience. We show that our discovered rule exhibits behaviour consistent with opponent shaping without reading opponent policies or parameters, and ranks 1st in normalised mean score and 1st in self-play among tournament entrants.
- **Key innovations:**
  - **Meta-learned opponent-shaping update rule:** discovers an update rule for general-sum games (DUOS) rather than hand-designing shaping dynamics.
  - **No opponent access at deployment:** shapes opponents using only the agent’s own experience, unlike LOLA/M-FOS-style requirements for opponent internals.
  - **Lifetime-return meta-objective:** trains the update rule to maximize expected lifetime return while updating an inner policy network.
  - **Reported behavior/performance:** exhibits opponent-shaping behavior without reading opponent policies/parameters; ranks 1st in normalized mean score and self-play among tournament entrants.

### 15. RIDGE: State-Conditioned Reward Blending for Behavioral Coverage in Deep RL Game Agents
- **Authors:** Arip Asadulaev, Artur Garipov, Andrey Kuznetsov, Mikhail Tseslik, Alexander Panov
- **Institution/Company:** Not specified in arXiv metadata
- **arXiv:** [2611.05601](https://arxiv.org/abs/2611.05601) (submitted 2026-11-03)
- **Categories:** cs.LG, cs.SE
- **Comment:** Conference of Games (per arXiv comment); 4 pages
- **Abstract:** A deep RL agent trained on a fixed persona reward plays one way: an Explorer keeps exploring while starving, a Survivor hoards on an empty map. Since each persona fixes its own reward, the only way to cover behaviors is to train one agent per persona. RIDGE trains a single agent on a mixed-objective MDP where the reward is a convex combination of persona rewards, blended via a state-conditioned weight function computed from handcrafted state features. The features encode abstract game situations rather than persona-specific signals, so the same formulation applies to any persona set and environment. A PPO agent trained with RIDGE covers 7 of 9 procedurally generated Crafter configurations; one agent per persona covers at most 5. RIDGE also discovers emergent strategies absent from any single-persona agent, such as harvesting wood while fleeing from zombies.
- **Key innovations:**
  - **State-conditioned persona reward blending:** convex combination of persona rewards with weights computed from handcrafted state features.
  - **Single-agent behavioral coverage:** replaces one-agent-per-persona with a mixed-objective MDP trained by PPO.
  - **Abstract situation features:** features target game situations rather than persona-specific signals, aiming for transfer across persona sets/environments.
  - **Reported coverage:** covers 7/9 procedurally generated Crafter configurations vs at most 5 for single-persona agents; discovers emergent hybrid strategies.

### 16. AceAction-5M: Hierarchical Goals for Generalist Action Learning Across 3D Game Worlds
- **Authors:** Xiancheng Ye, Nanyang Ye, Yangyang Wu, Feng Cheng, Jinchang Xu, Yuxi Li, Yu Chen, Dawei Cheng
- **Institution/Company:** Not specified in arXiv metadata
- **arXiv:** [2611.04241](https://arxiv.org/abs/2611.04241) (submitted 2026-11-03)
- **Categories:** cs.AI
- **Abstract:** Video games provide a practical setting for collecting vision-language-action (VLA) data, whose acquisition in physical environments is costly. Existing datasets, however, remain limited in scale and annotation richness, which restricts the development of generalist agents. We present AceAction-5M, a large-scale, hierarchical vision-language-action dataset for 3D gameplay, covering 500K annotated clips (over 5M frames) across 12 popular first/third-person titles and six genres. Each clip is labeled with executable low-level actions and corresponding high-level task descriptions. We introduce a unified annotation pipeline that combines model-assisted temporal segmentation, event detection, and human verification to ensure accuracy and consistency. To demonstrate the utility of AceAction-5M, we train a vision-language-action model that maps visual observations and language goals to low-level actions, achieving 95.8% execution success over 500 evaluation trajectories. AceAction-5M establishes a foundation for scalable VLA learning, multimodal reasoning, and generalist game agents.
- **Key innovations:**
  - **Large hierarchical VLA game dataset:** 500K clips / 5M+ frames across 12 3D games and 6 genres, with low-level actions and high-level task descriptions.
  - **Unified annotation pipeline:** model-assisted temporal segmentation + event detection + human verification.
  - **Downstream VLA training evidence:** reported 95.8% execution success over 500 evaluation trajectories for a trained vision-language-action model.

### 17. NPCBench: A Clinical Apprenticeship Benchmark for Multimodal Care-Pathway Reasoning in Nasopharyngeal Carcinoma
- **Authors:** Pengkai Wang, Wei-Wei Zhang, Yan Li, Min Tang, Zhitian Hou, Zeyu Liu, Guanghao Zhu, Yuanyi Wang, Yanggan Gu, Wenjun Wang, Minheng Ni, Congkai Xie, Zhijie Sang, Jianmin Wu, Ying Sun, Hongxia Yang
- **Institution/Company:** Not specified in arXiv metadata
- **arXiv:** [2611.08369](https://arxiv.org/abs/2611.08369) (submitted 2026-11-05)
- **Categories:** cs.AI
- **Abstract:** Current medical benchmarks typically break down clinical competence into isolated factual questions, single-image tasks, or static case vignettes. These tests score individual answers, but reveal less about whether a model can integrate subspecialty knowledge with multimodal evidence and track a patient's condition throughout a course of care. To close this gap, we introduce NPCBench, a clinical apprenticeship benchmark for nasopharyngeal carcinoma (NPC). NPCBench mirrors specialist training, from guideline and foundational knowledge to case planning, longitudinal review, CarePath integration, and open-ended consultation. It contains 4,777 component and consultation items and a 100-patient CarePath cohort with 417 scored diagnostic and care tasks. The episode-level evaluation tests whether diagnostic and care answers are jointly correct within a care pathway. By linking stepwise tasks to patient-level care trajectories, NPCBench evaluates whether models ground decisions in visual evidence, interpret changes in patient state, and meet clinical requirements in consultation. Across 30 evaluated models, we observe a composition gap: strong performance on individual tasks does not ensure jointly correct diagnostic and care answers for the same patient. Among 21 multimodal models, strict CarePath success reaches at most 23%. Paired controls and physician calibration further examine evidence grounding, longitudinal revision, and consultation judging.
- **Key innovations:**
  - **Care-pathway benchmark design:** evaluates multimodal reasoning across longitudinal patient trajectories, not just isolated QA/image tasks.
  - **Episode-level joint correctness:** tests whether diagnosis and care decisions are jointly correct within the same care pathway.
  - **Scale and structure:** 4,777 items plus a 100-patient CarePath cohort with 417 scored diagnostic/care tasks.
  - **Key finding:** a composition gap — single-task strength does not imply pathway-level correctness; strict CarePath success ≤23% among 21 multimodal models (as reported).

---

## Cross-cutting Observations

- **Agents are moving from prompting to systems design:** several papers target reliability/efficiency via latent coordination (SwarmEvolve), step-level resampling (StepBack), deterministic capability bundles (Skillware), and real-source productivity data (Agent-R²).
- **Recommendation/ranking is shifting toward sequence, slate, and generative objectives:** JBM/ICE models browsing journeys, OneTrans-GSR unifies reranking+mix-ranking as slate generation, and BRIDGE addresses semantic loss in SID-based generative recommendation.
- **Industrial constraints remain central:** multiple rec/ads/search papers report online A/B tests, latency, traffic percentages, or production deployment details; reported gains should be interpreted in their platform context.
- **Game AI spans both decision-making and data infrastructure:** DUOS targets learning dynamics in general-sum games, RIDGE targets behavioral coverage in RL agents, and AceAction-5M provides large-scale VLA data for generalist game agents.
- **Affiliation metadata is incomplete on recent arXiv submissions:** for rigorous provenance, follow each arXiv link to the PDF/author pages or later conference/journal versions.

---

## Source / Reproducibility Notes

- Queries were executed against `export.arxiv.org/api/query` on 2026-11-07, sorted by `submittedDate` descending.
- Query themes included: LLM/foundation models, AI agents/reasoning, recommendation/sequential modeling, CTR/click-through/advertising/reranking/generative recommendation, and game/NPC/self-play/video-game agents.
- This report is a curated synthesis (17 papers) from the retrieved/deduplicated result set, selected for coverage across the requested domains and recency.
- All performance numbers are **as reported by the papers/authors** unless independently verified; this report does not reproduce experiments.
