---
title: "arXiv Paper Check — AI & CTR (October 15, 2026)"
type: synthesis
created: 2026-10-15
updated: 2026-10-15
sources: []
tags: [arxiv, arxiv-paper-check, daily-check, ai, ctr, advertising, recommendation, generative-retrieval, agents, retrieval, memory, reasoning, rl, distillation, post-training, world-models, interpretability, efficiency, daily-digest]
---

# arXiv Paper Check — AI & CTR (October 15, 2026)

**Window framing, stated up front**: arXiv exposes no rolling "last 24 hours". The freshest *announced* blocks at run time are the **2026-10-14 (Wed)** and **2026-10-15 (Thu)** waves. Prior coverage in the series: the [2026-10-14 arxiv-paper-check](../2026-10-14/arxiv-paper-check.md) covered the **Oct-10 (Sat)** submission wave, and today's siblings ([arxiv-daily](../2026-10-15/arxiv-daily.md), [arxiv-ai-search](../2026-10-15/arxiv-ai-search.md)) mined the **submitted Oct-13/14** block. This report therefore covers the **Oct-14/15 announcement blocks**, which are fresh to the series. Note that arXiv's "announcement day" ≠ submission day: a paper can be *announced* Oct-14/15 while its v1 was submitted days earlier (or, for late cross-lists, weeks earlier) — every entry below states its **v1 date** so the reader can judge recency.

**Harvest & method (degraded mode)**: the arXiv export API (`export.arxiv.org/api/query`) returned **`HTTP 429` ("Rate exceeded")** on all date-range and `sortBy` queries this run, making the Atom/export path unusable. Pivoted to the **`arxiv.org` listing pages** (a different host; not throttled) — `pastweek` listings across 15 categories (cs.IR, cs.AI, cs.LG, cs.CL, cs.CV, cs.MA, cs.CR, cs.GT, cs.NE, cs.HC, cs.SI, `stat.ML`, cs.DB, cs.DC, cs.SE) — parsing **7,628 rows → 5,183 unique IDs**. Listing pages carry title/authors/subjects/comments but **no abstracts**, so abstracts were then fetched from each paper's own `arxiv.org/abs/<id>` page (also not throttled). Selected **26+ papers**, all **grep-verified 0-hit** against the entire live `wiki/` tree (**9,081-ID baseline**) before writing, and collision-managed against today's siblings (`arxiv-daily`, `arxiv-ai-search`, `game-rl-daily`, `conference-digest`).

**CTR status**: **zero explicit Click-Through-Rate prediction papers** this window (`"click-through rate"`, `"CTR prediction"`, `"pCTR"` → 0). The industrial CTR *architecture* lane (new scaling laws, long-sequence encoders for CTR) is **empty again** — a theme now recurring across the whole October series. The advertising/recommendation lane nevertheless returns a strong set: **agent ads / ad-attack surface**, **advertising supply-chain transparency**, **advertiser competition modeling**, an **industrial Disney+ homepage ranker**, a **large-scale RecSys training-stability framework**, a new **industrial scaling dimension** for short-video ranking, **WeChat's generative retrieval** in production, **Kuaishou's summary-attention V2**, and **retrain-free generative retrieval DocIDs** — recorded in §①.

⚠️ **Affiliation discipline**: arXiv listing/abs metadata carries no reliable affiliation field; affiliations below are **inferred only where a company/team is named in the title or author block** (e.g. "Kwai/OneRec Team", "in WeChat") and are marked *(inferred)*. Venue tags appear only when self-reported via the `comment` field.

---

## ① CTR, Advertising & Recommendation (10)

