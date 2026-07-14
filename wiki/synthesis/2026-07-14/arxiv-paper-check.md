---
title: arXiv Paper Check — AI & CTR (July 14, 2026)
type: synthesis
created: 2026-07-14
updated: 2026-07-14
sources: [arxiv-cs.AI-2026-07-13, arxiv-cs.IR-2026-07-13]
tags: [arxiv, ai, ctr, recommendation, agents, llm, benchmarking]
---

# arXiv Paper Check — AI & CTR (July 14, 2026)

> Curated from arXiv new submissions on Monday, July 13, 2026 (cs.AI: 27 new, cs.IR: 2 new).  
> Selected for relevance to AI agents, LLM systems, recommendation/CTR, and evaluation.

## Summary

| Category | Papers Scanned | Selected |
|----------|----------------|----------|
| cs.AI | 27 | 7 |
| cs.IR | 2 (new) + 3 (cross-list) | 3 |
| **Total** | **32** | **10** |

## Key Themes

1. **Agent reliability & verification** — Multiple papers address making LLM agents more reliable through external control, verification, and memory.
2. **Benchmarking long-horizon tasks** — New benchmarks push evaluation beyond short, simple tasks to complex, multi-step workflows.
3. **Memory as critical bottleneck** — Shared selective persistent memory and KV-cache transfer highlight memory architecture challenges.
4. **Reward hacking in multimodal RL** — Systematic study of reward hacking when visual evidence is evaluated by weak rewards.
5. **Recommender systems evolution** — Shift from raw IDs to semantic planning; recommendation algorithms tested with LLM agent users.
6. **Explanation-prediction coupling** — Rashomon explanation set paradigm shows explanation fidelity can improve prediction accuracy.

## Selected Papers

### 1. CogniConsole: Externalizing Inference-Time Control as a Formal Abstraction for Reliable LLM Interactions

- **Authors:** Vanessa Figueiredo, Wilter Franceschi
- **arXiv:** 2607.08774
- **Key Contribution:** Introduces CogniConsole, an architectural framework that externalizes inference-time control into a structured interface. Through 489 controllability probes, shows that increasing structural scaffolding systematically reduces output variance and failure rates under fixed model architecture. Argues many observed failures arise from under-specified control rather than insufficient capability.

### 2. GATS: Graph-Augmented Tree Search with Layered World Models for Efficient Agent Planning

- **Authors:** Maureese Williams, Dymitr Nowicki
- **arXiv:** 2607.08894
- **Key Contribution:** Combines systematic UCB1-based tree search with a layered world model to eliminate LLM calls during inference while achieving superior planning performance. Achieves 100% success rate on synthetic planning tasks (vs. 92% for LATS, 64% for ReAct) and 100% on 12 challenging scenarios (vs. 88.9% for LATS, 23.9% for ReAct) with zero LLM calls per task.

### 3. Long-Horizon-Terminal-Bench: Testing the Limits of Agents on Long-Horizon Terminal Tasks with Dense Reward-Based Grading

- **Authors:** Zongxia Li, Zhongzhi Li, Yucheng Shi, et al.
- **arXiv:** 2607.08964
- **Key Contribution:** Introduces a terminal benchmark of 46 long-horizon tasks spanning nine categories (experiment reproduction, software engineering, multimodal analysis, interactive games, scientific computing). Each task decomposes into fine-grained graded subtasks enabling dense intermediate rewards. Evaluates 15 frontier models; even the strongest achieves only 15.2% pass@1 at partial-reward threshold of 0.95.

### 4. ProofCouncil: An LLM Agent for Solving Open Mathematical Problems

- **Authors:** Johannes Schmitt, Tim Gehrunger, Jasper Dekoninck, et al.
- **arXiv:** 2607.09474
- **Key Contribution:** Mathematical agent using author-critic architecture for open problems. Served as submission to FirstProof challenge; submissions for 6 of 10 problems judged correct up to minor revisions (best performance among participating teams). Released as open source.

### 5. Multimodal Reward Hacking in Reinforcement Learning

