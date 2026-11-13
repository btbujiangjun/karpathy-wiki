---
title: "arXiv AI Search — Recent Papers (2026-11-13)"
type: synthesis
created: 2026-11-13
updated: 2026-11-13
sources:
  - https://arxiv.org/list/cs.CL/recent
  - https://arxiv.org/list/cs.LG/recent
  - https://arxiv.org/list/cs.AI/recent
  - https://arxiv.org/list/cs.IR/recent
  - https://export.arxiv.org/api/query
tags: [arxiv, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, agents, retrieval, post-training]
---

# arXiv AI Search — Recent Papers (2026-11-13)

Curated recent arXiv submissions (Nov 5–11, 2026) across AI, LLMs, recommendation, advertising, sequential modeling, CTR/ranking, and games/agents. Data collected via arXiv API and recent listing pages on 2026-11-13. Affiliations are reported as listed in arXiv metadata when available; many submissions do not expose structured affiliations in the Atom feed.

## 1. LLMs & AI

### 1.1 SpecCTMC: Exact Speculative Simulation of Diffusion Language Model Continuous-Time Markov Chains
- **Authors:** Siva Rajesh Kasa, Yasong Dai, Sumit Negi, Hongdong Li
- **Institution/Company:** Not specified in arXiv metadata
- **Abstract:** Masked diffusion language models offer parallel text generation, but independently sampling multiple tokens can disrupt their dependencies and change the output distribution. Exact continuous-time sampling avoids this approximation, yet typically requires one sequential model evaluation per token. SpecCTMC is a training-free speculative sampler that reduces this sequential bottleneck without a separate draft model. It proposes successive token updates using previously computed model predictions, evaluates intermediate states in parallel, and applies an exact acceptance-and-correction procedure. The method preserves the joint distribution of event times, generation order, and token values of the underlying continuous-time Markov chain, introducing neither time-discretization error nor additional factorization error from parallel decoding. Experiments on LLaDA-8B-Instruct and Dream-v0-Instruct-7B across five benchmarks demonstrate 1.73-4.38x fewer sequential model evaluations than direct continuous-time sampling while preserving the reference sampling distribution.
- **Key innovations:**
  - Training-free speculative sampling for diffusion language models without a separate draft model.
  - Exact acceptance-and-correction procedure that preserves the CTMC joint distribution (event times, generation order, token values).
  - Parallel evaluation of proposed intermediate states to cut sequential model calls while maintaining sampling fidelity.
- **arXiv:** https://arxiv.org/abs/2611.08362

### 1.2 AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models
- **Authors:** Zijian Zhang, Rizhen Hu, Jiangweizhi Peng, Shiyang Li, Sujay Bhatt, Sihan Zeng, Mingyi Hong
- **Institution/Company:** Not specified in arXiv metadata
- **Abstract:** Reinforcement learning with verifiable rewards (RLVR) produces rich training experience, but outcome rewards compress each attempt into a single scalar and leave much information unused. AutoScaffold is an AI-for-AI framework that turns a student's training experience into adaptive scaffolds with minimal domain-specific information and no human intervention during training. A frozen teacher periodically examines experience, diagnoses bottlenecks, and designs scaffolds in two forms: strategies shared across task classes and hints for individual hard tasks, adjusting support as the student learns. Scaffolds are removed at evaluation. Across ALFWorld, search-based QA, mathematical reasoning, and GPU kernel generation, students trained with AutoScaffold outperform corresponding RL baselines when evaluated without scaffolds.
- **Key innovations:**
  - Adaptive teacher-generated training scaffolds (shared strategies + per-task hints) derived automatically from RLVR experience.
  - Domain-general framework requiring minimal domain-specific design and no human intervention during training.
  - Demonstrated transfer of scaffold-induced gains to scaffold-free evaluation across reasoning, agentic, QA, and code-generation tasks.
- **arXiv:** https://arxiv.org/abs/2611.14515

