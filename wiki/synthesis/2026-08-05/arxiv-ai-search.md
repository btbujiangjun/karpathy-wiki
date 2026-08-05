---
title: "arXiv AI Research Scan — August 5, 2026"
type: synthesis
created: 2026-08-05
updated: 2026-08-05
tags: [arxiv, survey, llm, agents, reasoning, alignment, recommendation, search, advertising, ctr, sequential-modeling, retrieval, rag, games, simulation, benchmark, reinforcement-learning]
---

# arXiv AI Research Scan — August 5, 2026

Curated papers from the Wed Aug 5, 2026 arXiv listing (Tue Aug 4 submissions, IDs 2608.02604–2608.04008) spanning recommendation/search/advertising, retrieval & RAG, LLM agents & reasoning, and games/simulation/benchmarks. All papers verified against the arXiv Wed Aug 5 listing. Complements the [Aug 5 daily digest](./arxiv-daily.md) — **no overlap** with the papers covered there (SITA, ATLAS, SmartGR, OMEGA, RTB dispatch, STEPS, Position Bias, Between-User Collapse, LIME-Rec, SFT-conflicts, ReflectRL, TurnSight, Soft Guidance, Logic Before Language, FM game theory, WorldCup Arena, ALiBi, GDPevo, ContinualSkillBench, Field-Aware Skill Retrieval, Inter-Seed Cross-Play, RubricRanker, SIEVE, Hierarchical BM25) or with the [Aug 4 scan](../2026-08-04/arxiv-ai-search.md) / [Aug 4 paper check](../2026-08-04/arxiv-paper-check.md). This scan draws on the cs.IR replacement stream (Kuaishou/WWW, industry rec architecture), cs.CL new submissions (WeChat Pay, long-context), and cs.AI/cs.MA/cs.LG cross-listed papers.

---

## Recommendation, Search & Advertising

### 1. Knowledge-Geometry Decoupling: Refreshable Pretrained Transfer for Streaming Recommendation (KGD)
- **Authors**: Zixuan Wang, Yuhong Chen, Yuxuan Zhu, Guidong Lei, Zhiluohan Guo, Yu Zhao, Kun Wang, Bangyang Hong, Kangle Wu, Yabo Ni, Anxiang Zeng, Cong Fu, Hui Li
- **Institution**: Shopee (tentative, based on affiliations and deployment disclosure)
- **Abstract**: Industrial recommenders increasingly adopt pretrain-then-transfer, but behavioral distribution drift raises two questions: *what* to learn from behavior sequences and *how* to transfer the learned knowledge while the pretrained model is continually refreshed. KGD answers both via knowledge-geometry decoupling: (1) Behavioral Multi-Token Prediction (BMTP) retains only collaboratively or semantically related future items as supervision instead of plain next-token prediction, yielding cleaner, more transferable behavioral knowledge; (2) a refreshable encoder owns behavioral knowledge while a task learner reads encoder states through read-only cross-attention and writes task-specific geometry via Anchored Calibration Residual (ACR) orthogonal to the pretrained embedding — so continual refresh never interferes with downstream adaptation. Improves pretrain-transfer baselines by 4–12% on eight public benchmarks, sustains gains over a 90-day production stream where baselines stall, and is fully deployed at Shopee: live A/B on Homepage Search lifts GMV per user +1.75% and advertising revenue +1.53%.
- **Key Innovations**: Decoupled *ownership* of pretrained behavioral knowledge vs task-specific geometry (orthogonal residual + read-only cross-attention), making continual model refresh safe; BMTP filters spurious adjacency-based transitions. Directly relevant to the streaming-recommendation track.
- **Link**: https://arxiv.org/abs/2608.02738

### 2. Bumblebee: Interleaved Mixed-Layer Building Blocks for Large-Scale Recommendation Systems
- **Authors**: David Bauer, Cancan Zhang, Wenshun Liu, Xiaoyi Zhang, Weijia Liu, Wanli Ma, Yue Weng, Wei Li, Rui Li, Jing Qian, Huayu Li, Xiaoyi Liu, Linhong Zhu, Jerry Fu
- **Institution**: N/A (tentative; industry co-authors)
- **Abstract**: Recommendation architectures evolved along two separate tracks — sequence-modeling approaches and feature-interaction methods — that rarely talk to each other. Bumblebee is an interleaved, stackable block design: each block implements a micro-pipeline combining sequence personalization, attention-based encoding, and feature crossing into a self-contained unit that produces a joint representation of both modalities consumed by the next block. Residual connections between blocks create cross-modal pathways that add predictive performance without extra parameters; blocks can be specialized by selectively dropping components for quality/throughput trade-offs. Evaluated on large-scale industrial data, it consistently beats comparable baselines, and ablations confirm the interleaved composition itself — not depth — drives the gains.
- **Key Innovations**: Interleaving heterogeneous functional units (sequence + feature-interaction) instead of composing deep stacks — a candidate architectural recipe that unifies the two rec-modeling paradigms.
- **Link**: https://arxiv.org/abs/2607.24804