- **Authors:** Jiayu Yao, Yiwei Wang, Anmeng Zhang, et al.
- **arXiv:** 2607.09492
- **Key Contribution:** First systematic study of reward hacking in multimodal LLM RL. Outcome-only rewards cause severe hacking (48.1% Reward Hacking Rate). Introduces Newly Rewarded Failure Rate (NRFR) measuring failures among samples whose proxy reward improves over SFT baseline. Shows scaling reduces but does not eliminate hacking; answer-aware rewards improve oracle trend at every scale.

### 6. Shared Selective Persistent Memory for Agentic LLM Systems

- **Authors:** Sanjana Pedada, Aditya Dhavala, Neelraj Patil
- **arXiv:** 2607.09493
- **Key Contribution:** Architecture that identifies and retains four categories of reusable context (task specifications, data schemas, tool configurations, output constraints) while discarding session-specific reasoning traces. Achieves 96% task completion (vs. 79% without memory, 71% with full history). Zero-token refresh eliminates LLM re-invocation for recurring updates (14x task-time reduction).

### 7. Agora: Enhancing LLM Agent Reasoning Via Auction-Based Task Allocation

- **Authors:** Kaiji Zhou, Ales Leonardis, Yue Feng
- **arXiv:** 2607.09600
- **Key Contribution:** Introduces incentive-compatible auction mechanism for dynamically allocating tasks to expert models and tools. Treats reasoning steps as tradeable items; agents bid based on rectified competence ensuring critical logic is routed to most capable solver. Improves over matched single-model, routing, and cascade baselines across five benchmarks.

### 8. From Raw IDs to Semantic Planning: How Recommender Systems Utilize Information at Scale

- **Authors:** Changhong Jin, Shiqiu Yang, Roger Zhe Li, et al.
- **arXiv:** 2607.09540
- **Key Contribution:** Examines evolution of recommender systems from raw IDs to semantic IDs and proposes semantic planning as future direction. Argues shift reflects broader evolution in how recommender systems utilize information under industrial-scale constraints. System first predicts semantic target of next exposure, then instantiates as specific item or generated creative.

### 9. Do Recommendation Algorithms Work When Users Are LLM Agents? A Case Study on Moltbook

- **Authors:** Daming Li, Simeng Han, Jialu Zhang
- **arXiv:** 2606.29762 (replacement)
- **Key Contribution:** Studies recommendation for LLM agents on Moltbook, a large-scale social media platform exclusively for autonomous AI agents. Finds simple popularity-based rules or item-side collaborative filtering outperform techniques that explicitly learn user representation. Static agent persona descriptions fail to add value. Suggests recommendation depends more on platform/item structural signals than user-specific personalization.

### 10. All Explanations are Wrong, But Many Are Useful: Exploring the Rashomon Explanation Set with Large Language Models

- **Authors:** Pan Li
- **arXiv:** 2607.09502 (cross-list from cs.LG)
- **Key Contribution:** Introduces Rashomon Explanation paradigm building a set of faithful, prediction-guiding explanations rather than single one. Proposes RashomonLLM agentic workflow generating explanations by iteratively aligning them with predictions. Across customer-churn classification, clinical survival regression, and industrial click-through prediction on large-scale live-streaming logs, significantly outperforms SOTA prediction and XAI baselines on both accuracy and explanation quality.

## CTR-Specific Highlights

| Paper | Key Insight | Potential Impact |
|-------|-------------|------------------|
| All Explanations are Wrong (2607.09502) | Rashomon explanation set for click-through prediction | Couples explanation fidelity with prediction accuracy; tested on live-streaming logs |
| From Raw IDs to Semantic Planning (2607.09540) | Semantic planning as future direction for rec systems | Shifts paradigm from item retrieval to semantic target prediction |
| Do Rec Algos Work for LLM Agents? (2606.29762) | Structural signals dominate for agent users | Implications for recommendation as agents increasingly populate platforms |

## Safety & Verification Highlights

- **Scoped Verification for Long-Horizon Agentic Context** (2607.09175): GRACE maintains persistent instruction as typed semantic graph, improving reliability from 0.091 to 0.673 under distribution shift.
- **Neuro-Agentic Control** (2607.09076): Couples LLM planner with Time-Series Foundation Model for physics-grounded autonomous defense; zero hallucinated actions executed.
- **TrustX Agent Risk Classification Framework** (2607.09586): 12-dimension scoring rubric for agentic AI systems producing three-tier governance output.