### 1.3 A Theory of Policy Optimization in Post-Training: Coverage Collapse and Reference Resets
- **Authors:** Audrey Huang, Nan Jiang, Sham M. Kakade, Sadhika Malladi, Akshay Krishnamurthy, Dylan J. Foster
- **Institution/Company:** Not specified in arXiv metadata
- **Abstract:** This paper revisits the theoretical foundations of policy optimization for LLM post-training, focusing on coverage-preserving algorithms whose sample and gradient complexity scale with the base model's ability to sample optimal responses. It shows that REINFORCE-style methods underlying PPO and GRPO can suffer coverage collapse, driving the probability of optimal responses toward zero even as reward improves, which can stall optimization. The authors propose repeated KL reference resets and formalize them in Approximate Policy Mirror Descent (APMD), a meta-algorithm solving a sequence of KL-regularized RL subproblems. For softmax linear policies over pretrained features, APMD yields global convergence guarantees and coverage-preservation results for stylized post-training algorithm families, including PPO/GRPO variants and squared-loss formulations.
- **Key innovations:**
  - Formal analysis of coverage collapse in REINFORCE/PPO/GRPO-style post-training, including under KL regularization to the base model.
  - Reference-reset mechanism and APMD meta-algorithm balancing strong regularization with convergence to global optimality.
  - Coverage-preserving theoretical guarantees connecting regularization, clipping, and objective choice to sampling/optimization costs.
- **arXiv:** https://arxiv.org/abs/2611.14467

### 1.4 Continual-ARC: Measuring Skill Acquisition over a Working Lifetime
- **Authors:** Daniel Lenton
- **Institution/Company:** Not specified in arXiv metadata
- **Abstract:** Continual-ARC is a lifelong benchmark stream built from the three ARC-AGI editions to measure skill acquisition without domain knowledge. Tasks recur after dormant gaps with fresh instances while new tasks continue to arrive. Learners can spend a feedback budget on demonstrations, submissions, and harness actions, with retries on incorrect submissions; scoring is based on budget share consumed. Because learners may retain anything between instances, memory-based and weight-based systems are compared on the same scale. After the stream, learners are frozen and tested on fresh instances of seen tasks (memorization) and unseen tasks (generalization). Experiments compare agent harnesses with and without persistence, prompting floors, program induction, and weight imitation, highlighting gaps between harness persistence and true continual skill acquisition.
- **Key innovations:**
  - Lifelong, recurring-task evaluation protocol enabling fair comparison of memory-based and weight-based continual learners.
  - Budget-aware scoring that accounts for demonstrations, actions, and retries rather than only final accuracy.
  - Empirical separation of memorization vs. generalization, showing limited gains from naive harness persistence and stronger gains from weight-based learning.
- **arXiv:** https://arxiv.org/abs/2611.14505

## 2. Recommendation Systems

### 2.1 When Does a Recommendation Spark Curiosity? Theory, Measurement, and Field Evidence
- **Authors:** Pan Li, Alexander Tuzhilin
- **Institution/Company:** Not specified in arXiv metadata
- **Abstract:** This work formalizes the information-gap theory of curiosity into five axioms and derives a computational measure of the curiosity evoked by a recommended item. The measure is validated through a survey study showing alignment with consumers' self-reported curiosity and superiority over proxy metrics. The authors build a curiosity-aware recommender system by incorporating the measure into utility design and demonstrate offline improvements on three real-world datasets. A large-scale online controlled experiment at a major video-streaming platform in Asia shows significant gains in click-through rate, video views, and time spent over the production system, with deployment reported in production.
- **Key innovations:**
  - Axiomatic, computational formulation of curiosity grounded in information-gap theory for recommender systems.
  - Empirical validation against human self-reports and integration into recommendation utility optimization.
  - End-to-end evidence from offline benchmarks and large-scale online A/B testing with production deployment impact.
- **arXiv:** https://arxiv.org/abs/2611.14938

