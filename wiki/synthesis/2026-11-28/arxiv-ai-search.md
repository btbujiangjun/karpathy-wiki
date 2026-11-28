---
title: arXiv AI Search Report — 2026-11-28
type: synthesis
created: 2026-11-28
updated: 2026-11-28
sources: [arxiv.org]
tags: [arxiv, search, ai, llm, recommendation, advertising, ctr, sequential-modeling, games]
---

# arXiv AI Search Report — 2026-11-28

**Recent window:** arXiv submissions 2026-11-14 → 2026-11-28 (14 days; run date 2026-11-28). **36 curated papers** across AI/LLMs, Recommendation, Advertising, CTR/Conversion, Sequential Modeling, and Games.

## Method

Queried arXiv Export API (`https://export.arxiv.org/api/query`, `sortBy=submittedDate`, `sortOrder=descending`) over categories `cs.AI`, `cs.CL`, `cs.LG`, `cs.IR`, `cs.GT`, `cs.MA`, `stat.ML` plus keyword sweeps for LLM, recommendation/recommender, CTR/click-through/click prediction, advertising/adtech/ad ranking/auto-bidding/RTB, sequential modeling/sequential recommendation, and games/game AI/game theory, bounded by `submittedDate:[202611140000 TO 202611290000]`. Curated 36 unique papers; deduplicated by arXiv ID. Authors and abstracts are from arXiv metadata. Institution/Company is best-effort from the paper title page/PDF page 1; not all papers list affiliations, and unclear cases are marked 'Not stated'. Key innovations are condensed from abstracts; no full-text review. Benchmark numbers and claims are author-reported. arXiv itself does not guarantee affiliation completeness; verify institution against the PDF for citation-critical use.

Preference file active: `EXTEND.md` (repo root; `bm25.mode: auto_prompt`; BM25 not triggered for external arXiv search).

## AI / LLMs

