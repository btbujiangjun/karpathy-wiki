---
title: arXiv AI Search Report — 2026-11-24
type: synthesis
created: 2026-11-24
updated: 2026-11-24
sources: [arxiv.org]
tags: [arxiv, search, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, multi-agent, e-commerce, agents, retrieval, ranking]
---

# arXiv AI Search Report — 2026-11-24

Query sweep via the arXiv API (`export.arxiv.org/api/query`, sorted by `submittedDate` desc) over six queries: `all:(LLM OR "large language model" OR "foundation model" OR GPT OR "sequence model")`; `all:(recommendation OR recommender OR CTR OR "click through rate" OR "sequential modeling" OR advertising OR "ad prediction")`; `all:(CTR OR "click through rate" OR "sequential recommendation" OR "session based recommendation" OR ads OR "ad ranking")`; `all:("game AI" OR "video game" OR "game recommendation" OR "game generation")`; `cat:cs.AI`; `all:(advertising OR "ad prediction" OR "ads prediction" OR RTB OR "real time bidding")`. Window: submissions 2026-11-03 → 2026-11-24 (today); 14 papers, all submitted within the last 21 days; organized by topic (Recommendation & Sequential Modeling, Advertising, CTR, Games, AI/LLM Agents & Infrastructure).

**Institution/Company lines are not listed in arXiv metadata.** Verified for the 14 selected papers: the arXiv Atom API and the arXiv abs pages expose author names only; institutional attribution would require fetching PDFs, and it is not repeated here.

**Key innovations** are derived from paper abstracts (PDFs not fetched; all metrics/claims are author-reported). Abstracts are verbatim from the Atom API.

---

## 1. Recommendation & Sequential Modeling