### 2.2 ShopMind: A Mental World Model for Personalized and Realistic E-commerce User Simulation
- **Authors:** Peixuan Hou, Bin Chen, Li He, Jian Xu, Xiuli Ma, Guojie Song
- **Institution/Company:** Not specified in arXiv metadata
- **Abstract:** ShopMind is a mental world model for e-commerce user simulation that explicitly models how consumers interpret shopping information and how mental states (beliefs, uncertainties, intentions) evolve through interaction. Instead of directly predicting next actions from history and context, it captures latent mental dynamics to improve personalization and behavioral realism. Behavior-mental state pairs synthesized by ShopMind are used to train a Mental State Reconstruction (MSR) model that infers latent mental states from observable behavior. Experiments report improvements in personalization and behavioral realism over strong alternatives, and downstream gains in consumption value measurement and CTR prediction.
- **Key innovations:**
  - Theory-of-Mind-inspired mental state modeling for user simulation beyond direct next-action prediction.
  - Synthetic behavior-mental state supervision enabling a reconstruction model for latent user states.
  - Demonstrated utility for downstream e-commerce tasks including CTR prediction and consumption value measurement.
- **arXiv:** https://arxiv.org/abs/2611.11897

### 2.3 LUMIR: Decoupled Multimodal Representation Learning from Heterogeneous Data for Next-POI Recommendation
- **Authors:** Zehui Wang, Wolfram Höpken, Dietmar Jannach
- **Institution/Company:** Not specified in arXiv metadata
- **Abstract:** LUMIR addresses multimodal next-POI recommendation by decoupling representation learning from downstream model optimization. Heterogeneous multimodal tourism information is semantically unified into a shared textual representation space using large language models. An interaction-aware fusion mechanism models cross-modal interactions, while sequential signals provide structural constraints during representation learning. Evaluations across multiple sequential recommendation backbones show consistent improvements over multimodal fusion baselines on accuracy-oriented and beyond-accuracy metrics.
- **Key innovations:**
  - Decoupled, reusable multimodal representation learning framework for sequential recommendation.
  - LLM-based semantic unification of heterogeneous modalities into a shared textual space.
  - Interaction-aware fusion guided by sequential structure, improving generality across downstream backbones.
- **arXiv:** https://arxiv.org/abs/2611.14004

## 3. Advertising, CTR & Sequential Modeling

### 3.1 Query- and Candidate-Aware Long User Sequence Modeling for Sponsored Product Ranking in Search
- **Authors:** Dongyue Xie, Sergey Kolbin, Manavender Malgireddy, Iurii Shcherbak, Weixing Tang, Arushi Jain, Wanchen Shao, Kurt Zimmer, Raja Hafiz Affandi, Matt Lindsay
- **Institution/Company:** Not specified in arXiv metadata (production sponsored-product search context reported)
- **Abstract:** This paper presents a production sequence framework for sponsored-product ranking in search, where current query intent and candidate products jointly determine which parts of long-term user history are relevant. The method augments recent behavior with two retrieval channels over long-term history: candidate-nearest-neighbor retrieval and query-nearest-neighbor retrieval. Selected actions are encoded with dedicated query and candidate context tokens, and candidate-aware early fusion injects candidate information into every history token. Offline ablations show gains over a production baseline, and an online A/B test on sponsored-product search traffic increased CTR, attributed conversion rate, and orders per impression.
- **Key innovations:**
  - Dual long-history retrieval (query-aware + candidate-aware) tailored to sponsored search ranking.
  - Candidate-aware early fusion and explicit query/candidate context tokens for relevance-sensitive sequence encoding.
  - Validated production impact with offline improvements and online lifts in CTR and conversion-related metrics.
- **arXiv:** https://arxiv.org/abs/2611.11675

