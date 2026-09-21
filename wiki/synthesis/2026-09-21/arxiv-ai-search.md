---
title: "arXiv AI Research Paper Search Report"
type: synthesis
created: 2026-09-21
updated: 2026-09-21
sources: [arxiv.org]
tags: [arxiv, AI, LLM, recommendation, advertising, sequential-modeling, CTR, games, agent-eval, agent-memory, long-context, RAG, security, unlearning, speculative-decoding, attention, tokenizer, world-models, quantum-games, game-logic, daily-digest]
---

# arXiv AI Research Paper Search Report — 2026-09-21

Generated: 2026-09-21 (Monday). **Topic-targeted sweep of the fresh Monday 21 Sep 2026 mailing** (IDs **2609.20823–2609.22064+**; the same window today's `arxiv-daily` already mined). This report re-mines that window and features the **unclaimed remainder** across the target topics (AI / LLM / recommendation / advertising / sequential modeling / CTR / games). **609 unique IDs parsed** from 10 category listing pages, **390 in-window**, **342 unclaimed** after `arxiv-daily` claimed 49; **21 papers featured in full + 6 runner-ups**. Every featured/runner-up ID was **grep-verified 0 hits in `wiki/`** at selection time.

**Methodology**: The public arXiv API (`export.arxiv.org`) was reachable this window (used for shortlist abstract retrieval); full ID coverage came from direct page fetches of `/list/{cat}/new` for **cs.AI, cs.LG, cs.IR, cs.CL, cs.GT, cs.MA, cs.NE, cs.SI, cs.CY, cs.CV** (609 unique IDs; 390 within the current 20823+ window). ~40 titles keyword-screened on target topics, full abstracts fetched for 24, **21 featured + 6 runner-ups**. Probe HTML/API XML cached under the pre-approved temp dir `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/arxiv-search/` and kept for same-day sibling dedup checks. Institutions are author-affiliation inferred where arXiv does not print them (marked *tentative*).

> **Dedup note**: `arxiv-daily` (2026-09-21) already claimed the auto-bidding/oCPX cluster (OneBid, ADAPT), the production rec/search papers (hybrid GPU-CPU retrieval, EvoPilot, DSRec, APCL, ODU), the long-context serving papers (RBS-Attention, ETA, TierKV, SpecQuant), the post-training/RL cluster (GVPO++, λ-GRPO, repulsive/attractive teachers, SWE-Proof), the world-model/game cluster (TaxiGPT, GameASG-Bench, RecreationWorld), and the eval cluster (TrustReviewer, judge-panel, PIR, ETD, RegimeAbstain). Those sets are **not re-featured** here; the featured set below is the genre-diverse unclaimed remainder.

## Summary Statistics

| Scope | Value |
|---|---|
| Window covered | Mon 21 Sep 2026 mailing; IDs 2609.20823–2609.22064+ |
| Categories parsed | cs.AI, cs.LG, cs.IR, cs.CL, cs.GT, cs.MA, cs.NE, cs.SI, cs.CY, cs.CV |
| Unique IDs parsed | 609 (390 in-window; 342 unclaimed after today's daily's 49) |
| Featured in full in this report | 21 papers (6 sections) + 6 shortlisted runner-ups |
| Direct advertising / CTR / pCTR papers | **0** (consistent with the ~8–9-window daily-layer drought; ads/auto-bidding lives in `arxiv-daily`, which took OneBid + ADAPT) |
| Target-topic fresh content | Rec/Rank tooling (AutoRecLab, news-rec engineer study), agent memory & eval (DLD-RL, production 574-run bench, next-turn gap, AutoViewMem, MDL controller), LLM runtimes & attention primitives (TinyCeNN-LM, abstention/noise-filtering, phonemic tokenizer, RheoSampling), unlearning/steering (GUARD, task vectors, latent-to-language gap), RAG/agent security (micro-collaborative poisoning, Loopjacking), games/game-logic & game theory (GameLogicBench, MORM, MEFPIA, Colonel Blotto deterrence), NTPP forecasting |
| Dedup | All 26 curated IDs grep-verified 0 hits in `wiki/` + absent from today's `arxiv-daily` claimed set |

**Theme of the window (unclaimed remainder)**: the Monday remainder concentrates **agent & memory engineering** (deepresearch long-context RL boost, production-agent benchmarking fidelity, the "better next-turns ≠ better agents" gap, memory decision/self-organizing views), **LLM internals & runtimes** (cellular-recurrent attention replacement, wafer-thin softmax abstention/noise-filtering primitives, phonemic tokenization, stochastic dynamic-tree speculative decoding), **security primitives in concrete products** (micro-collaborative RAG poisoning 108-config sweep; Loopjacking reproduced in shipped agents), **unlearning trajectory quality for reasoning models**, and a **games cluster** (behavioral-tick evaluation of coding agents in Godot, MORM multiplicative-optimism regret, quantum-game equilibrium search, Colonel Blotto deterrence with information structures). Recommendation-layer content is thin (2 papers, RecSys tooling/industry-practice) and **no CTR/advertising paper remains** here — the daily took both ads papers.

---

## 1 Recommendation, Ranking & RecSys Tooling

### 1.1 AutoRecLab — Describe the Experiment, Get the Code! (2609.21863)
- **Title**: AutoRecLab: Describe the Experiment, Get the Code!
- **Authors**: Moritz Baumgart, Philipp Meister, Justus Krell, Michael Schmidt, Bela Gipp, Joeran Beel
- **Institution**: University of Wuppertal-aligned (Gipp, Beel; tentative)
- **Date**: Announced 21 Sep 2026 (cs.AI; online)
- **arXiv**: https://arxiv.org/abs/2609.21863
- **Abstract**: Empirical evaluation is central to RecSys research, but turning experimental designs into executable code is manual and error-prone. **AutoRecLab** is a Python-based autonomous RecSys lab that automates recommender experiments from natural-language prompts: given a research idea it derives explicit experiment requirements, builds and validates a prototype, and iteratively expands it into the requested full experiment. The workflow combines **RAG for documentation lookup, static type verification, and execution-steered tree search**. In a baselining run it autonomously implements an explicit-to-implicit feedback conversion study; across six algorithms and three datasets, **8 of 9 runs succeed at an average cost of ≈$1/run** with GPT-5.4-mini.
- **Key Innovations**: (1) natural-language → executable RecSys experiment automation (a first for the RecSys tooling line); (2) execution-steered tree search + static type verification as the correctness loop; (3) cost modeling (~$1 per successful experiment) making broad ablation sweeps practical.
- **Venue**: Preprint (system/demo).

### 1.2 Do We Care About Personalization and Explainability? — News Recommendation Engineers (2609.21547)
- **Title**: Do We Care About Personalization and Explainability? An Interview Study with News Recommendation Engineers
- **Authors**: Jasmin Kareem, Siddharth Mehrotra, Martijn C. Willemsen, Maarten de Rijke
- **Institution**: University of Amsterdam / TU Eindhoven-aligned (de Rijke, Willemsen; tentative)
- **Date**: Announced 21 Sep 2026 (cs.HC / cs.IR)
- **arXiv**: https://arxiv.org/abs/2609.21547
- **Abstract**: Explainability research in recommender systems centers on end users, overlooking the builders/maintainers and use cases like model debugging. This study examines how news engineers and technical stakeholders perceive and implement personalization and explainability in practice, via **15 semi-structured interviews across nine news organizations** spanning diverse regions (public and private sectors). Findings: personalization is **not always a straightforward or desirable choice** for news orgs (user tracking, editorial control, resource constraints limit adoption); even in production personalized news rec, **explainability is rarely prioritized**, with day-to-day operational demands taking precedence over longer-term transparency goals; definitions of explainability vary widely, though some organizations show promising internal practices and visualization tools that bridge engineering teams and newsrooms. Provides actionable guidelines for adopting explainability within a news-personalization pipeline.
- **Key Innovations**: (1) first interview study of *news-recommendation engineers* (not users) on explainability; (2) evidence that explainability is treated as operational debt, not product value; (3) concrete adoption guidance for a news-personalization pipeline.
- **Venue**: Preprint.

---

## 2 Sequential Modeling, NTPP & LLM Runtimes

### 2.1 Probabilistic Forecasting of Business Process Executions with Neural Temporal Point Processes (2609.21382)
- **Title**: Probabilistic Forecasting of Business Process Executions with Neural Temporal Point Processes
- **Authors**: Jiaxin Yuan, Daniela Grigori, Han van der Aa
- **Institution**: INRIA Paris / University of Mannheim-aligned (tentative)
- **Date**: Announced 21 Sep 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.21382
- **Abstract**: Operators of service-based systems act on forecasts of how a running execution will continue, and a forecast is actionable only if its reliability is known. Mainstream DL models for this task are discriminative and deterministic (single next activity + single remaining-time estimate, no distribution). This paper casts the problem as **generative sequence modeling with marked temporal point processes**, which define a joint density over the next mark and its inter-event time and deliver predictive distributions by construction. Real event logs violate the simple-point-process assumption (consecutive events frequently carry identical timestamps) — the model handles such **ties explicitly**, combining a transformer encoder with a **mixture decoder over inter-event times**, trained by exact log-likelihood. On ten public logs: matches discriminative baselines on point accuracy, **dominates on calibration and sharpness of remaining-time distributions**, and is cheapest at inference (full predictive distribution in one forward pass, no sampling).
- **Key Innovations**: (1) generative marked-NTPP framing of business-process forecasting (reliability by construction); (2) explicit handling of timestamp ties that break the simple-point-process assumption; (3) exact log-likelihood training with a transformer + mixture decoder — cheaper and better-calibrated than discriminative baselines.
- **Venue**: Preprint.

### 2.2 TinyCeNN-LM — Quality-Gated Conversion of Pretrained Attention (2609.21139)
- **Title**: TinyCeNN-LM: Quality-Gated Conversion of Pretrained Attention with CeNN-Inspired Cellular-Recurrent Layers
- **Authors**: Kabeh Mohsenzadegan, Vahid Tavakkoli, Kyandoghere Kyamakya
- **Institution**: University of Klagenfurt-aligned (Kyamakya; tentative)
- **Date**: Announced 21 Sep 2026 (cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.21139
- **Abstract**: Replacing attention in a pretrained LM is a *compatibility* problem: a plausible substitute may alter representations expected by later layers. **TinyCeNN-LM** introduces a **quality-gated post-training conversion** framework using CeNN-inspired cellular-recurrent layers with bounded local processing, compact recurrent memory, routing, fusion, and accept-or-rollback validation. Three implementations studied (Integrated Memory, MemoryFusion, PDelta3-GDN2-CLVR+Local32). Strict PDelta3 conversion accepts a layer only when representation and NLL criteria pass fixed thresholds: on SmolLM2-135M, layers 0–2 accepted (cumulative ΔNLL=+0.01209) while layer 3 is **rejected despite acceptable NLL because representation fidelity fails**; on Qwen3.5-0.8B, full-attention layers 3/7/11 accepted (final ΔNLL=+0.02073). Integrated Memory keeps perplexity within −0.07%/+0.93% while reducing total cache up to 6.01%.
- **Key Innovations**: (1) conservative, *quality-gated* structural conversion (accept-or-rollback per layer) rather than blanket attention replacement; (2) representation-fidelity gating catching failures NLL alone misses; (3) a concrete design point for the SSM/linear-attention-replacement debate — conversion works only where fidelity gates pass.
- **Venue**: Preprint.

### 2.3 Abstention and Noise Filtering — Two Missing Primitives of Softmax Attention (2609.22005)
- **Title**: Abstention and Noise Filtering: Two Missing Primitives of Softmax Attention
- **Authors**: Richard Zhe Wang
- **Institution**: — (single author; tentative)
- **Date**: Announced 21 Sep 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.22005
- **Abstract**: Gating the value pathway of attention reportedly improves LM pretraining, but prior studies disagree on *why*. The paper argues gates supply two different things softmax attention lacks — (**1) abstention** (an attention head emitting nothing, bypassing the normalize-to-one requirement) and (**2) noise filtering** (suppressing interference from superposed features in the residual stream). In matched models from 10M–350M: the **benefit of abstention declines with scale, while noise filtering's benefit increases** (abstention ≈ all the gain at 10M, filtering ≈ most at 350M); the best model at every scale has both primitives; and injecting controlled interference into a head's values confirms the gate removes it, with each gate form having a characteristic blind spot. Both primitives add negligible parameters and remain KV-cache compatible.
- **Key Innovations**: (1) resolves the "why does gating help" debate by decomposing gates into abstention + noise filtering with opposite scaling trends; (2) scale-dependent attribution (10M vs 350M) as a new fact for attention-primitive design; (3) practical: both primitives are cheap and cache-compatible.
- **Venue**: Preprint.

### 2.4 Beyond Atomic Tokens — Factorizing Syllables for LM Pretraining (2609.21362)
- **Title**: Beyond Atomic Tokens: Factorizing Syllables for Language Model Pretraining
- **Authors**: Nghia Hieu Nguyen, Thai Bao Huynh, Binh-An Dinh-Le, Phu Gia Hoang, Dat Tien Nguyen, Kiet Van Nguyen, Ngan Luu-Thuy Nguyen
- **Institution**: Vietnam National University / UIT-aligned (tentative)
- **Date**: Announced 21 Sep 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2609.21362
- **Abstract**: Conventional tokenizers treat text as characters or statistical subwords, overlooking the internal phonological structure of syllables. **Phonemic Tokenizer**: converts each syllable (Vietnamese/Chinese) to IPA and factorizes it into three phonological components — **onset, rime, tone** — jointly occupying one contextual position (syllable-level sequence length preserved, representation shared across phonologically related syllables), with character-level fallback. Deterministic, **no corpus-dependent vocabulary learning**, vocabularies of only **112 entries (Chinese) / 256 (Vietnamese)**. Higher Rényi efficiency in both languages, Fertility exactly 1 on a standard Vietnamese syllable dictionary, generally shorter Vietnamese sequences. Instantiated as **PhonemicBERT** (factorized component embeddings + three prediction heads reconstructing masked syllables): competitive-or-better than character/subword/SubChar under controlled Chinese pretraining, and competitive with established Vietnamese/multilingual pretrained models.
- **Key Innovations**: (1) phonological factorization (onset/rime/tone) as a tokenization primitive — 100× smaller vocabularies; (2) representation sharing across phonologically related syllables; (3) PhonemicBERT confirms the approach on real pretraining with competitive downstream results.
- **Venue**: Preprint.

### 2.5 RheoSampling — Stochastic Dynamic-Tree Speculative Decoding (2609.21827)
- **Title**: RheoSampling: Resolving the One-Hot Dilemma in Stochastic Dynamic-Tree Speculative Decoding
- **Authors**: Qiao Hu, Yepeng Weng, Bo Zhang, Takehisa Yairi
- **Institution**: University of Tokyo-aligned (Yairi; tentative)
- **Date**: Announced 21 Sep 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2609.21827
- **Abstract**: Dynamic-tree speculative methods (EAGLE-3) excel under greedy decoding via deterministic top-K expansion and global pruning, but under stochastic decoding (T>0) they **collapse the draft distribution into one-hot probabilities**, crashing acceptance rate. Core problem: the same probability distribution serves two conflicting tasks — tree construction and token verification. **RheoSampling decouples them**: a sampled token receives a *proxy probability* for tree expansion/pruning alongside its *true* sampling probability for verification (injecting a sampled token among deterministic top-K slots). Claimed **first dynamic-tree method with both context-aware top-K construction and stochastic sampling while maintaining losslessness**, established via equivalence-class analysis compressing the stochastic tree space. OT-based verification + sparse-draft mechanism translate theory into efficiency; improved acceptance and speedup over SOTA dynamic-tree methods.
- **Key Innovations**: (1) names and resolves the one-hot dilemma of stochastic dynamic-tree decoding via role-decoupled probabilities; (2) lossless guarantee via equivalence-class compression of stochastic tree space; (3) a template for analyzing stochastic tree structures.
- **Venue**: Preprint.

---

## 3 LLM Post-Training, Unlearning & Steering

### 3.1 GUARD — Natural Forgetting in Large Reasoning Models (2609.21677)
- **Title**: GUARD: Natural Forgetting in Large Reasoning Models via Guided Answer-Reasoning Distillation
- **Authors**: Zeyu Yan, Guanghao Zhou, Minghui Qiu, Ming Gao, Cen Chen
- **Institution**: academic + industrial (Qiu/Ming Gao; tentative)
- **Date**: Announced 21 Sep 2026 (cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.21677
- **Abstract**: Unlearning in large reasoning models (LRMs) is harder because protected facts / unsafe rationales may surface in intermediate CoT traces before the final answer. Existing unlearning objectives suppress target content or redirect representations but never specify how the post-forgetting trajectory should continue → hallucinated substitutes, malformed boundaries, repetitive outputs. **GUARD** learns a **natural forgetting trajectory**: a coherent non-disclosing CoT followed by a stable refusal-style answer replacing the original disclosure — converts model-generated unsafe disclosures into safe-exit trajectories, aligns a frozen LRM via guidance tokens, and distills guided behavior into parameters. Introduces **NFRS (Natural Forgetting Reasoning Score)** capturing structural stability, fluency, and unsupported substitutes (beyond leakage). On R-TOFU + a STAR-1-derived harmful-intent setting, GUARD substantially reduces unsafe/privacy disclosures across two distilled LRMs while preserving reasoning utility.
- **Key Innovations**: (1) natural-forgetting-trajectory objective (trajectory quality, not just suppression); (2) NFRS metric for replacement quality beyond leakage; (3) works on distilled LRMs while preserving reasoning utility.
- **Venue**: Preprint.

### 3.2 Geometry of Values — Task Vector Composition for Ethical Alignment (2609.21094)
- **Title**: Geometry of Values: Task Vector Composition for Ethical Preference Alignment in Language Models
- **Authors**: Utkarsh Agarwal, Monojit Choudhury
- **Institution**: MBZUAI-aligned (Choudhury; tentative)
- **Date**: Announced 21 Sep 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2609.21094
- **Abstract**: LLMs deployed where clashing moral values must be weighed still exhibit hidden biases and brittle instruction-following across languages. Introduces a **12,000-instance dataset** of two-option dilemmas covering pairwise value conflicts (Honesty vs Justice, Justice vs Autonomy, Autonomy vs Honesty) with translations into Hindi/Arabic/Spanish/Chinese. GPT-5-mini consistently favors **Honesty over Autonomy** across all five languages policy-free; Llama-3.2-1/3B show strong first-option bias, but plain FT and DPO remove it (>98%). To decouple dataset correlations from abstract values, proposes **task-vector transfer**: compute a value-preference task vector, **orthogonalize it against the general instruction-following vector**, enabling task arithmetic that isolates the specific value preference (and successfully flips the model's stance).
- **Key Innovations**: (1) 12k multilingual value-dilemma dataset (5 languages, pairwise conflicts); (2) empirical cross-lingual bias map (Honesty>Autonomy universal in GPT-5-mini); (3) orthogonalized task-vector arithmetic isolates value preference from general instruction following.
- **Venue**: Preprint.

### 3.3 When Steering Fails in Latent Reasoning — A Latent-to-Language Transition Gap (2609.21662)
- **Title**: When Steering Fails in Latent Reasoning: A Latent-to-Language Transition Gap
- **Authors**: Gaoxiang Huang, Lei Qi
- **Institution**: Southeast University-aligned (tentative)
- **Date**: Announced 21 Sep 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2609.21662
- **Abstract**: Activation steering is widely used to control LMs during explicit CoT, motivating extension to **latent/continuous CoT**. Finding: steering continuous thoughts produces **substantially weaker effects on subsequent language generation** than steering explicit CoT, even at comparable hidden-representation displacement. Task information remains identifiable in continuous thoughts (so it's not absence of signal), leading to a hypothesized **latent-to-language transition gap**: an intervention in latent space fails to transfer to language generation. Two supporting results: the output distribution **changes abruptly at the transition boundary**, and task-related directions exert **much weaker bidirectional control in latent CoT than in explicit CoT**. The transition interface is identified as a central target for evaluating/designing latent-steering methods.
- **Key Innovations**: (1) identifies and names the latent-to-language transition gap (first controlled comparison latent vs explicit CoT steering); (2) task information is present yet interventions don't transfer — negating a "no signal" explanation; (3) sharp transition-boundary evidence making the interface the design target.
- **Venue**: Preprint.

---

## 4 Agents: Long-Context, Evaluation, Memory

### 4.1 Boosting Deepresearch and Long-Context Ability via Self-Generated Rollouts (2609.20844)
- **Title**: Boosting Deepresearch and LongContext Ability with Self-Generated Deepresearch Rollouts Traces
- **Authors**: Zihan Wang, Hao Wang, Boyuan Jiang, Yiqun Zhang, Shi Feng, Xiaocui Yang, Yiwen Ye, Jianghang Lin
- **Institution**: — (academic; tentative)
- **Date**: Announced 21 Sep 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2609.20844
- **Abstract**: Deepresearch (DR) agents interact with real web environments via multi-turn search/visit, so contexts grow rapidly. Even after DR Agentic RL (DR-RL), **61.6% of remaining prediction errors are attributable to insufficient long-context understanding** (long-context hallucination, failed cross-document evidence integration). Proposes **DR Rollouts to LongContext-QA (DR-to-Long)**: repurpose DR-RL trajectories (search histories, visited webpages, evidence snippets, answer supervision), replacing compact snippets/webpage summaries with the **full contents of their URLs** → substantially longer multi-document contexts while preserving evidence relationships. Then **DLD-RL** (DR→LongQA→DR): short DR-RL stage to collect rollouts → converted to LongQA instances at zero annotation cost → LongQA-RL to strengthen long-context → full DR-RL to continue DR capability. DLD-RL outperforms standard DR-RL by **7.3%** on three deepresearch benchmarks and improves **13.5%** on three long-context benchmarks.
- **Key Innovations**: (1) quantifies the long-context bottleneck of DR-RL (61.6% of errors); (2) zero-annotation trajectory→LongQA data conversion (DR-to-Long); (3) DLD-RL curriculum (DR→LongQA→DR) with gains on both deepresearch and long-context benchmarks.
- **Venue**: Preprint.

### 4.2 Efficient Benchmarking in Production — 574-Run Study of an Evolving LLM Agent (2609.21267)
- **Title**: Efficient Benchmarking in Production: A Study of an Evolving LLM Agent
- **Authors**: Yining She, Lei Lin
- **Institution**: — (industrial; tentative)
- **Date**: Announced 21 Sep 2026 (cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.21267
- **Abstract**: Production LLM agents are evaluated repeatedly as they evolve, but full agent benchmarks are costly to rerun. Studies efficient recurring evaluation for a **production analytics agent serving tens of thousands of MAU**, using **574 historical benchmark runs** split into calibration/held-out periods. Compares random sampling, historical caching, fixed representative subsets, and **IRT-based adaptive testing**. Multidimensional 2PL adaptive testing achieves the best score fidelity (**200 questions = 38.5% of a full run → 1.03 pp MAE**); they nonetheless deployed **difficulty-stratified fixed subsets** for operational simplicity, showing transfer without recalibration to five other agent families and stability across calibration windows as short as one day.
- **Key Innovations**: (1) rare first-party data (574 runs) on efficient recurring production-agent eval; (2) IRT-adaptive vs fixed-subset tradeoff quantified (1.03 pp at 38.5% cost); (3) cross-family transfer + short-window stability of stratified fixed subsets.
- **Venue**: Preprint.

### 4.3 When Better Turns Do Not Make Better Agents (2609.21187)
- **Title**: When Better Turns Do Not Make Better Agents: Diagnosing the Gap Between Next-Turn Metrics and Workflow Success
- **Authors**: Md Tahmid Rahman Laskar, Xue-Yong Fu, Gundeep Singh, Karol Chang, Kevin Sanders, Shi Zong, Tania Habib, Julien Bouvier Tremblay
- **Institution**: — (industrial; tentative)
- **Date**: Announced 21 Sep 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2609.21187
- **Abstract**: Agent models are frequently evaluated one decision at a time (predict next action from gold history, score against reference). Tests whether improvement under this protocol predicts autonomous workflow success, using pre-SFT and SFT **Qwen3 4B/14B and Gemma 3 4B/12B** on multi-turn customer-support workflows. SFT consistently improves text-turn success and overall next-turn success under gold-history eval — **but these improvements do not transfer to autonomous workflow execution**. None of the four SFT models succeeds under holistic workflow evaluation; strict trajectory completion reaches at most **10.4%**. Next-turn evaluation is not a reliable proxy for workflow success → motivates separate reporting of text quality, local action correctness, tool execution, and end-to-end task completion.
- **Key Innovations**: (1) controlled diagnosis (pre/SFT × 4 models) of the next-turn-metric → workflow-success gap; (2) SFT improves local turns yet strict trajectory completion ≤10.4% — a sharp negative result; (3) actionable eval-splitting recommendation (text / action / tool / completion).
- **Venue**: Preprint.

### 4.4 AutoViewMem — Self-Configuring Orthogonal Views for Conversational Long-Term Memory (2609.21940)
- **Title**: AutoViewMem: Self-Configuring Orthogonal Views for Conversational Long-Term Memory
- **Authors**: Zijie Cao, Xijun Qu, Zhicheng Gu, Xiaoshu Chen, Duanyang Yuan, Yanning Hou, Sihang Zhou, Jianxing Gong
- **Institution**: — (academic / industrial; Sihang Zhou; tentative)
- **Date**: Announced 21 Sep 2026 (cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.21940
- **Abstract**: Long-term memory is essential for LLM agents' consistency/personalization over extended interactions. Existing systems use fixed granularities/static schemas, which struggle when heterogeneous info (preferences, events, constraints, temporal updates) sits in one mixed representation — semantic interference makes top-K retrieval noise-sensitive and ranks relevant evidence poorly. **AutoViewMem** organizes conversational memory into **self-configuring, low-overlap semantic views before indexing**: discovers candidate views from interaction traces, selects a compact complementary view set, and uses views to guide write-time structured extraction of provenance-grounded memories. This **representation-first design moves semantic disentanglement from retrieval time to write time**, so standard top-K similarity can retrieve focused evidence without routing/iterative retrieval. Offline consolidation improves compactness/consistency. On LoCoMo and PersonaMem with Qwen3-8B/14B, improves long-horizon QA and personalization over strong baselines while keeping a simple inference pipeline.
- **Key Innovations**: (1) write-time semantic disentanglement via self-configuring orthogonal views (vs retrieval-time routing); (2) view discovery + compact complementary selection from interaction traces; (3) provenance-grounded extraction + offline consolidation.
- **Venue**: Preprint.

### 4.5 An Interpretable Memory Decision Controller for LLM Agents (2609.22043)
- **Title**: An Interpretable Memory Decision Controller for LLM Agents Based on Three-Signal Complementarity: Decoupling Confidence and Consistency
- **Authors**: Yiming Zhang, Jinghong Zhang, Haoran Zhao, Yiren Ma, Chunlei Zhao
- **Institution**: — (academic; tentative)
- **Date**: Announced 21 Sep 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2609.22043
- **Abstract**: Memory systems focus on efficient retrieval but under-address *whether retrieved memories should be trusted*. With conflicting memory positions, standard RAG **blindly injects memories and amplifies hallucinations** (higher than a memory-free baseline). Proposes the **Memory Decision Layer (MDL)**, a **zero-parameter** memory-decision controller between retrieval and generation: a three-signal complementary encoder fusing **relevance, reliability, and task risk** via QR-based orthogonal subspace projection + a meta-working-memory signal into an interpretable decision representation. Explicitly decouples confidence from consistency, adds risk inversion and explicit abstention. On mainstream LLMs and open datasets: hallucination rate under conflicting memories down **~56.04%** in general scenarios, ≈0 in high-risk scenarios; fully white-box, no trained parameters, **~0.14 ms/decision** (≈50× faster than embedding retrieval, 4–5 orders faster than an LLM self-eval call).
- **Key Innovations**: (1) trustworthiness-of-memory as a first-class decision (three-signal + risk inversion + abstention); (2) zero-parameter, fully-white-box controller (geometric ops only); (3) ~56% hallucination reduction under conflicting memories at negligible latency.
- **Venue**: Preprint.

---

## 5 RAG & Agent Security

### 5.1 Micro-Collaborative Poisoning — A Distributed Attack on RAG Systems (2609.21573)
- **Title**: Micro-Collaborative Poisoning: A Distributed Attack on RAG Systems
- **Authors**: Pedro Pereira, Eva Maia, Isabel Praça
- **Institution**: University of Porto / GECAD-aligned (Praça; tentative)
- **Date**: Announced 21 Sep 2026 (cs.CR)
- **arXiv**: https://arxiv.org/abs/2609.21573
- **Abstract**: RAG grounds outputs in external knowledge, creating a poisoning surface. **Micro-Collaborative Poisoning** = a distributed attack in which a false claim is **divided across multiple locally-plausible documents** instead of concentrated in one malicious passage. Evaluated across **108 RAG configurations** (dataset × retriever × retrieval depth × database composition × number poisoned DBs × generator). Findings: the attack is **not driven by a single dominant passage but by accumulation of weak adversarial signals across retrieved sources**; larger top-k and more poisoned DBs raise co-occurrence probability; clean-DB diversity and stronger retrievers reduce influence; document-level poisoning-visibility analysis shows the threat is **hard to expose via isolated document inspection** (weaker explicit signature than direct poisoning).
- **Key Innovations**: (1) a distributed/emergent RAG-poisoning attack (signal-accumulation, not single-passage); (2) 108-config exhaustive sweep mapping attack conditions; (3) negative-visibility analysis: isolated inspection can't detect it.
- **Venue**: Preprint.

### 5.2 Loopjacking — Hijacking Human-in-the-Loop Approval in Shipped Agents (2609.21081)
- **Title**: Loopjacking: Hijacking Human-in-the-Loop Approval
- **Authors**: Adithyan Arun Kumar
- **Institution**: — (single author; tentative)
- **Date**: Announced 21 Sep 2026 (cs.CR)
- **arXiv**: https://arxiv.org/abs/2609.21081
- **Abstract**: Human approval is the last security boundary before an agent executes a consequential operation — only meaningful if the presented operation IS the later-authorized/released one. **Loopjacking** = failures of this binding: human approves operation A while the implementation uses that decision for materially different operation B. Two variants: **representation-based** (B pre-encoded but omitted/misrepresented at approval) and **post-approval state-substitution** (human sees correct A, mutable workflow state later replaces it with B). Reproduced post-approval substitution in **7 tested Agno AgentOS releases (≤3.0.9) and 12 tested LangGraph Agent Server compositions (≤0.14.0)**; representation mismatch in OpenClaw 2026.2.23 (rejected in 2026.2.24); OpenAI Agents SDK 0.22.0/0.22.2 as negative control (serialized continuation preserves per-call binding). Complete canonical approval rendering + exact use-time comparison, or preventing unauthorized pending-state mutation, block the tested attacks.
- **Key Innovations**: (1) canonizes "approval/presentation binding" as an attack surface for agentic products (Loopjacking taxonomy — representation vs state-substitution); (2) reproductions across real shipped agent frameworks (Agno, LangGraph, OpenClaw, OpenAI SDK); (3) concrete mitigations (canonical rendering + exact use-time comparison / no unauthorized pending-state mutation).
- **Venue**: Preprint.

---

## 6 Games, Game Content & Strategic Play

### 6.1 GameLogicBench — Evaluating Coding Agents on Runtime Game Logic (2609.21562)
- **Title**: GameLogicBench: Evaluating Coding Agents on Runtime Game Logic with Tick-Level State Assertions
- **Authors**: Xinyu Che, Yunfei Ge, Shihao Li, Yanchen Liu, Hang Yan, Xinping Lei, Yanghai Wang, Zixuan Dong
- **Institution**: — (academic/industrial; tentative)
- **Date**: Announced 21 Sep 2026 (cs.SE / cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.21562
- **Abstract**: Coding agents must implement gameplay rules, but a game can **end in a valid state even after violating its rules during the run**. Existing game-dev benchmarks replay fixed examples, score videos, or ask an LLM judge — none checks rules throughout execution across varied evaluator-selected scenarios with exactly reproducible verdicts. **GameLogicBench**: 72 gameplay-logic tasks in Godot projects; an automated evaluator checks rules **at every simulation tick**; 403 hand-designed scenarios + seeded parameter variations → **1,451 test cases**. Evaluator must accept multiple correct implementations while rejecting mutants (a capability removed). Tasks span isolated mechanics → multi-system interactions → repository-scale features. Across 20 model×scaffold combos, best run solves **52.78%**; under Claude Code, all twelve models solve fewer tasks as scope expands; agents inspect code more and call tools more on repo-scale tasks. Most unsuccessful submissions are runnable but implement game behavior incorrectly. **Without mutant-based validation, incorrect agent submissions passed** — and with network access open, agents copy code from public repos.
- **Key Innovations**: (1) tick-level state-assertion evaluation of runtime game logic (vs end-state/video/LLM-judge); (2) mutant-validated evaluator accepting correct implementations while rejecting removed-capability mutants; (3) scalable 1,451-test-case setup revealing task-scope scaling + external-code-copying effects on agent scores.
- **Venue**: Preprint.

### 6.2 MORM — Multiplicative Optimism for Constant Regret in Games (2609.21976)
- **Title**: Multiplicative Optimism for Constant Regret in Games (paper title: "Multiplicative Optimism for Constant Regret in Games")
- **Authors**: Ashkan Soleymani, Georgios Piliouras
- **Institution**: SUTD-aligned (Piliouras; tentative)
- **Date**: Announced 21 Sep 2026 (cs.GT)
- **arXiv**: https://arxiv.org/abs/2609.21976
- **Abstract**: Introduces **Multiplicatively Optimistic Regret Matching (MORM)**, an uncoupled learning rule for finite general-sum games. Under simultaneous full-information self-play, **every player achieves external regret O(√n · log d) uniformly over all horizons** using only one-step optimism. The analysis combines a potential-based regret-matching argument with multiplicative stability and **Hellinger control of strategy movement**. A learning-rate safeguard additionally gives O(√(T log d)) regret against adversarial utilities.
- **Key Innovations**: (1) a single-step-optimism regret-matching rule with uniform-over-horizon O(√n log d) regret in self-play; (2) multiplicative stability + Hellinger control as the proof engine; (3) adversarial-utility safeguard — a clean theory update for the game-dynamics line.
- **Venue**: Preprint.

### 6.3 Guiding Agents of Quantum Games to Equilibrium — MEFPIA (2609.21944)
- **Title**: Guiding Agents of Quantum Games to Equilibrium using Matrix Exponential Fixed-Point Iteration
- **Authors**: Alireza Habibi, Luis F. Abanto Leon, Setareh Maghsudi
- **Institution**: — (academic; tentative)
- **Date**: Announced 21 Sep 2026 (quant-ph / cs.MA)
- **arXiv**: https://arxiv.org/abs/2609.21944
- **Abstract**: Quantum game theory studies decision-making in multi-agent systems using quantum principles, but computing equilibria is hard because the joint Hilbert-space dimension grows as the product of players' local dimensions. Considers an **extended Gutoski-Watrous (EGW)** game with local density-matrix strategies; derives **tensor-contraction expressions for payoffs and gradients** that avoid building the full joint density matrix. Proposes **MEFPIA (Matrix Exponential Fixed-Point Iteration with Annealing)** to search for equilibria, compared against Matrix Multiplicative Weights Update (MMWU): both approach the same strategy profiles/payoffs on tested instances, **MEFPIA with lower relative error in fewer iterations**.
- **Key Innovations**: (1) tensor-contraction payoff/gradient computation avoiding joint-Hilbert-space construction; (2) MEFPIA annealing fixed-point search vs MMWU baseline; (3) quantum-games → multi-agent decision-making applications.
- **Venue**: Preprint.

### 6.4 Colonel Blotto Model of Deterrence — Information Structure of Defection (2609.21064)
- **Title**: Information Structure of Defection Decisions in a Colonel Blotto Model of Deterrence
- **Authors**: Tristan Mott, David Grimsman, Keith Paarporn
- **Institution**: Brigham Young University-aligned (Paarporn; tentative)
- **Date**: Announced 21 Sep 2026 (cs.GT)
- **arXiv**: https://arxiv.org/abs/2609.21064
- **Abstract**: In strategic interactions, deterrence = one party incentivizing the other not to participate — applied here to **Colonel Blotto games where troops can be deterred from following orders**. Deterrence depends not only on troop allocation but on the **information available to troops when deciding to follow orders or defect**. Studies a two-battlefield Colonel Blotto deterrence model under multiple information structures (aggregate-only decisions up to local-battlefield observations). Shows how information structures alter the induced game's structure, equilibrium existence, and expected utilities; proves that **the ratio of troops available to each general combined with a capture-probability threshold** is enough to inform generals which information to give troops.
- **Key Innovations**: (1) information-structure lens on defection/deterrence in Colonel Blotto (vs pure allocation); (2) equilibrium-existence and utility results across information regimes; (3) a simple two-parameter rule (troop ratio × capture threshold) for information design.
- **Venue**: Preprint.

---

## Key Trends Across This Window (Unclaimed Remainder)

1. **Agent evaluation loudness continues to be challenged** (21187 next-turn≠workflow gap ≤10.4% strict completion; 21267 production 574-run benchmarking fidelity 1.03 pp at 38.5% cost): the field keeps finding that cheap/local proxies overstate agent capability, and is now shipping *deployment-grade* evaluation economics to correct it.
2. **Reasoning-model unlearning moves from suppression to trajectory quality** (21677 GUARD: natural forgetting CoT; NFRS metric) and **latent steering hits a hard ceiling** (21662 latent-to-language transition gap): both point at the sequence-level interface (language output / CoT) as the only place interventions reliably take effect.
3. **Attention primitives get a molecular decomposition** (22005 abstention vs noise-filtering with opposite scale trends; 21139 quality-gated attention replacement where representational fidelity gates conversion): the "replace attention" debate is maturing into per-primitive, per-layer, fidelity-gated engineering.
4. **Memory systems for agents move from retrieval engineering to decision engineering** (21940 write-time orthogonal views; 22043 zero-parameter 3-signal memory decision controller, ~56% hallucination cut under conflicts): the *whether-to-trust* decision is now as important as the *what-to-retrieve* step.
5. **Game evaluation for coding agents turns behavioral** (21562 GameLogicBench tick-level assertions + mutant validation; agents copy public repos when unplugged): a reproducible-verdict benchmark that rejects end-state-only scoring — the games line gains a second measurement discipline alongside game-RL.
6. **Security primitives are now product-level** (21573 micro-collaborative RAG poisoning invisible to single-document inspection; 21081 Loopjacking reproduced across Agno/LangGraph/OpenClaw): both argue that countermeasures (multi-source signal, canonical-approval binding) are just as systemic as the defenses they replace.
7. **Ads/CTR confirmed again at ~0 in this remainder** (8th+ consecutive window at the daily layer): the two ads papers of the day (OneBid, ADAPT) were claimed by `arxiv-daily`; nothing fresh remains here except rec-adjacent process forecasting (21382 NTPP) and news-rec practice (21547).

## ADS / CTR Coherence Check

0 direct CTR/advertising papers in the unclaimed remainder of the Mon-21 window (today's daily claimed OneBid 2609.21550 + ADAPT 2609.21308). Pattern consolidation: classic end-to-end CTR/rank-model content continues to appear only in conference batches (KDD/CIKM/WWW digests), not at the daily arXiv layer. Closest this report gets: AutoRecLab (rec experiment automation), news-rec explainability study, business-process NTPP forecasting (event-log distributional forecasting), and the affordable-bidding/effort implication threads in the trends.

## Cross-Reference Index (Sibling & Runner-Up Coordinates)

- Same-window sibling: `arxiv-daily` (2026-09-21) claimed IDs 2609.20823/20824/20831/20845/20886/20888/20942/20971/20974/21032/21044/21172/21190/21257/21277/21281/21293/21308/21325/21378/21383/21392/21423/21425/21432/21475/21496/21527/21533/21548/21550/21561/21605/21619/21626/21672/21704/21748/21888/21894/21899/21953/21996/22000/22041/22055/22056/22064/22068. The 21 featured + 6 runner-ups below are all outside that set.
- Runner-ups this window (grep-verified 0 hits): **2609.21945** Learning to Move Cities (deep meta-models + RL for urban network calibration/control; −51% travel time); **2609.21320** Diagonalized Attention for Individualized Regression (latent-row localization + prediction); **2609.20973** Complex Problem Solving in LLMs: A Statistical Control Survey and Diagnostic Framework; **2609.21214** Ability-Residual Decoupled Modeling for Affective Cognitive Diagnosis (educational rec-adjacent); **2609.21791** RegKT: Interpretable & Robust Deep Knowledge Tracing with IRT-regularizer (educational sequential modeling); **2609.21096** Detecting Hallucination in LLMs via Topological Signatures of Impaired Context Sharing.
- Sub-window map for future dedup: IDs **20823–21550** (daily claimed the auto-bidding/rec/seq/serving cluster), **21550–22068** (daily claimed the eval/post-training/game cluster); the report's unclaimed remainder (20825–22043 span) is where this and future topic sweeps should look.