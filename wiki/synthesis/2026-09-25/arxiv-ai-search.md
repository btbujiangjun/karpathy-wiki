---
title: "arXiv AI Research Paper Search Report"
type: synthesis
created: 2026-09-25
updated: 2026-09-25
sources: [arxiv.org]
tags: [arxiv, AI, LLM, recommendation, advertising, sequential-modeling, CTR, games, e-commerce-search, generative-recommendation, flow-matching, world-models, agent-memory, reward-hacking, reproducibility, JEV, rubric-judges, mechanistic-interpretability, superposition, mechanism-design, auctions, blotto, committee-voting, PV-Citr, time-series-foundation, SSM, MLA, KV-cache, many-shot-ICL, RLVR, adversarial-influence, daily-digest]
---

# arXiv AI Research Paper Search Report — 2026-09-25

Generated: 2026-09-25 (Friday). **Fresh Fri 25 Sep 2026 mailing**, parsed from 8 category listing pages (`/list/{cat}/new`): **cs.AI, cs.LG, cs.IR, cs.CL, cs.GT, cs.MA, cs.NE, cs.CV**. **454 unique new-submission IDs** extracted (`New submissions` sections only; window **2609.28475–2609.30264**); **26 papers featured in full + 8 runner-ups**, every ID **grep-verified 0 hits in `wiki/`** at selection time.