### 3. DualGR: Generative Retrieval with Long and Short-Term Interests Modeling
- **Authors**: Zhongchao Yi, Kai Feng, Xiaojian Ma, Yalong Wang, Yongqi Liu, Han Li, Zhengyang Zhou, Yang Wang
- **Institution**: Kuaishou (tentative, based on deployment disclosure)
- **Abstract**: Deploying Generative Retrieval (GR) in short-video feeds faces long-short interest interference, context-induced noise in hierarchical SID generation, and the lack of explicit learning from exposed-but-unclicked feedback. DualGR combines (i) a Dual-Branch Long/Short-Term Router (DBR) with selective activation, (ii) Search-based SID Decoding (S2D) that constrains fine-level decoding within the current coarse bucket for efficiency and noise control, and (iii) an Exposure-aware Next-Token Prediction Loss (ENTP-Loss) that treats unclicked exposures as coarse-level hard negatives to promote timely interest fade-out. On Kuaishou's large-scale short-video system, online A/B shows +0.527% video views and +0.432% watch time. Best Short Paper at WWW 2026.
- **Key Innovations**: Explicit exposure-as-negative training for GR + interest-routing to separate long/short-term preferences; complements the GR serving work in the [daily digest](./arxiv-daily.md) (SITA/ATLAS/SmartGR/OMEGA) from the interest-modeling and loss side.
- **Link**: https://arxiv.org/abs/2511.12518

### 4. LLM-Derived Priors for Thompson Sampling in Cold-Start Comment Recommendation
- **Authors**: Eugene Lee, Oseong Choi, Byungsoo Kang, Taeyeong Jang
- **Institution**: N/A (tentative; industry co-authors)
- **Abstract**: Thompson-sampling bandits adapt from online feedback but suffer cold-start when new arms have little interaction history. When candidate arms are user-generated textual comments, semantic content can reveal appeal before feedback accumulates. This work uses LLMs to extract semantic signals from comment text and convert them into Bayesian priors that warm-start Thompson sampling, maintaining separate segment-level posteriors per gender–age segment. A real-world online A/B/C test compares a uniform prior against a Gender Prior (demographic-affinity cues) and a Content Prior (title-specific identity cues): LLM priors help most in sparse-feedback regimes, gains emerge once a little interaction evidence accumulates, and prior design drives distinct funnel-level effects with strong demographic heterogeneity.
- **Key Innovations**: LLM-as-prior for bandit cold-start in text-rich recommendation — a cheap warm-start mechanism validated online rather than in simulation.
- **Link**: https://arxiv.org/abs/2608.03382

### 5. CILER: Conditionally Identifiable Latent-Environment Modeling for Out-of-Distribution Recommendation
- **Authors**: Qianqian Wang, Wenwu Gong, Yunshan Li, Zhenqing Wu, Ruili Wang, Lili Yang
- **Institution**: N/A (tentative, based on author affiliations)
- **Abstract**: OOD recommendation is vulnerable to preference shifts induced by a latent environment, but the statistical meaning of the latent environment and its effect on preference are underdetermined in existing methods. CILER formulates the task as conditionally identifiable risk-aware recommendation (CI-RR): it models the latent environment with a user-conditioned exponential family, specifies how it changes preference with a feature-indexed polynomial, and predicts by marginalizing item probabilities over the inferred environment distribution. Under sufficient variation, correct specification, and decoder regularity, CILER identifies the environment-sensitive representation up to a stated equivalence class and bounds excess deployment log-risk by environment-inference error. Improves all twelve OOD ranking metrics across feature, temporal, and geographical shifts on three datasets.
- **Key Innovations**: Identifiability guarantees (not just heuristics) for latent-environment OOD recommenders, with a deployable risk bound tied to environment-inference quality.
- **Link**: https://arxiv.org/abs/2608.03647

