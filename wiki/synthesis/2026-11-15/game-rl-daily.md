# Game RL & Game AI Bot — Daily Paper Digest (2026-11-15)

- **Date**: 2026-11-15
- **Window**: ~2026-08-27 → 2026-11-11 (recent arXiv submissions/revisions and identified proceedings/workshop venues available at query time)
- **Scope**: Game RL (classic and modern game environments), multi-agent/self-play and strategic learning, LLM/VLM-powered game agents and NPC intelligence, game foundation/world models and generalist action learning, procedural/content and environment generation for games, game/agent benchmarks, and industry/game-application AI systems.
- **Method note**: Discovery used arXiv Export API queries via `curl`/`webfetch` on 2026-11-15; `websearch` was unavailable in this run, so recent non-arXiv proceedings coverage is limited to venue/status metadata exposed on arXiv pages. Paper metadata, abstracts, venues, affiliations, and reported results below are taken from fetched arXiv abstract pages and are **author-reported** unless otherwise noted. Where affiliations are not explicitly listed in arXiv metadata, this is stated. Papers already covered in recent game-rl digests (`2026-11-10/11/12/13`) and overlapping 2026-11-15 syntheses (e.g. `arxiv-ai-search` entries such as 2611.16175 and 2611.16981) were intentionally excluded.

## Executive Summary

This window highlights a shift from single-task game policies toward **shared representations, reusable skills, and diagnosable agent systems**. On the world-model side, CoCode-World (2611.15602) coordinates two-player generation with shared 3D proxies in GTA V, while OnlyAct (2611.14420) extracts action representations from pretrained V-JEPA 2 features to improve scene-invariant action-conditioned world modeling across robot, camera, game, and driving domains. For generalist gameplay, AceAction-5M (2611.04241) contributes hierarchical goal-structured human gameplay data across 3D games for VLA/action learning. LLM game-agent work spans both systems and measurement: a systematic mapping study of LLM-based NPCs (2611.05427, IEEE Transactions on Games Early Access) quantifies adoption/latency/safety/reproducibility gaps, while applied systems explore LLM-guided runtime strategy selection in multi-agent combat (2609.02931), diagnosis-guided post-training for small dialogue-game agents (2608.28458, LM Playschool Workshop @ EMNLP 2026), and real-time esports directing/commentary with a single streaming VLM (2610.31734). In competitive and benchmark settings, Faynt (2610.02144) scales and post-trains Transformer policies for Super Smash Bros. Melee, SpeedrunBench (2610.08076) probes long-horizon strategy formation in video-game speedrunning, and Inner-Learning (2610.38304) turns hand-coded Skat beliefs into declarative/cardinality-aware knowledge improved through self-play. Related self-play analysis (2610.37988) cautions that engine opening rankings from limited samples can overstate certainty.

---

## 1) Game Foundation Models, World Models, and Generalist Action Learning

