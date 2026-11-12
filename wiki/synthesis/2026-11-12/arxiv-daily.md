---
title: "arXiv Daily — AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games (2026-11-12)"
type: synthesis
created: 2026-11-12
updated: 2026-11-12
sources: [arxiv.org]
tags: [arxiv, daily, ai, llm, agents, recommendation, generative-recommendation, advertising, ctr, retrieval, sequential-modeling, games, multi-agent, daily-digest]
---

# arXiv Daily Report (2026-11-12)

> **Query time**: 2026-11-12 (Thu). This report surveys recently submitted/indexed arXiv papers from the 2026-11-08 to 2026-11-11 window visible at query time (including Wed, 11 Nov 2026 announcements on arXiv recent lists), covering AI, LLMs, recommendation, advertising/CTR, sequential modeling, and games/strategic multi-agent settings.
>
> **Method**: Reviewed arXiv recent/category listings (`cs.AI`, `cs.IR`, `cs.MA`, `cs.GT`) and fetched selected abstracts/pages via web tools for papers matching the requested topics. Abstracts are condensed from arXiv metadata/pages; all performance claims and deployment numbers are **author-reported** unless explicitly noted. Affiliations/companies are listed when stated or clearly inferable from title/abstract context; otherwise marked **not specified in arXiv metadata**.
>
> **Caveats**: Abstract-level screening only (no reproduction). Venues, affiliations, and online A/B results should be verified from PDFs/project pages when needed. Topic overlap is common; each paper is placed in its primary theme.

## Summary

- **Advertising and generative retrieval** continue to push toward production constraints: on-demand geo-validity, set-level diversity/reward, and ad-side optimization for LLM-native ranking are becoming first-class design objectives.
- **Sequential modeling for recommendation/ranking** is increasingly treated as a systems-and-representation problem: reusable compressed states, timestamp-addressable exports, and latency-compatible interfaces matter alongside backbone quality.
- **Recommendation quality work** spans both structure and feedback: adaptive semantic-ID tokenization for generative recommenders, proactive denoising in graph collaborative filtering, and LLM-mediated explanations for counterfactual recommendations.
- **LLM agents** emphasize reliability and coordination: evidence-linked memory to reduce memory-induced degradation, trace-aware evaluation/red-teaming for enterprise analytics agents, and information-network design for steering emergent multi-agent behavior.
- **Games/reasoning environments** highlight cooperative/asymmetric collaboration benchmarks and symbolic/evolutionary approaches to ARC-style abstraction-and-reasoning tasks.

---

## A. Advertising, CTR, and Retrieval