### Diverse Alternative Reasoning Traces for Hard Math Problems
- **arXiv:** [2611.34928v1](https://arxiv.org/abs/2611.34928v1)
- **Authors:** Lukas Aichberger; Adam Golinski; Arno Blaas; Arwen Bradley; Jacob Springer; Mehrdad Farajtabar; Michael Kirchhof; Sinead Williamson
- **Institution/Company:** Not stated on arXiv/PDF page 1
- **Submitted:** 2026-11-25
- **Category:** cs.CL (all: cs.CL, cs.AI, cs.LG)
- **arXiv comment:** NeurIPS 2026 (Workshops)
- **Abstract:** Post-training large language models (LLMs) for mathematical reasoning often relies on accepted traces whose final answers pass a verifier. For hard math problems, however, such traces can be rare under independent Monte Carlo (MC) sampling. To address this, we propose Diverse Alternative Reasoning Traces (DART), a trace-mining method that starts from a rejected trace, decomposes it into reasoning steps, and ranks them by position-weighted uncertainty. It then generates deliberately distinct alternative candidates for highly ranked steps using reference-answer guidance and a meta-thought before completing the resulting traces. On greedy-unsolved DeepMath-103K problems, DART recovers 37% more problems than MC sampling at a matched number of generated traces. Its estimated generation cost per recovered problem is nearly identical, while its cost per accepted trace is 30% lower. Post-training Llama-3.1-8B-Instruct on traces mined by DART achieves the highest point estimate in five of six evaluations across MATH-500 and AIME benchmarks. These results demonstrate that revisiting rejected traces with DART can expand problem coverage and provide effective post-training data.
- **Key innovations:**
  - DART mines training signal from rejected reasoning traces rather than only accepted/verifier-passing traces.
  - Decomposes rejected traces into steps, ranks them by position-weighted uncertainty, generates deliberately distinct alternatives with reference-answer guidance and meta-thoughts, then completes traces.
  - On greedy-unsolved DeepMath-103K, recovers 37% more problems than independent Monte Carlo sampling at matched trace count; 30% lower cost per accepted trace; post-training Llama-3.1-8B-Instruct achieves best point estimate in 5/6 MATH-500/AIME evaluations.

### DFly2: Turbocharging Long-Context Speculative Decoding by Sharing the Target's Sparsity
- **arXiv:** [2611.34776v1](https://arxiv.org/abs/2611.34776v1)
- **Authors:** Hong Liu; Rui Cen; Junhan Shi; Lin Niu; Runzhi Fan; Zhaojing Zhou; Haodi Lei; Jiebin Zhang; Saiyong Yang; Junqiang Zheng; Zhenghai Xue; Guanghua Yu; Jianchen Zhu
- **Institution/Company:** Tencent Inc.
- **Submitted:** 2026-11-25
- **Category:** cs.CL (all: cs.CL)
- **arXiv comment:** 20 pages, 8 figures
- **Abstract:** To avoid the quadratic cost of dense attention over long contexts, models such as DeepSeek-V4 and Hy4 have turned natively sparse, and speculative decoding, which matters most where decoding is slowest, increasingly runs on them. Their drafters, however, still keep a context cache of their own, over the whole prompt or a sliding window. Beyond memory, such a cache costs prefill time, prefix-cache hits and decode concurrency. Drafters that read the target's cache avoid one of their own, but settle only which cache, not which positions, and still read everything or a recent window. Neither rule is made for the query at hand, and computing a selection per query in the drafter would cost more as the context grows. Yet a natively sparse target already picks positions for each query, over a cache it keeps anyway. Both of the drafter's choices are therefore already made, and paid for, by the target: its cache and its selection. We measure how far one selection carries: made a step early, it still covers close to nine tenths of what each later token selects on DS-V4.1-Flash. We present DFly2, a block-parallel drafter that shares the target's sparsity. Each draft layer reads the KV its paired target layer cached (KV sharing), at the positions that layer's indexer selected, a fixed number anywhere in the context (Index sharing). DFly2 thus runs no scoring pass and keeps no cache of its own. On DS-V4.1-Flash, GLM-5.3-Flash and Hy4~flash, whose sparse attention and architecture differ, it accepts more tokens per step than DFlash and DSpark trained on the same recipe, over general, long-context and agentic benchmarks. Its margin over the stronger baseline widens from 3.9%-10.5% on general workloads to 10.0%-31.5% on long-context and agentic ones. At high concurrency on DS-V4.1-Flash, at matched per-user decode speed, its throughput is 62% and 81% higher on two 64K sets.
- **Key innovations:**
  - DFly2 is a block-parallel speculative-decoding drafter for natively sparse long-context targets.
  - KV sharing reuses the target's cached key/value tensors; Index sharing reuses the target layer's selected positions, so the drafter needs no own cache and no scoring pass.
  - A selection made a step early still covers ~90% of later token selections; accepts more tokens/step than DFlash/DSpark; gains widen on long-context/agentic tasks; ~62%/81% throughput at matched per-user speed on 64K sets.

### TASK Memory: Beyond Text-Only Memory with Activation Steering and Knowledge Editing against Memory Hallucination
- **arXiv:** [2611.34762v1](https://arxiv.org/abs/2611.34762v1)
- **Authors:** Jinkun Zhao; Wenjun Wu
- **Institution/Company:** SKLCCSE, Institute of Artificial Intelligence, Beihang University; Beijing Advanced Innovation Center for Future Blockchain and Privacy Computing, Beihang University
- **Submitted:** 2026-11-25
- **Category:** cs.AI (all: cs.AI)
- **Abstract:** LLM agents increasingly rely on external memory, yet they still hallucinate about what they remember. Often the correct memory is retrieved and placed in the prompt, but the answer contradicts it or the memory is applied to the wrong question. We call these use-time memory hallucinations. Across five open models, we find that they arise from the conflict between parametric knowledge and external memory and take three forms: memory-ignoring, where the model returns to a stale fact in its weights (up to 46% of queries); memory-misapplying, where it attributes the memory to unrelated entities (up to 24%, and 49% when retrieval is combined with weight editing); and version confusion, where 53% of answers about revised facts assert the superseded value when both versions remain stored. We propose TASK memory, which goes beyond text-only memory by combining a Text note with Activation Steering and Knowledge editing that share one in-model address. The text holds the content. A removable knowledge edit supplies the address through its subject key and supports multi-hop composition. A pair of steering vectors decides, query by query, whether the model adopts the memory or keeps its own answer; the vectors store no content and control how the text memory is used. On frozen models under a pre-registered, test-once protocol, TASK reduces memory-ignoring hallucinations to at most 1.5% in all ten model-dataset cells and cuts neighbour misuse from 39.2% to 7.5% (+10.8 pp composite on CounterFact). It improves a 300-memory library over BM25 RAG by 16.4 pp, an advantage that holds at 3,000 memories, resolves fact revisions without fact IDs, and adds 7.5 pp of multi-hop accuracy on MQuAKE. 21 of 23 cross-model comparisons (8B-27B, four families) are significant, and TASK beats three recent context-steering methods in 9 of 10 model-dataset cells.
- **Key innovations:**
  - TASK Memory combines a text note, removable knowledge editing, and activation-steering vectors sharing one in-model address.
  - Text stores content; knowledge edit supplies addressing/subject key and multi-hop composition; steering vectors query-by-query decide whether model adopts memory or keeps its own answer.
  - Reduces memory-ignoring to <=1.5%; neighbor misuse 39.2%→7.5%; +10.8pp CounterFact composite; +16.4pp vs BM25 RAG on 300-memory library; resolves revisions without fact IDs; +7.5pp multi-hop on MQuAKE.

### ZeroHero: Training Small Language Agents from Scratch
- **arXiv:** [2611.34635v1](https://arxiv.org/abs/2611.34635v1)
- **Authors:** Nikita Sorokin; Zoya Volovikova; Alexey Skrynnik; Aleksandr Panov
- **Institution/Company:** Cognitive AI Systems Lab; Moscow Independent Research Institute of Artificial Intelligence
- **Submitted:** 2026-11-25
- **Category:** cs.AI (all: cs.AI)
- **arXiv comment:** 18 pages, 6 figures, 2 tables. Interactive demo: https://zoyav.github.io/-ZoyaV-zerohero-demo
- **Abstract:** Large pretrained language models provide capable policies for interactive tasks, but how much model capacity is necessary for a specialized language agent? We introduce ZeroHero, a framework for training small language agents (SLAs) from scratch. In each environment, a large language model acts as the expert, and we collect its successful trajectories. We pretrain each SLA, which has fewer than 50 million parameters, to predict the expert's responses given the interaction history. We then post-train the agent on its own interactions using proximal policy optimization (PPO). During post-training, reasoning alignment supplements environment rewards with expert supervision on the language the agent generates alongside its actions. We evaluate the agents in three multistep environments where acting requires both understanding and generating language. In Crafter, agents interpret textual observations and generate reasoning before acting. In WebShop, they translate shopping instructions into search queries. In Alfworld-Dialogue, they ask clarifying questions and use the answers to guide household actions. The agents approach expert performance on WebShop and surpass their respective demonstration experts on Crafter training rollouts and held-out Alfworld-Dialogue tasks. An interactive demo is available at https://zoyav.github.io/-ZoyaV-zerohero-demo.
- **Key innovations:**
  - ZeroHero trains small language agents (<50M params) from scratch in each environment, not from a large pretrained LLM.
  - A large LLM expert collects successful trajectories; agent pretrained to imitate expert, then post-trained with PPO on own interactions.
  - Reasoning alignment adds expert supervision on generated language alongside environment reward; approaches expert on WebShop; surpasses demonstration experts on Crafter rollouts and held-out Alfworld-Dialogue.

### AliceAI-Foundation-80B-A3B-Base
- **arXiv:** [2611.34529v1](https://arxiv.org/abs/2611.34529v1)
- **Authors:** Nikolay Skachkov; Ekaterina Redina; Maksim Konoplev; Evgenii Uskov; Veronika Zykova; Ivan Tsarikov; Artemii Zakharov; Mariia Godunova; Dmitrii Lunin; Maria Nikiforova; Valerii Levanov; Anton Kalsin; Daniil Panteleev; Alexey Gerasev; Ilia Kopytin; Yermek Kapushev; Egor Liakhov; Irina Lialikova; Tatiana Taekina; Anastasia Volotova; Assol Kubaeva; Kirill Alekseev; Pavel Otlivanchik; Mukhammadfirdavs Kosimov; Vladislav Negodin; Ivan Vinogradov; Anton Andriushchenko; Maksim Nikitin; Daniil Sukhoi; Alexander Mazitov; Maksim Abraham; Philip Zmushko; Maksim Ignatov; Ivan Sapozhkov; Timofey Byzov; Edgar Shmavonian
- **Institution/Company:** Yandex (Alice AI Team)
- **Submitted:** 2026-11-25
- **Category:** cs.CL (all: cs.CL, cs.LG)
- **Abstract:** We present AliceAI-Foundation-80B-A3B-Base, a mixture-of-experts language model with 80 billion total parameters and approximately 3 billion active parameters per token, trained from scratch at Yandex and released under the Apache 2.0 license. The model combines Kimi Delta Attention with full attention, uses Attention Residuals, and is trained with Muon. Training comprises general pretraining on 17.5 trillion tokens, two context-extension stages, and a dedicated stage for reasoning and agentic interaction. We describe the data collection and augmentation pipelines, evaluation protocols, architectural ablations, and scaling-law experiments. We identify the limitations of held-out training loss as a proxy for downstream performance and introduce an auxiliary loss on mixture-of-experts outputs to stabilize training at the predicted learning rate. Domain-specific data selection and augmentation improve factual knowledge, mathematics, and programming skills, while agent trajectories introduced during pretraining improve performance on agentic benchmarks after supervised fine-tuning. In zero-shot reasoning evaluation, the model achieves leading results among open base models of comparable size, with 88.7% pass@8 on IMO-AnswerBench and 82.9% pass@8 on LiveCodeBench v5-v6. To evaluate Russian-language factual knowledge, we introduce and release two benchmarks with their evaluation protocols: WikiWebFacts, which tests short factual questions drawn from encyclopedic sources and search queries, and HardMultiQA, which tests more demanding factual questions inspired by user interactions. Our model scores 86.5% on WikiWebFacts and 67.9% on HardMultiQA, compared with 83.2% and 65.4% for DeepSeek-V4-Flash-Base (284B total and 13B active parameters) and 72.8% and 54.5% for Nemotron-3-Super-120B-A12B-Base (120B total and 12B active parameters), outperforming both larger models on these benchmarks.
- **Key innovations:**
  - AliceAI-Foundation-80B-A3B-Base: open Apache-2.0 MoE LM, 80B total / ~3B active per token, trained from scratch at Yandex.
  - Combines Kimi Delta Attention with full attention, Attention Residuals, Muon optimizer.
  - 17.5T token general pretraining + two context-extension stages + reasoning/agentic stage; auxiliary MoE-output loss stabilizes training; domain data selection/augmentation; agent trajectories in pretraining; 88.7% pass@8 IMO-AnswerBench, 82.9% pass@8 LiveCodeBench v5-v6; releases WikiWebFacts + HardMultiQA.

### Any-Rate: Half-Bit Multi-Precision LLM Quantization with Coded Bit-Planes
- **arXiv:** [2611.34402v1](https://arxiv.org/abs/2611.34402v1)
- **Authors:** Hoonki Lee; Haechan Shin; Hyuntaek Jung; Yeonu Choi; Sangyeob Kim
- **Institution/Company:** Not stated on arXiv/PDF page 1
- **Submitted:** 2026-11-25
- **Category:** cs.LG (all: cs.LG, cs.AR, cs.CL)
- **arXiv comment:** 41 pages, 17 figures. (Equal contribution : Hoonki Lee and Haechan Shin)
- **Abstract:** Nested multi-precision quantization derives multiple precisions from a single checkpoint by reading only the leading bits of each weight, which makes it attractive for on-device deployment under varying memory and energy budgets. However, existing methods offer only integer bits, leaving large accuracy gaps between adjacent precisions and severe degradation at 2 bits. To address this, we propose Any-Rate, which serves 2-8 bits from one checkpoint, in half-bit steps over 2-4 bits. Any-Rate restricts some bit-planes to extended Hamming codewords in 8-weight blocks (0.5 bits per weight), shares one LUT per row across precisions, and encodes all precisions jointly with a separate target for each, reducing the loss from sharing bit-planes. Across four LLMs, Any-Rate achieves state-of-the-art accuracy among multi-precision methods at 2 and 3 bits, keeping 69% of FP16 accuracy at 2 bits, and is within one point of the best at 4 bits. It decodes about as fast as existing kernels, and an LPDDR energy model estimates up to 27% less energy at equal accuracy. Code is available at https://github.com/hoonki2002/Any-Rate.
- **Key innovations:**
  - Any-Rate nested multi-precision quantization serves 2–8 bits from one checkpoint, half-bit steps over 2–4 bits.
  - Some bit-planes restricted to extended Hamming codewords in 8-weight blocks (0.5 bits/weight); one shared LUT per row; joint encoding with separate target per precision.
  - State-of-the-art accuracy among multi-precision methods at 2 & 3 bits; keeps 69% FP16 accuracy at 2 bits; within 1 point of best at 4 bits; similar decode speed; up to 27% less LPDDR energy at equal accuracy.

### Lightweight Reasoning Transfer via Chain-of-Thought Vector Projection
- **arXiv:** [2611.34183v1](https://arxiv.org/abs/2611.34183v1)
- **Authors:** Yulin Qi; Shuo Xu; Shuxia Lin; Qingjian Ni; Xu Yang; Xin Geng
- **Institution/Company:** School of Computer Science and Engineering, Southeast University
- **Submitted:** 2026-11-25
- **Category:** cs.CL (all: cs.CL)
- **Abstract:** Transferring reasoning capabilities from large language models to smaller ones often requires extensive teacher supervision or costly student adaptation. We study projected cross-model Chain-of-Thought (CoT) Vector transfer, a two-stage approach that keeps both models frozen. First, we learn a task-level CoT Vector in the teacher using dataset-provided solution traces and final-answer supervision. We then train a lightweight linear projector to map the fixed vector into a smaller student's residual space. Student-side training uses only final-answer cross-entropy on a small subset of task training examples; it requires neither teacher outputs nor intermediate solution traces. We select the student injection layer and intervention scale on a labeled support set and report results on the disjoint remainder of each evaluation split. On GSM8K and MATH, the projected vector improves base students by 10.37-21.98 accuracy points across the evaluated teacher-student settings. On four code-generation benchmarks, the Qwen2.5-7B-Instruct student gains 3.23-4.67 pass@1 points, while the base Qwen2.5-7B student gains up to 9.65 points. These results show that a teacher-side reasoning vector can be reused across smaller students with different residual dimensions through projector-only adaptation.
- **Key innovations:**
  - Cross-model Chain-of-Thought Vector transfer keeps both teacher and student frozen.
  - Learn task-level CoT vector in teacher from provided solution traces + final-answer supervision; train lightweight linear projector into student's residual space.
  - Student-side training uses only final-answer cross-entropy on small subset; no teacher outputs or intermediate traces; selects injection layer & intervention scale on labeled support set; +10.37–21.98 accuracy points GSM8K/MATH; +3.23–4.67 pass@1 instruct / +9.65 base Qwen2.5-7B on code.

### Stable Gated DeltaNet-2: Understanding and Mitigating Recurrent State Instability
- **arXiv:** [2611.34051v1](https://arxiv.org/abs/2611.34051v1)
- **Authors:** Xichong Zhang; Xixuan Hao; Zhichen Liu; Le Zhou; Zeyu Zhang; Boyu Chen; Mingfei Lu; Zehao Lin; Bo Tang; Yonggang Zhang; Linyun Liu; Feiyu Xiong; Jianlin Su; Zhiyu Li
- **Institution/Company:** MemTensor; USTC; HKUST(GZ); SUSTech; SJTU; HKUST; kexue.fm
- **Submitted:** 2026-11-25
- **Category:** cs.CL (all: cs.CL, cs.LG)
- **Abstract:** Linear attention offers an efficient solution for long-sequence modeling via linear complexity and fixed-size recurrent states. Gated DeltaNet-2 (GDN-2) introduces independent channel-wise control over erasure and writing, enhancing state-update expressiveness and in-context retrieval, yet it suffers from training failures during long-context training. We trace these failures to the asymmetry between reading and modification directions during erasure, which yields non-normal erase operators whose directional gains accumulate across tokens, triggering exponential state growth even without new writes. To resolve this, we propose \model{}, employing symmetric erasure to ensure non-expansive state propagation and decay-regulated residual writing to preserve writing flexibility. Theoretically, we establish an $O(\sqrt{T})$ upper bound on recurrent state growth while retaining chunkwise parallel computation. Experiments on ~1.6B parameter models show that \model{} achieves stable training alongside improved long-context retrieval. Compared to GDN-2, it boosts the 128K average RULER score by 6.80 points in the recurrent setting and average accuracy across nine downstream tasks by 0.62 points in the hybrid setting.
- **Key innovations:**
  - Stable Gated DeltaNet-2 diagnoses training failure as asymmetry between reading & modification directions during erasure, producing non-normal erase operators and exponential state growth.
  - Symmetric erasure ensures non-expansive state propagation; decay-regulated residual writing preserves writing flexibility.
  - O(√T) recurrent-state-growth bound while retaining chunkwise parallel computation; ~1.6B models stable training + improved long-context retrieval; +6.80 128K RULER recurrent / +0.62 downstream hybrid vs GDN-2.

---

## Recommendation

### Grounding User Preferences in Shared Multimodal Concepts for Recommendation
- **arXiv:** [2611.34436v1](https://arxiv.org/abs/2611.34436v1)
- **Authors:** Ao Xu; Jinhui Huang; Wenqiang Tang; Tiehua Mei; Hongru Hou; Hengrui Chen; Jiaqing Liang; Deqing Yang
- **Institution/Company:** School of Data Science, Fudan University
- **Submitted:** 2026-11-25
- **Category:** cs.IR (all: cs.IR)
- **arXiv comment:** Accepted at WSDM 2027 (Main Conference). 10 pages, 7 figures, 6 tables
- **Abstract:** Multimodal recommendation has substantially advanced item understanding by incorporating rich visual and textual content. Yet user preferences are still commonly encoded as implicit signals tied to individual items, leaving recurring semantic factors without persistent identities that can be shared across items. We introduce MKGE, a multimodal knowledge graph framework that represents these factors as canonical, addressable concepts. MKGE induces a domain-adaptive concept vocabulary from item images and titles, grounds each user's interaction history in supported concepts, and jointly models direct user-item evidence and concept-mediated preference signals. By turning recurring semantics into shared coordinates, MKGE enables evidence from different items to accumulate around the same preference factors. Extensive experiments on three public benchmarks demonstrate that MKGE consistently outperforms collaborative, knowledge-graph, multimodal, and recent LLM/MLLM-based recommenders across all six reported metrics. Controlled studies further demonstrate the importance of canonical concept identities and personalized user-concept correspondence, with especially pronounced gains over removing or rewiring the user graph for low-activity users. These results establish canonical multimodal concepts as effective units for preference modeling and transfer. Code, constructed knowledge graphs, and prompts are available at https://github.com/Garden1a-X/MKGE.
- **Key innovations:**
  - MKGE multimodal knowledge-graph framework uses canonical addressable concepts instead of per-item preference identities.
  - Induces domain-adaptive concept vocabulary from item images/titles; grounds user history in concepts; jointly models direct user-item & concept-mediated signals.
  - Shared coordinates accumulate evidence across items; outperforms collaborative/KG/multimodal/LLM recommenders on 3 benchmarks & 6 metrics; gains especially for low-activity users; releases KGs/prompts.

### Agentic Waterfall: An Intent-Driven Information Discovery Framework for Reclaiming User Control in the Attention Economy
- **arXiv:** [2611.34407v1](https://arxiv.org/abs/2611.34407v1)
- **Authors:** Yige Luo; Shining Zhang; Jikun Liu; Hongjiao Qiang; Ran Guan
- **Institution/Company:** 2012 Laboratories, Huawei
- **Submitted:** 2026-11-25
- **Category:** cs.AI (all: cs.AI, cs.IR)
- **Abstract:** We formalize Agentic Waterfall Feed, a new problem of personalized information discovery in which users actively direct recommendations and the system adapts to evolving needs inferred from both explicit requests and browsing behavior. We address this problem with the Agentic Waterfall framework, whose language-model controller maintains persistent user state and coordinates content retrieval, ranking, and state updates. To evaluate systems on this task, we contribute the Agentic Waterfall Dataset and a replay-based evaluation protocol. The dataset combines real content metadata with simulated interaction histories. The protocol compares systems under shared histories using relevance scores and blind judgments of how well recommendations satisfy current user goals and constraints. Agentic Waterfall remains competitive with strong baselines on conventional recommendation tasks across five public benchmarks. On the Agentic Waterfall Dataset, it outperforms the strongest baseline in both evaluations, with relative improvements of up to 16.1%.
- **Key innovations:**
  - Agentic Waterfall Feed: personalized information discovery where users actively direct recommendations and system adapts to explicit requests + browsing behavior.
  - LLM controller maintains persistent user state; coordinates retrieval, ranking, state updates.
  - Agentic Waterfall Dataset + replay evaluation; real content metadata + simulated histories; relevance & blind goal/constraint satisfaction; competitive on 5 benchmarks; up to +16.1% on new dataset.

### LazUnirec: Unifying Retrieval and Ranking in Multi-scenario Industrial Recommendation
- **arXiv:** [2611.32590v1](https://arxiv.org/abs/2611.32590v1)
- **Authors:** Xiaodong Li; Junfeng Zhang; Shichao Nie; Ziyue Guo; Yiming Liu; Xinxin Xu; Xurong Li; Jinyuan Dang; Zhanming Ou; Jianan Yan; Tao Luo; Xiaoyi Zeng
- **Institution/Company:** Alibaba International Digital Commerce Group
- **Submitted:** 2026-11-24
- **Category:** cs.IR (all: cs.IR)
- **Abstract:** Modern industrial recommendation systems typically divide retrieval and ranking into two separate cascaded stages, leading to inconsistent optimization objectives, redundant encoding of user sequences, and a waste of computational resources. Previous efforts have investigated using Transformers to model both retrieval and ranking simultaneously. However, these studies still face two major limitations: (1) Since retrieval and ranking share a single Transformer backbone, the gradient conflict arises when the gradient directions of the two tasks are inconsistent. (2) When gradient conflict occurs, the model cannot determine a reliable direction for gradient updates. To this end, we propose a Unified Retrieval and Ranking approach for Multi-scenario Industrial Recommendation, termed as LazUnirec. Specifically, we construct task-shared and task-private parameters on the Transformer backbone to mitigate the gradient conflict. Wherein, for the attention components, we propose LoRA-modulated attention, enabling retrieval and ranking to share attention parameters while preserving task-private parameters. For the feed-forward networks (FFN), we present task-adaptive sparse mixture-of-experts (MoE) to mitigate gradient conflict by constructing task-shared and task-private experts. Moreover, we propose an uncertainty estimation that evaluates the gradient reliability of the retrieval and ranking, thereby guiding the model toward a more reliable gradient update direction when gradient conflict occurs. In addition, knowledge distillation from ranking to retrieval further enables cross-task knowledge transfer. Extensive offline experiments and online A/B testing demonstrate the effectiveness and superiority of LazUnirec. LazUnirec has been deployed in online multi-scenario industrial recommendation system and currently delivers significant gains for the platform.
- **Key innovations:**
  - LazUnirec unifies retrieval and ranking in multi-scenario industrial recommendation, resolving gradient conflict.
  - Task-shared + task-private Transformer parameters; LoRA-modulated attention; task-adaptive sparse MoE in FFN.
  - Uncertainty estimation measures gradient reliability; ranking→retrieval knowledge distillation; offline + online A/B gains on industrial platform.

### Needwise: Generation-Free Conversational Recommendation from Need-Level Typed Decisions
- **arXiv:** [2611.31175v1](https://arxiv.org/abs/2611.31175v1)
- **Authors:** Sungchul Kim; Weixiao Huang; Mekala Raja Sekhar Reddy; Amrutha Srinivasan
- **Institution/Company:** Adobe Research; Adobe Inc.
- **Submitted:** 2026-11-23
- **Category:** cs.AI (all: cs.AI)
- **Abstract:** Conversational recommenders must rank items against needs that catalogs record only in part, while users add, withdraw and reverse needs and switch between requests. LLM rankers re-read the dialogue at every turn: they are slow, and their ordering does not show which needs an item meets. We show that a conversational recommender can be built from typed decisions instead: named questions over fixed options, answered with option probabilities rather than generated text. On each turn, one typed request maps the message onto the catalog's fields, keeps what no field expresses in the user's words, and decides how the turn changes each earlier need. Needwise then ranks candidates must-first: the needs on the kind of item, its place and its price form a tier, and within it one holistic decision and need-level verdicts (supported, contradicted or unknown) are combined with equal weight (Needwise-HF). With the graded attributes withheld from the records, so that needs must be inferred from names, descriptions and reviews, Needwise-HF ranks Google Local requests significantly better than GPT-6 Sol (0.383 against 0.343 nDCG@10) and is not significantly different from the strongest LLM ranker on Google Local and Yelp; these comparisons keep their sign under every treatment of unrecorded attributes we test. It costs a fraction of GPT-6 Sol's API price and answers in 2.5 s at the median on Google Local, against 5.6 s for GPT-6 Sol. In conversations, the typed state keeps the ranking across switches and returns, but it recognizes only 19-27% of withdrawn needs.
- **Key innovations:**
  - Generation-free conversational recommender built from typed decisions: named questions, fixed options, option probabilities, not generated text.
  - Each turn maps message to catalog fields, preserves unrecorded needs in user words, updates earlier needs; Needwise-HF ranks must-first tier + holistic + need-level verdicts (supported/contradicted/unknown).
  - nDCG@10 0.383 vs GPT-6 Sol 0.343 on Google Local; matches strongest LLM ranker; ~fraction of API cost; 2.5s median vs 5.6s; note: recognizes only 19–27% of withdrawn needs.

### From Head to Tail: LLM-Augmented Sequential Recommendation and Trade-off Optimization
- **arXiv:** [2611.31052v1](https://arxiv.org/abs/2611.31052v1)
- **Authors:** Adeep Hande; Shaghayegh Agah; Neeraj Sharma; Karina Halevy; Sardar Hamidian
- **Institution/Company:** Applied AI Research, Comcast; Carnegie Mellon University
- **Submitted:** 2026-11-23
- **Category:** cs.IR (all: cs.IR, cs.AI)
- **arXiv comment:** 7 pages, 4 figures, 7 tables. Accepted at GRAIL 2026: Workshop on Generative, Retrieval-augmented, and Agentic Intelligence for Personalization, held at CIKM 2026
- **Abstract:** Recommender systems exhibit popularity bias, often under-serving long-tail and cold-start items with sparse interaction data. We propose a group-specific data augmentation approach that leverages LLMs to generate synthetic interactions, formulated as a constrained optimization problem, maximizing group-specific NDCG@20 and coverage while bounding overall NDCG@20 degradation within an acceptable threshold. Items are partitioned by interaction frequency to find the optimal augmentation strategy for each group. We further study combining the augmentation across groups simultaneously and find that while individual optimal strategies navigate the multi-group augmentation design, they are not simply additive. We further ablate on the LLM-based augmentation itself, comparing LLM scales, augmentation configuration under token constraints, finding that augmentation quality scales with contextual richness, albeit at a proportionally higher cost. Experiments with SASRec demonstrate the effectiveness of the proposed approach, achieving over 100% and 60% improvement in group-specific NDCG@20 for extreme and regular long-tail items, respectively, on our industrial dataset, and 40%, 25% for MovieLens-32M, while increasing their coverage without significant overall degradation.
- **Key innovations:**
  - LLM-augmented sequential recommendation targets popularity bias / long-tail & cold-start items.
  - Group-specific synthetic interaction augmentation by interaction frequency; constrained optimization maximizing group NDCG@20 + coverage while bounding overall NDCG@20 degradation; combine across groups (not simply additive).
  - SASRec: >100% group NDCG@20 extreme long-tail +60% regular long-tail industrial; +40%/+25% MovieLens-32M; coverage up; small overall degradation; augmentation quality scales with context, cost higher.

### Speculative Decoding for Semantic-ID-Based Generative Recommendations
- **arXiv:** [2611.32855v1](https://arxiv.org/abs/2611.32855v1)
- **Authors:** Harshal A. Chaudhari
- **Institution/Company:** Not stated on arXiv/PDF page 1
- **Submitted:** 2026-11-24
- **Category:** cs.IR (all: cs.IR)
- **arXiv comment:** 33 pages, 19 figures (23 pages main text, appendices A-E follow). Preprint
- **Abstract:** Generative recommender systems with Semantic IDs (SIDs) represent each item as a short sequence of $L$ discrete tokens and use a sequence model to predict the next item's tokens from a user's history. Industry-scale deployments typically use these models to retrieve multiple candidates per request with constrained beam search. However, this incurs a fixed cost of $L$ sequential model calls per request, and accuracy degrades as the SID generator becomes less sharp, without a guarantee on how close the output is to the exact top-$K$. Production systems therefore cannot detect degraded retrieval for individual requests. We propose SIDECAR, which uses approximate draft candidates and a tree-attention pass to score the entire draft in a single model call, memory permitting. This pass bounds the probability of every unexplored SID prefix and certifies the exact top-$K$ if the draft contains them. Otherwise, a branch-and-bound fallback expands only the parts of the trie that can still change the output, reaching certification within at most $L$ calls for any draft. Moreover, under a budget of $M$ tokens per call and $Y$ calls, which for $Y = L$ matches the resources of a beam search of width $M$, SIDECAR announces a factor $1 + δ$ within which its list will be exact at every rank. Depending on model sharpness, SIDECAR returns the exact top-$K$ using a fraction of beam search's calls or memory. Even when the budget is too small to recover the exact top-$K$, SIDECAR, unlike beam search, reports the announced factor, allowing the serving system to stop early once a quality target or latency limit is reached.
- **Key innovations:**
  - SIDECAR speculative decoding for Semantic-ID (SID) generative recommendation.
  - Approximate draft candidates + single tree-attention scoring pass; bound unexplored SID prefixes; certify exact top-K if draft contains it; branch-and-bound trie expansion fallback.
  - ≤L calls certification; announces (1+δ) exactness factor under token/call budgets; fewer calls/memory than constrained beam search; reports quality target for early stopping.

### MADRec: Reliable Multi-Agent Reasoning with Evidence-Grounded Debate for Recommendation
- **arXiv:** [2611.28604v1](https://arxiv.org/abs/2611.28604v1)
- **Authors:** Zunlong Liu; Weijie Feng; Jingzhi Li; Lei Zhu; Zhiyong Cheng; Meng Wang
- **Institution/Company:** Hefei University of Technology; Tongji University
- **Submitted:** 2026-11-21
- **Category:** cs.IR (all: cs.IR)
- **Abstract:** Large Language Models (LLMs) are transforming recommender systems from conventional preference matching toward reasoning-driven and explainable decision-making. Multi-agent collaboration further advances this paradigm by distributing recommendation reasoning across specialized agents. However, existing frameworks rarely assess the reliability of intermediate reasoning during collaboration, allowing erroneous judgments to propagate across agents and ultimately degrade recommendation quality. To address this issue, we propose Multi-Agent Debate-based Recommendation (MADRec), an evidence-grounded multi-agent framework that enhances the reliability of multi-agent recommendation reasoning. MADRec consists of three coordinated modules. First, the Multi-Agent Debate (MAD) module enables an Interaction Agent and a Semantic Agent to analyze interaction signals and content-level semantic signals from complementary perspectives, generating diverse recommendation judgments through structured debate. Second, the Evidence-Grounded Retrieval-Augmented Reasoning (EG-RAR) module grounds the Semantic Agent's reasoning in item-level evidence and refines candidate scores by assessing how well the evidence supports the corresponding semantic claims. Third, the Judge-based Ranking Calibration (JRC) module leverages debate-derived reliability cues to adaptively calibrate interaction-based and semantic ranking results for the final recommendation. Extensive experiments on three real-world datasets demonstrate that MADRec consistently outperforms competitive baselines and enhances the reliability of multi-agent recommendation reasoning.
- **Key innovations:**
  - MADRec multi-agent debate recommendation with reliability checks on intermediate reasoning.
  - Interaction Agent + Semantic Agent structured debate; Evidence-Grounded Retrieval-Augmented Reasoning (EG-RAR); Judge-based Ranking Calibration (JRC).
  - Grounds semantic claims in item evidence; calibrates interaction vs semantic ranking using debate reliability; outperforms baselines on 3 real-world datasets.

### MARS Technical Report
- **arXiv:** [2611.24006v1](https://arxiv.org/abs/2611.24006v1)
- **Authors:** Tong Liu; Chaoqun Hou; Longxiang Xiong; Junhong Lou; Jiaqi Zheng; Qixin Li; Zixin Zhao; Yong Duan; Xiannian Hu; Fengze Jiang; Yu Zhu; Cheng Guo; Xinyuan Qi; Zi Zhuang; Ping Liu; Lv Shao; Zongwei Wang
- **Institution/Company:** MARS Team (not further specified; evaluated on Taobao scenarios)
- **Submitted:** 2026-11-18
- **Category:** cs.IR (all: cs.IR)
- **arXiv comment:** 46 pages, 5 figures
- **Abstract:** Modern industrial recommender systems use multi-stage cascades--retrieval, pre-ranking, ranking, and re-ranking--to narrow millions of candidates to a personalized list. While each stage deploys sophisticated models, pipeline-level decisions on channel activation, quotas, model selection, and score fusion remain engineer-tuned and user-agnostic within each scenario. This report presents MARS (Multi-stage Agentic Recommendation System), extending personalization from individual-stage predictions to full pipeline orchestration. A near-line agent built on fine-tuned Qwen3-0.6B generates per-user configurations--a seven-dimensional action covering pipeline mode, retrieval quotas, model selection, fusion weights, and reranker settings--from a constrained action space. Configurations are validated, cached, and consumed asynchronously; the cascade never waits for LLM inference. Schema checks, fallbacks, and a kill switch ensure serving safety. The policy is trained in three stages: Confidence-aware SFT distills schema-valid generation from a teacher model; Format-Anchored Preference Optimization (FAPO) learns action preferences via ActionMask with posterior weighting; Group Relative Policy Optimization (GRPO) refines the policy through Sandbox replay with a frozen reward model, without exposing exploratory actions to live traffic. Two-week A/B tests across five Taobao scenarios with over ten million daily users show positive gains on all key metrics. The largest reach +5.22% V2P and +7.34% GMV, with positive CTR lifts on both click surfaces. About 20% of requests use a lightweight Minimal mode, and deployment shows 12 ms lower mean serving latency versus production.
- **Key innovations:**
  - MARS (Multi-stage Agentic Recommendation System) extends personalization to full pipeline orchestration.
  - Near-line agent (fine-tuned Qwen3-0.6B) emits 7-dimensional action per user; async cached validated configs; kill switch/fallback; no waiting for LLM in serving.
  - Confidence-aware SFT + FAPO + GRPO sandbox replay; two-week A/B on 5 Taobao scenarios >10M DAU; +5.22% V2P +7.34% GMV; positive CTR; ~20% Minimal mode; -12ms mean latency.

---

## Advertising

### Budget, Readout or Reasoning? Where Small Reasoning Models Lose Value in Auction Bidding
- **arXiv:** [2611.34068v1](https://arxiv.org/abs/2611.34068v1)
- **Authors:** Mahbod Khaleti; Seyed Reza Tavakoli; Baran Hoseini; Alireza Noori; Amir Amini; Koorosh Aslansefat; Marjan Alirezaie; Ali Habibnia
- **Institution/Company:** Dataism Laboratory for Quantitative Finance; Independent researcher; Princeton University; University of Hull; Toronto Metropolitan University; Virginia Tech
- **Submitted:** 2026-11-25
- **Category:** cs.AI (all: cs.AI, cs.CL, econ.GN)
- **arXiv comment:** 19 pages, 2 figures, 23 tables. Code and data: https://github.com/DataismLab/bid-reasoning
- **Abstract:** Ad platforms and marketplaces show bidders a bid landscape, the estimated chance of winning at each candidate bid, and increasingly let agents built on reasoning language models choose the bid. We give six open reasoning models of 4B to 14B parameters such landscapes, with win curves from eBay closing prices and from a simulated advertising market (AuctionNet), and score their bids on held-out auctions against an exact calculator. Because the agent is handed the estimates, the lost value can be split by cause. Two failures belong to the models. They pass over the best option even when the values written in their own trace already rank it first, and their wrong answers lean toward the highest bid on the menu. The lean is about the bid's size, not its place in the list, and it survives sampling. At 768 forced tokens on eBay, under pay-your-bid pricing, the wrong answers cost bidders 7-17% of the surplus the calculator's bids earn. Arithmetic errors are rare. Two further losses come from operator choices. A token cap cuts traces short: allowed to stop on their own within 4,096 tokens, five models recover 91-100% of the calculator's lead over a model that does no reasoning. Asking for the answer while the reasoning block is still open misreads it: closing the block first lifts the weakest model from 42% to 84% on eBay and from 24% to 81% on AuctionNet. Finally, an audit that flags bids disagreeing with the trace's own numbers, and overrides them with the calculator's bid, raises the share of the calculator's lead recovered at 768 forced tokens from 42-85% to 84-100% on eBay under nested cross-validation, and the same reader settings transfer from eBay to AuctionNet.
- **Key innovations:**
  - Analyzes where small reasoning models lose value in auction bidding when given bid landscapes & win curves.
  - Separates model failures from operator choices; audit flags bids disagreeing with own trace & overrides with calculator bid.
  - Models pass over best option; lean toward highest bid; wrong answers cost 7–17% surplus at 768 tokens eBay; token caps hurt; closing reasoning block first helps; audit recovers 84–100% calculator lead; transfers eBay→AuctionNet.

### AdProducer: Towards Agentic Advertising Video Generation
- **arXiv:** [2611.31466v1](https://arxiv.org/abs/2611.31466v1)
- **Authors:** Kunyang Li; Chaoyang Wang; Mubarak Shah; Yuzhang Shang
- **Institution/Company:** Institute of Artificial Intelligence, University of Central Florida
- **Submitted:** 2026-11-23
- **Category:** cs.CV (all: cs.CV, cs.AI)
- **arXiv comment:** Project page: https://lky-ang.github.io/AdProducer-page/ Code: https://github.com/lky-ang/AdProducer
- **Abstract:** Recent advances in video generation have made automated advertising production increasingly feasible. However, an effective advertisement must faithfully represent the product and communicate its selling points through compelling visual storytelling, which requires more than visual synthesis: it calls for deeper product understanding and strategic decisions about how to present product value. Crucially, product research and creative design are closely intertwined, as the information gathered about a product determines which features can be faithfully demonstrated and how they should be presented. In this paper, we introduce AdProducer, the first end-to-end agentic framework for advertising video creation, transforming concise creative briefs into finished advertisements. Our multimodal agent autonomously researches products through web and image search and translates its findings into selling-point-driven storyboards that guide a frozen video generator. To achieve this, we develop a dedicated data construction pipeline that yields two training datasets, AdProducer-SFT and AdProducer-RL, and train the agent through supervised fine-tuning followed by reinforcement learning with joint optimization of storyboard- and video-level rewards. We further introduce AdCreation-Bench, comprising 305 advertising briefs across eight domains, with two complementary metrics: PG-Score for product correctness and creative execution, and Ad-Score for overall advertising effectiveness assessed by an independent judge. Experiments demonstrate that AdProducer improves the PG-Score of MiniMax H3 from 17.3 to 51.3 and generalizes to Veo 3.1 without additional training, improving its score from 28.0 to 35.9, with consistent gains in Ad-Score, VideoScore2, and human evaluations. Code, models, and data are released.
- **Key innovations:**
  - AdProducer first end-to-end agentic advertising video generation framework.
  - Multimodal agent researches product via web/image search, builds selling-point storyboards, guides frozen video generator; SFT + RL with joint storyboard/video rewards.
  - AdProducer-SFT/RL datasets; AdCreation-Bench (305 briefs, 8 domains; PG-Score + Ad-Score); PG-Score MiniMax H3 17.3→51.3; Veo 3.1 28.0→35.9; human/video gains; releases code/models/data.

### Iterative Scarcity-Guided Exploration: Bootstrapping Generative Auto-bidding from Narrow Support
- **arXiv:** [2611.26060v1](https://arxiv.org/abs/2611.26060v1)
- **Authors:** Qingmao Yao; Guangzheng Hu; Yusen Huo; Zhilin Zhang; Chuan Yu; Jian Xu; Xu Chu; Bo Zheng; Xiaotie Deng
- **Institution/Company:** Peking University; Alimama Tech, Taobao & Tmall Group of Alibaba; City University of Hong Kong; Independent Researcher
- **Submitted:** 2026-11-19
- **Category:** cs.LG (all: cs.LG)
- **arXiv comment:** Accepted at NeurIPS 2026 (poster)
- **Abstract:** Auto-bidding is a core algorithmic component in online advertising auctions. In practical cold-start settings, iterative training is commonly used to compensate for low-quality, narrowly supported historical data. Unfortunately, in iterative training, representative diffusion-based AI-Generated Bidding (AIGB) methods fail to sustain extrapolation beyond the narrow data support and stagnate at a suboptimal level. In this paper, we theoretically attribute this stagnation to Signal-to-Noise Ratio (SNR) collapse: the weak radial return signal is overwhelmed by a curvature-induced penalty. To break this stagnation, we propose \textbf{Iterative Scarcity-Guided Exploration (ISGE)}, which introduces a guidance handoff: as the return signal collapses, scarcity subsequently takes over as an exploratory signal to elevate the SNR above a critical threshold. Specifically, ISGE iteratively alternates between a \emph{Judger} that assigns scarcity scores to trajectories and an \emph{Explorer} that performs guided generation of high-scarcity and high-return trajectories, thereby bootstrapping from the narrow support with such self-generated trajectories. Extensive experiments on the industrial AuctionNet benchmark demonstrate that ISGE, starting from cold-start datasets, effectively surpasses the performance of the Full-Dataset baseline within three iterations. Code is available at https://github.com/alimama-tech/ISGE
- **Key innovations:**
  - Iterative Scarcity-Guided Exploration (ISGE) bootstraps generative auto-bidding from narrow-support cold-start data.
  - Attributes stagnation to SNR collapse; guidance handoff; alternates Judger (scarcity scores) + Explorer (high-scarcity & high-return trajectory generation).
  - Raises SNR above critical threshold; AuctionNet cold-start beats Full-Dataset baseline within 3 iterations; releases code.

### Ads for Agents: Measuring Ad-Serving MCP Servers
- **arXiv:** [2611.28911v1](https://arxiv.org/abs/2611.28911v1)
- **Authors:** Shahrooz Pouryousef; Sohini Chakraborty; Ali Montazer; Muoi Tran
- **Institution/Company:** Chalmers University of Technology and University of Gothenburg; Stockholm University; Google
- **Submitted:** 2026-11-21
- **Category:** cs.CR (all: cs.CR)
- **Abstract:** AI agents call external tools through protocols such as the Model Context Protocol (MCP). Some MCP servers return paid advertisements (ads) into the model's context. The model then decides whether these ads and their disclosures reach the user. We trace these ads from their sources to the agent's tool results across public MCP servers and packages. We find the servers through their public traces in ad networks, package registries, certificate logs, hostnames, MCP directories, and GitHub configurations. We then query the ad-serving servers with read-only requests and inspect their ad links. Ads appear on only 0.57% of 101,363 open MCP endpoints and 0.04% of 122,656 local MCP packages. Although 173 ad networks target agents, operators insert the ads themselves on about half of the 226 ad-returning servers. Nearly all ad-serving packages likewise carry the operator's own affiliate identifier. While ads adapt to the topic and intent of the query, their disclosure stays fixed within each tool. Only 9.3% of the ads carry an explicit sponsored label. Most ad links also hide their destinations. Since operators insert most ads themselves and label them inconsistently, we propose a per-item ad annotation in MCP results. Clients can show this annotation to the user independently of the model's answer.
- **Key innovations:**
  - Ads for Agents measures ad serving inside MCP (Model Context Protocol) agent tools.
  - Traces ads to agent tool results; read-only queries; analyzes disclosure & links; proposes per-item ad annotation in MCP results.
  - Ads on 0.57% of 101,363 open MCP endpoints + 0.04% of 122,656 local packages; 173 ad networks target agents; ~half operators self-insert; affiliate IDs; only 9.3% explicit sponsored label; hidden destinations; clients should show annotation independently.

### CutAgent: Creative-Gene-Driven Planning and Experience-Guided Self-Refinement for High-CTR E-commerce Advertising Video Creation
- **arXiv:** [2611.22418v1](https://arxiv.org/abs/2611.22418v1)
- **Authors:** Xuyue Huang; Guanbo Huang; Jiasong Feng; Run Ling; Ao Ma; Xi Zhao; Yaoyu Li; Jie Gao; Ke Cao; Wei Feng; Zhanjie Zhang; Hao Wang; Jinghe Hu
- **Institution/Company:** JD.com; Tsinghua University; Tianjin University; Zhejiang University
- **Submitted:** 2026-11-17
- **Category:** cs.CV (all: cs.CV)
- **Abstract:** E-commerce advertising video creation requires both high-level creative planning and reliable multi-modal production. However, existing methods often map product attributes directly to scripts or editing decisions without explicitly modeling advertising strategies, narrative structures, and production styles. They also have limited ability to reuse past production failures. To address these limitations, we propose $\textbf{CutAgent}$, a dual-agent framework that formulates advertising video creation as a Plan--Execute--Self-Evolve process. CutAgent comprises two collaborative agents, $\textbf{GeneAgent}$ and $\textbf{VideoAgent}$, connected by a structured creative gene that bridges product understanding and video production. GeneAgent maps multi-modal product inputs---textual attributes together with product images---to creative genes that specify narrative units and production rules. To train GeneAgent, we construct $\textbf{CutAgent-70K}$ with approximately 70K samples of product attributes/images, reverse-extracted creative genes, cleaned clip pools, and real-world CTR, and apply high-CTR supervised fine-tuning followed by CTR-guided GRPO. Guided by the generated gene, VideoAgent retrieves category-then-gene failure--correction experiences from a long-term memory as constraints for shot-script planning, then coordinates material retrieval, narration, subtitles, music, and timeline rendering. Independently, a reflection loop diagnoses quality defects, revises deficient production decisions, and writes verified corrections back to memory for later retrieval. Experiments on $\textbf{CutAgent-Eval}$ show that CutAgent outperforms representative baselines in e-commerce advertising video creation, achieving the highest online CTR of $\textbf{2.21\%}$.
- **Key innovations:**
  - CutAgent dual-agent Plan–Execute–Self-Evolve for high-CTR e-commerce advertising video.
  - GeneAgent maps multimodal product inputs to structured creative gene; VideoAgent retrieves failure→correction memory; script/shot planning; material retrieval; narration/subtitles/music; rendering.
  - CutAgent-70K; high-CTR SFT + CTR-guided GRPO; reflection loop; CutAgent-Eval; highest online CTR 2.21%.

### Platform Recommendation and Competition in Search Markets
- **arXiv:** [2611.24464v1](https://arxiv.org/abs/2611.24464v1)
- **Authors:** Sanxi Li; Jun Yu; Mingsheng Zhang
- **Institution/Company:** School of Economics, Renmin University of China; School of Economics, Shanghai University of Finance and Economics
- **Submitted:** 2026-11-18
- **Category:** econ.TH (all: econ.TH)
- **Abstract:** Recommendation rules affect both sellers' incentives and the alternatives consumers expect to find. We develop a framework for evaluating these rules with heterogeneous sellers, endogenous pricing and advertising, and costly consumer search. For a broad class of separable recommendation scores, we establish conditions under which a unique market equilibrium exists. Three applications illustrate the use of the framework. A stronger reward for low prices does not necessarily lower equilibrium prices and benefit consumers when products are sufficiently differentiated in qualities. Quality guidance can lower the price of each product and benefit consumers while raising the average transaction price. With heterogeneous match distributions, a reward for the best initial inspection can help consumers with advertising fixed and harm them when advertising adjusts. A two-type design extension shows that no finite optimum over implementable outcomes uses positive weights on both quality and low prices, even when the platform values consumer surplus.
- **Key innovations:**
  - Platform Recommendation and Competition in Search Markets theory.
  - Separable recommendation scores; heterogeneous sellers; endogenous pricing & advertising; costly consumer search; unique equilibrium conditions.
  - Low-price reward not always consumer-beneficial; quality guidance can lower individual price but raise average transaction price; best-initial-inspection effects depend on advertising; no finite optimum using both quality & low-price weights.

### TokenFormer V2: Breaking the Resolution-Complexity Dilemma in Unified Recommendation
- **arXiv:** [2611.19074v1](https://arxiv.org/abs/2611.19074v1)
- **Authors:** Kaihui Wu; Guoming Li; Liang Guo; Yifeng Zhou; Yuehong Hu; Junwei Pan; Zhixiang Feng; Chengguo Yin; Wenqi Fan; Haijie Gu; Jie Jiang
- **Institution/Company:** Tencent Inc.; The Hong Kong Polytechnic University
- **Submitted:** 2026-11-14
- **Category:** cs.IR (all: cs.IR, cs.LG)
- **arXiv comment:** Technical Preprint. 12 pages, 5 figures
- **Abstract:** Industrial recommendation faces a resolution--complexity dilemma: dense interactions make detailed modeling of long behavior histories expensive, while compact history summaries restrict the evidence available to prediction. A unified backbone must preserve rich behavioral details within strict serving budgets. We introduce \textbf{TokenFormer V2}, a unified architecture that explicitly decouples \emph{representation resolution} from \emph{interaction density}. Its group-wise token layout jointly encodes behavior segments with non-sequential context, expands interaction ranges via hierarchical group merging, and coordinates distributed groups through \emph{NS Fusion} and \emph{Global Sync} modules. Through this \emph{local--global decomposition} paradigm, computation is concentrated on structured interactions while preserving fine-grained evidence, ensuring that every encoded event remains directly accessible to the \emph{Full-Resolution Readout} module. On the Tencent Advertising Algorithm Competition 2026 (TAAC 2026) benchmark, TokenFormer V2 achieves top-ranking accuracy among unified recommendation baselines while using \textbf{5.1$\times$ fewer FLOPs} than leading baselines, sustaining its advantage across long histories and imbalanced behavior domains. Furthermore, in billion-parameter evaluations on WeChat Channels advertising, it consistently outperforms state-of-the-art industrial baselines, yielding up to a \textbf{+0.07 pp} overall AUC gain. In live online A/B testing against the production model, TokenFormer V2 delivers a statistically significant \textbf{2.33\% increase in GMV}. These results establish TokenFormer V2 as a battle-tested blueprint for scalable, full-resolution behavior modeling in industrial recommendation.
- **Key innovations:**
  - TokenFormer V2 decouples representation resolution from interaction density in unified recommendation.
  - Group-wise token layout; non-sequential context; hierarchical group merging; NS Fusion + Global Sync; Full-Resolution Readout.
  - Local–global decomposition; top-ranked TAAC 2026 with 5.1× fewer FLOPs; billion-parameter WeChat Channels +0.07pp AUC; +2.33% GMV online; long histories + imbalanced domains.

---

## CTR / Conversion

### DNA: Unlocking Depth Scaling in CTR Models
- **arXiv:** [2611.25659v1](https://arxiv.org/abs/2611.25659v1)
- **Authors:** Caiyuan Li; Wenjie Wu; Yuheng Huang; Xiao Zhou; Silu Zhou; Ke Chen; Zinan Zhao; Xinrui Zeng; Hanmo Xu; Chaoqun Song; Hua Zong; Zongyuan Wu; Hongbin Zhou; Huimin Yi; Zhixuan Zhang; Dan Ou; Haihong Tang
- **Institution/Company:** Alibaba Group (DNA-4 deployed in Taobao search)
- **Submitted:** 2026-11-19
- **Category:** cs.IR (all: cs.IR)
- **arXiv comment:** 10 pages, 5 figures
- **Abstract:** Long user behavior sequences are among the strongest signals for click-through rate (CTR) prediction. Cross-attention makes these sequences practical for industrial ranking by keeping compute linear in sequence length. Yet the gains from stacking cross-attention layers taper off: on Taobao search, growing a cross-attention stack from 16 to 28 layers adds only 0.02 percentage points (pt) of AUC. We argue that the key-value side is the bottleneck. Each layer projects the same behavior sequence into keys and values, so adding depth gives the model more reads of a fixed sequence. We propose DNA (Dual-stream Nexus Attention), which lets the sequence itself evolve with depth. At each layer, the request representation (the search query, user features and scene) first reads the sequence. Each behavior token then attends to the updated request representation and uses what it reads to update itself, so the next layer reads a sequence shaped by the current request. The update runs once per request, all candidates share the resulting sequence, and both the reads and the update keep linear complexity in sequence length. At comparable forward FLOPs, DNA improves AUC over cross-attention stacks by 0.08 to 0.26 pt and keeps improving in the depth range where those stacks level off. DNA-4 is deployed in Taobao search. In an online A/B test against the production model, it improves CTR by 0.8% and GMV by 0.5%.
- **Key innovations:**
  - DNA (Dual-stream Nexus Attention) enables depth scaling in CTR models.
  - Request representation first reads behavior sequence; each behavior token then attends to updated request and updates itself; next layer reads request-shaped sequence.
  - Per-request update once, shared across candidates; linear complexity; addresses fixed-KV bottleneck; +0.08–0.26pt AUC at comparable FLOPs; DNA-4 Taobao +0.8% CTR +0.5% GMV.

### X-split Argus: Learning Reusable History Tokens for Efficient CTR Prediction
- **arXiv:** [2611.24283v1](https://arxiv.org/abs/2611.24283v1)
- **Authors:** Alexander Ploshkin; Nikita Stepanov; Alexey Pismenny; Viacheslav Ovchinnikov; Nikolay Savushkin
- **Institution/Company:** Not stated on arXiv/PDF page 1 (large-scale real-time bidding system in evaluation)
- **Submitted:** 2026-11-18
- **Category:** cs.IR (all: cs.IR)
- **arXiv comment:** Alexander Ploshkin, Nikita Stepanov and Alexey Pismenny contributed equally to this work
- **Abstract:** Accurate click-through rate (CTR) prediction depends on user representations that capture both persistent preferences and recent intent, yet processing extensive behavioral histories for every ranking request is costly under production compute and latency constraints. We present X-split ARGUS, a framework for ad ranking whose history compressor and online ranker are trained end to end. The compressor encodes past interactions into a compact set of tokens that are computed offline and reused across candidates, while the online ranker scores ads through cross-attention to these tokens and representations of recent events. Training combines an autoregressive loss for click feedback with distillation of candidate-specific click logits from a larger teacher that scores each candidate using the uncompressed history. The number of compressed history tokens and the length of recent history can be adjusted to fit serving compute and latency budgets. Offline evaluation shows a 0.81% relative reduction in normalized entropy (NE) compared with the production baseline. Deployment in a large-scale real-time bidding system increases online inference cost by 15% relative to the production baseline. An online A/B test against this baseline yields relative gains of 4.65% in a business metric reflecting the monetary value of conversions generated for advertisers and 2.96% in clicks.
- **Key innovations:**
  - X-split ARGUS compresses user history into reusable tokens for efficient CTR.
  - End-to-end history compressor + online ranker; offline reusable compressed tokens + recent events; cross-attention scoring.
  - Autoregressive click loss + teacher distillation; adjustable token count/history length; -0.81% NE; +4.65% conversion-value +2.96% clicks online; +15% inference cost.

### MTL-MHOL: Predicting Online Conversions under Delayed Feedback and Data Sparsity
- **arXiv:** [2611.30648v1](https://arxiv.org/abs/2611.30648v1)
- **Authors:** Mario Tejera Vicente; Eva Hagen; Emma van Breukelen; Quinten van de Vijver; Kathrin Gruber
- **Institution/Company:** Erasmus School of Economics, Erasmus University Rotterdam
- **Submitted:** 2026-11-23
- **Category:** cs.LG (all: cs.LG, stat.ML)
- **arXiv comment:** To be published in TMLR
- **Abstract:** This paper proposes the model-agnostic Multi-Task Learning Multi-Head Online Learning (MTL-MHOL) framework for conversion rate (CVR) prediction. Existing approaches typically address key challenges in CVR prediction, such as delayed feedback and data sparsity, in isolation or lack flexibility and practical applicability. MTL-MHOL adopts a time bucketing approach to account for delayed feedback and combines it with multi-task learning of an auxiliary task to mitigate data sparsity. We evaluate the framework on proprietary datasets from a private company and on a public dataset from Criteo. MTL-MHOL matches or outperforms all benchmark models in terms of Negative Log-Likelihood (NLL) and Relative Cross Entropy (RCE), and it correctly captures temporal trends in the data using an MLP backbone, while maintaining strong performance with a DeepFM backbone. In particular, MTL-MHOL matches the performance of the advanced delayed-feedback method FSIW, outperforms the entire-space approach ESMM by 21.5% in RCE, and achieves up to 81% lift in RCE compared to the best-performing classical benchmark.
- **Key innovations:**
  - MTL-MHOL model-agnostic multi-task learning + multi-head online learning for CVR under delayed feedback & sparsity.
  - Time bucketing for delayed feedback; auxiliary task mitigates data sparsity; works with MLP + DeepFM backbones.
  - Matches/outperforms benchmarks on NLL + RCE; proprietary + Criteo; matches FSIW; +21.5% RCE vs ESMM; up to +81% RCE vs best classical; TMLR.

### HME-PFD: Heterogeneous Mixture-of-Experts Privileged Feature Distillation
- **arXiv:** [2611.29094v1](https://arxiv.org/abs/2611.29094v1)
- **Authors:** Wen Xu; Xiaomin Zhang; Yucheng Yang; Danny Liu; Xunlong Gui; Fei Huang; Sha Meng
- **Institution/Company:** Meta; University of Toronto
- **Submitted:** 2026-11-21
- **Category:** cs.LG (all: cs.LG, cs.IR)
- **Abstract:** Knowledge distillation (KD) is widely used to transfer knowledge from large teacher models to smaller student models, facilitating efficient serving of machine learning systems. In the context of ads recommendation, privileged features distillation (PFD) extends KD by allowing the teacher model to leverage privileged features, i.e., features available only during training, to enhance distillation performance. However, in real-world scenarios, privileged features often have limited coverage and exhibit heterogeneous distributions, resulting in training examples of varying importance for distillation and model learning. We propose Heterogeneous Mixture-of-Experts Privileged Feature Distillation (HME-PFD), a novel approach that incorporates privileged features into the routing module of a Mixture-of-Experts-based student model. Our method introduces both hard-coded and learnable routing modules, enabling the student to dynamically determine expert assignment based on the availability and values of privileged features. This design allows the student model to better handle the heterogeneous data scenario, where privileged features are partially observed, by differentiating between high- and low-signal samples. Extensive experiments on two post-click conversion prediction tasks demonstrate that HME-PFD consistently outperforms baseline methods. Our results show that leveraging privileged features for expert routing in the student model leads to improved model performance, even when privileged features are incomplete or sparse.
- **Key innovations:**
  - HME-PFD heterogeneous MoE privileged feature distillation for ads/conversion.
  - Privileged features used only at training incorporated into student routing; hard-coded + learnable routing; handles partial privileged features.
  - Routes high-/low-signal samples; outperforms baselines on two post-click conversion tasks; improves with incomplete/sparse privileged features; Meta + University of Toronto.

### Lost in the Funnel: Selection-Induced Miscalibration in Ranking and Decision Systems
- **arXiv:** [2611.22595v1](https://arxiv.org/abs/2611.22595v1)
- **Authors:** Aditya Somani; Rahul Ragesh; Vikas Joshi; Amit Singh
- **Institution/Company:** Microsoft Ads
- **Submitted:** 2026-11-17
- **Category:** cs.LG (all: cs.LG)
- **arXiv comment:** Under Review
- **Abstract:** Modern ranking and decision systems combine components with divergent objectives, and scores calibrated at the model boundary are used as calibrated probabilities throughout the funnel, across filtering, reranking, business-rule enforcement, and auctions. Yet calibration is typically validated only where the score is produced, so its breakdown where the score is used is routinely overlooked. We ask when calibration survives this selection, how inherited error differs from selection effects, and what can fail for a perfectly calibrated score at a component boundary. We study these questions through a boundary-wise diagnostic framework of residual identities. We target rubric-judged relevance rather than presentation-dependent metrics such as CTR, so calibration is measurable at every funnel layer of interest. We first present an industry-wide case study that applies our diagnosis to settings where calibration deteriorates at decision time, tracing the degradation to selection rather than model error. This diagnosis motivates Funnel-Aware Recalibration (FAR): post-hoc, selection-policy-aware recalibration at the boundary where scores drive decisions. In a live two-region production A/B test, FAR cuts decision-time expected calibration error (ECE) by 60-80% and improves auction efficiency. We further adapt two public datasets to simulate industry settings, providing additional evidence for the mechanism. We plan to release the adapted datasets and their generation pipeline to support further research. Finally, we distill these findings into practical operating principles for calibrating multi-stage scoring systems.
- **Key innovations:**
  - Lost in the Funnel diagnoses selection-induced miscalibration across ranking/auction funnel stages.
  - Boundary-wise residual-identity diagnostic; Funnel-Aware Recalibration (FAR) post-hoc selection-policy-aware recalibration at decision boundary.
  - Production A/B: decision-time ECE -60–80%; auction efficiency up; industry case + public adapted datasets; rubric relevance targets calibration independent of CTR.

---

## Sequential Modeling

### State Space Attention: Learning Context-Dependent Memory Retention
- **arXiv:** [2611.33625v1](https://arxiv.org/abs/2611.33625v1)
- **Authors:** Ege Çakar; Cengiz Pehlevan
- **Institution/Company:** Department of Statistics, Harvard University; John A. Paulson School of Engineering and Applied Sciences, Harvard University
- **Submitted:** 2026-11-25
- **Category:** cs.LG (all: cs.LG, cs.CL)
- **arXiv comment:** 36 pages, 3 figures, 37 tables. Code: https://github.com/Ege-Cakar/State-Space-Attention
- **Abstract:** Standard attention's key-value cache grows linearly with context length. Bounding it raises the question of what a sequence model should retain for long-context reasoning. We argue this choice should be learned, and introduce State Space Attention (SSA), which learns to keep a bounded set of past representations and reads them with standard attention. A learned scorer rescores every chunk against newly arriving context and the rest of memory. A fixed-context Transformer is then the special case that always keeps the most recent tokens. We train the scorer and reader jointly, either moving gradually from a differentiable soft weighting of memories to hard retention, or with hard retention from the start. To produce signal for the scorer, we generate supervised samples during training, a technique we call recovery. We compare SSA with recurrent models, bounded-memory attention methods, and full-attention Transformers across retrieval, variable tracking, multi-hop reasoning, and language modeling. On our retrieval and reasoning benchmarks, SSA matches or comes within a few points of full attention on most tasks, far outperforms a Transformer with the same readable budget on every long-context retrieval task we evaluate, and matches or outperforms one with about 4 times that budget, while using constant inference memory. The largest remaining gap to full attention at small language model scale is on RULER. SSA makes a fixed number of tokens useful over a longer context, and since it reads memory with standard attention, we propose that it can be stacked with KV cache eviction methods. We also pretrain and post-train 400M-parameter models and measure how SSA's training and inference costs scale with context length and model size. Together, these experiments examine the capabilities and limitations of learned memory retention for long-context sequence modeling.
- **Key innovations:**
  - State Space Attention (SSA) learns context-dependent memory retention with bounded memory.
  - Learned scorer rescores chunks against new context + memory; joint scorer/reader training; recovery supervised samples; soft→hard retention or hard from start.
  - Constant inference memory; near full-attention on retrieval/reasoning; outperforms same-budget Transformer; ~4× budget parity; stacks with KV eviction; 400M pretraining scaling; code released.

### One Token, Many Lessons: Sliding-Window Attention within Gated Delta Networks
- **arXiv:** [2611.33257v1](https://arxiv.org/abs/2611.33257v1)
- **Authors:** Yuchen Song; Yangbin Chen
- **Institution/Company:** Not stated on arXiv/PDF page 1
- **Submitted:** 2026-11-24
- **Category:** cs.LG (all: cs.LG, cs.AI)
- **Abstract:** Linear attention compresses historical context into a fixed-size recurrent state, reducing the computational and memory costs of long-sequence modeling. From the perspective of test-time regression (TTR), the state matrix can be viewed as an online-learned regression model, where keys and values serve as inputs and targets respectively, and queries are used to read from the model. From this perspective, the effectiveness of state learning depends not only on the update rule but also on how the key-value learning pairs used for state updates are constructed. While existing work has largely focused on how the state is updated and organized, we investigate how the learning pairs used for state updates are constructed. To this end, we propose Sliding-Window Gated DeltaNet (SWGDN), which replaces short convolutions in Delta-Rule linear attention with sliding-window attention to perform content-dependent local aggregation of projected queries, keys, and values. Our experiments show that SWGDN makes the key-value pairs used in consecutive updates more similar in both GDN2 and KDA. In SWGDN, carrying information from the same token across updates can help the recurrent state reinforce a previously learned association. The local mixing strategy can be incorporated into any Delta-Rule-based linear attention architecture without changing its state update equations or chunkwise parallel algorithms. We apply this strategy to two Delta-Rule variants, GDN2 and KDA, and experimental results demonstrate that SWGDN outperforms the original Delta-Rule baseline across multiple benchmarks.
- **Key innovations:**
  - Sliding-Window Gated DeltaNet (SWGDN) changes construction of key-value learning pairs in Delta-Rule linear attention.
  - Replaces short convolutions with sliding-window attention for content-dependent local aggregation of projected Q/K/V.
  - No change to state update or chunkwise parallel algorithm; reinforces previously learned associations; outperforms original Delta-Rule baseline on GDN2 + KDA.

### LimeTree: Linear-Memory Graph Neural Networks over Tree-Graphs for Resource-Efficient Language Modeling and Context Extrapolation
- **arXiv:** [2611.30934v2](https://arxiv.org/abs/2611.30934v2)
- **Authors:** Elisabeth Fink
- **Institution/Company:** Department of Computer Science, Middlesex University
- **Submitted:** 2026-11-23
- **Category:** cs.CL (all: cs.CL, cs.LG)
- **Abstract:** The search for computationally efficient alternatives to the Transformer has yielded numerous architectures in recent years; however, most exhibit severe weaknesses in associative recall-such as key-value (KV) retrieval-and length extrapolation, where even standard Transformers struggle. This paper introduces LimeTree, a linear-complexity architecture in both memory and compute for sequence modeling. By integrating synthetic KV retrieval tasks directly into standard language modeling training, LimeTree achieves strong perplexity alongside reliable recall. Two variants were evaluated on WikiText-103 and PG-19 under strict compute constraints. On WikiText-103, LimeTree reaches a token-level perplexity of 19 in just 6 hours on four Quadro RTX 8000 GPUs, while maintaining 100\% KV retrieval accuracy even when extrapolating from a training context length of 512 to an evaluation length of 16,384. On PG-19, the model achieves a token-level perplexity of 10.84 in 35.5 hours on a single RTX PRO 6000 Blackwell GPU with minimal hyperparameter tuning. These results position LimeTree as a competitive linear-complexity alternative to Transformers, combining superior perplexity and training throughput with robust in-context retrieval and length extrapolation.
- **Key innovations:**
  - LimeTree linear-complexity sequence modeling over tree-graphs.
  - Integrates synthetic KV retrieval tasks into standard LM training.
  - Linear memory + compute; strong perplexity + reliable recall; WikiText-103 perplexity 19 +100% KV recall 512→16,384; PG-19 perplexity 10.84; low compute; length extrapolation.

---

## Games

### AlphaDefect: Expert-Level AI for Slay the Spire 2
- **arXiv:** [2611.31076v1](https://arxiv.org/abs/2611.31076v1)
- **Authors:** Qiyue Chen; Taian Yu; Junpei Komiyama; Haobo Huang
- **Institution/Company:** AgroParisTech, Université Paris-Saclay; University of New South Wales; Mohamed bin Zayed University of Artificial Intelligence; Chinese University of Hong Kong
- **Submitted:** 2026-11-23
- **Category:** cs.AI (all: cs.AI, stat.ML)
- **Abstract:** Slay the Spire 2 (STS2) is a single-player deck-building game that requires long-term planning under heavy randomness. We present AlphaDefect, an expert-level AI system for STS2: for each character, one network trained with proximal policy optimization (PPO) makes every decision of a run, in combat and outside it. At the highest difficulty, Ascension 10, on two versions of the game current in November 2026 and on test seeds not played in training, AlphaDefect wins 62-77% of runs across six characters with greedy play and 68-80% with test-time search, after 1.3 to 6.7 billion decisions of training per character; runs uploaded by human players of all levels are won 11-20% of the time at the same difficulty. The networks read the game as entity records that identify each card, relic and enemy through a learned embedding and attributes from the game data, together with consequences of public information computed by the engine. Ablations show how much the agent depends on this encoding: without these identities, the network did not win a single run, and without the computed consequences it won 8.3 points fewer. To our knowledge, AlphaDefect is the strongest publicly reported STS2 agent as of November 2026.
- **Key innovations:**
  - AlphaDefect expert-level AI for Slay the Spire 2 (STS2), one PPO network per character for all combat & non-combat decisions.
  - Entity-record encoding with learned card/relic/enemy embeddings + game-data attributes + engine-computed consequences of public info.
  - Ascension 10 held-out seeds: 62–77% greedy /68–80% test-time search vs 11–20% human-uploaded; 1.3–6.7B training decisions per character; ablations; strongest public STS2 agent Nov 2026.

### GameDojo: Benchmarking Real-Time Interactive Agents in Video Games
- **arXiv:** [2611.30771v1](https://arxiv.org/abs/2611.30771v1)
- **Authors:** Kuan Zhang; Zhihao Yang; Yukun Chen; Xingyilang Yin; Mingyu Ouyang; Yue Su; Xiangnan Wu; Jiaming Li; Longze Chen; Run Luo; Zirong Chen; Lu Wang; Yiming Li
- **Institution/Company:** Tsinghua University; University of Chinese Academy of Sciences; University of Macau; National University of Singapore; University of Hong Kong
- **Submitted:** 2026-11-23
- **Category:** cs.AI (all: cs.AI)
- **arXiv comment:** 28 pages. Project page: https://gamedojo-benchmark.github.io/ , and code: https://github.com/THUSI-Lab/GameDojo
- **Abstract:** Interactive intelligence requires agents to act on observations and adapt to the consequences of actions. Studying these abilities calls for diverse, challenging tasks under controlled conditions. We introduce GameDojo, a controllable interactive gameplay benchmark of 120 boss encounters across 20 games for evaluating model capabilities, learning algorithms, and agent harnesses. Coding agents reconstruct the environments and write gameplay scripts, producing GameDojo-Data with 600 hours of gameplay trajectories. Experiments reveal substantial challenges for frontier models, especially in real-time interaction. Training on GameDojo-Data brings GameDojo-4B to frontier performance, with the strongest real-time performance. We also find joint training improves individual tasks, and learned policies transfer across bosses. Together, these findings establish GameDojo as a challenging and valuable interactive gameplay benchmark for the community. Our project page is at https://gamedojo-benchmark.github.io/ , and our code is at https://github.com/THUSI-Lab/GameDojo .
- **Key innovations:**
  - GameDojo controllable real-time interactive gameplay benchmark.
  - 120 boss encounters across 20 games; coding agents reconstruct environments & write gameplay scripts; GameDojo-Data 600h trajectories.
  - Evaluates model capabilities, learning algorithms, agent harnesses; real-time hard for frontier; GameDojo-4B frontier after training; joint training + cross-boss transfer; public project/code.

### Coding4Games: Can Modern Coding Agents Play Modern Video Games?
- **arXiv:** [2611.31974v1](https://arxiv.org/abs/2611.31974v1)
- **Authors:** Shifang Zhao; Haoyu Wang; Yuyang Yin; Dong Chen; Xingyilang Yin; Yunkang Tao; Honghao Chen; Guangzhi Wang; Yiran Wang; Junfu Pu; Cheng Cheng; Xiaodong Cun; Ying Shan
- **Institution/Company:** Tencent ARC Lab; GVC Lab, Great Bay University; Beijing Jiaotong University; Nanjing University
- **Submitted:** 2026-11-24
- **Category:** cs.AI (all: cs.AI)
- **arXiv comment:** Project Page: https://coding4game.github.io/
- **Abstract:** Games, especially modern AAA games, challenge language models to perceive complex scenes, control actions, and make decisions over long horizons. Existing game benchmarks primarily test language models as computer-use agents that query a language model throughout play, incurring repeated inference cost and, in real-time games, acting while the environment continues to evolve. We ask whether coding agents can learn from game interaction to develop standalone game-playing programs that run without language model inference. We thus introduce Coding4Games, a benchmark for evaluating whether coding agents can develop standalone programs that play modern games through visual observations and standard game inputs. Coding4Games has three defining features: 1) Diverse Modern Games, covering 15 games with diverse visual, strategic, and control demands; 2) Development-Test Separation, in which a coding agent uses a sandbox and the standard player interface to iteratively develop a program, after which the selected program is frozen and independently tested without language-model inference; and 3) Outcome and Process Evaluation, which measures not only game performance and reliability but also how agents use feedback, revise programs, and resolve problems during development. Across 15 games, the best program per game outscores the strongest GUI baseline on 13 and ties it on one. The human player outscores all agents on 10 games. We additionally examine the effects of development budgets. Coding4Games evaluates whether coding agents can turn their understanding of complex interactive environments into programs that work reliably on their own.
- **Key innovations:**
  - Coding4Games benchmarks coding agents that build standalone game-playing programs.
  - Development–test separation; sandbox + standard player interface; frozen final program; no LLM inference at test time.
  - 15 modern games; outcome + process evaluation; best program outperforms GUI baseline on 13 +tie 1; human better on 10; development budget effects; public project.

### Exploring Multi-Player Social Games as Verifiable Training Grounds for Large Language Models
- **arXiv:** [2611.31821v1](https://arxiv.org/abs/2611.31821v1)
- **Authors:** Keyu He; Michael Li; Jiarui Liu; Mingqian Zheng; Koichi Onoue; Tongshuang Wu; Maarten Sap
- **Institution/Company:** Carnegie Mellon University; Fujitsu Research of America
- **Submitted:** 2026-11-24
- **Category:** cs.CL (all: cs.CL, cs.AI, cs.LG, cs.MA)
- **Abstract:** The training of socially intelligent language models often relies on large language model (LLM) judges, which are expensive, noisy, and vulnerable to reward hacking. Multi-player social games offer a natural alternative: they require open-ended communication to coordinate with teammates and infer hidden roles, while their rules provide an objective outcome which can serve as a verifiable reward for training. Using three social games, we explore how much social intelligence Qwen3 models can acquire through supervised fine-tuning (SFT) and reinforcement learning with verifiable rewards (RLVR). Results show that against a much stronger Gemma-3-27B model, SFT and RLVR raise the win rate of Qwen3-4B from 33% to 81% on the three trained games, and from 39% to 54% on three additional held-out games. In contrast, in-context strategies such as prompting improve the win rate of Qwen3-4B by only about 6 pp across the same games we train and evaluate on. Furthermore, we show that the gains from SFT and RLVR hold across the model sizes 1.7B, 4B, and 32B. Qualitative analyses of agent behavior show signs of stronger social intelligence; for example, trained agents tend to share information more openly, check each other's claims against public evidence, and coordinate their votes. More broadly, our results demonstrate that training LLMs on verifiable outcomes in social games can cultivate generalizable social behaviors, which offers a scalable path for building socially intelligent agents.
- **Key innovations:**
  - Multi-player social games as verifiable RL training grounds for LLMs.
  - Objective game outcomes as verifiable rewards; SFT + RLVR on Qwen3; no noisy LLM judge.
  - Qwen3-4B 33%→81% trained games +39%→54% held-out vs Gemma-3-27B; prompt-only ~+6pp; scales 1.7B/4B/32B; social intelligence signals; CMU + Fujitsu Research.

### Computing Normal-Form Correlated Equilibria in Extensive-Form Games is in PPAD
- **arXiv:** [2611.34897v1](https://arxiv.org/abs/2611.34897v1)
- **Authors:** Vincent Cheval; Florian Horn; Soumyajit Paul; Mahsa Shirmohammadi
- **Institution/Company:** University of Oxford; CNRS, IRIF
- **Submitted:** 2026-11-25
- **Category:** cs.GT (all: cs.GT, cs.CC)
- **Abstract:** We study the computational complexity of finding any normal-form correlated equilibria (NFCE for short) in the succinct games of extensive-form with perfect recall, which is considered as a major open problem in algorithmic game theory. Our main results place this problem in PPAD for an arbitrary numbers of players. Our second result establishes PPAD-hardness of computing such an NFCE with support size of at most quadratic in the size of the game, even for two-player games. The posed restriction on the support size in PPAD-hardness construction is motivated by our PPAD algorithm, which constructs an NFCE with support size quadratic in the size of the input extensive-form game.
- **Key innovations:**
  - Computing normal-form correlated equilibria (NFCE) in succinct extensive-form perfect-recall games is in PPAD for any number of players.
  - PPAD algorithm constructs NFCE with support size quadratic in game size.
  - PPAD-hard even for two-player games with support size at most quadratic; resolves a major open algorithmic-game-theory problem.

---