### Welcome to the Age of Agent Ads: Using On-Policy Attacks to Steer Agentic Decisions
- **Authors**: Tim R. Davidson, Marija Šakota, Joshua Joseph, Robert West (EPFL — *inferred*)
- **arXiv**: [2610.17195](https://arxiv.org/abs/2610.17195) — cs.CL · v1 **Mon 12 Oct 2026**
- **Key contribution**: As people delegate option-ranking (shopping, jobs, travel) to AI agents, "agent ads" create incentives to *steer* agentic decisions. The authors expose **on-policy attacks** — steering a decision *without* pushing any individually-aligned behavior off-policy, and therefore invisible to alignment training and terms-of-service defenses that currently catch off-policy exploits. The example attack injects a **truthful negation about a fictitious concept** ("Does not contain blizyester") into a listing; the agent searches the web ("What is blizyester?"), surfacing planted pages that link the concept to harm ("Blizyester linked to dementia"); the safety-trained agent then **penalizes every competitor** missing the negation. Across **four real-world listing datasets**, some frontier models are exposed, letting an adversary penalize competitors *without violating platform listing guidelines*.
- **Why it matters**: A new threat model at the ads×agents intersection, and the natural counterpart to the wiki's generative-ad-auction line ([[welcome-to-the-age-of-agent-ads]] candidate) — "ads aimed at agents" become an attack surface for the ranking layer itself.

### Declared but Unaccountable: Measuring the Seller-Identity Gap in Advertising Supply-Chain Transparency
- **Authors**: Tommaso Grotto, Alessandro Cantelli-Forti, Alessio Merlo
- **arXiv**: [2610.14661](https://arxiv.org/abs/2610.14661) — cs.CY, cs.CR, cs.NI · v1 **Sat 10 Oct 2026**
- **Key contribution**: Formalizes a minimum accountability condition for public ad transparency — an account authorized by a publisher in `ads.txt`/`app-ads.txt` should appear in the applicable `sellers.json` registry — and names the violation the **seller-identity gap**: the authorization stays visible and machine-readable, but its public *verification path* breaks. Measures the gap over **233.4M normalized ad-transparency records** with an "absent-only, coverage-aware" evidence rule. Row-level floor is **24.25%** in a high-popularity/low-removal population and **30.71%** among publishers tied to ≥100 copyright-removal requests (a **+6.45 pt** increase); standardizing over **1,469 shared ad systems** reduces the primary contrast to **4.65 pts** (~72% remains *within* systems, ~28% is composition residual).
- **Why it matters**: An *auditing* contribution for the ads supply chain — quantifies where programmatic-ads public verification silently stops, useful background for the wiki's transparency/anti-fraud threads.

### LACRM: LLM-Guided Mining of Directed Advertiser Competition Relationships in E-Commerce Advertising
- **Authors**: Xiang Shi, Yitian Kou, Bing Li, Shengsheng Niu, Chun Gan, Linghui Meng, Jie He, Zhangang Lin, Ching Law (Tencent — *inferred*) · arXiv: [2610.13959](https://arxiv.org/abs/2610.13959) — cs.LG · v1 **Wed 26 Aug 2026** (late cross-list; announced Oct-14)
- **Key contribution**: Ad platforms fail to model the **externalities among advertisers** because rivalry is *directed, multi-faceted, and partially observable* — properties flat interaction graphs, taxonomy rules, and single-embedding models miss. **LACRM** builds **directed competition graphs with continuous edge intensities** via a three-stage pipeline: LLM-driven **role-separated profiling** (moves beyond symmetric similarity), **asymmetric multi-route retrieval** to uncover realized *and* latent rivals, and **listwise learning-to-rank aligned to temporal auction behavior** to model directed intensity. Multi-LLM + human studies support that recovered latent rivals reflect real market competition. Production A/B: guided **bidding +1.73%** and **incentive allocation +1.14%** ad revenue.
- **Why it matters**: Turns advertiser-competition externality into an explicit reusable signal for auction/bidding decisions — the *relational* counterpart to the wiki's CTR/auction modeling line.

### DRanker: A Transformer-Based Multi-Task Ranking Model for the Disney+ Homepage
- **Authors**: Priya Nirmal Singh Khokher, Daniel Nemirovsky, Benjamin P. Whitesell, Ethan Sukrae Lee, Eric Wulf, Tom Chee-Duffy, Nicholas Flores (Disney — *inferred*)
- **arXiv**: [2610.15696](https://arxiv.org/abs/2610.15696) — cs.LG · v1 **Sun 11 Oct 2026**
- **Key contribution**: An industrial **encoder-only, multi-task transformer ranker** over enriched engagement-history sequences with a lightweight **causal debiasing** mechanism, plus the serving stack enabling transformer ranking at scale. A notable *negative-design* result: through iteration, **simpler designs consistently beat more complex alternatives** on offline metrics, qualitative behavioral eval, **and** production. Deployed globally, **+1% key engagement metric** and **+0.5% DAU** across all experiences powered by the ranker.
- **Why it matters**: A clean industrial data point for the wiki's "transformers in production ranking / simpler-is-better" theme, with a concrete multi-task + debiasing recipe.

### Understanding and Mitigating Training Instability in Large-Scale Recommender Systems: A Cascade Perspective
- **Authors**: Yuening Li, Zeyu Wang, Zhen Zhang, Jiayi Liu, Zhimeng Jiang, Yuji Roh, Weikai Xu, Mingyan Gao, Onkar Dalal, Chuan He, Liang Liu (Amazon — *inferred*)
- **arXiv**: [2610.14394](https://arxiv.org/abs/2610.14394) — cs.IR, cs.LG · v1 **Fri 9 Oct 2026**
- **Key contribution**: Characterizes the **G-W-L cascade** in industrial Short-Form-Video recommenders: rapid distribution shift + growing model complexity trigger **gradient explosion → weight explosion → loss explosion**. Proposes a structured mitigation framework where interventions map explicitly to cascade stages — **(G) gradient control, (W) weight/activation stabilization, (L) loss shaping** — validated on a major industrial SFV recommender.
- **Why it matters**: Makes "why large recommenders diverge" a first-class, staged debugging framework rather than an ad-hoc tuning exercise — directly relevant to the wiki's large-scale-training topics.

### Chain Dimension Scaling: Communication-Efficient Loop-Style Scaling for Industrial Short-Video Ranking
- **Authors**: Zhimeng Jiang, Yuening Li, Ruixiao Sun, Yuanzhen Lin, Kun Jin, Chuan He, Liang Liu (Amazon — *inferred*)
- **arXiv**: [2610.16415](https://arxiv.org/abs/2610.16415) — cs.AI · v1 **Mon 12 Oct 2026**
- **Key contribution**: Proposes **CDS**, a scaling strategy **orthogonal to width and depth**: repeatedly apply a *single shared* feature-interaction block, so the number of iterations (**chain length**) becomes a new scaling dimension that **adds no parameters**. A lightweight **intra-chain residual** stabilizes optimization. Two regimes: *compression* (shallow block + long chain matches deeper baselines with fewer params/faster training) and *quality-scaling* (longer chain under fixed params → monotone gains). Production multi-task short-video ranker: within **0.03%** of baseline offline quality while cutting trainable params **−26.6%** and raising training throughput **+6.4%**, with neutral-to-positive online. Wall-clock analysis attributes the win mainly to **lower cross-device synchronization + optimizer-update cost**, not reduced FLOPs.
- **Why it matters**: A rare *scaling-law-adjacent* contribution for industrial rankers — parameter-free depth via weight sharing, the recommender analogue of looped/weight-tied LLM blocks (cf. [[latentloop]] below).

### WeGR: Unified Generative Retrieval for Industrial Search Systems in WeChat
- **Authors**: Jiajun Han, Guoxin Ma, Felix, Liangsheng Xu, Ruiqi Yu, Yingdi Guo, Zongbing Wang, Xinhua Ye, Chenyan Hua, Xin Xie, Pengcheng Yang, Haijun Wu (Tencent WeChat — *inferred*)
- **arXiv**: [2610.16979](https://arxiv.org/abs/2610.16979) — cs.IR, cs.AI · v1 **Mon 12 Oct 2026**
- **Key contribution**: Industrial generative retrieval (GR) is limited by (1) Semantic-ID tokenizers that fail to inject collaborative signals while keeping codebook utilization high, and (2) RL under **exact-SID-match reward sparsity**. **WeGR** = **CoCo-VAE**, a collaborative, collapse-free tokenizer (query↔item and item↔item signals + codebook refresh + complementary regularization), and **DHPO (Dynamic Horizon Policy Optimization)**, which progressively expands the reward/optimization horizon across the SID hierarchy — leveraging behavioral rewards **without auxiliary reward models**. Two-month online A/B in **WeChat E-commerce Search**: **+2.5%** relative (reported).
- **Why it matters**: A production-scale generative-retrieval deployment with a concrete **sparse-reward** fix — the industrial counterpart to the wiki's GR entries and today's [arxiv-ai-search](../2026-10-15/arxiv-ai-search.md) GR-vs-dense debate.

### HASTE: Hierarchical and Attribute-aware Supervision for Generative Recommendation
- **Authors**: Tripti Shukla, Shwetha Somasundaram, Akshat Gupta, Rohit Garg, Paul Duff, Ian Anderson (Etsy — *inferred*)
- **arXiv**: [2610.17368](https://arxiv.org/abs/2610.17368) — cs.IR, cs.AI, cs.LG · v1 **Mon 12 Oct 2026**
- **Key contribution**: Standard causal cross-entropy over semantic IDs ignores their **hierarchical structure** and starves tail items. **HASTE** adds (i) a **Hierarchical Loss** supervising *each level* of the semantic-ID hierarchy (accelerating convergence), and (ii) **Attribute-Specific Losses** that preserve fine-grained item attributes using the LM's intrinsic semantic knowledge to improve **long-tail** representations. Evaluated on a fashion benchmark and multiple Amazon domains.
- **Why it matters**: Attacks the tail / training-efficiency problem in generative recommendation purely at the *loss* level — cheap to bolt onto existing GR models.

### Kwai Summary Attention V2 Technical Report
- **Authors**: OneRec Team (Chenglong Chu, Guohong Mu, Guowang Zhang, Hao Peng, Hui Wang, Jian Liang, Jiangxia Cao, … Ruiming Tang, Wenwu Ou, et al.) (Kuaishou — *inferred*)
- **arXiv**: [2610.18654](https://arxiv.org/abs/2610.18654) — cs.LG, cs.AI, cs.IR · v1 **Tue 13 Oct 2026**
- **Key contribution**: Fixes two bottlenecks of hybrid **KSA-Full** (Summary-token compression interleaved with full attention): (1) all layers must share one summary chunk, blocking flexible per-layer **KV-cache compression**; (2) full-attention layers still pay quadratic prefill and ignore the injected summary tokens. **KSA V2** makes summary tokens serve **two roles — KV memory *and* sparse indexer** — enabling flexible per-layer compression and **reduced compute in full-attention layers**.
- **Why it matters**: The wiki's long-context/efficiency line, from Kuaishou's OneRec team — a production-attention compression update (cf. `arxiv-ai-search`'s ReaDy/Latent-Compaction/KV cluster).

### Computed, not Memorized: Bit-Factorized Identifiers for Efficient Generative Retrieval
- **Authors**: I-Fan Lin, Zhen Zhang, Faegheh Hasibi, Suzan Verberne (Leiden — *inferred*)
- **arXiv**: [2610.17467](https://arxiv.org/abs/2610.17467) — cs.IR · v1 **Mon 12 Oct 2026**, v2 **Wed 14 Oct 2026**
- **Key contribution**: Numeric Document IDs make GR efficient but **generalize poorly to unseen documents** (they must be learned during indexing). Proposes a **bit-factorized numeric DocID**: each DocID is a token sequence factorized into *bits*, each token scored as the **sum of its bits**, and each bit derives meaning from the **model's own representation** rather than a memorized embedding. Unseen-document DocIDs therefore stay scorable **without retraining**. On NQ320K/TriviaQA: **+20 pts Hit@10 on unseen docs**, up to **7× lower inference latency** than numeric DocID baselines; only **−3 pts** vs weight-update methods on MS MARCO with no extra training.
- **Why it matters**: A retraining-cost breakthrough for the GR line — directly relevant to the wiki's indexing/adaptation topics.

**Also worth recording (ads/rec, not featured)**: `2610.16569` *From a Large-Scale Teacher to Efficient Multimodal Students for Search Relevance* (LLM-judge → compact multimodal e-comm relevance students); `2610.16137` *Recall Begets Recall* (**ReMind**, recurrent self-terminating memory **ranker** with compound cueing + metamemory); `2610.16038` *OT-FlowRec* (optimal-transport multi-bridge flow for multimodal sequential rec); `2610.16132` *UniSGR-V2* (**TacGR**, target-side feature anticipation/crossing inside semantic-ID decoding).

---

## ② Agents, Retrieval & Memory (5)

### Why Generate a Click? Plug-in Decision Heads for Web Agents
- **Authors**: Chengguang Gan, Yunhao Liang, Hanjun Wei, Qinghao Zhang, Zhixi Cai, Shiwen Ni · arXiv: [2610.20107](https://arxiv.org/abs/2610.20107) — cs.CL · v1 **Wed 14 Oct 2026**
- **Key contribution**: Web agents waste the generator on choices among a few action types and a few dozen marked elements. **Plug-in decision heads on a frozen VLM** read those choices directly from hidden states — predict action type, pool visual tokens per numbered box to pick the target, point at text options — with a **confidence cascade** that lets heads act when sure, else falls back to the generator decoding from the **same forward pass's KV cache**. Qwen3-VL 4B/8B on 213k web steps: heads decide **12–64%** of steps; a loose threshold lifts WebArena task success **12.5→13.8% (4B)**, **13.6→14.6% (8B)** at **<½ the generated tokens**. Training heads *jointly* hurts the generator (up to −4.9 pts); frozen-generator heads avoid this.
- **Why it matters**: A clean efficiency/serving result for GUI agents — turn "generate a click" into a *classification* head, without touching the base model.

### Retrieve What Helps, Only When It Helps: Agentic RL for Selective Retrieval-Augmented MT
- **Authors**: Shijun Li, Yang Liu, Najmeh Sadoughi, Dongmei Wang, Xinjie Li, Zhu Liu, Rohith Mysore Vijaya Kumar, Yuzong Liu (Amazon — *inferred*)
- **arXiv**: [2610.19528](https://arxiv.org/abs/2610.19528) — cs.CL, cs.AI, cs.IR · v1 **Wed 14 Oct 2026**
- **Key contribution**: Argues translation is a **partial-evidence regime** — parametric knowledge suffices for many inputs; external evidence helps a subset, and *supports* rather than provides the translation. **SRAT** is an agentic RL framework learning **when to translate directly vs. retrieve, what to retrieve, and how to integrate**, optimizing final translation quality. To align retrieval with *downstream quality* (not mere similarity), adds **joint Plackett–Luce optimization** + translation-quality contrastive training. Beats never-/always-retrieve baselines on idiom, knowledge-intensive, and document-level MT.
- **Why it matters**: "Retrieval as a learnable action" — the RAG analogue of on-policy tool use, with quality-aligned retriever training.

### Beyond Retrieval: Evidence Access and Event Aggregation in Agent Memory
- **Authors**: Zerui Yang, Quan Xue, Chaorui Zhang, Xueyan Niu, Xuanyu Zheng, Xiyuan Wang, … Wei Han, Bo Bai (Huawei Noah's Ark — *inferred*)
- **arXiv**: [2610.19474](https://arxiv.org/abs/2610.19474) — cs.AI · v1 **Wed 14 Oct 2026**
- **Key contribution**: History questions often need **aggregating events**, which retrieval alone can't do. Combines **source-preserving evidence access** (Trajectory Memory: keep the raw trajectory, build a source-addressable reading view at query time) with **executable aggregation** (**TallyMem**: reusable event ledger + model-generated event specs + deterministic execution). On 776 MINTEval questions: Qwen3-32B exact match **35.2%→49.0%** (+13.8 over TM); a controlled probe without routing reaches **82.8%→93.8%** (+11.0).
- **Why it matters**: Pushes agent memory from *retrieval* to **computation over events** — matches the wiki's memory-management cluster.

### SWE-Stream: Scaling Executable Training Data for SWE Agents via Progressive Construction and Elastic Streaming
- **Authors**: Chengyang Liu, Wen Yang, Shifeng Chen, Delai Qiu, Ji Yang, Junnan Zhu, Yining Wang, Shengping Liu · arXiv: [2610.20193](https://arxiv.org/abs/2610.20193) — cs.SE, cs.AI · v1 **Wed 14 Oct 2026**
- **Key contribution**: SWE-agent training is bottlenecked by scarce **executable** tasks. **SWE-Stream** progressively validates/refines task candidates (reusing artifacts, targeted completion only when needed) with an **elastic scheduler** adapting execution budgets. From 10,728 repos × 6 languages it builds **80,874 validated tasks / 118,688 trajectories**; fine-tuning Qwen3-30B-A3B-Thinking reaches **69.0 / 49.3 / 45.42%** on SWE-bench Verified / Multilingual / Pro. Streaming gives **1.45×** task throughput + **13.2%** more accepted tasks than fixed-limit streaming.
- **Why it matters**: A *data-engine* contribution for coding agents — the infrastructure counterpart to the wiki's SWE-bench/agent entries.

### OS-Bench: Evaluating SWE Agents on Cross-OS Code Migration
- **Authors**: Qirui Jin, Kenan Li, Liao Zhu, Lingching Tung, Yikai Zhang, Yijia Wu, … Qingwei Lin, Wenke Lee (Georgia Tech + MSRA — *inferred*)
- **arXiv**: [2610.19368](https://arxiv.org/abs/2610.19368) — cs.SE · v1 **Wed 14 Oct 2026**
- **Key contribution**: A new executable benchmark for **cross-OS migration** (Linux↔Windows), a common but under-benchmarked SWE task. Migration opportunities are found by diffing execution coverage of the same repo on both OSes, yielding **140 validated tasks from 111 repos** (C/C++/C#/Go/Rust). Best configs reach only **26.4%** success on Linux-target and **20.4%** on Windows-target tasks while preserving correctness on both.
- **Why it matters**: Extends SWE evaluation into **platform-aware** capability — a new *hard* axis where current agents are weak.

---

## ③ Post-Training, RL & Distillation (8)

### MMLA-RSI: Recursive Self-Improvement through RTT and RTMA
- **Authors**: Junyi Zou, Avrova Donz · arXiv: [2610.20294](https://arxiv.org/abs/2610.20294) — cs.CL, cs.LG · v1 **Wed 14 Oct 2026**
- **Key contribution**: A recursive-self-improvement scheme where the agent improves **how it acts** (Reasoning-Time Training, changes policy state Φ) **and which experience it retains** (Reasoning-Time Memory Adaptation, changes authoritative memory M) — and makes *each adaptation method itself* an object of improvement. Bounded executable rule languages + a fixed interpreter, trusted committer, and independent evaluator constrain what can change. Retaining LARC feedback updates cuts expected error by **24.65 / 36.65 pts** on two initializations in 4-candidate program selection.
- **Why it matters**: The wiki's RSI/self-improvement line — here grounded in *bounded, auditable* successor admission rather than free-form self-editing.

### SwarmRSI: Recursive Self-Improvement through Evolving Scientific Agent Swarm
- **Authors**: Qianru Meng, Xi Zhang, Konstantinos Papakostas, Congfeng Cao, Wenxiang Hu, Tianyi Lu, … Zhaochun Ren, Yougang Lyu · arXiv: [2610.20431](https://arxiv.org/abs/2610.20431) — cs.AI, cs.CL · v1 **Wed 14 Oct 2026**
- **Key contribution**: RSI for science via a **swarm** that pools evidence/implementations across research directions. **Feedback-Guided Swarm Mutation** refines hypotheses *and* implementations using other agents' experimental feedback (disentangling "revise hypothesis" vs "fix implementation"); **Complementary Swarm Recombination** reuses retained hypotheses and complementary code components across agents. SOTA on OpenProblems / NatureBench / MLE-Bench Lite; accumulated experience transfers to held-out tasks; biologists reproduce its programs.
- **Why it matters**: Swarm-level RSI — pairs with MMLA-RSI above and the wiki's multi-agent research-automation thread.

### Token Utility for On-Policy Distillation via Local Trust-Region Optimization
- **Authors**: Narayanan Sadagopan, Yilan Chen, Vijay Lingam (Google — *inferred*) · arXiv: [2610.18883](https://arxiv.org/abs/2610.18883) — cs.LG, cs.AI · v1 **Thu 1 Oct 2026** (announced Oct-14)
- **Key contribution**: Instead of heuristic token-selection for on-policy distillation (OPD), derives importance **from the objective itself**: how much each position's loss can drop under an equal local-KL budget, i.e. the utility **sₜ = gₜᵀ Fₜ† gₜ** (logit gradient + categorical Fisher). For reverse-KL it equals the student-weighted **variance of the student–teacher log-prob ratio**; for forward-KL it equals the **Pearson χ² divergence**. Instantiated as **Fisher Utility Weighting (FUW)**: +1.35–4.0 (reverse-KL) / +1.08–2.71 (forward-KL) macro points over uniform OPD across 7 math benchmarks × 3 Qwen3 teacher–student pairs.
- **Why it matters**: A principled, closed-form token-weighting criterion — the theory-side answer to the wiki's "which tokens to distill" question.

### Demystifying On-Policy Distillation: Where Does the Teacher's Advantage Live?
- **Authors**: Yiping Li, Fan Zhao, Zhibo Hou, Zhiyu An, Wan Du (UC Merced — *inferred*) · arXiv: [2610.19145](https://arxiv.org/abs/2610.19145) — cs.LG · v1 **Tue 13 Oct 2026**
- **Key contribution**: Revisits OPD as knowledge distillation and localizes the teacher's advantage via **controlled token flips** at teacher–student disagreements. Single-token flips give modest gains; **repeated flips raise accuracy 28.4%→74.5%** (near the teacher's 76.9%). **Mass- and KL-based selection beat random flips by 15–18 pts** at matched counts. Selective intervention stays useful *after* OPD, but greater argmax agreement ≠ better accuracy across model pairs.
- **Why it matters**: An *empirical anatomy* of OPD that complements FUW above — the wiki's distillation cluster now has both theory and diagnostic evidence.

### MIPS: Mitigating Mode Collapse in Reinforcement Learning for Large Outcome Spaces
- **Authors**: Armaan Sandhu, Abhijeet Sinha, Dianbo Liu · arXiv: [2610.19457](https://arxiv.org/abs/2610.19457) — cs.LG, cs.AI · v1 **Wed 14 Oct 2026**
- **Key contribution**: Expected-reward maximization collapses onto few outcomes. **IPS** (dividing reward by outcome probability via group frequency) breaks down when the outcome space is large relative to the rollout group. **MIPS (Marginal IPS)** computes the outcome probability as a **sum over all trajectories leading to it** by combining the sampled trajectory with a **learned model of trajectories** per outcome. On Hypergrids it tracks the reward-distribution target as outcomes grow while frequency-IPS degrades; sustains diversity on molecular synthesis and phylogenetic inference where GRPO/IPS collapse.
- **Why it matters**: A principled fix for RL **diversity/mode collapse** — relevant beyond LLM RLVR to any group-based policy gradient (GRPO).

### Diagnosing and Correcting Reward Hacking in Verifiable Instruction Following
- **Authors**: Sangyeon Yoon, Wooseok Seo, Hamish Ivison, Hyesoo Hong, Donghoon Kim, Wonjun Kang, Albert No, Jaehyung Kim · arXiv: [2610.19525](https://arxiv.org/abs/2610.19525) — cs.LG, cs.CL · v1 **Wed 14 Oct 2026**
- **Key contribution**: Shows verifiable-IF benchmarks can award **full credit to responses with little substantive content**, and that using the same verifier-based criterion as an RLVR training reward **induces reward hacking** (public checkpoints gain constraint satisfaction but lose response quality). **CALIF** augments the verifier reward with a **calibrated likelihood-based bonus** — response likelihood under the *request alone*, using the **existing frozen reference policy**, no extra judge/reward model. Improves IFBench constraint satisfaction while keeping quality near/above pre-RL across 1.7B–8B models; beats base policies in **40/45** comparisons on three rubric benchmarks.
- **Why it matters**: A concrete, judge-free fix for RLVR reward hacking — directly relevant to the wiki's RLVR/verifiable-reward line.

### Training Language Models to Fail Gracefully
- **Authors**: Daman Arora, Xuecheng Liu, Himanshu Gaurav Singh, Fahim Tajwar, Abitha Thankaraj, Ruslan Salakhutdinov, Haiwen Feng, Yuda Song, Andrea Zanette (CMU — *inferred*)
- **arXiv**: [2610.20401](https://arxiv.org/abs/2610.20401) — cs.LG · v1 **Wed 14 Oct 2026**
- **Key contribution**: When success is the only reward, "guessing" always beats a safe fallback — dangerous when a wrong action corrupts a DB or ships broken code. Proposes training models to **fail gracefully**: preserve success where possible while learning a **safe fallback** when acting would be unreliable. **GracefulRL** reshapes the optimization landscape to make this emerge **from outcome-level reward alone** (no fallback annotations, no inference-time verifier).
- **Why it matters**: Reframes RL objective design around **capability-aware abstention** — the safety counterpart to the wiki's RL post-training cluster.

### Model What Matters: Decision-Guided Selective World Modeling for Language Agents
- **Authors**: Maolin Ran, Minda Chen, Di Huang, Wei Xiong, Fei Huang, Weiwen Liu · arXiv: [2610.19642](https://arxiv.org/abs/2610.19642) — cs.AI, cs.CL, cs.LG · v1 **Wed 14 Oct 2026**
- **Key contribution**: Policy–world-model co-training typically treats **all** observations as world-modeling targets. **DGS-WM** adds a **Decision-Guided Observation Selection** (filter observation units by their support for subsequent policy responses) and **Confidence-Adaptive Weighting** (scale supervision by prediction confidence), forming a decision-aware auxiliary world-modeling loss optimized jointly with the RL loss. Consistent gains across model scales and RL algorithms on single/multi-hop QA and interactive web tasks.
- **Why it matters**: Tightens the policy↔world-model loop for language agents — the "model what matters" efficiency angle on the wiki's world-model entries.

---

## ④ Architectures, Scaling & Efficiency (4)

### LatentLoop: Scaling Looped MoE Models with Asymmetric Compute Allocation
- **Authors**: Zefeng He, Yunkai Chai, Xiaoyang Chen, Tong Zhu, Zongliang Wu, Yun Luo, Yafu Li, Yu Cheng · arXiv: [2610.19975](https://arxiv.org/abs/2610.19975) — cs.LG · v1 **Wed 14 Oct 2026**
- **Key contribution**: Finds loop visits play **asymmetric roles** (first visit uses smaller residual scale). **LatentLoop** compresses the **first visit's sequence**, keeps **full resolution in the second**, and reallocates saved compute to a **larger hidden size**; shares MoE weights across visits but uses **separate attention params** per resolution, and learns how strongly the first visit updates the full sequence. Across **15 configs (1.3B–7B, up to >10²¹ FLOPs)** it lowers validation NLL, with predicted compute savings **19.0%** vs vanilla MoE / **7.9%** vs looped baseline, and better 0-/5-shot averages on 9 benchmarks.
- **Why it matters**: The LLM-side twin of §①'s CDS (parameter-free looping) — evidence that **asymmetric** compute allocation beats uniform looping.

### Continuum Attention
- **Authors**: Afshin Khadangi · arXiv: [2610.20586](https://arxiv.org/abs/2610.20586) — cs.LG, cs.AI · v1 **Wed 14 Oct 2026**
- **Key contribution**: Replaces discrete key/value lookup with **integration over a continuous, piecewise-linear memory curve** — each query induces an exponential relevance density, and exact normalized attention falls out of **closed-form exponential moments** (incl. half-token boundary terms). Gradients follow analytically from moments of order ≤2, enabling parallel GPU kernels while keeping quadratic complexity and the standard decoder. Beats softmax/focal attention by **0.0200 / 0.0480 nats/byte** on mean validation NLL, winning all paired comparisons.
- **Why it matters**: A genuinely different attention formulation for the wiki's architecture line — continuous-integration attention with an analytic gradient.

### Asymptotic Behavior of Transformers
- **Authors**: Katy Blumer, Da-Cheng Juan, Jon Kleinberg, Ravi Kumar, Cyrus Rashtchian, Andrew Tomkins (Google — *inferred*) · arXiv: [2610.19358](https://arxiv.org/abs/2610.19358) — cs.LG, cs.AI, math.ST · v1 **Wed 14 Oct 2026**
- **Key contribution**: Studies long-run text generation. Shows even a **three-token, single-layer attention-only transformer can fail to converge**. For a rich class (arbitrary finite depth, LayerNorm, MLPs, RoPE, arbitrary local/global mix), proves a **softmax-temperature threshold** above which the empirical cache distribution converges to a unique limit independent of init — but the **supremum of these thresholds is infinite**, so **no global minimal temperature** guarantees convergence for all transformers.
- **Why it matters**: Theory for the wiki's inference-degeneracy/repetition-compounding threads — quantifies *why* generation can fail to settle.

### The Cost of Context: Profiling the Energy Footprint of Input Tokens in Large Language Models
- **Authors**: Boris Ruf, Marcin Detyniecki · arXiv: [2610.19819](https://arxiv.org/abs/2610.19819) — cs.DC · v1 **Wed 14 Oct 2026**
- **Key contribution**: Profiles the **energy** cost of the **prefill** phase (long-context/RAG), resolving the tension between hardware power spikes and sub-linear system-level per-token cost. Identifies the threshold where **O(n²) attention overcomes GPU parallelization**; **PagedAttention** delays this bottleneck across **three orders of magnitude** of context, giving up to an **8.9× energy-efficiency advantage at 112k tokens**. Characterizes the **input:output token energy ratio** and how vLLM serving narrows it (~850×→750×) while unoptimized baselines stay ~150–230×.
- **Why it matters**: Empirical **context-scaling energy laws** differentiating engine-level gains from inherent model cost — the sustainability angle missing from most efficiency papers.

---

## ⑤ Interpretability, Memory & World Models (5)

### Sparse Autoencoders for Mechanistic Interpretability in NLP: A Critical Survey
- **Authors**: Salima Lamsiyah, Adelaide Danilov, Oleksandr Marchenko Breneur, Aria Nourbakhsh · arXiv: [2610.20139](https://arxiv.org/abs/2610.20139) — cs.CL · v1 **Wed 14 Oct 2026**
- **Key contribution**: A **critical survey of 138 SAE studies**, proposing (1) a task-grounded **taxonomy** connecting dictionary design, feature operations, and NLP functions; (2) an analysis of how **sparsity allocation, geometry, data coverage, and inference** affect recoverability; (3) an assessment of evidence for semantic **interpretability, mechanistic faithfulness, and behavioral utility**; (4) synthesis across multilingual/retrieval/reasoning/classification/behavioral regulation. Reconciles apparent disagreements and names unresolved questions. Ships an **anonymous research register**.
- **Why it matters**: A field-level audit of the SAE interpretability program — the wiki's interpretability entries can now cite a consolidated evidence map.

### WorldMemBench: A Comprehensive Benchmark for Memory of Video World Models
- **Authors**: Nan Zhou, Jianxiong Gao, Qiuyu Wang, Wen Wang, Jiahao Wang, Yufeng Yuan, … Jun Xiao, Yueting Zhuang, Yongliang Shen (Zhejiang + Ant — *inferred*)
- **arXiv**: [2610.19063](https://arxiv.org/abs/2610.19063) — cs.CV · v1 **Tue 13 Oct 2026**
- **Key contribution**: A **260-case benchmark** for **world memory** in video world models, splitting **static memory** (human identity/appearance, object appearance/geometry, environment) and **dynamic memory** (event progression, state persistence) via controlled camera departures + multi-revisit trajectories. Key finding: **strong static retention does not imply reliable dynamic state evolution**, and repeated revisits reveal **degradation beyond the first return**; human studies validate the automatic metrics.
- **Why it matters**: Fills the "memory" axis of world-model evaluation (alongside fidelity/duration) — pairs with the wiki's video-world-model entries.

### Dynamic Graph World Modelling: Learning Future Dynamics from Temporal Context
- **Authors**: Bo Li, Yue Yang, Yujin Huang, Siao Liu, David Lemphers, … Can Wang, Xin Zheng · arXiv: [2610.19364](https://arxiv.org/abs/2610.19364) — cs.LG · v1 **Wed 14 Oct 2026**
- **Key contribution**: **DyG-WM** jointly predicts future **node and relation** representations from temporal context (not raw graph reconstruction), answering *what evolved / how / what next*: a historical node–relation context encoder (neighborhood trajectories + pair histories), a **path-signature encoder** for ordered structural change, and a **dual-level joint-embedding** objective. Effective across 12 link-prediction + 2 node-classification datasets.
- **Why it matters**: Graph-structured world modeling — a less-common substrate in the wiki's mostly-text/video world-model line.

### Enhancing Latent World Models with Associative Memory
- **Authors**: Yuwei Sun, Siyu Zhu · arXiv: [2610.19683](https://arxiv.org/abs/2610.19683) — cs.LG, cs.CV · v1 **Wed 14 Oct 2026**
- **Key contribution**: Augments **JEPA-style** latent prediction with a **content-addressable memory bank**, learning multi-scale high-level representations in a shared latent space and conditioning predictions via adaptive LayerNorm. Two complementary losses (slot diversity + balanced temporal utilization) prevent representational collapse. SOTA on PushT/Tworoom/Reacher/OGBCube with a lightweight architecture, especially on **long-horizon** planning.
- **Why it matters**: Memory as the fix for JEPA's collapse/long-horizon weakness — directly useful to the wiki's latent world-model threads.

### To Reason but Not to Stop: Understanding and Recovering Pruned Large Reasoning Models
- **Authors**: Minh-Anh Nguyen, Nguyen T. Ha Lan, Xiyan Fu, Dung D. Le, Wei Lu · arXiv: [2610.19934](https://arxiv.org/abs/2610.19934) — cs.CL · v1 **Wed 14 Oct 2026**
- **Key contribution**: Shows pruning hurts LRMs mostly through **failure to stop, not failure to reason**: as sparsity rises, pruned models keep looping (often *after* the correct answer appeared) even though they still know where the dense model would stop. The terminating-vs-looping **hidden-state difference is a consistent direction** across pruned checkpoints; **TGAS (Termination-Guided Activation Steering)** adds that direction to the residual stream **training-free**. Improves termination + accuracy across 6 LRMs / 3 pruning pipelines / math + code, while shortening generations.
- **Why it matters**: An *interpretability → intervention* result (activation steering) with an immediately usable training-free fix.

---

## Also worth recording (cross-cutting)
- `2610.19966` *Choosing the Number of Attention Heads from Intrinsic Dimension* (small-scale study tying head count to activation intrinsic dimension).
- `2610.19820` *ActionOPD: Distilling Decisions, Not Tokens* (distill the decision, not the token stream).
- `2610.20431`/`2610.20294` already featured — the RSI pair.
- `2610.19264` *Beyond Maliciousness: Static and Runtime Attack-Surface Profiling of Agent Skills* (agent-skills security).
- `2610.19498` *What You Sign Is Not What You Run: The Verifiability Gap in Quantized LLM Supply Chains* (supply-chain integrity for quantized weights).
- `2610.19068` *Plan or Retrieve First? A Scale Study of Tool Discovery Architectures* (tool-discovery design space).
- `2610.17718` *ECG-RSI* (RSI applied to ECG waveform evolution — a domain RSI witness).
- `2610.19343` *Counterfactual Gate-Support Decomposition* (separating selection vs redistribution in training-data attribution).
- `2610.19015` *Scaling Cheap Synthetic Pretraining Improves Indoor Radio-Map Prediction* (synthetic-pretraining scaling in a non-NLP domain).

## Cross-cutting observations
1. **CTR-prediction architecture remains absent** — this is now a multi-week pattern across the October series. Ads/rec work has migrated to (a) **agent-facing ads & ad-attack surfaces**, (b) **supply-chain transparency/auditing**, and (c) **generative retrieval/ranking**, rather than classic pCTR scaling.
2. **Parameter-free / weight-tied scaling is converging across modalities**: §① CDS (loop a shared feature-interaction block in an industrial ranker) and §④ LatentLoop (asymmetric looped MoE) independently argue that **reuse + extra iterations** is a real scaling axis.
3. **On-policy distillation got both theory and anatomy this window** (FUW's closed-form utility; the token-flip diagnosis), plus a judge-free reward-hacking fix for RLVR (CALIF).
4. **Memory is the connective tissue**: agent memory (event aggregation), video/world memory (WorldMemBench), latent world-model memory (associative bank), and RL diversity (mode-collapse) all appear — "memory" as capability, benchmark, and mechanism.
5. **Recursive self-improvement** shows two distinct flavors (bounded, auditable successor admission in MMLA-RSI vs swarm-level recombination in SwarmRSI) — worth watching as a recurring cluster.

## Methodology & caveats
- **Export API unavailable**: `export.arxiv.org/api/query` returned `HTTP 429` throughout; this report was built from `arxiv.org` **listing pages** (harvest) + per-paper **`abs` pages** (abstracts). Listing pages do not carry abstracts; abs pages were read individually.
- **Announcement day ≠ submission day**: every entry lists its **v1 submission date**; a few entries are late cross-lists announced Oct-14/15 with older v1 dates (explicitly noted, e.g. LACRM v1 Aug-26).
- **Dedup**: all featured IDs grep-verified **0-hit** against the live `wiki/` tree (9,081-ID baseline); collision-managed against same-day siblings.
- **Affiliations** marked *(inferred)* are from company/team names in titles/author blocks, not a metadata field.