### 3.2 TS-GEAR: Taobao Shangou GEnerative Ad Retrieval
- **Authors:** Guofeng Tong, Xu Zhang, Guangliang Yu, Haiqiang Wang, Guannan Cong, Xing Guo, Yang Zhou, Jingjing Duan, Shuang Li, Feng Shi, Hualei Liu
- **Institution/Company:** Taobao Shangou / Alibaba ecosystem (inferred from title and reported deployment in Taobao Shangou search advertising; individual affiliations not specified in arXiv metadata)
- **Abstract:** TS-GEAR is a generative retrieval framework for on-demand delivery advertising, where merchants outside the delivery range are invalid rather than merely low-ranked. It addresses three challenges: encoding geographic reachability in generation, conditioning behavior aggregation on real-time query and location, and optimizing for set-level retrieval value under autoregressive training. The framework introduces Geo-Semantic IDs (geographic prefix + semantic suffix), Query-Geo Target Attention for location/query-conditioned history aggregation, and GMPO for group/marginal advantage optimization with deduplicated rewards. Deployed with a lightweight 0.1B backbone serving over 150 million queries per day, it reports gains in HitRate, geographic validity, ad impressions (+3.8%), and ad revenue (+4.2%).
- **Key innovations:**
  - Geo-Semantic ID design that makes geographic reachability a first-class prediction target in generative retrieval.
  - Query- and geo-conditioned target attention for real-time, location-aware user interest modeling.
  - Set-aware policy optimization (GMPO) reducing redundant candidates and improving collective retrieval value at production scale.
- **arXiv:** https://arxiv.org/abs/2611.12180

### 3.3 CHO-Bench: How Do Context Hints Affect Ad Rankings in LLM Advertising?
- **Authors:** Shiqi Zhang, Yang Fei, Xiaokui Xiao
- **Institution/Company:** Not specified in arXiv metadata
- **Abstract:** This paper studies ad-side ranking optimization in LLM advertising, where ads are ranked from user conversations and advertisers can provide natural-language context hints (what/who/when). It formulates Context Hint Optimization (CHO) as constructing hints to improve ad ranking under a budget. The authors propose seven hint-generation strategies derived from marketing frameworks plus a unified strategy, and introduce CHO-Bench with over 1.19 million paired evaluations across five datasets using embedding-based and LLM-based rankers. Results show context hints improve rankings, with strategy effectiveness varying by ranker type and diminishing returns as hint budget increases.
- **Key innovations:**
  - Formalization of Context Hint Optimization (CHO) for LLM-native advertising ranking.
  - CHO-Bench benchmark enabling large-scale, paired evaluation of hint strategies across datasets and ranker families.
  - Empirical insights on strategy-ranker interactions and budget-aware diminishing returns for ad context hints.
- **arXiv:** https://arxiv.org/abs/2611.11955

### 3.4 DynamAuction: A Reinforcement Learning Environment for Repeated Auctions with Dynamic Value
- **Authors:** Eugénie Patard, Corentin Pla, Benjamin Heymann, Patrick Loiseau
- **Institution/Company:** Not specified in arXiv metadata
- **Abstract:** DynamAuction is a synthetic environment for single-buyer sequential bidding in repeated auctions where item value depends on past wins through a carry-over state. It targets the planning problem often neglected in repeated-auction learning formulations that treat opportunities as contextual bandits. The environment supports first- and second-price auctions, non-homogeneous Poisson arrivals, delayed feedback, saturation, and recency effects. The authors also introduce Model Predictive Control (MPC) algorithms that outperform off-the-shelf deep RL baselines (PPO, SAC, TD3) and a tuned shading baseline on the benchmark scenario.
- **Key innovations:**
  - Environment explicitly modeling dynamic, history-dependent value/carry-over effects in repeated auctions.
  - Rich auction simulation features (pricing rules, arrivals, delayed feedback, saturation/recency) for realistic bidding research.
  - MPC-based bidding policies demonstrating advantages over standard deep RL and shading baselines.
- **arXiv:** https://arxiv.org/abs/2611.14000

## 4. Games & Interactive Agents