### CoCode-World: Shared 3D Proxy Representation for Multi-Player World Models
- **Authors**: Qirui Li, Xin Zhang, Yabo Chen, Jinkun Hao, Paul L. Rosin, Yu-Kun Lai, Haibin Huang, Yin Chen, Ran Yi, Chi Zhang
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue/conference**: arXiv preprint
- **Date**: 2026-11-11 (v1)
- **Abstract**: Multiplayer generative world models must produce observations that agree on shared entities despite different camera motions and occlusions. CoCode-World proposes a shared 3D proxy framework separating structural control from visual synthesis for two-player video generation. Programmable proxies specify scene layout, motion, and occlusion, while RGB references guide character and scene appearance. Paired proxy videos, appearance references, and target views are concatenated in a consistent spatial layout and generated jointly with a pretrained video model using native attention for cross-view communication and LoRA adaptation for proxy adherence and appearance correspondence.
- **Key innovations**:
  - Shared 3D programmable proxy representation for multi-player spatial consistency and controllability.
  - Joint two-view generation that leverages pretrained video-model attention for cross-view coordination instead of a separate synchronization module.
  - Two-player GTA V dataset pairing synchronized RGB observations with proxy videos derived from shared map geometry and game-engine state.
  - Reports improved video quality and cross-view player identity over the evaluated baseline, with appearance transfer to characters/scenes unseen during training (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2611.15602) | [PDF](https://arxiv.org/pdf/2611.15602) | [Project](https://iapple233.github.io/CCW/)

### OnlyAct: Extracting Action Representations from Foundation Models for World Models
- **Authors**: Runjia Li, Minghao Chen, Junyu Xie, Philip Torr, Andrea Vedaldi, Tomas Jakab
- **Affiliation**: Not explicitly listed in arXiv metadata (authors are publicly associated with University of Oxford contexts; verify full affiliations from PDF)
- **Venue/conference**: arXiv preprint
- **Date**: 2026-11-10 (v1)
- **Abstract**: Video world models are limited by scarce and fragmented action supervision. Instead of learning latent actions from scratch with a reconstruction bottleneck, OnlyAct starts from pretrained V-JEPA 2 frame-pair embeddings that already contain action information and uses label-free contrastive adaptation to keep action content while discarding scene information.
- **Key innovations**:
  - Foundation-model-first action extraction: repurposes V-JEPA 2 embeddings rather than training an action encoder from scratch.
  - Contrastive objective pulls together frame pairs with the same motion under different scenes and pushes apart same-scene/different-motion pairs, avoiding reconstruction bottleneck trade-offs.
  - Unified evaluation across action expressiveness, scene invariance, and action-conditioned video generation quality on robot manipulation, camera navigation, game, and driving benchmarks (many unseen during adaptation).
  - Reports substantially more expressive representations than annotation-free latent-action methods with comparable scene invariance and more faithful transfer of demonstrated actions to new scenes (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2611.14420) | [PDF](https://arxiv.org/pdf/2611.14420)

### AceAction-5M: Hierarchical Goals for Generalist Action Learning Across 3D Game Worlds
- **Authors**: Kailing Li, Ruoxuan Zhang, Zheyuan Zhou, Boyang Chu, Yingshan Lei, Hongxia Xie, Liang Du, Zixun Sun
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue/conference**: arXiv preprint
- **Date**: 2026-11-03 (v1), revised 2026-11-06 (v2)
- **Abstract**: AceAction introduces a human gameplay dataset across multiple 3D games for learning skill composition and subgoal transitions. Demonstrations are organized around complete tasks linking overall instructions, ordered subgoals, and local skill instructions to temporally aligned visual observations and keyboard-and-mouse actions.
- **Key innovations**:
  - Hierarchical task annotation: task instructions → ordered subgoals → local skill instructions aligned with visual/action trajectories.
  - VLM-based annotation pipeline that identifies subgoals from objective/interaction-target changes, anchors navigation goals to visual waypoints, and composes task instructions.
  - Coverage of navigation, reconnaissance, combat, interaction, and recovery with explicit stage boundaries for subgoal switching.
  - Reports 95.8% pass rate in an audit of 500 trajectories across independent reviewer assessments (author-reported), providing a data foundation for generalist 3D game agents.
- **Links**: [arXiv](https://arxiv.org/abs/2611.04241) | [PDF](https://arxiv.org/pdf/2611.04241)

---

## 2) Game AI Bots, NPC Intelligence, and LLM-Powered Gameplay

### LLM-based NPCs in Video Games: A Systematic Mapping Study
- **Authors**: Dilan Mian, Jeremy Bradbury, Yann-Gaël Guéhéneuc, Fabio Petrillo, Cristiano Politowski
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue/conference**: IEEE Transactions on Games (Early Access), accepted manuscript
- **Date**: 2026-11-02 (arXiv v1)
- **Abstract**: This systematic mapping study surveys 377 academic papers and analyzes 42 in depth to characterize LLM-based NPC research across component adoption, latency, safety coverage, and reproducibility. It finds near-universal use of short-term memory and world-state grounding but rarer adoption of long-term memory, reflection, and retrieval-augmented generation, alongside large latency ranges and structural barriers to commercial adoption.
- **Key innovations**:
  - First quantitative mapping (per authors) of LLM-NPC component adoption, response latency, safety coverage, and reproducibility across the field.
  - Empirical adoption profile: short-term memory (60%) and world-state grounding (69%) common; long-term memory (31%), reflection (38%), and RAG (14%) rare; reported response times span 2.6–15 seconds.
  - Identifies six structural barriers to commercial adoption and provides evidence-based recommendations for developers and researchers.
  - Useful survey baseline for NPC intelligence frameworks, evaluation practices, and deployment constraints.
- **Links**: [arXiv](https://arxiv.org/abs/2611.05427) | [PDF](https://arxiv.org/pdf/2611.05427) | [DOI](https://doi.org/10.1109/TG.2026.3733302)

### LLM-Guided Reinforcement Learning for Adaptive NPC Behavior in Multi-Agent Combat Games
- **Authors**: Hrithika Deepu Nair, Kayvan Karim
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue/conference**: arXiv preprint
- **Date**: 2026-08-27 (v1)
- **Abstract**: Studies a runtime strategy-selection framework where a locally hosted LLM (Mistral 7B via Ollama) reads live game state every five seconds and assigns tactical tags to guide a trained shared PPO policy in Unity, without modifying policy weights. Evaluated across 600 episodes against balanced, evasive, and aggressive scripted opponents.
- **Key innovations**:
  - Decouples strategic guidance from low-level control: LLM selects tactics while PPO executes learned behavior.
  - Runtime adaptation mechanism for multi-agent combat NPCs under changing opponent styles.
  - Reports win-rate improvement vs balanced opponents (11%→24%) and longer episodes, with mixed/negative outcomes against other opponent types (author-reported).
  - Diagnoses a key limitation: strategy selection collapsed toward "Surround" in 83.8% of 2,430 decisions, highlighting zero-shot strategic differentiation limits at this model scale.
- **Links**: [arXiv](https://arxiv.org/abs/2609.02931) | [PDF](https://arxiv.org/pdf/2609.02931)

### Acquire, Repair, Preserve: A Diagnosis-Guided Post-Training Recipe for Small-Model Dialogue Game Agents
- **Authors**: Nan Li
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue/conference**: Accepted to the LM Playschool Workshop at EMNLP 2026 (as stated on arXiv)
- **Date**: 2026-08-28 (v1)
- **Abstract**: Investigates small-model (2B open-weight) failures in interactive dialogue games where agents must track state, interpret feedback, and choose valid actions. The proposed recipe uses supervised fine-tuning to acquire broad participation, turn-local preference pairs to repair mechanically verifiable failures in a targeted family, and preservation objectives to retain general capabilities.
- **Key innovations**:
  - Diagnosis-guided training decomposition: **acquire** (SFT), **repair** (targeted preference pairs), **preserve** (capability retention).
  - Turn-local supervision focused on repeated guesses, malformed actions, and feedback violations—common failure modes in dialogue/game interaction.
  - Reports public clemscore improvement from 10.67 to 38.92 and closed in-domain score 13.41 to 41.17 while approximately preserving aggregate static performance (44.14 vs 44.24 baseline); out-of-domain clemscore remains low at 7.88 (author-reported).
  - Provides evidence that broad SFT drives most gains, while precise local repairs transfer mainly within-family.
- **Links**: [arXiv](https://arxiv.org/abs/2608.28458) | [PDF](https://arxiv.org/pdf/2608.28458) | [Model](https://huggingface.co/chnln/Qwen3.5-2B-playpen-playornotplay)

---

## 3) Game RL, Self-Play, and Strategic Learning

### Faynt: Scaling and Optimizing Policies for Competitive Melee
- **Authors**: Ali Janati, Nikita Kuzmin, Rohit Swamy, Charles Niu
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue/conference**: Preprint, in review (as stated on arXiv)
- **Date**: 2026-10-01 (v1)
- **Abstract**: Faynt presents 10M- and 75M-parameter Transformer policies for Super Smash Bros. Melee controlling all 26 characters with single checkpoints. The pipeline combines large-scale human replay pretraining (~840k replays), supervised post-training, rank/outcome curricula, 75M→10M distillation, and RL restricted to Fox mirror matches.
- **Key innovations**:
  - Unified multi-character competitive game policy family with scaling and optimization study (architecture, data, hyperparameter transfer, distillation, targeted RL).
  - Strong competitive results: after RL, the 10M model wins 240/244 same-character games (98.4%) against fourteen specialist/multi-character releases on supported rosters, with caveats about delay differences noted by authors.
  - Demonstrates post-training effects beyond raw prediction loss (reduced damage per minute, larger early leads, better recovery after losing first life); validation loss used for checkpoint selection aligned with win-rate ordering (author-reported).
  - Practical deployment/benchmarking focus: optimized inference (5.2 ms/decision for 10M, 8.7 ms for 75M on NVIDIA T4, excluding emulator/communication) and open-sourced weights/benchmarks/tournament platform.
- **Links**: [arXiv](https://arxiv.org/abs/2610.02144) | [PDF](https://arxiv.org/pdf/2610.02144)

### Inner-Learning: From Hand-Coded Beliefs to Declarative Knowledge in Trick-Taking Games
- **Authors**: Stefan Edelkamp
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue/conference**: arXiv preprint
- **Date**: 2026-10-28 (v1)
- **Abstract**: Presents a declarative approach to belief-state modeling in Skat, extracting hand-coded inference rules into a domain-specific language based on impossibility/cardinality constraints. The extracted, expert-annotated, and cardinality-constrained rules are evaluated in self-play, improving over the original hand-coded engine.
- **Key innovations**:
  - Automatic extraction of hand-coded belief/inference logic into a declarative DSL with round-trip code generation and bug auditing.
  - Extends representation with cardinality constraints (at-most-k / at-least-k) enforced at world-generation time and confidence parameters for probabilistic belief updates.
  - Unifies code-derived rules, symmetric derivation, and expert strategy annotations in one knowledge representation.
  - Reports measurable self-play improvements in winning percentage and score, with contributions from extracted rules, human annotations, and cardinality constraints (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2610.38304) | [PDF](https://arxiv.org/pdf/2610.38304)

---

## 4) Game Benchmarks and Evaluation

### SpeedrunBench: Challenging LLM Agents with Video Game Speedrunning
- **Authors**: Yoshinari Fujinuma, Keisuke Kamahori, Ryuto Koike, Abdelrahman Madkour, Varun Prashant Gangal, Monty Bichouna, Martyna Markiewicz, Shivani Jain, Duncan Curtis, Rebecca Qian, Anand Kannappan
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue/conference**: arXiv preprint
- **Date**: 2026-10-06 (v1)
- **Abstract**: Introduces SpeedrunBench, a benchmark evaluating frontier LLM agents on speedrunning across 9 video games. Agents must iteratively improve strategies, reflect on performance, exploit learned knowledge, and reason over long horizons to achieve faster completion times.
- **Key innovations**:
  - Frames speedrunning as a saturation-resistant evaluation of strategy formation, exploration, and iterative self-improvement beyond known human solutions.
  - Multi-game, long-horizon benchmark requiring repeated refinement rather than one-shot task completion.
  - Reports frontier agents approaching human world records in simple platformers but remaining behind human performance on longer, more complex games under practical budgets (author-reported).
  - Useful for studying planning, reflection, exploitation of game mechanics, and sample/budget efficiency in LLM game agents.
- **Links**: [arXiv](https://arxiv.org/abs/2610.08076) | [PDF](https://arxiv.org/pdf/2610.08076)

---

## 5) Industry and Real-World Game/Esports AI Applications

### DirCast: Live Esports Directing and Commentary with a Single Streaming Video-Language Model
- **Authors**: Zixian Gao, Lixin Xiu, Penghao Luo, Xiangcheng Cao, Ziqi Cai, Zhen Li, Erwin Wu, Kaipeng Zhang
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue/conference**: arXiv preprint
- **Date**: 2026-10-22 (v1)
- **Abstract**: DirCast studies live esports broadcast production from raw per-player camera feeds, jointly performing camera directing and commentary with a single streaming video-language model in Dota 2. The model scans all cameras at low resolution, makes hold-or-switch directing decisions, and reads the selected camera at high resolution before speaking, with bounded-cost streaming context management.
- **Key innovations**:
  - Unified streaming model for **directing + commentary** from raw multi-camera inputs rather than a human-produced broadcast feed.
  - Hold-or-switch director, multi-resolution camera scanning, and bounded-memory context that retains aired views/commentary while expiring other views.
  - Dataset of 27 professional Dota 2 matches with per-hero cameras, human director choices, and caster commentary.
  - Reports better directing than rule-based/zero-shot directors (including GPT-5 in their comparison) and 29.2% commentary preference wins vs GPT-4o under Proact-VL protocol, compared to 19.4% for strongest baseline streaming commentator (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2610.31734) | [PDF](https://arxiv.org/pdf/2610.31734)

---

## 6) Related Techniques (Self-Play, Analysis, and Learning Signals)

### Opening Rankings from Engine Self-Play Are Less Certain Than They Look: Sampling Error, Draws, and Strength Dependence in Strength-Limited Stockfish Games
- **Authors**: Conrad Flick, Jaysen Jensen, Jingyu Huang, Mario Camara Paslar
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue/conference**: arXiv preprint (stat.AP)
- **Date**: 2026-10-27 (v1)
- **Abstract**: Analyzes statistical uncertainty in chess opening rankings derived from engine self-play. Across 17,400 strength-limited Stockfish 15.1 games and follow-up studies, the work shows leaders can change by tiny margins, rankings are sensitive to sampling error/draws/hardware/configuration, and limited game counts can overstate certainty.
- **Key innovations**:
  - Rigorous uncertainty analysis for self-play-based evaluation/ranking in games (chess openings) with positive control (Connect Four).
  - Quantifies instability: with 290 games/opening, observed leader matched true best in only ~44% of simulated studies under a modest between-opening effect assumption (author-reported).
  - Highlights implementation/hardware and evaluation-design confounds relevant to self-play RL and engine-based benchmarking.
  - Useful methodological caution for game AI systems that rely on self-play tournaments, leaderboards, or automated curriculum signals.
- **Links**: [arXiv](https://arxiv.org/abs/2610.37988) | [PDF](https://arxiv.org/pdf/2610.37988) | [Data/code](https://doi.org/10.5281/zenodo.23357406)

---

## Cross-Cutting Observations

- **World models are becoming more structured and controllable**: shared 3D proxies (2611.15602) and foundation-model-derived action representations (2611.14420) target consistency, transfer, and scene/action disentanglement rather than unconstrained generation.
- **Game agent progress is split between capability and reliability**: NPC/agent systems show adaptation gains (2609.02931, 2610.31734) but also expose bottlenecks in strategy selection, latency, safety, reproducibility, and out-of-domain generalization (2611.05427, 2608.28458).
- **Benchmarks increasingly stress iteration and diagnosis**: speedrunning (2610.08076), dialogue-game post-training diagnostics (2608.28458), and competitive evaluations (2610.02144) emphasize long-horizon improvement and failure analysis over single-score leaderboards.
- **Self-play and game evaluation need uncertainty accounting**: statistical analysis of engine self-play rankings (2610.37988) complements RL/self-play advances by questioning confidence from limited samples.

## Coverage Notes and Gaps

- **Deduplication**: Excluded papers already featured in recent `game-rl-daily` digests (`2026-11-10`–`2026-11-13`) and overlapping 2026-11-15 synthesis entries where applicable.
- **Proceedings/industry coverage**: `websearch` unavailable; venue information limited to arXiv-exposed status (e.g. IEEE T-G Early Access, LM Playschool Workshop @ EMNLP 2026, preprint/in-review notes). Major-studio deployment papers were sparse in accessible metadata this run; DirCast is included as a real-time esports/game-broadcast application.
- **Affiliations**: Several papers do not provide structured institution/company fields in arXiv metadata; affiliations should be verified from PDFs before canonical entity attribution.
- **Topic balance**: This digest includes direct coverage for LLM/NPC agents, world/foundation models, generalist game action data, competitive RL/self-play-adjacent learning, benchmarks, and evaluation methodology. Classic-environment RL (Atari/StarCraft/Dota/Go/poker/NetHack-specific new papers) was less prominent in non-duplicate recent results retrieved during this run.

## Sources Consulted (arXiv API / pages)

- `all:game AND (all:"reinforcement learning" OR all:RL)` (submittedDate desc)
- `(all:"game agent" OR all:"NPC" OR all:"autonomous gameplay") AND (all:LLM OR all:"large language model" OR all:VLM)` (submittedDate desc)
- `all:"world model" AND (all:game OR all:Atari OR all:Minecraft OR all:"video game")` (submittedDate desc)
- `all:"procedural content generation" AND (all:game OR all:RL OR all:LLM)` (submittedDate desc)
- `(all:Minecraft OR all:Atari OR all:StarCraft OR all:Dota OR all:NetHack OR all:poker OR all:chess OR all:Go) AND (all:RL OR all:agent)` (submittedDate desc)
- `(all:"self-play" OR all:"multi-agent reinforcement learning" OR all:"population-based") AND all:game` (submittedDate desc)
- `all:"game benchmark" OR (all:benchmark AND all:"game agent")` (submittedDate desc)
- `all:"game foundation model" OR (all:generalist AND all:game AND all:agent)` (submittedDate desc)
- `all:"video game" AND (all:benchmark OR all:evaluation)` (submittedDate desc)
- Individual abstract/PDF pages for featured papers above