### 1.1 MADRec: Reliable Multi-Agent Reasoning with Evidence-Grounded Debate for Recommendation
- **arXiv:** [2611.28604v1](https://arxiv.org/abs/2611.28604v1) [cs.IR] — 21 Nov 2026
- **Authors:** Zunlong Liu, Weijie Feng, Jingzhi Li, Lei Zhu, Zhiyong Cheng, Meng Wang
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Large Language Models (LLMs) are transforming recommender systems from conventional preference matching toward reasoning-driven and explainable decision-making. Multi-agent collaboration further advances this paradigm by distributing recommendation reasoning across specialized agents. However, existing frameworks rarely assess the reliability of intermediate reasoning during collaboration, allowing erroneous judgments to propagate across agents and ultimately degrade recommendation quality. To address this issue, we propose Multi-Agent Debate-based Recommendation (MADRec), an evidence-grounded multi-agent framework that enhances the reliability of multi-agent recommendation reasoning. MADRec consists of three coordinated modules. First, the Multi-Agent Debate (MAD) module enables an Interaction Agent and a Semantic Agent to analyze interaction signals and content-level semantic signals from complementary perspectives, generating diverse recommendation judgments through structured debate. Second, the Evidence-Grounded Retrieval-Augmented Reasoning (EG-RAR) module grounds the Semantic Agent's reasoning in item-level evidence and refines candidate scores by assessing how well the evidence supports the corresponding semantic claims. Third, the Judge-based Ranking Calibration (JRC) module leverages debate-derived reliability cues to adaptively calibrate interaction-based and semantic ranking results for the final recommendation. Extensive experiments on three real-world datasets demonstrate that MADRec consistently outperforms competitive baselines and enhances the reliability of multi-agent recommendation reasoning.
- **Key innovations:**
  - Multi-Agent Debate (MAD): Interaction Agent + Semantic Agent analyze interaction signals and content-level semantic signals with structured debate, generating diverse recommendation judgments.
  - Evidence-Grounded Retrieval-Augmented Reasoning (EG-RAR): grounds the Semantic Agent in item-level evidence and refines candidate scores by assessing evidence–claim support.
  - Judge-based Ranking Calibration (JRC): adaptively calibrates interaction-based and semantic ranking results using debate-derived reliability cues.

### 1.2 Beyond Relevance: An Empirical Study of Multimodal LLMs for Diversity-Aware Recommendation Reranking
- **arXiv:** [2611.28379v1](https://arxiv.org/abs/2611.28379v1) [cs.IR] — 20 Nov 2026
- **Authors:** Chengkai Liu, Yan Fu, Huiyuan Chen, Sheikh Sarwar, Qilin Qi
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Large language models (LLMs) have emerged as promising rerankers for recommendation, yet most existing approaches rely on textual item descriptions and primarily focus on relevance. In visually oriented domains such as video streaming, item images provide complementary signals that may also inform recommendation diversity. This raises two questions: when does visual information improve recommendation quality, and can multimodal LLMs (MLLMs) enhance relevance and diversity simultaneously? We investigate these questions through a training-free, diversity-aware multimodal reranking framework that jointly incorporates item images, textual metadata, and user interaction histories. We conduct an empirical study across three public Amazon Review datasets and an industrial Amazon Prime Video dataset, using both open-source and proprietary MLLMs. Our results reveal substantial domain-dependent effects: adding visual information yields up to 121.9% relative improvement in NDCG@5 on Prime Video, while producing limited or inconsistent gains on product recommendation datasets. Furthermore, MLLM-based reranking improves both relevance and category-diversity-sensitive ranking quality over a sequential recommendation baseline, achieving up to 71.0% improvement in NDCG@5 and 14.1% in $\alpha$-NDCG@5 on Prime Video. These findings highlight the conditional value of visual information and the potential of training-free MLLMs for relevance- and diversity-aware recommendation reranking.
- **Key innovations:**
  - Training-free, diversity-aware multimodal reranking combining item images + textual metadata + user interaction histories (per-candidate scoring without model training).
  - Empirical study on 3 public Amazon Review datasets + industrial Amazon Prime Video; visual info gives up to 121.9% relative NDCG@5 gain on Prime Video.
  - MLLM reranking improves relevance and α-NDCG over sequential baselines (up to 71.0% NDCG@5, 14.1% α-NDCG@5 on Prime Video).

### 1.3 PROSPER: LLMs as Sparse Retrievers for First-Stage Product Search
- **arXiv:** [2611.28645v1](https://arxiv.org/abs/2611.28645v1) [cs.IR] — 21 Nov 2026
- **Authors:** Hongru Song, Yu-An Liu, Ruqing Zhang, Jiafeng Guo, Maarten de Rijke, Sen Li, Wenjun Peng, Fuyu Lv, Xueqi Cheng
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Product search is a crucial component of large-scale e-commerce platforms, where first-stage retrieval should achieve high recall while ensuring efficient online deployment. Sparse retrieval remains attractive for this setting due to its interpretability and deployability, yet it suffers from severe vocabulary mismatch challenges, especially for short queries and product titles. Large language models (LLMs) offer strong semantic capabilities, but directly applying them to sparse retrieval in product search introduces new challenges: (i) semantic expansion may distort critical literal signals such as brand names and model identifiers; and (ii) learning meaningful sparse representations is difficult in the high-dimensional vocabulary space induced by LLMs.To address these challenges, we propose PROSPER, a framework that uses LLMs as sparse retrievers for product search while explicitly preserving lexical fidelity. PROSPER combines (i) a literal residual network that alleviates lexical expansion hallucination by reinforcing underweighted literal terms through a residual compensation mechanism; and (ii) a lexical focusing window that uses top-k selection for rapid early sparsification and effective training initialization. Extensive offline evaluations and large-scale online A/B tests demonstrate that PROSPER consistently improves over existing sparse retrievers, and provides revenue gains for industrial hybrid retrieval systems.
- **Key innovations:**
  - LLM-based sparse retriever with a **literal residual network** that reinforces underweighted literal terms (brand names, model IDs) to counter semantic-expansion hallucination.
  - **Lexical focusing window**: top-k selection for rapid early sparsification and effective training initialization.
  - Offline evals + large-scale online A/B: improved over existing sparse retrievers, with revenue gains for industrial hybrid retrieval.

### 1.4 DCDN: Deep Cross-Division Network for Product-and-Ratio Feature Interactions in Industrial Ranking
- **arXiv:** [2611.27514v1](https://arxiv.org/abs/2611.27514v1) [cs.IR; cs.LG] — 20 Nov 2026
- **Authors:** Mikhail Trapeznikov, Sofia Gulevskaia, Maksim Utushkin, Aleksandr Poslavsky, Alexander D'yakonov
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Learning effective feature interactions is essential for industrial recommender systems. DCN and DCNv2 efficiently automate polynomial feature crossing. However, their cross layers construct interactions using only non-negative integer powers of the input features, with the maximum degree controlled by network depth. Consequently, they cannot directly represent the reciprocal terms required for ratios, rates, and normalized counts unless such features are explicitly provided as inputs. We introduce DCDN, a Deep Cross-Division Network that augments a DCNv2-style cross layer with a division branch. DCDN jointly learns product, ratio, and mixed product-ratio interactions. We characterize the representable interactions as multivariate Laurent polynomials and show that a $K$-layer DCDN generates Laurent monomials of $\ell_1$-order up to $K+1$, with signed degree between $-K$ and $K+1$. We evaluate DCDN against a production-optimized neural-ranking baseline built around DCNv2 and supplied with manually engineered ratio features. Replacing the DCNv2 block with DCDN allowed us to eliminate the entire class of manually engineered ratio features from the model input, reducing the number of input features by $40.1\%$. DCDN is deployed in the production ranking stack of a major short-video service. In a live A/B test on this service, DCDN increased likes by $3.25\%$, shares by $16.26\%$, total view time (TVT) by $0.33\%$, and clicks to open fullscreen by $0.38\%$; all changes were statistically significant. The number of shown videos decreased slightly ($-0.24\%$). These results demonstrate that DCDN can improve user engagement while eliminating reliance on manually engineered ratio features. Our code is publicly released at https://github.com/rw404/DCDN.
- **Key innovations:**
  - DCDN: DCNv2-style cross layer + **division branch** — jointly learns product, ratio, and mixed product-ratio interactions; representable space = multivariate Laurent polynomials (signed degrees $[-K, K+1]$ for a $K$-layer DCDN).
  - Eliminated 40.1% of manually engineered ratio features in production; live A/B: likes +3.25%, shares +16.26%, TVT +0.33%, fullscreen clicks +0.38% (all statistically significant).

---

## 2. Advertising

### 2.1 CutAgent: Creative-Gene-Driven Planning and Experience-Guided Self-Refinement for High-CTR E-commerce Advertising Video Creation
- **arXiv:** [2611.22418v1](https://arxiv.org/abs/2611.22418v1) [cs.CV] — 17 Nov 2026
- **Authors:** Xuyue Huang, Guanbo Huang, Jiasong Feng, Run Ling, Ao Ma, Xi Zhao, Yaoyu Li, Jie Gao, Ke Cao, Wei Feng, Zhanjie Zhang, Hao Wang, Jinghe Hu
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** E-commerce advertising video creation requires both high-level creative planning and reliable multi-modal production. However, existing methods often map product attributes directly to scripts or editing decisions without explicitly modeling advertising strategies, narrative structures, and production styles. They also have limited ability to reuse past production failures. To address these limitations, we propose CutAgent, a dual-agent framework that formulates advertising video creation as a Plan--Execute--Self-Evolve process. CutAgent comprises two collaborative agents, GeneAgent and VideoAgent, connected by a structured creative gene that bridges product understanding and video production. GeneAgent maps multi-modal product inputs---textual attributes together with product images---to creative genes that specify narrative units and production rules. To train GeneAgent, we construct CutAgent-70K with approximately 70K samples of product attributes/images, reverse-extracted creative genes, cleaned clip pools, and real-world CTR, and apply high-CTR supervised fine-tuning followed by CTR-guided GRPO. Guided by the generated gene, VideoAgent retrieves category-then-gene failure--correction experiences from a long-term memory as constraints for shot-script planning, then coordinates material retrieval, narration, subtitles, music, and timeline rendering. Independently, a reflection loop diagnoses quality defects, revises deficient production decisions, and writes verified corrections back to memory for later retrieval. Experiments on CutAgent-Eval show that CutAgent outperforms representative baselines in e-commerce advertising video creation, achieving the highest online CTR of 2.21%.
- **Key innovations:**
  - Dual-agent Plan–Execute–Self-Evolve framework: **GeneAgent** maps product attributes/images to "creative genes" (narrative units + production rules); **VideoAgent** retrieves failure–correction experiences from a long-term memory as shot-script constraints.
  - CutAgent-70K dataset (~70K product samples + real-world CTR) with SFT + CTR-guided GRPO training.
  - Live CTR of 2.21% on CutAgent-Eval (best among baselines).

### 2.2 Iterative Scarcity-Guided Exploration: Bootstrapping Generative Auto-bidding from Narrow Support
- **arXiv:** [2611.26060v1](https://arxiv.org/abs/2611.26060v1) [cs.LG] — 19 Nov 2026
- **Authors:** Qingmao Yao, Guangzheng Hu, Yusen Huo, Zhilin Zhang, Chuan Yu, Jian Xu, Xu Chu, Bo Zheng, Xiaotie Deng
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Auto-bidding is a core algorithmic component in online advertising auctions. In practical cold-start settings, iterative training is commonly used to compensate for low-quality, narrowly supported historical data. Unfortunately, in iterative training, representative diffusion-based AI-Generated Bidding (AIGB) methods fail to sustain extrapolation beyond the narrow data support and stagnate at a suboptimal level. In this paper, we theoretically attribute this stagnation to Signal-to-Noise Ratio (SNR) collapse: the weak radial return signal is overwhelmed by a curvature-induced penalty. To break this stagnation, we propose Iterative Scarcity-Guided Exploration (ISGE), which introduces a guidance handoff: as the return signal collapses, scarcity subsequently takes over as an exploratory signal to elevate the SNR above a critical threshold. Specifically, ISGE iteratively alternates between a Judger that assigns scarcity scores to trajectories and an Explorer that performs guided generation of high-scarcity and high-return trajectories, thereby bootstrapping from the narrow support with such self-generated trajectories. Extensive experiments on the industrial AuctionNet benchmark demonstrate that ISGE, starting from cold-start datasets, effectively surpasses the performance of the Full-Dataset baseline within three iterations. Code is available at https://github.com/alimama-tech/ISGE
- **Key innovations:**
  - Explains cold-start stagnation as **SNR collapse** (return signal overwhelmed by curvature-induced penalty) and designs a guidance handoff.
  - **Judger + Explorer alternation**: Judger assigns scarcity scores to trajectories; Explorer generates high-scarcity + high-return trajectories (bootstrapping from narrow support).
  - Outperforms the Full-Dataset baseline within 3 iterations on AuctionNet.

---

## 3. CTR & Sequential Modeling

### 3.1 X-split ARGUS: Learning Reusable History Tokens for Efficient CTR Prediction
- **arXiv:** [2611.24283v1](https://arxiv.org/abs/2611.24283v1) [cs.IR] — 18 Nov 2026
- **Authors:** Alexander Ploshkin, Nikita Stepanov, Alexey Pismenny, Viacheslav Ovchinnikov, Nikolay Savushkin
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Accurate click-through rate (CTR) prediction depends on user representations that capture both persistent preferences and recent intent, yet processing extensive behavioral histories for every ranking request is costly under production compute and latency constraints. We present X-split ARGUS, a framework for ad ranking whose history compressor and online ranker are trained end to end. The compressor encodes past interactions into a compact set of tokens that are computed offline and reused across candidates, while the online ranker scores ads through cross-attention to these tokens and representations of recent events. Training combines an autoregressive loss for click feedback with distillation of candidate-specific click logits from a larger teacher that scores each candidate using the uncompressed history. The number of compressed history tokens and the length of recent history can be adjusted to fit serving compute and latency budgets. Offline evaluation shows a 0.81% relative reduction in normalized entropy (NE) compared with the production baseline. Deployment in a large-scale real-time bidding system increases online inference cost by 15% relative to the production baseline. An online A/B test against this baseline yields relative gains of 4.65% in a business metric reflecting the monetary value of conversions generated for advertisers and 2.96% in clicks.
- **Key innovations:**
  - Offline history compressor produces reusable compact tokens shared across candidates (no per-request recompute of the full history).
  - Distillation from a larger teacher on uncompressed history + autoregressive click loss; compute/latency budget via token count and recent-history length.
  - Offline NE −0.81%; online A/B: +4.65% business value, +2.96% clicks (inference cost +15%).

---

## 4. Games & AI Agents

### 4.1 AutoPILOT: A Visual Agent Harness for Real-Time Gameplay
- **arXiv:** [2611.28202v1](https://arxiv.org/abs/2611.28202v1) [cs.AI] — 20 Nov 2026
- **Authors:** Mark Zhao, Pengcheng Wang, Rui Yang, Jiarui Yao, Xirui Jiang, Yuxi Chen, Bingxuan Li, Hanyang Chen, Ke Yang, Manling Li, Tong Zhang, Huan Zhang
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Multimodal foundation models can play video games well when the game waits for them, but often fail when it keeps running. We find that much of this gap lies in the harness, which decides what the model sees, what it remembers, and how its outputs become actions over time. Existing harnesses such as VISTA improve the first two, yet turn each model call into at most one action, so the agent acts only as often as its model thinks. We introduce AutoPILOT, which changes the third: in each model call, the model can send a primitive action, start an open-loop macro, or write a closed-loop controller that keeps playing from the screen without further model calls until it hands control back. To evaluate agents in real-time games, we build AFK-Bench, 120 diverse browser games grouped by how they respond to inaction and playable in real time or with the clock paused. With GPT-6.1 Sol under the same budgets, AutoPILOT reaches 68.6% real-time success against 38.3% for VISTA, and on GameWorld it keeps 80.0% in real time while VISTA drops from 84.1% to 42.9%. Its gains hold across models, and it reaches VISTA's final success rate at a fifth of its API cost. Our results suggest that how a harness turns model outputs into actions over time is a central yet underexplored part of agent design, and we hope AutoPILOT and AFK-Bench will serve as a foundation for agents in a world that does not wait.
- **Key innovations:**
  - AutoPILOT harness: in each model call, the model can send a primitive action, start an open-loop macro, or write a **closed-loop controller** that keeps playing until control is handed back — adapting to real-time games.
  - **AFK-Bench**: 120 diverse browser games grouped by inaction response; playable in real time or clock-paused for evaluation.
  - With GPT-6.1 Sol: AutoPILOT 68.6% real-time success vs VISTA 38.3%; reaches VISTA's final rate at 1/5 API cost.

### 4.2 CAMOPD: Conflict-Aware Multi-Teacher On-Policy Distillation in Aligned Action Spaces for Cross-Game Generalization
- **arXiv:** [2611.21094v1](https://arxiv.org/abs/2611.21094v1) [cs.AI] — 16 Nov 2026
- **Authors:** Jing Yi, Cehao Yang, Hualei Zhang, HTai Li
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Zero-shot cross-game generalization aims to consolidate accessible source-game experts into a single vision-language model (VLM) that controls unseen games from raw pixels without target-game parameter updates. While multi-teacher on-policy distillation (MOPD) mitigates offline exposure bias and single-game reinforcement learning (RL) overfitting, scaling it to autoregressive VLMs faces two bottlenecks. First, token-to-action misalignment from subword length bias distorts discrete action probabilities and uncertainty margins. Second, multi-teacher policy conflict arises as source teachers under incompatible dynamics issue contradictory closed-loop corrections, causing negative transfer. We propose CAMOPD (Conflict-Aware Multi-Teacher On-Policy Distillation), a post-training framework that resolves multi-teacher policy conflict within an aligned semantic action space. CAMOPD first uses complete-action alignment to normalize command completion likelihoods over each game's legal action set, forming a calibrated categorical policy that provides reliable uncertainty margins for selective on-policy retention and visual specialist probes that can be evaluated across source games. To resolve policy conflict without target-game data, conflict-aware multi-teacher consolidation cross-evaluates these specialists across source games to capture both visual identifiability and inter-teacher compatibility, upweighting compatible teachers while suppressing conflicting corrections. On GameWorld's temporal and directional transfer suites with Qwen3.5-4B, CAMOPD achieves 26/30 (86.7%) and 24/30 (80.0%) Task-1 zero-shot success on unseen GeoDash and Doodle Jump, outperforming prompting, weight-merging, and multi-task baselines.
- **Key innovations:**
  - **Complete-action alignment**: normalizes command completion likelihoods over each game's legal action set → calibrated categorical policies with uncertainty margins; enables selective on-policy retention + visual specialist probes.
  - **Conflict-aware multi-teacher consolidation**: cross-evaluates specialists across source games for visual identifiability + inter-teacher compatibility; upweights compatible, suppresses conflicting teachers (no target-game data needed).
  - Zero-shot results: 86.7% (GeoDash) and 80.0% (Doodle Jump) Task-1 on Qwen3.5-4B.

### 4.3 GameWM: Toward Next-Generation Video Games with Interaction-Centric World Models
- **arXiv:** [2611.19247v2](https://arxiv.org/abs/2611.19247v2) [cs.CV] — 14 Nov 2026
- **Authors:** Bing He, Runze Wang, Fei Zha, Zhongyuan Wu, Ke Xu, Tao Zhuang, Yuxuan Xie, Zhongyuan Liu
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** For more than half a century, video games have pursued better graphics, more natural interaction, and more engaging gameplay. Generative video models (VMs) now bear on all three. Neural networks already draw most of the pixels in shipped games, and recent world models let a lightweight game engine keep the world state while a VM turns the engine's coarse proxy video into final frames. These systems, however, treat the VM as a renderer that only restyles motion the engine has already authored, which leaves most of its generative capacity unused and limits the diversity a game can offer. We present GameWM, a design for next-generation games built on a clear division of labor. The GameWM-engine keeps what must be exact: rules, state, camera, and the layout of the world, which also spares the video model from having to remember it. The GameWM-VM generates what is expensive to author by hand: the look of the world and the detail of the player's interactions. One game mechanic can then be realized in many visually and physically distinct ways, while its outcome stays exactly as the engine computed it. To realize this division of labor, we build GameWM as a complete system: a data engine centered on interactions rather than exploration, an interface through which authored character sheets, scene art, and skill descriptions enter the model, and a model family from 5B to 33B parameters with a real-time causal variant for play. Together they give every player a fresh version of the same game: each player's own character, world, and skills turn the same engine mechanics into a new experience, while every event keeps the timing and outcome the GameWM-engine computed.
- **Key innovations:**
  - GameWM engine/VM division: engine keeps exact rules/state/camera/world layout; VM generates world look + player interaction details; outcomes stay engine-computed.
  - Interaction-centric data engine (per-interaction data rather than exploration-driven).
  - Model family 5B–33B + real-time causal variant; per-player personalization from authored character/scene/skill inputs.

### 4.4 ViCoR: Acting by Intent, Reacting by Sight: Visual Conditioned Reflexes for Real-Time VLM Agents
- **arXiv:** [2611.18723v1](https://arxiv.org/abs/2611.18723v1) [cs.CV; cs.AI] — 9 Nov 2026
- **Authors:** Qiancheng Zhou, Wenhua Zhang
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Vision-Language Models (VLMs) have shown strong capabilities as generalist agents that perceive, reason, and act in interactive environments. Yet real-time environments such as video games demand both deliberate control for exploration and split-second reactions to fast-moving hazards. Existing agents struggle to handle both: relying solely on direct VLM actions is too slow for sudden events, whereas delegating execution to fixed scripts leaves the agent blind at the moment of action, leading to frequent misfires whenever the scene shifts. Humans overcome this by pairing normal conscious control with conditioned reflexes-while the mind handles deliberate actions and shapes reflex rules, the reflex itself still relies on live vision to make the final instant decision. Emulating this mechanism, we propose ViCoR (Visual Conditioned Reflex). Alongside normal gameplay actions, the main VLM defines and updates lightweight situational guidance for recurring events, while a fast visual reflex branch (invoking the VLM in no-thinking mode) inspects live local views with motion cues to make the final sub-second action decisions. By offloading 67.8% of high-frequency reactions to the reflex branch (680 ms per check), ViCoR reduces average per-action decision latency by 2.6x (from 14.0 s to 5.4 s) and cuts token consumption by 36.9%. Across 17 diverse 2D and 3D games in the GameWorld benchmark, ViCoR achieves state-of-the-art performance, improving task success rate by +11.8% (from 52.9% to 64.7%) and average normalized progress by +13.9% (from 66.5% to 80.4%) over the strongest deliberative VLM and script baselines. In fast-paced real-time games, ViCoR refines its reflexes across episodes to boost progress by 1.67x, and even with a low-effort main planner, surpasses high-effort deliberative baselines by +8.1% at one-third of the token cost.
- **Key innovations:**
  - **Visual Conditioned Reflex (ViCoR)**: main VLM defines/updates lightweight situational guidance; fast reflex branch (VLM in no-thinking mode) inspects live local views to make sub-second decisions.
  - 67.8% of high-frequency reactions offloaded to the reflex branch (680 ms/check); per-action decision latency 2.6× lower (14.0s → 5.4s); token use −36.9%.
  - GameWorld: +11.8% task success, +13.9% normalized progress over deliberative baselines (52.9% → 64.7%; 66.5% → 80.4%).

### 4.5 From Game Generation to Game Playing: Fully Automated Ability Training for Vision-Language-Action Models
- **arXiv:** [2611.11136v2](https://arxiv.org/abs/2611.11136v2) [cs.CV] — 8 Nov 2026
- **Authors:** Changran Liu, Qi Wu, Wenchao Ma, Sharon X. Huang, Haomiao Jiang
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Training vision-language-action (VLA) models to follow gameplay instructions across diverse games is limited by the cost of collecting demonstrations. We introduce a framework that automatically generates game environments and expert demonstrations. An LLM-powered agent uses game-building tools to construct executable environments and tasks targeting specified skills. Programmatic experts then use privileged simulator state to generate aligned instructions, rendered observations, and keyboard and mouse actions. We train our game policy, Script2Play, by post-training a 4B vision-language model with behavior cloning on 150.3 hours of synthetic gameplay in Minecraft and Roblox, without human gameplay demonstrations or reinforcement learning. Evaluation on multiple public game benchmarks demonstrates that Script2Play follows gameplay instructions effectively and generalizes across game engines, highlighting the effectiveness of targeted synthetic supervision.
- **Key innovations:**
  - LLM agent uses game-building tools to generate executable environments + skill-targeted tasks; programmatic experts generate aligned instructions/observations/actions.
  - Trains Script2Play (4B VLA) via BC on 150.3 h of synthetic gameplay (Minecraft + Roblox) — no human demos, no RL.

### 4.6 Stack More Levels: How to Get General and Human-Like Mario Playing
- **arXiv:** [2611.16175v1](https://arxiv.org/abs/2611.16175v1) [cs.AI] — 12 Nov 2026
- **Authors:** Shinichi Arimura, Yuchen Li, Julian Togelius
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Super Mario Bros. is widely used in game AI and procedural content generation (PCG), yet it remains unclear whether a model-free agent can reliably win unseen levels. To address this question, we train Proximal Policy Optimization (PPO) agents on increasingly large sets of PCG-generated Mario levels and evaluate their generalization on 1000 held-out test levels. We then shape competent PPO policies into three gameplay archetypes---runner, killer, and collector. Finally, we fine-tune these PPO policies using Diffusion-Reward Adversarial Imitation Learning (DRAIL) with human gameplay demonstrations. We find that increasing the number of distinct PCG-generated training levels generally improves unseen-level performance, and that fine-tuning PPO policies with DRAIL increases action-level human-likeness while preserving much of the persona induced by PPO pretraining.
- **Key innovations:**
  - Increasing distinct PCG-generated training levels improves unseen-level generalization (PPO, 1000 held-out levels).
  - Gameplay archetypes (runner/killer/collector); DRAIL + human demos increases action-level human-likeness while preserving pretraining persona.

---

## 5. AI / LLM Agents & Infrastructure

### 5.1 MASSys: Benchmarking Multi-Agent Serving Substrates
- **arXiv:** [2611.28671v1](https://arxiv.org/abs/2611.28671v1) [cs.MA; cs.AI; cs.LG] — 21 Nov 2026
- **Authors:** Haoyuan Zheng, Dongting Li, Hancheng Ye, Qinsi Wang, Mingyuan Ma, Yuncheng Yao, Yifei Wang, Baijun Zhou, Zishan Shao, Tingjun Chen, Hai Helen Li, Danyang Zhuo, Yiran Chen
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Multi-agent systems (MAS) usually coordinate heterogeneous models and tools to solve complex tasks, creating a growing need for reliable evaluation. However, a multi-agent workflow that is fastest in one serving environment can lose its advantage in another, even when its models, prompts, and task remain fixed. This makes a benchmark result conditional on how the workflow is executed. We introduce MASSys, a benchmark for measuring this dependence in multi-agent large language model (LLM) systems. MASSys executes the same candidate-task pairs across serving substrates and load regimes, using five workload families spanning software repair, research synthesis, financial analysis, interactive control, and diagram generation. It records task quality alongside delivery, latency, cost, resource pressure, and failure evidence. In a controlled motivation diagnostic, the Star workflow falls from first to fourth in mean-latency rank under KV-cache pressure, while Chain rises from fourth to first. The substrate sweeps further show that increasing load creates long runtime tails and timeout pressure. In several task families, quality among evaluated outputs changes less than effective quality over submitted jobs: the system delivers fewer usable results even when the surviving outputs remain competitive. Tool and runtime traces reveal that these outcomes involve both model serving and non-model execution. Together, the results motivate evaluating MAS designs over explicit operating conditions and reporting which tasks are delivered, how well they are solved, and where execution breaks down.
- **Key innovations:**
  - **MASSys benchmark**: same candidate-task pairs executed across serving substrates and load regimes (5 workload families); records quality + delivery, latency, cost, resource pressure, failure evidence.
  - Motivation diagnostic shows Star workflow drops from 1st → 4th in mean-latency rank under KV-cache pressure while Chain rises 4th → 1st — i.e., results are substrate-dependent.
  - Motivates evaluating MAS designs over explicit operating conditions and reporting delivery/solve/breakdown per task.