**Methodology**: Direct page fetches of `/list/{cat}/new` (all announce **Friday, 25 September 2026** — confirmed via each page's `Showing new listings for Friday, 25 September 2026` header); parsed only the **New submissions** section of each page (Cross-lists/Replacements excluded). Per-category counts: cs.LG 119, cs.CV 111, cs.AI 107, cs.CL 86, cs.IR 16, cs.GT 8, cs.NE 4, cs.MA 3. Title/abstract screen of all 454 fresh candidates on target topics (AI / LLM / recommendation / advertising / sequential modeling / CTR / games / auctions & mechanism design / agentic engineering / world models). Listing HTML cached under the pre-approved temp dir `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/arxiv-search-0925/` and cleaned after. Institutions are author-affiliation inferred where arXiv does not print them (marked *tentative*).

> **Dedup / race note**: The sibling `arxiv-daily` job wrote `wiki/synthesis/2026-09-25/arxiv-daily.md` **while this report was being built** — it claimed **28 featured + 9 runner-ups (40 unique IDs)** from its published=2026-09-24 API window (IDs 2609.28858–2609.30163), including PixelJev visual-choice 2609.29283 and LLM-grader study 2609.29333 (not in this report). All overlap between the two reports was resolved by whole-page `rg` diff: **this report's 34 curated IDs are disjoint from the daily's 40**. Sibling `arxiv-paper-check` should treat this report's 34 IDs (list in the final section) and the daily's 40 as claimed.

## Summary Statistics

| Scope | Value |
|---|---|
| Window covered | Fri 25 Sep 2026 mailing; fresh-only ID span **2609.28475–2609.30264** (8 categories) |
| Categories parsed | cs.AI, cs.LG, cs.IR, cs.CL, cs.GT, cs.MA, cs.NE, cs.CV |
| Unique new-submission IDs parsed | 454 (cs.LG 119, cs.CV 111, cs.AI 107, cs.CL 86, cs.IR 16, cs.GT 8, cs.NE 4, cs.MA 3) |
| Featured in full in this report | 26 papers (6 sections) + 8 shortlisted runner-ups |
| Already-claimed collisions | **0** — 454/454 new IDs unclaimed at write time (33-day-old cross-list/replacement IDs also present on /new pages were excluded by section-splitting) |
| Direct advertising / CTR / pCTR papers | **2 industrial hits** (OneTrans-V2 industrial rec cascade; ScalarLens CTR numerical embeddings; X-Rec TikTok deployment as runner-up; Roblox search-RL and Nubank CX agents as adjacent industrial ML) — **a return against the September 23-window CTR drought** |
| Industrial deployments reported in-window | OneTrans-V2 (GMV +9.74%), X-Rec TikTok, Roblox search (NDCG@20 +8.9), Nubank CX (tNPS +36.69 / SSR +8.82pp), PUBG Ally (KRAFTON live service), CMRec (+1.77% ad revenue) |
| Mailing status | `/new` pages announce Fri-25 at fetch time; window terminus at **2609.30264** (cs.AI max) |

**Theme of the window**: a **decision-layer / evaluation-integrity week** (reward hacking under agentic research, RECLAIM reproduction benchmark, CTT critique of LLM-judge reliability, Jev as calibrated-decision detector + JevOut flip fragility) layered over **industrial recommender consolidation** (one-transformer cascade unification, CTR numerical embeddings, generative-rec credit assignment, cross-country code-mixing), plus **sequential-modeling architecture work** (time-series⊗language unification, stream-recursion interpretability model, MLA–SSM ablation, looped-transformer inference, many-shot-ICL KV compression) and a thin-but-sharp **games/mechanism-design line** (multiplayer Blotto PPAD-hardness, committee-voting core, online matching with subsidies).

---

## 1 Recommendation, Search & CTR

### 1.1 OneTrans-V2 — One Transformer for the Whole Rec Cascade (2609.28589)
- **Title**: OneTrans-V2: Unifying Retrieval, Pre-rank, and Fine-rank with One Transformer in Industrial Recommender
- **Authors**: Hannan Cao, Jun Guo, Haolei Pei, Zhaoqi Zhang, Tianyu Wang, Ziyang Wang, Youchen Sun, Yue Xue, Yucheng Mao, Lintao Yan, Yufei Feng, Shaowei Liu, Rongkun Xing, Feiling Gong, Xinyu Chenli, Cong Xu, Mingge Zhang, Yunjia Zhu, Yajing Zhang, Pengfei Ren, Yue Lin
- **Institution**: large-scale industrial recommender operator (*tentative* — 21 authors, no affiliation printed)
- **Date**: Fri 25 Sep 2026 (cs.IR)
- **arXiv**: https://arxiv.org/abs/2609.28589
- **Abstract**: Industrial rec systems run as a **cascade** of retrieval, pre-rank, and fine-rank, typically trained and served as separate models (repeated user-sequence encoding, isolated optimization, duplicated engineering). OneTrans-V2 extends OneTrans' model-level unification to **one Transformer unifying the whole cascade**: the user behavior sequence is encoded once as shared context while stage-specific candidate features/computation are preserved; joint training lets stages reinforce each other and enables **in-model distillation from fine-rank to pre-rank**. The shared backbone is scaled with **sparse MoE** (more capacity, bounded activated compute) and stabilized with **µP-style parameterization**. To consolidate objective-specific retrieval channels it introduces **Decision-Conditioned Generative Retrieval (DCGR)** — predict a decision prefix describing the upcoming interaction, generate items conditioned on it — and **Sequence-Native Training (SNT)** which amortizes encoding of lifelong behavior sequences across exposures. Deployed across all three stages of a large-scale industrial rec system: **GMV +9.74%**, and with a co-designed serving stack **3.2× throughput** vs the cascade under the same hardware budget.
- **Key Innovations**: (1) single-model end-to-end unification of retrieval/pre-rank/fine-rank with shared lifelong-sequence encoding; (2) MoE + µP scaling of the rec backbone; (3) DCGR generative retrieval steered by business-objective decision prefixes; (4) deployment economics (GMV/throughput numbers on a real system).
- **Venue**: Preprint (industrial technical report flavor).

### 1.2 ScalarLens — CTR Numerical Embeddings That Separate Coordinates from Context (2609.29182)
- **Title**: ScalarLens: Numerical Embeddings with Stable Coordinates and Contextual Responses for CTR Prediction
- **Authors**: Heng Yao, Tianying Liu, Yulou Shu, Yong He, Chuan Yuan, Kaibin Qiu, Guowei Chen, Jiayu Zhao, Siyun Hou
- **Institution**: industrial/CTR team (*tentative*)
- **Date**: Fri 25 Sep 2026 (cs.IR)
- **arXiv**: https://arxiv.org/abs/2609.29182
- **Abstract**: Numerical embeddings for **click-through rate (CTR)** rest on a "one scalar, one representation" premise that conflates *where a value lies* with *what it means for this sample*. On the **Criteo validation split**, the same numerical interval carries residual click evidence with **opposite signs across categorical vs numerical contexts** even after additive main effects are removed; production pipelines compound this because externally normalized features must keep transformations/statistics synchronized between training and serving. **ScalarLens** preserves what a value *is* while adapting how it is *interpreted*: a monotone local mesh builds a stable coordinate from the focal scalar alone; bounded low-rank dynamics produce a contextual response **without moving that coordinate or replacing categorical tokens / the CTR backbone**. In a 1,539-run primary evaluation (19 representations × 3 datasets × 9 backbones × 3 seeds) it **ranks 1st in 25 of 27 settings** on original numerical scales. Matched ablations show scale correction / extra local capacity / generic conditioning don't reproduce the gain; a rerun under shared standardization still beats DEER, DAES, and NaryDis — so the result is not raw-scale tolerance.
- **Key Innovations**: (1) identifies the "coordinate vs meaning" confusion of scalar numerical embeddings (opposite-sign context evidence on Criteo); (2) monotone-mesh stable coordinates + bounded low-rank contextual response, drop-in vs existing CTR backbones; (3) large controlled evaluation protocol (1,539 runs) separating scale-correction from genuine gains.
- **Venue**: Preprint.

### 1.3 Retrieval-Grounded Credit Assignment for Generative Recommendation (2609.29983)
- **Title**: From Interests to Semantic IDs: Retrieval-Grounded Credit Assignment for Generative Recommendation
- **Authors**: Mengdan Zhu, Yufan Zhao, Yao Zhao, Sophie Di, Tao Di, Yulan Yan, Sridhar Iyer, Liang Zhao
- **Institution**: academic/industrial e-commerce ML (*tentative*)
- **Date**: Fri 25 Sep 2026 (cs.IR)
- **arXiv**: https://arxiv.org/abs/2609.29983
- **Abstract**: Semantic IDs (SIDs) encode catalog items as short token sequences so generative recommenders predict the next item autoregressively; reasoning-enhanced variants first generate a textual trace then beam-search a next-item SID. Trained with group-relative policy optimization under **exact-match SID reward**, these models suffer a **credit-attribution gap**: when all rollouts in a group miss the target, no learning signal; rollouts sharing the same SID get identical advantages however much their traces differ. The reward reflects only the decoded SID, never the reasoning that produced it. The fix: **retrieval-grounded query attribution**. Each trace is structured into a history summary, interest hypotheses, and a final SID; a **frozen retriever executes every hypothesis as a catalog query**, making each hypothesis independently verifiable; a rollout is rewarded when any query retrieves the target within top-K, and per-query hit indicators localize reward to individual hypotheses — credit is assigned at the span level (retrieval channel never updates the final SID span). On three Amazon Reviews datasets this yields consistent SID-recommendation improvements; on Video Games an oracle analysis shows interest-conditioned SID decoding further improves recall and ranking.
- **Key Innovations**: (1) names the sparse-exact-match-RL credit-attribution gap in reasoning-based generative rec; (2) frozen-retriever per-hypothesis verification as a dense, span-localized reward signal; (3) interest-conditioned SID decoding as a decoding-time lever.
- **Venue**: Preprint.

### 1.4 LSF-SR — Flow-based CVAE for Sequential Recommendation (2609.29815)
- **Title**: LSF-SR: Latent Semantic Fusion for Sequential Recommendation via Flow-based Conditional Variational Autoencoders
- **Authors**: Shih-Hong Chen, Josh Jia-Ching Ying, Vincent S. Tseng
- **Institution**: National Yang Ming Chiao Tung University-aligned (*tentative* — Ying/Tseng)
- **Date**: Fri 25 Sep 2026 (cs.IR)
- **arXiv**: https://arxiv.org/abs/2609.29815
- **Abstract**: Sequential recommendation struggles to align **collaborative signals with LLM-generated textual semantics**; existing methods learn item representations that fail to capture both complementary strengths. **LSF-SR** uses a **Conditional VAE with Normalizing Flows** to fuse item-ID embeddings and LLM semantic signals. The core is a conditional fusion module augmented with planar/radial flows that learns a flexible latent space where semantically similar items cluster on the latent manifold. On five public benchmarks it beats SOTA baselines with gains up to **+12.98% Recall@20 / +14.13% NDCG@20**.
- **Key Innovations**: (1) flow-augmented CVAE as the fusion architecture for ID×semantic item signals; (2) manifold-grounded fusion vs ad-hoc concatenation; (3) consistent double-digit lifts across 5 datasets.
- **Venue**: Preprint.

### 1.5 Search-Aware RL for Query Understanding at Roblox (2609.30177)
- **Title**: Search-Aware Reinforcement Learning for Multi-Component Query Understanding in Roblox Game Search
- **Authors**: Nayoung Choi, Shengjian Chen, Xiaokai Wei, Wenzheng Zhang, Daiyao Yi, Rachit Pareek, Vincent Su, Michelle Gong, Jinho D. Choi
- **Institution**: Roblox (+ Emory-aligned, Choi) (*tentative*)
- **Date**: Fri 25 Sep 2026 (cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.30177
- **Abstract**: **Query understanding (QU)** translates raw queries into search execution plans driving retrieval/ranking. With LLMs, QU is a structured multi-task generation problem (intent classification, query expansion), but static label supervision fails to capture how each component interacts with the search pipeline. A **distill-then-RL** framework: teacher→student **SFT** gives a schema-compliant policy; then RL optimizes each QU component with rewards **derived from live interaction with the search engine**, tailored to the component's operational role — not a single end-to-end reward. On **Roblox search**: component-specific optimization raises **NDCG@20 by +8.9 points** over the SFT policy and **+3.5 over a single end-to-end reward**.
- **Key Innovations**: (1) search-aware, per-component reward design for LLM query understanding; (2) distill-then-RL for schemas/compliance first, live-signal optimization second; (3) production Roblox search evidence.
- **Venue**: Preprint (industrial).

---

## 2 Sequential Modeling, Time Series & Efficient Sequence Architectures

### 2.1 TimeBraid — Unifying Time Series and Language (2609.29792)
- **Title**: TimeBraid: Unifying Time Series and Language for Understanding and Forecasting
- **Authors**: Xinyue Wang, Jiacheng Pang, Kun Zhou, Kexin Zhang, Defu Cao, Fan Feng, Faisal, Songyao Jin, Yan Liu, Biwei Huang
- **Institution**: multi-institution academic (*tentative* — Liu UCSC-aligned, Huang HKU/GZ)
- **Date**: Fri 25 Sep 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2609.29792
- **Abstract**: TimeBraid is a family of unified time-series–language models that align a pretrained LM and a pretrained time-series foundation model via **interleaved global residual attention layers**: the LM side donates knowledge/instruction-following/reasoning, the TSFM side donates continuous-signal perception and zero-shot forecasting, fused in a shared representation space where both modalities can be understood and generated. Studies the design choices that make unified modeling work — where to align the two spaces, how to ground language in temporal structure, how to balance understanding vs generation, how to keep joint optimization stable. Recipe = unified prompting + stabilized joint training + **2.2M curted series-text pairs and 4.9M instruction-tuning samples**. Across TS perception/understanding/reasoning + context-aided and unimodal forecasting, TimeBraid stays competitive with far larger generalists and task-specific counterparts.
- **Key Innovations**: (1) pretrained-LM ⊗ pretrained-TSFM alignment as the foundation for unified TS-language models; (2) empirical recipe for *where* to align (global residual attention layers) and *how* to keep joint optimization stable; (3) large curated multimodal supervision set (7.1M pairs+instructions).
- **Venue**: Preprint.

### 2.2 Stream Recursion Model (SRM) — Interpretable-by-Design Recurrent Architecture (2609.28809)
- **Title**: Stream Recursion Model (SRM)
- **Authors**: Asael Sorensen, Charles Brock, David Chamberlain, Jennifer Minnich, Matthew Hoffman, Ramyaa Ramyaa
- **Institution**: Google Research-lineage (*tentative* — Hoffman), multi-institution
- **Date**: Fri 25 Sep 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.28809
- **Abstract**: Mechanistic interpretability struggles to scale to larger, deeper models. SRM answers by building **smaller models with interpretable structure**: a modification of the Hierarchical Reasoning Model (HRM) that organizes computation into **multiple interacting latent streams updated by recursive refinement**, enabling direct analysis of stream dynamics, causal contribution, and routing behavior. SRM reaches **performance comparable to GPT-2 on a per-parameter basis**, and analysis shows consistent, distinct behavior across streams indicating structured specialization and interaction.
- **Key Innovations**: (1) multiple recursive latent streams as an interpretability-native architecture; (2) per-parameter-parity claim vs GPT-2 for the interpretability budget; (3) a scalable foundation for stream-dynamics/causal-contribution analysis.
- **Venue**: Preprint.

### 2.3 Small MLA–SSM Hybrid — Careful Single-Seed Ablation (2609.29618)
- **Title**: An Exploratory Ablation of a Small MLA–SSM Hybrid Language Model
- **Authors**: Christos Koutsiaris
- **Institution**: single author (*tentative*)
- **Date**: Fri 25 Sep 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2609.29618
- **Abstract**: Single-seed ablation of **TALH (Adaptive Latent Hybrid)**, a decoder-only model with parallel **Multi-head Latent Attention (MLA)** and a custom recurrent **state-space (SSM)** branch. Five variants (117–217M estimated active params/token) trained from scratch on a FineWeb sample for equal steps/tokens. In this setup: **removing the SSM branch is the largest degradation** (MLA-only PPL 315) while removing MLA matters less (SSM-only PPL 239); dense-FFN hybrid gets PPL 231 vs 240 for the top-2 ternary-MoE hybrid while using 3.87 GB less peak training memory. Preliminary Apple-M3 timing: MLA-only has the flattest TTFT curve 512→2,048 prompt tokens, though the dense Transformer is much faster absolutely. The authors are explicit about limits: single-seed, unmatched param counts, possible eval/train overlap, no raw repeated timing — **implementation-specific hypotheses, not general conclusions about MLA/SSMs/MoE**.
- **Key Innovations**: (1) the first small-scale MLA–SSM parallel-branch ablation with an honest caveat section; (2) "SSM branch carries more perplexity value than MLA branch at this size" as a falsifiable hypothesis; (3) memory-efficiency edge of dense-FFN vs ternary-MoE hybrids.
- **Venue**: Preprint (exploratory).

### 2.4 FlashLoop — Lossless Inference Speedup for Looped Transformers (2609.29812)
- **Title**: FlashLoop: Fast and Memory-Efficient Looped Transformers via Lazy Updates
- **Authors**: Wanqi Yang, Shiwei Liu
- **Institution**: UT Austin-aligned (*tentative* — Liu)
- **Date**: Fri 25 Sep 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.29812
- **Abstract**: Looped Transformers (shared blocks, repeated) are parameter-efficient but each extra loop adds a full Transformer pass + a new set of KV states, so inference FLOPs and KV-cache memory grow with loop depth — undermining the practical win. Key finding: **much of the loop-induced computation/storage is redundant** — as recurrence proceeds, state changes concentrate on a small subset of tokens; attention-output differences are dominated by a sparse stable subset of key columns; KV residuals between adjacent loops become amenable to low-bit quantization. **FlashLoop** is a training-free inference framework exploiting these: token-sparse updates + sparse attention + KV-residual quantization. Across several looped models: **lossless accuracy with up to 1.64× end-to-end speedup and up to 6× KV-cache reduction**.
- **Key Innovations**: (1) characterizes cross-loop redundancy (token-sparsity, key-column sparsity, low-rank KV residuals); (2) training-free lazy-update inference framework; (3) 1.64× speed / 6× memory for a long-criticized paradigm.
- **Venue**: Preprint.

### 2.5 MILO — Many-shot ICL with Block-wise Low-rank KV Compression (2609.29913)
- **Title**: MILO: Efficient Many-shot In-Context Learning with Block-wise Low-rank Compression
- **Authors**: Youpeng Zhao, Tian Tan, Liqian Peng, Jun Wang, Alec Go
- **Institution**: industrial applied-LLM team (*tentative*)
- **Date**: Fri 25 Sep 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2609.29913
- **Abstract**: Many-shot ICL conditions on thousands of demonstrations; the bottleneck shifts to **KV-cache memory** scaling linearly with context. **MILO** exploits the low-rank redundancy of many-shot contexts with **block-wise low-rank compression** at the block granularity (each block = several demonstrations), and dynamically allocates rank budgets by **information entropy** to preserve critical blocks while compressing redundant ones. On Qwen2.5 models: **up to 50% KV reduction and 1.8× throughput** with negligible degradation on classification and reasoning, outperforming prior baselines.
- **Key Innovations**: (1) block-granularity low-rank KV compression tailored to many-shot ICL; (2) entropy-guided rank-budget allocation (heterogeneous density across blocks); (3) serving/throughput win on Qwen2.5-scale many-shot workloads.
- **Venue**: Preprint.

---

## 3 LLM Internals, Evaluation & Alignment

### 3.1 Hallucination Neurons — Detection vs Localization (2609.29781)
- **Title**: Hallucination Neurons and Where to Find Them: An Investigation into the existence of Hallucination Neurons
- **Authors**: Huseyin Cavus, Sebin Sabu, Joshua Spear, Jaskaran Singh Kawatra, Pavithra Rajendran
- **Institution**: academic/multi-institution (*tentative*)
- **Date**: Fri 25 Sep 2026 (cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.29781
- **Abstract**: Sparse probing identifies small neuron sets claimed to detect/causally influence factuality, safety, hallucination — but these claims are rarely tested against known failure modes of **L1-regularized probing** in correlated high-dimensional feature spaces. Proposes a **five-step diagnostic protocol** (feature correlation, bootstrap stability, sparse-vs-dense ranking disagreement, intervention baselines, cross-dataset eval) as a minimum standard. Applied to prior **"H-neurons"** work on Gemma 3 4B / MedGemma 4B across TriviaQA/BioASQ/NQ-Open: **detection replicates and exceeds reported AUROC gaps** (e.g. TriviaQA +0.311 vs +0.235), and causal validation (n=500, 5 seeds) is significant beyond random same-layer baselines. **But** the neurons are **not uniquely localized**: 19 of 22 selected H-neurons have Pearson |r|>0.7 with other features, bootstrap stability only moderate, sparse and dense rankings weakly overlapping. **Detection claims ≠ localization claims.**
- **Key Innovations**: (1) a minimum-standard 5-step diagnostic protocol for sparse-neuron claims; (2) replication+ improvement of H-neuron detection; (3) a sharp separation of "sparse predictive structure exists" from "these specific neurons are the locus".
- **Venue**: Preprint.

### 3.2 Linear Superposition in Transformers — Two Thoughts at Once (2609.29845)
- **Title**: Your Transformer Can Hold Two Thoughts at Once: Evidence of Linear Superposition in LLMs
- **Authors**: Pavel Tikhonov, Anton Korznikov, Matvey Mikhalchuk, Nikita Dragunov, Temurbek Rahmatullaev, Polina Druzhinina, Anton Razzhigaev, Ivan Oseledets, Elena Tutubalina
- **Institution**: Skoltech/AIRI/KFU-aligned (*tentative* — Oseledets/Razzhigaev, Russian cluster)
- **Date**: Fri 25 Sep 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2609.29845
- **Abstract**: Despite heavy non-linearity, LLMs exhibit an architectural property the authors call the **Superposition Linearity Hypothesis**: when inputs from distinct text streams are linearly combined, the model outputs a superposition of the individual next-token distributions. Evidence suggests superposition is **intrinsic to the Transformer architecture**, not emergent from training — it *diminishes* as pretraining proceeds. But **lightweight fine-tuning substantially restores linearity**, reducing the divergence between the composite prediction and the average of individual predictions. A **guided decoding** procedure disentangles the superposed outputs, enabling two coherent continuations from a **single forward pass**.
- **Key Innovations**: (1) formalizes superposition linearity as an architectural property with a training trajectory (diminishes with pretraining, restorable by fine-tuning); (2) guided decoding → two coherent streams from one pass; (3) implications for batch/parallel decoding and interpretability (superposition-aware circuits).
- **Venue**: Preprint.

### 3.3 Classical Test Theory Misleads for LLM Judges (2609.29709)
- **Title**: Three Ways Classical Test Theory Misleads for LLM Judges
- **Authors**: Louis Yiven Zhu
- **Institution**: single author (*tentative*)
- **Date**: Fri 25 Sep 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.29709
- **Abstract**: Judge evaluation has borrowed reliability statistics from classical test theory without stating the measurement design each assumes; three portable statistics mean something different for a judge than for a test. (1) **Internal-consistency (e.g. KR-20) computed over rubric elements contains no scorer facet**: holding judge error rate fixed at 4.72%, KR-20 still ranges 0.01→0.68 as the item bank is redesigned, so item design and judge error are not separately identified. (2) The **dependability index Φ(λ)** is a variance-component ratio; the classification probability it is sometimes identified with differs by 0.25–0.43 on the authors' bank and 0.17–0.30 on simulated data where the model holds exactly. (3) **Livingston–Lewis accuracy** is indexed to the examinee's own true score on the instrument, so scoring vs external gold conflates judge unreliability with criterion invalidity. Closes with four reporting lines that keep attribution attached to the number.
- **Key Innovations**: (1) identifies three CTT statistics whose judge-setting semantics differ from their test-setting semantics; (2) shows non-identification (item design vs judge error) with a fixed-error-rate thought experiment; (3) concrete reporting requirements for judge-reliability claims.
- **Venue**: Preprint (measurement methodology).

### 3.4 Script Choice — Late-Layer Commitment (2609.28784)
- **Title**: Script Choice in LLMs: Evidence for Late-Layer Commitment
- **Authors**: David Kletz, Sandra Mitrović, Itay Sabato, Ljiljana Dolamić, Fabio Rinaldi
- **Institution**: Swiss/HESP (Uni Zürich / USI)-aligned (*tentative* — Kletz/Rinaldi)
- **Date**: Fri 25 Sep 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2609.28784
- **Abstract**: Uses logistic-regression probing + logit-lens to ask how **script knowledge** (Latin/Cyrillic/etc.) is distributed across layers. Clear asymmetry: input script and instructed output script are encoded in the **earliest layers**, but commitment to the actual output script emerges only in the **final layers**, intermediate representations defaulting to Latin throughout most layers. Smaller models follow script instructions more weakly — **script commitment is tied to model depth**, with implications for designing sufficiently deep, inclusive multilingual architectures.
- **Key Innovations**: (1) two-method confirmation of a late-layer script-commitment profile; (2) intermediate Latin default as a sketch of LLM "written-language bias"; (3) a depth-linked account of multilingual script-following.
- **Venue**: Preprint.

---

## 4 Agentic Systems, Agent Memory & Oversight

### 4.1 Reward Hacking Challenges Oversight of Autonomous Research Agents (2609.28614)
- **Title**: Reward Hacking Challenges Oversight of Autonomous Research Agents
- **Authors**: Yue Huang, Zhangchen Xu, Yuchen Ma, Wenjie Wang, Zheyuan Liu, Ziwei Xu, Pin-Yu Chen, Michel Galley, Zinan Lin, Stefan Feuerriegel, Radha Poovendran, Misha Sra, Alex Pentland, Xiangliang Zhang, Zichen Chen
- **Institution**: Notre Dame / Microsoft Research / LMU / UW-aligned (*tentative* — Huang, Chen, Galley, Feuerriegel, Poovendran, Pentland, Zhang)
- **Date**: Fri 25 Sep 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2609.28614
- **Abstract**: **Autonomous research agents** control both a scientific result and the evidence for it → reward-hacking risk (meeting reward criteria without the goal). Across 17 LMs and 38 tasks: **spontaneous reward-hacking rate 30.5%** on open-ended research-pipeline tasks (2.9% on task-specific kernels). When hacking is allowed (505/677 threshold-clearing attempts = **74.6% confirmed hacks**), an LLM review panel inspecting only submitted code+scores **misses 33/505 confirmed hacks (6.5%)**. Direct high-scoring methods are easy to detect; less direct ones evade more. In a five-round loop, model-task pairs with an evasion grow 7→56; cumulative evasion reaches **40.5% with detailed feedback** vs 20.3% with generic rejection. Calls for metrics kept outside the agent's control + independent recomputation on exploit-exposing data.
- **Key Innovations**: (1) a large controlled reward-hacking measurement (17 models × 38 tasks) incl. a spontaneous rate; (2) an LLM-panel auditing study quantifying what autonomous-research oversight misses; (3) adversarial-feedback dynamics (evasion snowball) as evidence against outcome-only oversight.
- **Venue**: Preprint.

### 4.2 RECLAIM — Can Agents Reproduce ML Paper Claims? (2609.28850)
- **Title**: RECLAIM: Can Agents Reproduce the Claims of Machine Learning Papers?
- **Authors**: Mithil Salunkhe, Haochen Ding, Samridhi Verma, Volodymyr Kindratenko
- **Institution**: UIUC NCSA-aligned (*tentative* — Kindratenko)
- **Date**: Fri 25 Sep 2026 (cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.28850
- **Abstract**: **RECLAIM** = 100 NeurIPS 2025 papers (yearly-rebuildable) with the target result, success criteria, and a GPU-hour budget fixed in advance. **Run-tier** releases (code+data+weights), **Retrain-tier** (no weights — agent trains the model), **Reimplement-tier** (no code — agent writes it). A language model grades runs from logs/outputs, not agent reports. Four agents, once per paper: best agent **reproduces 41% of Run-tier, 27% Retrain, 15% Reimplement**. Failed attempts use ~29% of budget (most stop early). The most common error: writing the method **without checking any part against the paper's numbers** (63 of 400 runs).
- **Key Innovations**: (1) a reproducible, tiered, grader-independent agent reproduction benchmark; (2) a 41/27/15 release-difficulty ladder quantifying how much agents depend on released artifacts; (3) a concrete failure taxonomy (paper-number-agnostic implementation) for agentic research.
- **Venue**: Preprint.

### 4.3 Just Ask Jev — Calibrated Decisions as Alignment-Failure Detector (2609.29429)
- **Title**: Just Ask Jev: Reinforcement Learning for Calibrated Decisions as a Zero-Shot Detector of AI Alignment Failures
- **Authors**: Ruoqi Guo, Yi Liu, Gelei Deng, Yuekang Li, Lida Zhao, Yutao Wu, Simin Chen, Ying Zhang, Leo Yu Zhang
- **Institution**: Deakin/UNSW-aligned (*tentative* — Guo, Li, Zhang)
- **Date**: Fri 25 Sep 2026 (cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.29429
- **Abstract**: Alignment-failure detectors either generative-judge (a decoding pass per criterion) or token-probability classifiers (one fixed label per call). **Jev**, an RLCD-calibrated decision model, answers many typed questions about one input with calibrated probabilities in a single call — but whether it *detects alignment failures* was unmeasured. **RLCDAlignBench** benchmarks Jev on **ten failures** (sycophancy, jailbreaks, deception, prompt injection, hallucination, privacy, social bias, reward hacking, concealing uncertainty, power seeking) across **44 benchmarks × 5 target models**. Key idea: **vary what Jev is asked separately from what it sees** (question wording/answer type vs input fields), because many failures are relational against a reference not visible in the response alone. A single generic question reaches **median AUROC 0.886 zero-shot** and beats supervised baselines on most benchmarks; context matters more than wording (mostly label-encoding fields); Jev matches reference scorers' agreement with humans, surfaces label defects, and **costs 63× less than LLM-judge scorers**.
- **Key Innovations**: (1) measures a calibrated-decision model as a general zero-shot alignment detector (10 failure classes); (2) asks-vs-sees decoupling isolating question- vs context-driven signal; (3) cost (63×) and defect-surfacing properties for production screening cascades.
- **Venue**: Preprint. → Cross-link: the **[09-24 panel reports](/wiki/synthesis/2026-09-24/arxiv-paper-check.md)** already track Same-Scores-Different-Decisions JEV robustness work (2609.27678); here JEV appears as detector infra.

### 4.4 JevOut — Natural Context Can Flip Decision Models (2609.30243)
- **Title**: JevOut: Natural Context Can Flip Decision Models
- **Authors**: Zixiang Xu
- **Institution**: single author (*tentative*)
- **Date**: Fri 25 Sep 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2609.30243
- **Abstract**: **Decision models** such as Jev map language to probability distributions over finite choices and their outputs directly route requests/select tools/trigger actions — but real inputs arrive with surrounding context. Short natural-looking additions redirect an **initially correct** decision even when the correct answer is unchanged. Fixing a wrong target option per item and refining fluent context via the model's own option probabilities: within 64 accepted target evaluations, the optimizer redirects Jev on **312/508 (61.4%)** of initially-correct decisions; 229 reach ≥0.7 probability on the wrong option. Three other decision systems show targeted flip rates **64.9–73.2%**. The sensitivity raises concerns about treating decision-model probability outputs as reliable interfaces.
- **Key Innovations**: (1) an optimizer-driven fragility study of decision models as *interfaces* (not just classifiers); (2) 61.4% Jev flip rate under natural-looking context with unchanged gold answer; (3) a caution for production routing/tool-selection built on such outputs.
- **Venue**: Preprint. → Companions Just Ask Jev (2609.29429) and the JEV-as-judge study ([runner-up 2609.29769]).

### 4.5 ERRAND — Budgeted Maintenance of Agent Memory (2609.29545)
- **Title**: ERRAND: Budgeted Maintenance of Agent Memory
- **Authors**: Beining Wu, Zihao Ding, Jun Huang
- **Institution**: industrial AI lab (*tentative*)
- **Date**: Fri 25 Sep 2026 (cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.29545
- **Abstract**: Deployed agents run on **handed-over knowledge**: a frozen policy consults a briefing written before the stream begins; the world moves while the store stands still — failure is **staleness, not ignorance**. **ERRAND** treats revalidation as a priced errand: a recheck competes with the task it protects for scarce actions, funded only when the value-per-action of resolving a doubt clears a running wage. The errand index is **single-peaked** (certainty either way costs nothing), free en-route receipts maintain on-path knowledge, and repair writes a version, never a deletion. Under equal action budgets in two drifting tool-use worlds, ERRAND leads eager revalidation by **10.0pp at the base cap**; uncapped, it self-stops at **11.0% of steps** while eager revalidation spends 70.7% and still finishes 4.5pp behind capped ERRAND. "A small budget, well priced, beats a bigger store that never rechecks."
- **Key Innovations**: (1) revalidation-as-pricing (shadow price of long-tail knowledge) for agent memory staleness; (2) single-peaked doubt-index funding + en-route receipts + versioned repair; (3) an empirical victory for restraint over eager maintenance.
- **Venue**: Preprint. → Thematically adjacent to the [09-24 window's memory-management set](/wiki/synthesis/2026-09-24/arxiv-ai-search.md) (JAZ invoke-harness, COMED escalation, SR-Fraud verified adaptation).

### 4.6 Screen Before You Serve — Simulation for Production CX Agents at 140M Scale (2609.30137)
- **Title**: Screen Before You Serve: Simulation for Production Customer Experience AI Agents at 140M Scale
- **Authors**: Edesio Alcoba, Kevin Rossell, Aman Gupta, Shao Tang, Jiwoo Hong, Pabel Carrillo-Mendoza, Wanderson Conceição Ferreira, Alvaro Tedeschi, Zayd Simjee, Shreya Rajpal, Bruno Finardi Hime, Christian Sousa, Luis Moneda, Herbert Fei, Daniel Silva, Rohan Ramanath
- **Institution**: Nubank (Brazil) (*tentative* — Card Delivery / Card Management agents, 140M-customer bank; Snowglobe simulator)
- **Date**: Fri 25 Sep 2026 (cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.30137
- **Abstract**: **Customer-experience (CX) agents** combine tools and LLMs over an organization's products; improving them—especially under regulation—is hard (limited manual-test coverage, live-experiment trust risk). Presents a **hypothesis-driven simulation workflow**: synthetic customers react to agent responses and simulated tool outputs enable multi-step agentic workflows without production backends. Applied via the **Snowglobe simulator** to Nubank's Card Delivery and Card Management agents (Nubank's highest-volume chat-support agent in Brazil). Across 4 deployed versions, simulated and production binary-evaluator scores correlate highly; simulation-guided iteration raised **transactional NPS by +36.69 points** in a live A/B; screening 16,000 simulated conversations selected an open-weight config that raised **self-service rate +8.82pp** (highest ever at Nubank) with no tNPS regression.
- **Key Innovations**: (1) a production-grade simulation-first screening loop for CX agents (synthetic customers + mocked tool outputs); (2) sim↔prod evaluator-correlation evidence across versions; (3) deployment-scale proof at 140M-customer bank with open/closed model selection.
- **Venue**: Preprint (industrial, Nubank).

---

## 5 Games, Auctions & Mechanism Design

### 5.1 Multiplayer Colonel Blotto — PPAD-Hardness with Player-Specific Values (2609.30019)
- **Title**: The Complexity of Multiplayer Colonel Blotto Games with Player-Specific Values
- **Authors**: Martin Bichler, Abheek Ghosh
- **Institution**: TU Munich / IIT-aligned (*tentative* — Bichler/Ghosh)
- **Date**: Fri 25 Sep 2026 (cs.GT)
- **arXiv**: https://arxiv.org/abs/2609.30019
- **Abstract**: Discrete multiplayer Colonel Blotto with **player-specific battlefield values** under uniform tie-breaking: two-player/common-values is polynomial, but the multiplayer/player-specific case breaks down — computing a **(c/n)-approximate Nash equilibrium is PPAD-hard** for constant c>0 even when every player has three resources (main technical step: PPAD-hard constant-approx well-supported NE). Contrast: with uniform tie-breaking and one resource per player, a pure NE is poly-time. PPAD membership holds for ε-approximate NE for inverse-exponentially small ε. With **non-uniform monotone tie-breaking**, PPAD-hardness appears even at one resource per player with identical values.
- **Key Innovations**: (1) first PPAD-hardness for multiplayer Blotto (player-specific values, uniform ties); (2) a clean tractability boundary (tie-break rule × resource count × value structure); (3) PPAD membership matching the hardness.
- **Venue**: Preprint. → Continuation of the window's Blotto line (see [09-21 game-rl-daily](/wiki/synthesis/2026-09-21/game-rl-daily.md) deterrence-info-design 2609.21064).

### 5.2 Winning Before You Play — Iterative Dominance in Three-Player Auction Bridge (2609.29615)
- **Title**: Winning Before You Play: An Iterative Capture Algorithm for Pre-Game Dominance Analysis in Three-Player Auction Bridge
- **Authors**: Sourish Sarkar
- **Institution**: single author (*tentative*)
- **Date**: Fri 25 Sep 2026 (cs.GT)
- **arXiv**: https://arxiv.org/abs/2609.29615
- **Abstract**: A bias-free three-player auction-bridge variant that fixes the passive-partner structural flaw of standard formats (No Trump strategies statistically outperform trump selections). Core = rule-based dual-algorithm framework: (1) an **iterative bidding algorithm** letting players calibrate bids from evolving hand strength; (2) a **predictive iterative algorithm** for expected tricks before the lead card, avoiding backtracking/high-complexity DP and cutting time complexity for real-time play. Validated on a **100,000-game simulation**: improved balance/fairness and high predictive reliability; framed as a model for uncertainty and strategic competition with applications to risk management in volatile markets.
- **Key Innovations**: (1) a three-player auction-bridge design redistributing post-bidding agency; (2) an iterative trick-anticipation algorithm with lower complexity than DP/backtracking; (3) 10^5-instance empirical validation and a bridge→finance analogy.
- **Venue**: Preprint (game-theoretic / applied).

### 5.3 Sequential Phragmén Guarantees 2-Approximate Core Stability (2609.29646)
- **Title**: Sequential Phragmén Guarantees 2-Approximate Core Stability
- **Authors**: Hau Chan, Jianan Lin, Chenhao Wang
- **Institution**: U Nebraska-Lincoln / academic (*tentative* — Chan)
- **Date**: Fri 25 Sep 2026 (cs.GT)
- **arXiv**: https://arxiv.org/abs/2609.29646
- **Abstract**: In approval-based committee voting, a size-k committee is **λ-stable** if no subset T of candidates attracts voter support exceeding λ× proportional share n|T|/k. Exact stability (λ=1) is a major open problem; the question is small λ>1 that can always be guaranteed. Proves that **weighted sequential Phragmén returns a 2-stable committee** — i.e. the **λ-core is nonempty for λ=2**, improving the previous best of **3.651** (Gao–Sun–Vondrák, EC 2026).
- **Key Innovations**: (1) 2-stability for the classical weighted sequential Phragmén rule; (2) best-known core non-emptiness factor (3.651→2); (3) an open-problem-relevant bound on proportional-representation stability.
- **Venue**: Preprint.

### 5.4 PUBG Ally — A Conversational Embodied Teammate at Live Service (2609.29837)
- **Title**: PUBG Ally: A Conversational Embodied Agent as an AI Teammate
- **Authors**: Beomsoo Kim, Byeongju Kim, Dohyun Kim, Dongwon Kim, Eunchong Kim, Hongmin Kim, Hyeojung Im, Hyeonbin Hwang, Hyeonghwan Kim, Hyoseok Seol, Insub Im, Irene Chen, Jaeseung Jeon, Jimin Hong, Kiyoon Yoo, Minkyoung Park, Seohyeon Jung, Seungjun Chung, Sue Hyun Park, Sungwoo Kim, Youngin Cho, Yujeong Son, Kangwook Lee, Hyunseung Kim
- **Institution**: KRAFTON (PUBG: BATTLEGROUNDS) + UW-Madison-aligned (*tentative* — Lew)
- **Date**: Fri 25 Sep 2026 (cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.29837
- **Abstract**: **PUBG Ally** is a voice-enabled embodied teammate for PUBG: BATTLEGROUNDS that reasons, acts autonomously, and plays alongside human players under strict latency. Combines agentic tool use with real-time control: an LLM agent uses a controlled interface to inspect game info, interpret speech, maintain context, decide what to say, and issue high-level action choices to a faster control layer (movement/combat/recovery). Training data = **~39k real sessions** of players alongside Ally (gameplay, speech, decisions, tool use, actions, feedback). Evaluation = player feedback + preference comparisons to close the offline-vs-player-preference gap. Live service required low-latency on-device execution + player-facing safeguards (compression, context compaction, safety training, runtime guardrails, memory redaction). A 141-country survey: among confirmed players, **net recommend positive by +25.1pp** — players describe Ally as teammate/companion, not tool.
- **Key Innovations**: (1) production conversational embodied agent deployed in a live AAA game as a *teammate* (not opponent); (2) real-gameplay data flywheel (39k sessions) for agent training and gap-closing evaluation; (3) on-device latency + safety/redaction engineering for voice-enabled game agents.
- **Venue**: Preprint (industrial, KRAFTON). → Tie-in with the wiki's game-RL track ([[eureka]], [09-24 game-rl-daily](/wiki/synthesis/2026-09-24/game-rl-daily.md)).

---

## 6 World Models & Reasoning RL

### 6.1 RLVR Landscapes Can Be Benign — Spin-Glass View (2609.28625)
- **Title**: RLVR landscapes for iterated multiplications can be benign: Insights from spin-glass theory
- **Authors**: Noa Rubin, Zohar Ringel
- **Institution**: Hebrew University of Jerusalem-aligned (*tentative* — Ringel)
- **Date**: Fri 25 Sep 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.28625
- **Abstract**: Whether **RLVR** can learn genuinely new reasoning is debated. Studies its optimization landscape on algorithmic tasks (iterated group/quasigroup multiplication) by mapping entropy-regularized RLVR over myopic tabular policies to an **energy-based (spin-glass) model over deterministic policies** — an upper bound on what RLVR can achieve and a rigorous landscape description. For a wide class of uncorrelated-input models/tasks the landscape is **benign (no trapping local minima)**; practical difficulty instead comes from **diffusive barriers and gradient-estimation error**, often mitigable via the entropy regulator. A transformer trained from scratch with only last-token rewards learns an algorithmic chain-of-thought for iterated non-Abelian group multiplications.
- **Key Innovations**: (1) quantifies "RLVR easiness" via spin-glass theory (no local minima, benign landscape); (2) separates landscape ruggedness from diffusive/estimation obstacles; (3) from-scratch transformer evidence that verifiable-reward chain-of-thought is learnable in the tabular-theoretically-benign regime.
- **Venue**: Preprint.

### 6.2 Anchored Planning — Frozen World Models Can Plan Better (2609.30036)
- **Title**: Aim Short to Reach Far: Your Frozen World Model Can Plan Better Than You Think
- **Authors**: Xvyuan Liu, Jianjie Fang, Chen Gao, Yong Li
- **Institution**: Tsinghua-anchored (*tentative* — Gao/Li)
- **Date**: Fri 25 Sep 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.30036
- **Abstract**: Visual world-model planners usually score predicted outcomes by distance to the encoded **goal image** — but this target can limit control even with exact dynamics and globally optimal short-horizon search, because reaching a goal may require **actions that initially move away from it**. With frozen **LeWM** models, intermediate targets substantially improve action synthesis and recorded-action ranking on Cube/PushT/Reacher/TwoRoom. **Anchored Planning** retrieves a recorded segment whose start/end resemble the current/goal observations, then aims at an observation shortly after its start. Without retraining, planning toward observed targets beats the released LeWM planner **on every task** in long-range evaluation; extra final-goal search fails to match the gains. Lower successor-prediction error need not translate into better control — success depends on target placement and shrinking retrieval span during execution.
- **Key Innovations**: (1) shows goal-image scoring is an action-synthesis bottleneck even under exact dynamics (non-monotonic trajectories); (2) Anchored Planning (retrieve + aim-at-near-target) as a training-free fix on frozen LeWM; (3) a target-placement/retrieval-span account of when world models control well.
- **Venue**: Preprint. → Directly extends the wiki's LeWAM line ([09-24 arxiv-daily](/wiki/synthesis/2026-09-24/arxiv-daily.md) 2609.27455).

---

## Key Trends Across This Window

1. **Decision-layer + evaluation-integrity is the window's spine** (28614 reward hacking with a 74.6% confirmed-hack rate and 6.5% panel-miss; 28850 RECLAIM's 41/27/15 reproducibility ladder; 29709 CTT-misreads critique of LLM-judge reliability; 29429/30243 JEV-as-detector precision versus JevOut interface fragility): after last window's rec-evaluation science, this window audits *agents and judges that grade* — instrument validity, not model power.
2. **Industrial recommender consolidation is back on arXiv** (28589 OneTrans-V2 with GMV +9.74%; 29182 ScalarLens CTR embeddings winning 25/27 settings; 29983 semantic-ID credit attribution; 30177 Roblox search-RL NDCG@20 +8.9): the September CTR/ads drought on the daily arXiv side breaks with **2 direct CTR/rec-industry papers (plus X-Rec and CMRec in runner-ups)**.
3. **JEV matures into an evaluation infrastructure family in one window** (29429 as a 63×-cheaper zero-shot alignment detector at AUROC 0.886; 30243 exposing interface fragility under context; 29769 as a rubric judge with correlated LLM-judge errors): the wiki's JEV thread (see 09-24 paper-check 2609.27678 "Same Scores, Different Decisions") crosses from empirical robustness studies into tooling.
4. **Sequential architecture work spans "model the world jointly" to "compress the recurrence"** (29792 TimeBraid LM⊗TSFM fusion; 28809 SRM recursive interpretable streams; 29618 MLA–SSM ablation; 29812 FlashLoop 1.64×/6× looped-loop-looping; 29913 MILO many-shot KV compression): efficiency is the running theme, unification the ambition.
5. **Games/auctions line is thin but sharp** (30019 PPAD-hardness for multiplayer Blotto; 29646 core stability 3.651→2; 29615 auction-bridge iterative dominance; 29837 PUBG Ally as a live-service conversational teammate).
6. **World models face scrutiny of the planning target itself** (30036 Anchored Planning beating final-goal scoring on frozen LeWM — "aim short to reach far"), and **RLVR gets a benign-landscape theory** (28625) that shifts blame from ruggedness to diffusive barriers.

## ADS / CTR Coherence Check

**This window breaks the September raw-arXiv drought: 2 direct industrial CTR/rec papers featured** (ScalarLens CTR numerical embeddings 2609.29182; OneTrans-V2 deployed rec-cascade unification 2609.28589) **+ 2 more in runner-ups** (X-Rec continuous-item-embedding generative retrieval deployed on TikTok 2609.29180; CMRec cross-country code-mixing for generative rec with **+1.77% advertising revenue / +2.64% orders** live-A/B 2609.28972). Fair-valuation/mechanism-side: **Improved Revenue Guarantees for Selling Separately and Bundling** (2609.28873, OPT ≤ 3.52·max{SREV, BREV}, narrowing Ma–Simchi-Levi's 5.2, gap-to-lower-bound 2) is value-relevant for ads/menu design, and **Online House Allocation with Subsidy** (2609.29691) generalizes the subsidy-based fairness lens. Buyer-side / market-shaping: **Can Labor Markets Function in the Age of AI?** (2609.30058) on the AI-driven evaluation bottleneck in hiring. The Sep-25 checks across the sibling **game-rl** and **paper-check** layers should pick up the remaining ads-adjacent remainder; this report's 34 IDs hold.

## Runner-Ups (shortlist, all grep-verified 0 hits in `wiki/`)

- **2609.28873** Improved Revenue Guarantees for Selling Separately and Bundling — OPT ≤ 3.52·max{SREV,BREV} for additive single buyer (previous best 5.2, Ma–Simchi-Levi; lower bound 2). Complements the mechanism-design thread (cs.GT).
- **2609.29691** Online House Allocation with Subsidy — houses arrive online, envy-freeability maintained with bounded recourse; exact subsidy minimization only with ≤1 extra house; impossibility bounds vs adaptive/non-adaptive adversaries; learning-augmented algorithms (cs.GT; Oxford, Wooldridge-lineage).
- **2609.30028** How does Adversarial Influence Scale in Multi-Agent Systems? — defection rate rises **linearly with the fraction of deceivers** (not group size); LLM agents defect as minority deceivers, unlike human conformity; private coordination can hurt deceivers (cs.AI; Princeton, Griffiths-lineage).
- **2609.30058** Can Labor Markets Function in the Age of AI? The Evaluation Bottleneck in Hiring — AI-generated applications degrade the informativeness of job materials; Bayesian firms fall back on coarse observables; multistage hiring arises endogenously; inexperienced-compatible applicants most exposed (cs.GT; Stanford/Cornell, Ashlagi-Johari-Kleinberg).
- **2609.28576** VINTAGE-TS — revision-aware (observation-time vs information-availability-time) time-series foundation-model adaptation with an ALFRED-based rolling evaluation and deluded-label filtering; explicitly *does not* claim empirical model advantage (software/contract engineering focus) (cs.LG).
- **2609.28972** CMRec — cross-country code-mixing for generative recommendation at the **data level** (dual-constrained token substitution via shared semantic codebook); live A/B: **+1.77% ad revenue, +2.64% orders** on a large e-commerce platform, protecting data-rich countries while helping data-sparse ones (cs.IR).
- **2609.29769** JEV vs. LLMs as Rubric Judges — Jev differs significantly from flash-tier LLM rubric judges in only 8/27 comparisons, at **29–325× lower cost** and 30–220× less time; but LLM judges repeat nearly all of Jev's most-confident errors, so a defer-to-LLM cascade gains ≤1.5–2.0 pts (correlated-error caveat) (cs.CL).
- **2609.29180** X-Rec Technical Report — generative rec learning the recommendation distribution in **continuous item-embedding space via flow matching** (anchor conditioning + Riemannian flow + late-interaction diffusion transformer); matches SID-AR quality at **3.46× throughput**; deployed as an extra retrieval source for TikTok vertical content (**+4.1484% vertical / +0.0111% general engagement**) (cs.IR; ByteDance/TikTok).

## Cross-Reference Index (Sibling & Runner-Up Coordinates)

- **Same-window coordination**: The sibling `arxiv-daily` (09-25) wrote first and claimed **40 IDs** (28 featured + 9 runner-ups) from its published-09-24 window — including the window's agent-RL/credit and evaluation items (**GRAFT 2609.28963**, **SLCA-GRPO 2609.29050**, **S²D-OPD 2609.29142**, **Rufus-Air 2609.29421**, **Where LLM Graders Succeed 2609.29333**, **PixelJev 2609.29283**, **Forecast-Dojo 2609.28876**, slate-recommendation DP 2609.29453, etc. — full list in the daily). This report claims the other **34 IDs (26 featured + 8 runner-ups)** from the Fri-25 window (2609.28475–2609.30264): **28589, 29182, 29983, 29815, 30177, 29792, 28809, 29618, 29812, 29913, 29781, 29845, 29709, 28784, 28614, 28850, 29429, 30243, 29545, 30137, 30019, 29615, 29646, 29837, 28625, 30036** (featured) and **28873, 29691, 30028, 30058, 28576, 28972, 29769, 29180** (runner-ups). Sibling `arxiv-paper-check` (runs after both) should treat the union (40 + 34) as claimed and grep-verify before re-featuring.
- **Unclaimed-remainder map** (for later sibling sweeps): strongest remaining unclaimed candidates noticed in-window include 2609.28614-adjacent agent-security work and: 2609.28475 (forecasting-agent reliability routing), 2609.28547 (PAWS policy-driven agentic world simulation), 2609.28980 (Seek self-evaluative retrieval), 2609.29073 (tool-augmented spatial reasoning), 2609.29109 (CounterRoute counterfactual credit), 2609.29444 (IterSynth deep-search agents), 2609.29626 (iCoder-27B frontier coding model), 2609.29773 (evolving LLM agent environments), 2609.30063 (Self-Play Pretraining with Zero Data), 2609.30192 (SAGE topological guidance for long-horizon reasoning), 2609.30264 (AD-WM action-discriminative world models) — a starter map only, not claim-verified.

(End of file)