### 6. SeqLLM: Augmenting LLMs with Behavioral-Sequence Modeling for High-Stakes Decisions at WeChat Pay
- **Authors**: Guilin Li, Jiaxing Zhang, Matthias Hwai Yong Tan, Bo Wang, Weiran Huang
- **Institution**: WeChat Pay / Tencent (tentative, based on deployment disclosure)
- **Abstract**: Merchant risk control at large payment platforms screens tens of millions of merchants daily — false positives harm legitimate merchants, false negatives leave harmful activity undetected, and the hardest cases need both textual profile and long behavioral sequence. SeqLLM adds behavioral-sequence modeling to a pretrained LLM while preserving language ability, via three components: a compact discrete vocabulary representing behavioral events as native tokens; a lightweight projector trained with a two-stage alignment curriculum grounding tokens in the LLM's semantic space; and prefix-guided capability injection acquiring sequence-modeling via task-prefixed SFT rather than continual pre-training. Deployed at WeChat Pay: screening precision rises 92.0% → 97.5% against the production DeepSeek baseline; behavior-token embeddings improve Precision@Top-0.01% by 26.8 pp in a billion-scale production fraud detector; and on MovieLens/Amazon it beats the User-LLM baseline by up to 32% relative Recall@5 while retaining stronger language ability, plus Pass@32 +14.2% over OneRec-8B at one-fifth the GPU-days.
- **Key Innovations**: Tokenizing *behavioral events* into the LLM's native vocabulary + alignment-curriculum projector — a template for LLM + sequence hybrid models directly relevant to CTR/sequential modeling and fraud-style high-stakes scoring.
- **Link**: https://arxiv.org/abs/2608.03063

---

## Retrieval & RAG

### 7. RAG-Stack: Co-Optimizing RAG Serving Performance and Quality
- **Authors**: Haiqiang Zhang, Yuanqing Lei, Wanting Li, Tao Zhang, Wenqi Jiang
- **Institution**: N/A (tentative, based on author affiliations)
- **Abstract**: Modern RAG systems expose many configuration choices (retrieval indexes, model selections, how models invoke retrieval), each yielding a different quality/serving-performance trade-off. RAG-Stack is a framework for efficiently discovering quality–performance Pareto frontiers: RAG-PE (iterative design-space exploration selecting the next configuration to evaluate), RAG-IR (a workload abstraction for diverse RAG algorithms), and RAG-CM (a performance model predicting optimal deployment on given hardware). This lets users search the joint algorithm–system space without deploying every candidate and transfer an existing Pareto frontier to a new serving system. Given the same optimization budget, frontiers found by RAG-Stack cover 52.5–153.2% more of the normalized quality–performance space than state-of-the-art configuration-search baselines.
- **Key Innovations**: Treating RAG as a joint algorithm–system design space with a predictive serving model — bridges retrieval research and systems engineering.
- **Link**: https://arxiv.org/abs/2608.03487

### 8. Diagnosing and Mitigating Context Rot in Long-horizon Search
- **Authors**: Shijie Xia, Yikun Wang, Zhen Huang, Pengfei Liu
- **Institution**: N/A (tentative; Pengfei Liu affiliated with SJTU/GAIR lineage)
- **Abstract**: A systematic study of four flagship models across three benchmarks identifies a previously overlooked failure mode of extensive-context search: *premature termination* — models give up or give uncertain incorrect answers long before exhausting the context window. Controlling for query difficulty, premature-termination rate is positively correlated with context length. Re-examining mitigations, the authors show seven context-management methods across three categories are inherently test-time-scaling strategies that reduce premature termination to enable more exploration, and provide model-dependent principles for method selection. For parallel sampling, a behavior-aware filtering strategy gains 2.6–4.9% across three aggregation methods.
- **Key Innovations**: Naming and quantifying "premature termination" as the mechanism behind context rot, and reframing context management as test-time scaling — actionable for agentic search design.
- **Link**: https://arxiv.org/abs/2606.29718