### 1. TS-GEAR: Taobao Shangou GEnerative Ad Retrieval
- **arXiv**: [2611.12180](https://arxiv.org/abs/2611.12180)
- **Authors**: Guofeng Tong, Xu Zhang, Guangliang Yu, Haiqiang Wang, Guannan Cong, Xing Guo, Yang Zhou, Jingjing Duan, Shuang Li, Feng Shi, Hualei Liu
- **Institution/Company**: Taobao Shangou / Alibaba ecosystem (inferred from title and abstract; not explicitly structured in arXiv metadata)
- **Categories**: cs.IR, cs.AI, cs.CL (submitted 2026-11-09)
- **Abstract**: On-demand delivery advertising differs from traditional e-commerce because merchants outside a user's delivery range are invalid, not merely low-ranked. TS-GEAR adapts generative retrieval to this setting by addressing three issues: semantic IDs that encode geography only softly, behavior aggregation that ignores real-time query/location, and autoregressive training that lacks set-level diversity signals. The proposed framework combines Geo-Semantic IDs, Query-Geo Target Attention, and Group Marginal Policy Optimization (GMPO). Deployed with a lightweight 0.1B backbone, it serves over 150 million queries per day in Taobao Shangou search advertising.
- **Key innovations**:
  - **Geo-Semantic ID**: splits merchant identifiers into geographic prefixes and semantic suffixes so reachability becomes a prediction target rather than a post-hoc filter.
  - **Query-Geo Target Attention**: conditions historical-behavior aggregation on the real-time query and location while encoding each behavior's own location in attention keys.
  - **GMPO**: rewrites GRPO-style advantages with deduplicated group reward/marginal advantage to discourage redundant near-duplicates without auxiliary diversity objectives.
  - **Author-reported results**: improves HitRate and geographic validity over generative retrieval baselines, with **+3.8% ad impressions** and **+4.2% ad revenue** online.
- **arXiv link**: https://arxiv.org/abs/2611.12180

### 2. CHO-Bench: How Do Context Hints Affect Ad Rankings in LLM Advertising?
- **arXiv**: [2611.11955](https://arxiv.org/abs/2611.11955)
- **Authors**: Shiqi Zhang, Yang Fei, Xiaokui Xiao
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.IR, cs.CL (submitted 2026-11-09)
- **Abstract**: LLM advertising ranks ads from conversational context, where user needs may go beyond explicit product queries. This paper formulates Context Hint Optimization (CHO): advertisers provide natural-language hints (what they offer, who may find it useful, and when it may be useful) to improve ad ranking under a budget. The authors introduce CHO-Bench and evaluate seven hint-generation strategies plus a unified strategy using over 1.19 million paired evaluations across five datasets with embedding-based and LLM-based rankers.
- **Key innovations**:
  - **CHO formulation**: treats ad-side natural-language hints as an optimization object for LLM-native ad ranking.
  - **CHO-Bench**: large-scale offline benchmark covering What/Who/When marketing dimensions and multiple ranker families.
  - **Practical findings**: hints generally improve rankings offline; embedding-based and LLM-based rankers favor different information dimensions, unified hints are not consistently best, and larger hint budgets show diminishing marginal gains (author-reported).
- **arXiv link**: https://arxiv.org/abs/2611.11955

---

## B. Sequential Modeling and Ranking Systems

### 3. SeqFold: Timestamp-Addressable Compressed States for User Action Sequence Backbones
- **arXiv**: [2611.13704](https://arxiv.org/abs/2611.13704)
- **Authors**: Mianwei Zhou, Duo Zhang, Henry Tsai, Yuqi Zheng, Jian Li, Juexin Lin, Sujay Khandagale, Vijay Rajaram, Dong Jiao, Tao Cheng
- **Institution/Company**: Not specified in arXiv metadata (evaluated on large-scale proprietary datasets)
- **Categories**: cs.AI, cs.SI (submitted 2026-11-10)
- **Abstract**: Instead of only improving sequence encoders or task-specific representations, SeqFold studies how to export multi-layer states from a frozen long-history user-action backbone as compact, timestamp-addressable representations for downstream training backfill and serving. The method combines learned multi-channel fusion, channel-specific temporal decay, and Lookup-Free Quantization (LFQ) to produce compact discrete codes; task-specific decoders map shared codes into flexible embedding spaces. A fused streaming implementation updates fusion recurrence per action while materializing states only at target timestamps.
- **Key innovations**:
  - **Compressed-state interface**: decouples long-history sequence modeling from downstream model consumption via reusable timestamp-aligned states.
  - **Discrete state export**: multi-channel fusion + temporal decay + LFQ compresses frozen backbone states for scalable storage/serving.
  - **Systems-aware streaming**: updates state recurrently per action but materializes only needed timestamps to reduce export cost.
  - **Author-reported results**: reduces per-state representation storage by **3,400×** while preserving most downstream ranking performance of the uncompressed model.
- **arXiv link**: https://arxiv.org/abs/2611.13704

---

## C. Recommendation Systems

### 4. Not All Branches Are Equal: Adaptive Semantic ID Construction for Generative Recommendation
- **arXiv**: [2611.11549](https://arxiv.org/abs/2611.11549)
- **Authors**: Guy Hadad, Haggai Roitman, Bracha Shapira
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.IR, cs.LG (submitted 2026-11-08; RecSys '26)
- **Abstract**: Generative recommenders represent items as semantic-ID token sequences. This work challenges fixed-codebook quantization assumptions by arguing that semantic IDs should behave as hierarchical paths where each token is conditioned on its prefix. The authors propose Adaptive Silhouette Tree (AST), a top-down divisive clustering method that dynamically chooses branching factors by maximizing silhouette coefficient, with constrained variants to preserve supervision for long-tail items.
- **Key innovations**:
  - **Prefix-conditioned semantic IDs**: aligns tokenization with the hierarchical path semantics used by generative recommenders.
  - **AST adaptive branching**: allocates finer splits in dense regions and compact groupings in homogeneous regions instead of fixed branching.
  - **Long-tail-aware constraints**: enforces minimum probability mass during splitting to improve supervision for rare items.
  - **Author-reported results**: significantly outperforms strong baselines on five Amazon Review datasets across varying sizes/domains.
- **arXiv link**: https://arxiv.org/abs/2611.11549

### 5. Proactive Dimension-Adaptive Denoising for Graph Collaborative Filtering via Representation Coherence
- **arXiv**: [2611.11801](https://arxiv.org/abs/2611.11801)
- **Authors**: Wenjun Li, Dong Zhao, Jiaying Shi, Juan Zhang, Zhaoming Pan, Zhimin Zhang
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.IR (submitted 2026-11-09)
- **Abstract**: Implicit feedback in recommender systems contains noisy interactions that contaminate graph-learned representations. Existing denoising methods often rely on training loss, a passive and confounded signal. Noise-aware Dimension Learning (NDL) introduces Representation Coherence Detection (RCD), which measures coherence between an interaction representation and a user's historical preference centroid, then fuses it with loss via activity-aware weighting and applies interaction-level dimension-adaptive masks.
- **Key innovations**:
  - **Representation Coherence Detection (RCD)**: proactive embedding-space noise signal independent of prediction loss.
  - **Activity-aware fusion**: emphasizes coherence for active users while falling back toward loss for cold-start users.
  - **Dimension-adaptive masking**: limits effective representation capacity for unreliable interactions during training without inference-time overhead.
  - **Author-reported results**: Recall@5 gains of **+17.95%** (Amazon-book), **+12.33%** (Yelp), and **+5.63%** (MovieLens-1M) over DAR.
- **arXiv link**: https://arxiv.org/abs/2611.11801

### 6. From Counterfactual Edits to Human Narratives: LLM-Driven Interpretations for Recommender System Explanations
- **arXiv**: [2611.13914](https://arxiv.org/abs/2611.13914)
- **Authors**: Vojtech Cahlik, Amir Reza Mohammadi, Rodrigo Alves, Pavel Kordik, Eva Zangerle
- **Institution/Company**: Not specified in arXiv metadata
- **Venue**: CIKM 2026 (Rome, Italy), pp. 6954-6959
- **Categories**: cs.AI, cs.IR (submitted 2026-11-10)
- **Abstract**: Counterfactual explanations for recommenders can identify which edits to a user's interaction history would change a recommendation, but raw edit lists are often long and hard to interpret. This paper uses LLMs as mediators that summarize counterfactual edit lists into concise natural-language narratives describing higher-level preference patterns. The mediators are optimized for correctness, informativeness, and linguistic quality, including Direct Preference Optimization (DPO), and evaluated with human-calibrated metrics on MovieLens-1M.
- **Key innovations**:
  - **Narrative mediation layer**: converts low-level counterfactual edits into user-facing preference explanations.
  - **Preference-optimized explanation generation**: applies DPO to improve semantic and linguistic explanation quality.
  - **Explanation-focused evaluation**: complements edit-count validity with human-calibrated correctness/informativeness/linguistic metrics.
  - **Author-reported findings**: high linguistic quality across settings; strongest semantic results with high-success CFX methods (e.g., ACCENT, SPINRec), and DPO improves semantic metrics in almost all evaluated settings.
- **arXiv link**: https://arxiv.org/abs/2611.13914

---

## D. LLMs and Agents

### 7. Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents
- **arXiv**: [2611.14320](https://arxiv.org/abs/2611.14320)
- **Authors**: Yukyeong Lee, Yumin Choi, Jinheon Baek, Sung Ju Hwang
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.AI, cs.MA (submitted 2026-11-10)
- **Abstract**: External memory can help LLM agents learn from past trajectories, but it can also cause memory-induced degradation when agents follow incorrect, misapplied, or misread lessons. WikiTrace addresses this by storing each lesson as a concise insight linked to a summary of why its source trajectory succeeded or failed and to the raw trajectory itself. At test time, agents can descend through these links to fill missing details or correct insights before acting.
- **Key innovations**:
  - **Evidence-linked memory**: pairs distilled lessons with trajectory summaries and raw evidence for verification.
  - **On-demand inspection**: agents inspect memory only when insights are underspecified, conflicting, or derived from failed tasks.
  - **Degradation-aware memory design**: targets failures introduced by memory itself rather than only memory recall quality.
  - **Author-reported results**: consistently outperforms existing memory approaches and a same-insight baseline on five agentic benchmarks while reducing memory-induced degradation.
- **arXiv link**: https://arxiv.org/abs/2611.14320

### 8. Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents
- **arXiv**: [2611.14493](https://arxiv.org/abs/2611.14493)
- **Authors**: Howard Zhang, Chuck Arvin, Logan Brown, Mihir Bhatia, Neelu Choudhary, Lily Miao
- **Institution/Company**: Not specified in arXiv metadata
- **Venue**: KDD 2026 (Jeju, Korea)
- **Categories**: cs.AI, cs.CL, cs.LG, cs.SE (submitted 2026-11-10)
- **Abstract**: Enterprise analytics agents require evaluation frameworks that can reliably detect failures in complex multi-tool workflows. This study compares three paradigms—trace-based LLM judging, text-only LLM judging with red-teaming, and deterministic heuristics—over frozen execution traces in a controlled setting. The analysis spans harness stability, detection of 72 ground-truth risks, and discovery of unknown risks.
- **Key innovations**:
  - **Three-phase evaluation methodology**: separates stability, known-risk detection, and unknown-risk discovery.
  - **Information-availability insight**: shows evaluation quality depends strongly on what the harness can observe (traces vs. text-only).
  - **Complementary functional/security testing**: functional and adversarial red-teaming uncover different failure classes.
  - **Author-reported results**: trace-based evaluation achieves best precision-recall balance (**F1=0.90**), text-only matches recall but yields ~5× more false alarms, and unknown-risk discovery finds 24 novel failures with zero overlap between functional testing and security red-teaming.
- **arXiv link**: https://arxiv.org/abs/2611.14493

---

## E. Games, Multi-Agent Interaction, and Strategic Reasoning

### 9. PARLEY: Evaluating LLM Collaboration Through Cooperative Asymmetric Puzzles
- **arXiv**: [2611.14242](https://arxiv.org/abs/2611.14242)
- **Authors**: Javier Hernandez, Andrew D. Wilson
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.MA (submitted 2026-11-10)
- **Abstract**: PARLEY is an extensible platform for studying LLM-agent collaboration through four asymmetric puzzle tasks grounded in cognitive psychology: referential communication, joint coordination, perspective-taking, and spatial reasoning. Across 400 GPT-4o agent-pair conversations, the authors analyze success/failure patterns and derive the PAC taxonomy (Perception, Adaptation, Coordination) with six failure types, then test a taxonomy-guided intervention.
- **Key innovations**:
  - **Asymmetric cooperative benchmark**: evaluates collaboration under partial/unequal information rather than single-agent task completion.
  - **PAC failure taxonomy**: organizes collaboration failures into perception, adaptation, and coordination categories from observed conversations.
  - **Intervention loop**: uses taxonomy-guided prompting/intervention to improve collaborative outcomes.
  - **Author-reported results**: 60.5% overall success (34–80% by task), failure to incorporate feedback strongly predicts unsuccessful collaboration, and intervention improves average success to **70.5%** in 200 additional runs.
- **arXiv link**: https://arxiv.org/abs/2611.14242

### 10. Steering Emergent Behavior in Multi-Agent LLM Systems via Information Networks
- **arXiv**: [2611.11714](https://arxiv.org/abs/2611.11714)
- **Authors**: Sepehr Ilami, Babak Heydari
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.MA, cs.AI, cs.GT, cs.SI (submitted 2026-11-09)
- **Abstract**: This paper treats the information network (who observes whom) as a controllable design object for multi-agent LLM systems, separate from the interaction network and fixed agent payoffs/messages. In 1,080 episodes across six repeated group-decision games with ten identical LLM agents, it studies how much peer information to share and how to allocate observation links under a fixed budget.
- **Key innovations**:
  - **Information-network control**: steers collective behavior by shaping observations rather than rewriting agent objectives or messages.
  - **Alignment-contingent disclosure**: shows more transparency can help when incentives align but amplify harmful behavior under free-riding/congestion.
  - **Topology-dependent effects**: at fixed budget, wiring matters most when coupling is harmful; modular "barbell" structures can entrench bad behavior.
  - **Author-reported results**: in a public-goods setting, the group performs best with no peer information, challenging default full-transparency assumptions for agent collectives.
- **arXiv link**: https://arxiv.org/abs/2611.11714

### 11. Ceci n'est pas une pipe — Toward a Symbolic Solver for the Abstraction and Reasoning Corpus Using Evolutionary Computation
- **arXiv**: [2611.13831](https://arxiv.org/abs/2611.13831)
- **Authors**: Luca Favole, Giorgio Mongardi, Giovanni Squillero, Alberto Tonda
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.AI (submitted 2026-11-10; ARC Prize 2026 Paper Track submission)
- **Abstract**: ARC/ARC-AGI evaluates few-shot abstraction and reasoning, a domain where symbolic, neural, and hybrid systems have been explored. This work presents a fully symbolic, evolutionary program-synthesis approach for ARC-AGI-2. It co-evolves the grid parser, output projector, and transformation program so that a task-specific language can emerge during synthesis, grounds extracted symbols in core knowledge concepts, and uses an object-aware fitness to reward partially correct outputs beyond pixel-level discrepancies.
- **Key innovations**:
  - **Co-evolved task-specific language**: jointly evolves parsing/projection/program components rather than fixing representation upfront.
  - **Cognitively grounded symbols**: anchors parser-extractable symbols in core knowledge theory from cognitive psychology.
  - **Object-aware fitness**: provides finer-grained credit assignment for partially correct ARC solutions than pure pixel matching.
  - **Author-reported contribution**: first fully symbolic evolutionary-based program synthesis approach submitted to the ARC-AGI-2 main contest (as stated by authors).
- **arXiv link**: https://arxiv.org/abs/2611.13831

---

## Notes

- **Coverage window**: At query time, the freshest clearly visible relevant submissions/announcements spanned roughly 2026-11-08 to 2026-11-11. Some papers from 2026-11-08/09 are included for topic completeness (sequential modeling, advertising, games/strategic interaction, recommendation) where 2026-11-12-only items were not yet broadly indexed.
- **Affiliations**: Many arXiv records do not expose structured affiliation fields in metadata; this report avoids guessing and marks unknowns explicitly. Company/product context is noted only when strongly implied by title/abstract (e.g., Taobao Shangou).
- **CTR note**: Direct "CTR prediction architecture" papers were less prominent in the visible window than adjacent ads/retrieval/ranking-serving work; TS-GEAR, CHO-Bench, and SeqFold are included for their direct relevance to CTR/ads ranking, ad retrieval, and sequential ranking systems.
- **Follow-up**: If desired, a second pass can extract affiliations from PDF author blocks and add more explicit CTR-prediction benchmarks or game-RL environment papers from the same window.