### 4.1 Re-Search: Dissecting LLM Ideation Through a Two-Player Questioning Game
- **Authors:** Muhan Gao, Hangxiao Zhu, Xinqi Su, Yu Zhang, Daniel Khashabi, Kuan-Hao Huang
- **Institution/Company:** Not specified in arXiv metadata
- **Abstract:** Re-Search adapts Twenty Questions to research ideation: given only a published paper's research problem, a model must rediscover the core idea by asking yes-or-no questions. Built from 200 ICML 2026 papers, it tracks idea evolution under binary oracle feedback to isolate ideation from execution. Across six recent LLMs, most progress occurs within the first ~30 of 100 questions, after which performance often plateaus. Controlled interventions indicate the main bottleneck is generation rather than judgment: models can recognize good ideas/questions when offered but struggle to produce them. Trace analyses show failures from over-exploitation or over-exploration.
- **Key innovations:**
  - Interactive, game-like evaluation protocol for iterative LLM ideation/search behavior.
  - Process-level tracing of hypothesis evolution under constrained questioning and binary feedback.
  - Diagnostic separation of generation vs. judgment bottlenecks with implications for auto-research system design.
- **arXiv:** https://arxiv.org/abs/2611.14487

### 4.2 Test-Time Self-Play: Scaling without a Verifier
- **Authors:** Akira Yoshiyama, Akmal Ashirmatov, Jonas Hübotter, Ido Hakimi, Andreas Krause
- **Institution/Company:** Not specified in arXiv metadata
- **Abstract:** Test-time scaling methods typically rely on a verifier to score or select candidate solutions, but strong verifiers may be unavailable at deployment. Test-Time Self-Play (TTSP) performs test-time scaling via asymmetric self-play without requiring a verifier. On a difficulty-calibrated subset of LiveCodeBench v6, TTSP outperforms baselines across evaluated verifier-strength settings, with the gap widening as verifier quality decreases. In the no-verifier limit, TTSP achieves a reported 35% absolute improvement in mean@8, with gains holding broadly except when base policy coverage of correct answers is near zero.
- **Key innovations:**
  - Verifier-free test-time scaling through asymmetric self-play.
  - Robust performance across verifier-strength regimes, especially in weak/no-verifier settings.
  - Strong empirical gains on coding benchmarks demonstrating practical self-play at inference time.
- **arXiv:** https://arxiv.org/abs/2611.07367

### 4.3 Optimal Learning in Games with Arbitrary Delays: Best-of-Both-Worlds for Self-Play and Adversarial Opponents
- **Authors:** Emmanuel Esposito, Andrew Jacobsen, Hao Qiu, Alexander Ryabchenko, Mengxiao Zhang
- **Institution/Company:** Not specified in arXiv metadata
- **Abstract:** This paper studies learning in zero-sum games with delayed feedback and introduces Multi-Anchor Optimistic Online Mirror Descent (MAO-OMD). The algorithm achieves fast rates in self-play on smooth games while maintaining minimax-optimal guarantees against arbitrary opponents under unknown and arbitrary feedback delays. In smooth zero-sum self-play, it obtains $O(\sigma_{\max}+1)$ social and individual regrets, where $\sigma_{\max}$ is the maximum number of outstanding gradients, and $O(\sqrt{T+d_{\mathrm{tot}}})$ individual regret against arbitrary opponents. The authors show these guarantees cannot be obtained simultaneously via standard black-box reductions to undelayed settings and extend results to multi-player and player-dependent delay settings.
- **Key innovations:**
  - MAO-OMD algorithm achieving best-of-both-worlds guarantees under delayed feedback in games.
  - Tight regret bounds for self-play and adversarial opponents without relying on black-box delay reductions.
  - Extensions to multi-player games and heterogeneous/player-dependent delay sequences.
- **arXiv:** https://arxiv.org/abs/2611.07773

## Notes
- **Date scope:** Emphasis on recent submissions from 2026-11-05 to 2026-11-11 (retrieved 2026-11-13).
- **Affiliations:** arXiv Atom metadata often omits structured author affiliations; entries above state "Not specified in arXiv metadata" unless clearly inferable from the paper context.
- **Key innovations:** Summarized from titles/abstracts and listed comments; consult linked papers for full methodological and experimental details.