### 9. MarginMerge: Coverage-Aware Compression for Multi-Vector Visual Document Retrievers
- **Authors**: Ailar Mahdizadeh, Aria Salari, Sohail Rajabi, Shahriar Mirabbasi, Panos Nasiopoulos, Alireza Morsali
- **Institution**: UBC (tentative, based on author affiliations)
- **Abstract**: Multi-vector visual retrievers (ColPali, ColQwen) get strong retrieval from fine-grained patch embeddings but pay with large indexes and costly late-interaction scoring. MarginMerge argues effective compression should preserve query-relevant *coverage* — the diverse document regions that could become the strongest MaxSim match — rather than selecting patches independently by salience. It selects coverage-aware anchors, clusters document patches, and synthesizes one representative per cluster with a lightweight shared network, at index time, keeping the standard MaxSim interface at retrieval. Across six datasets on ColQwen2.5 and ColPali it preserves 97–99% of average nDCG@5 while cutting stored vectors 90–95%, and at 5% retention cuts ranking flips vs geometric merging by ~41% on average, transferring to unseen datasets without retraining.
- **Key Innovations**: First principled argument (coverage, not salience) for compressing multi-vector visual retrieval — a cheap 10–20× index reduction with near-lossless ranking.
- **Link**: https://arxiv.org/abs/2608.02969

### 10. SciRet: A Compute-Aware Empirical Study of Retrieval and Reranking for Scientific RAG
- **Authors**: Kaysarul Anas Apurba, Md. Hasibul Hasan, Rofiqul Alam Shehab, Asad Azad
- **Institution**: N/A (tentative, based on author affiliations)
- **Abstract**: Rather than proposing a new model, SciRet evaluates a fixed scientific RAG pipeline over CORD-19 across three corpus scales (1K/5K/15K papers): sentence-window chunking, BM25, BGE-M3 dense retrieval, reciprocal rank fusion, optional cross-encoder reranking, and grounded answer generation. Hybrid retrieval is more robust than either sparse-only or dense-only (Recall@10 = 1.000 at 1K and 15K), while an MS MARCO-trained cross-encoder *reduces* precision on the scientific corpus — domain mismatch outweighing stronger query–passage interaction. Generation faithfulness (RAGAS) increases with corpus scale. Labels are pseudo-relevance from the hybrid system, so results are framed as controlled comparative evidence, not a benchmark claim.
- **Key Innovations**: A cautionary compute-aware result: domain-mismatched cross-encoders can hurt scientific RAG; released code/indexes/eval outputs for replication.
- **Link**: https://arxiv.org/abs/2608.03860

---

## Large Language Models, Agents & Reasoning

### 11. OM-GRPO: Outcome-Masked Group Relative Policy Optimization for Label-Free RLVR
- **Authors**: Yongshi Ye, Liang Zhang, Yidong Chen, Xiaodong Shi, Biao Fu
- **Institution**: Xiamen University (tentative, based on author affiliations)
- **Abstract**: RL with Verifiable Rewards (RLVR) usually needs ground-truth answers; voting-based label-free RLVR replaces gold supervision with answer-level consensus from model samples, but collapses because the same answer-level signal is used both to estimate rewards and to drive token-level optimization — reinforcing answer tokens rather than improving reasoning. OM-GRPO decouples the two: it masks gradients on the answer span while retaining answer-level rewards through a soft consensus signal, plus a Contrast-Augmented Reward that refines reward estimation via low-cost pairwise comparisons over existing trajectories with no extra rollouts. It consistently beats label-free baselines across reasoning benchmarks and three backbones, matches supervised GT-reward training, and in the Test-Time Training setting surpasses majority voting by 4.24 points.
- **Key Innovations**: Gradient-masked answer spans prevent the "reward hacking" of label-free RLVR — an optimization-stability fix with direct TTT payoff.
- **Link**: https://arxiv.org/abs/2608.03119

### 12. LoCA: Forward-Only LLM Tuning after One-Shot Calibration with Local Credit Assignment
- **Authors**: Linhan Xia, Rui Liu, Zhaofeng Zhang, Yihao Wang, Binrui Shen, Shengxin Zhu
- **Institution**: N/A (tentative, based on author affiliations)
- **Abstract**: Parameter-efficient post-training still needs repeated end-to-end backprop through the frozen backbone, requiring backward-capable hardware and stored/recomputed activations. LoCA replaces the repeated backward chain with a one-time calibration: a single probe backward pass fits a low-rank map at each transformer block from final prediction error to a local hidden-state correction; LoCA then reuses these maps to form blockwise regression targets from forward activations and fits low-rank adapters with closed-form ridge solves — no further backbone backward pass. Across five benchmarks and Qwen2.5 0.5B–14B, LoCA beats the corresponding LoRA run on 16 of 25 task–scale comparisons, with 26–29% lower GPU peak (incl. calibration), 36–52% lower CPU steady-state memory, and 43–48% lower per-pass time.
- **Key Innovations**: Amortizing global credit assignment into one calibration pass, enabling forward-only tuning — a route to PEFT on backprop-less hardware.
- **Link**: https://arxiv.org/abs/2608.03020

### 13. PI-Mem: Pushing Long-Context Reasoning to 3.6M Tokens with Parallel-Iterative Memory
- **Authors**: Dawei Liu, Haixu Song, Shuang Cheng, Shijie Wang, Haozheng Hou, Kaifeng Liu, Ermo Hua, Zhonghang Yuan, Zhijie Zhong, Yuchen Fan, Biqing Qi, Bowen Zhou
- **Institution**: N/A (tentative; Bowen Zhou lineage, Tsinghua-affiliated)
- **Abstract**: Recurrent-memory long-context approaches face two inherent challenges: sequential chunk-wise updates let later irrelevant content overwrite early critical evidence, and serial inter-chunk dependencies limit parallelism. PI-Mem processes all chunks in parallel and iteratively refines a shared memory over a bounded number of turns: each turn reads all chunks in parallel conditioned on current memory, selects new/complementary evidence per chunk, and merges it into a compact shared memory; an RL-trained turn-efficiency reward lets the model adaptively exit once evidence suffices. On HotpotQA up to 3.6M tokens, PI-Mem beats a recurrent-memory baseline by +6.25 (Qwen3.5-35B-A3B) and +7.81 (Qwen2.5-7B) absolute points with 6.1× and 2.1× inference speedups, breaking the accuracy–efficiency trade-off in long-context reasoning.
- **Key Innovations**: Parallel chunk reads + iterative memory refinement (vs sequential recurrence), with adaptive exit learned by RL — a scalable long-context architecture.
- **Link**: https://arxiv.org/abs/2608.03048

### 14. HyperAgent: Planning and Acting over Tool-Schema Hypergraphs for Tool-Use LLM Agents
- **Authors**: Zian Zhai, Xingyu Tan, Gaowang Zou, Xiaoyang Wang, Wenjie Zhang
- **Institution**: UNSW (tentative, based on author affiliations)
- **Abstract**: Reliable tool-use planning is limited by implicit reasoning over textual tool descriptions and evolving execution environments. HyperAgent models tool relations at the schema level as a directed Tool–Schema Hypergraph (tools = hyperedges from required input-schema nodes to output-schema nodes). Given a task it extracts a task-relevant tool context graph to guide construction of a schema-aware Task DAG, then during execution dynamically realizes each subtask by building a state-conditioned tool support graph through deficit-oriented expansion — identifying unresolved requirements and retrieving supporting producer tools from the current agent state. On AppWorld, HyperAgent improves task completion while reducing redundant API calls, LLM interactions, and token consumption vs existing agent baselines.
- **Key Innovations**: Graph-structured (schema-level) tool reasoning that plans from dependency deficits — a structural remedy for inefficient tool exploration.
- **Link**: https://arxiv.org/abs/2608.02650

### 15. Speculative Correction: Draft-then-Refine Decoding for Diffusion Language Models
- **Authors**: Brian K Chen, Chong Wu, Kenji Kawaguchi
- **Institution**: MIT (tentative, based on author affiliations)
- **Abstract**: Diffusion LMs (DLMs) revise tokens bidirectionally but are usually forced into left-to-right block generation. This paper studies a plug-and-play pattern: generate a complete draft, then refine the full response with bidirectional diffusion. Flash-Flash (same Flash model drafts and refines) improves GSM8K-384 accuracy 0.848 → 0.899 while running 1.20× faster, and MBPP-384 0.545 → 0.693; Mini-Flash (Mini drafts, Flash refines — "speculative correction") reaches MATH-384 0.294 vs 0.300 for Flash-only while running 2.17× faster. Causal ablations show completed drafts are the useful initialization (refinement from fully masked spans performs poorly) and global refinement adds a clear GSM8K gain.
- **Key Innovations**: Bidirectional refinement as a general decoding primitive for DLMs + a training-free speculative scheme pairing a small drafter with a larger refiner.
- **Link**: https://arxiv.org/abs/2608.02625

---

## Games, Simulation & Benchmarks

### 16. Adversarial Fast-Moving Real-World Domains as Test Beds for Benchmarking AI Scientist Capabilities
- **Authors**: William Bolton, Philip Torr
- **Institution**: University of Oxford (based on author affiliations)
- **Abstract**: Benchmarking AI scientists for novel-idea generation is confounded by synthetic tasks and retrospective targets. This paper tests adversarial, fast-moving real-world domains where expert practitioners independently generate observable outputs: Formula 1 (models ideate 2026 car-design concepts against real pre-season innovations as ground truth) and Magic: The Gathering (models propose decks from a new card pool, evaluated against 19 Pro Tour decklists). Models produce plausible outputs but few align with expert solutions: in F1, GPT-5.2 matched 10 of 40 real innovations across 166 ideas; in MTG, the best deck (Gemini 3 Flash) recovered 5 of 7 new-set cards from the third-place PT deck, and across 108 decks the most-selected cards correlate with the most-adopted PT cards (Spearman ρ = 0.74). The key gap is not idea generation but *filtering, prioritization, and coherent novelty* (ICML 2026 AI for Science workshop).
- **Key Innovations**: Live, leakage-resistant domains (F1/MTG) as AI-scientist benchmarks, yielding a crisp diagnosis: idea breadth exists, selection and coherence do not.
- **Link**: https://arxiv.org/abs/2608.03569

### 17. Improving Sample Efficiency in Multi-Agent RL for Simulated Football Games via Exploration (RND-TiZero)
- **Authors**: Amir Baghi, Jens Sjölund, Joakim Bergdahl, Linus Gisslén, Alessandro Sestini
- **Institution**: Linköping University (Sjölund) / RISE (Gisslén) et al. (tentative, based on author affiliations)
- **Abstract**: Multi-agent RL for team games demands enormous training — TiZero takes 40 days to train high-quality policies in the football environment. This paper adds a random-network-distillation bonus inside the multi-agent TiZero framework to promote exploration, plus architectural changes for computational efficiency. RND improves sample efficiency per training phase by 13.3% vs original TiZero and enhances generalization/adaptability to previously difficult scenarios. Qualitative gameplay evaluation shows higher shooting accuracy and lower variance in gameplay metrics — more stable learned behavior.
- **Key Innovations**: A clean, low-risk exploration fix (RND) with measurable sample-efficiency gains on a flagship multi-agent football benchmark — practical for game-AI production.
- **Link**: https://arxiv.org/abs/2503.13077

### 18. Emergence of Biased Consensus in Multi-Agent LLM Debates
- **Authors**: Maya Okawa
- **Institution**: Stanford University (based on author affiliation)
- **Abstract**: Multi-agent LLM debates achieve strong performance yet their safety/fairness risks are poorly understood — interaction can amplify single-LLM biases. This work identifies the emergence of collective (often biased) norms in multi-agent debates and shows noise (e.g., sampling temperature) is a key driver. Using physics-inspired models of social dynamics, it predicts a phase transition to collective bias when conformity surpasses a critical threshold given initial bias and debate noise; controlled experiments observe a finite-size crossover consistent with an underlying phase transition. Agent heterogeneity suppresses emergence by smoothing the transition. Results generalize to realistic tasks including investment decisions and LLM-as-a-judge evaluation (ICML 2026).
- **Key Innovations**: A phase-transition account of debate bias amplification with practical levers (temperature, heterogeneity) — directly relevant to the wiki's games/MARL and multi-agent safety tracks.
- **Link**: https://arxiv.org/abs/2608.02827

---

## Run Summary
- **Batch**: Wed Aug 5, 2026 arXiv listing (Tue Aug 4 submissions; cs.IR 26 entries incl. cross/replacements, cs.AI 416 total, cs.CL 200 total, cs.MA 26, cs.LG 302). arXiv ran system maintenance Aug 4–5, so some entries landed in the Wed Aug 5 window.
- **Papers in this scan**: 18 curated, all verified against the arXiv Wed Aug 5 listing.
- **No overlap**: excludes the Aug 5 arxiv-daily (SITA/ATLAS/SmartGR/OMEGA, RTB dispatch, STEPS, position bias, LIME-Rec, post-training, ALiBi, agent-evolution benchmarks, retrieval infrastructure) and prior scans; flagships of this batch's GR serving wave were covered there.
- **Themes**: (1) LLM×behavioral-sequence hybrids going to production (SeqLLM at WeChat Pay, KGD's refreshable transfer at Shopee); (2) generative-retrieval interest modeling maturing (DualGR's exposure-as-negative loss); (3) retrieval quality/performance co-optimization as a first-class problem (RAG-Stack, MarginMerge, SciRet); (4) RLVR and long-context optimization-stability fixes (OM-GRPO gradient masking, PI-Mem parallel-iterative memory); (5) debate/social-dynamics theory with phase transitions (biased consensus, pluralistic-ignorance companion work in cs.MA); (6) leakage-resistant AI-scientist and exploration-improved game-AI benchmarks.
