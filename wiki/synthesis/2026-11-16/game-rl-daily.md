# Game RL & Game AI Bot — Daily Paper Digest (2026-11-16)

- **Date**: 2026-11-16
- **Window**: ~2026-08-05 → 2026-11-13 (recent arXiv submissions/revisions and arXiv-exposed venue metadata available at query time)
- **Scope**: Game RL and strategic learning, LLM/VLM-powered game agents and NPC/social-deduction intelligence, game foundation and generalist game-playing models, world models in game/POSG settings, procedural content generation and game creation benchmarks, and game-based agent evaluation.
- **Method note**: Discovery used arXiv Export API queries via `curl` on 2026-11-16 (HTTPS endpoint); `websearch` was unavailable in this run, so coverage of recent non-arXiv proceedings is limited to venue/status metadata exposed on arXiv pages (comments/journal references/DOIs where present). Paper metadata, abstracts, venues, affiliations, and reported results below are taken from fetched arXiv abstract pages and are **author-reported** unless otherwise noted. Affiliations are listed as “not explicitly listed in arXiv metadata (verify from PDF)” when structured affiliation fields were absent. Candidate papers were deduplicated against arXiv IDs already appearing in prior `wiki/synthesis/*/game-rl-daily.md` digests.
- **Active preference file**: `EXTEND.md` (repo root).

## Executive Summary

Recent game-agent work emphasizes **generalist interaction, diagnosable evaluation, and social/strategic communication** rather than only task-specific control. Gamer (2611.18397) targets a shared perception-memory-reasoning stack for long-horizon, real-time 2D/3D gameplay from large-scale keyboard-mouse trajectories and multi-turn RL. On the evaluation/generation side, OCTAVE (2611.17681) decomposes end-to-end HTML5 game generation into capability-resolved requirements, while ABHBench (2611.09326, NeurIPS 2026 Datasets & Benchmarks track, camera-ready) probes first-person moral agency in *Detroit: Become Human*. LLM world-model research (2611.14419) shows that mechanically valid generated partially observable stochastic games can still diverge structurally from intended decision problems, a caution for neuro-symbolic game reasoning. Social-deduction games remain a rich testbed for LLM agents: Werewolf studies examine proactive utterance timing (2610.32107, AIWolfDial @ INLG 2026), linguistic style/politeness effects (2611.09768), accusation-source trust and belief shifts (2609.12446, EMNLP 2026 main), and human emotion dynamics (2608.04605). A Minecraft/PCG-adjacent quantum-search study (2610.33139) quantifies Grover-oracle resource costs for procedural seed recovery, linking game content structure to hardware-aware algorithm design.

---

## 1) Game Foundation Models and Generalist Game Agents

### Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent
- **Title (EN)**: Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent
- **Authors**: Run Luo; Kuan Zhang; Qi Deng; Yukun Chen; Zhihao Yang; Yufei Zhang; Renrong Hu; Yi Zhang; Guiyu Ma; Tianyu Fan; Longze Chen; Hao Sun; Jiaming Li; Jiaming Yang; Xiaohao Liu; Tao Tan; Minzheng Wang; Hangtian Jia; Shuai Yuan; Lvdi Wang; Xiao Liu; Chao Ma; Yuting Zou; Yinhe Zheng; Xiaobo Xia; Dawei Jiang; Shaoqing Ren
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue/conference**: arXiv preprint
- **Date**: 2026-11-13 (v1)
- **Abstract**: Gamer is a generalist agent framework for long-horizon tasks in complex interactive environments, combining perception, memory management, and multi-step reasoning in an end-to-end architecture. A shared training and deployment pipeline supports interaction with both conventional 2D graphical interfaces and complex 3D simulated worlds. The authors continue pre-training on trajectories from tens of thousands of hours of device-level keyboard-and-mouse interaction spanning simulated games and embodied environments, then apply sparse-thinking instruction tuning and stable multi-turn reinforcement learning to handle finite context, accumulated rollout errors, and sparse rewards. A cloud-edge inference engine supports concurrent simulated environments, unbounded-context execution, and low online inference latency.
- **Key innovations**:
  - **Unified VLA game-agent stack**: integrates perception, memory, and multi-step reasoning for 2D/3D interactive environments under a shared train/deploy pipeline.
  - **Large-scale device-level pretraining**: learns dynamics from keyboard-and-mouse trajectories across virtual and embodied domains, positioning low-level interaction traces as scalable supervision.
  - **Long-horizon optimization**: sparse-thinking instruction tuning to reduce redundant computation and multi-turn RL tailored to long rollouts/sparse rewards.
  - **Real-time systems support**: cloud-edge inference for concurrent environments and low-latency online execution.
  - **Reported results**: solid generalization and operational efficiency comparable to skilled players across multiple challenging 3D open-world games, plus competitive results on conventional 2D game benchmarks (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2611.18397) | [PDF](https://arxiv.org/pdf/2611.18397)

---

## 2) Procedural Content Generation and Game Creation Benchmarks

### OCTAVE: A Capability-Resolved Benchmark for End-to-End HTML5 Game Generation
- **Title (EN)**: OCTAVE: A Capability-Resolved Benchmark for End-to-End HTML5 Game Generation
- **Authors**: Kehang Li; Xinlan Xu; Yulin Jin; Heng Cao; Xuchen Li; Houxian Ren; Zihao Ji; Qiang Luo; Yadong Mao; Qilin He; Jian Zhang; Jian Zhao; Zihao Wang
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue/conference**: arXiv preprint
- **Date**: 2026-11-13 (v1)
- **Abstract**: OCTAVE evaluates complete HTML5 game generation, where agents must coordinate rules, interactions, states, and presentation over long development processes. Instead of a single aggregate score, it organizes evaluation into eight capability dimensions with 180 tasks and 1,800 evaluation requirements from real player requests, commercial-mechanics reconstruction, and expert design. The benchmark covers PC Web, Mobile Web, 2D, and 3D, distinguishes completeness from richness, and uses static source-code judgments for requirement-level diagnosis.
- **Key innovations**:
  - **Capability-resolved evaluation**: moves beyond aggregate scores to requirement/capability/task-condition diagnosis for end-to-end game creation.
  - **Completeness vs. richness**: separates publicly specified core implementation from hidden/deeper system relationships.
  - **Broad task design**: 180 tasks and 1,800 requirements spanning platforms/modalities (PC/Mobile Web, 2D/3D) and multiple capability dimensions.
  - **Empirical gap analysis**: across 11 model-harness combinations, reports 33.2% completeness and 32.5% richness; 19.9% of generation records are static gate failures or missing artifacts; excluding same-model self-evaluation, best combinations remain below 50% on public and hidden requirements (author-reported).
  - **Capability profile**: relatively stronger on core rules/numerical design, with larger gaps in AI/NPC behavior and feedback/game feel (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2611.17681) | [PDF](https://arxiv.org/pdf/2611.17681)

### The Cost of a Real Grover Oracle: Minecraft Seed Search from Software to Quantum Hardware
- **Title (EN)**: The Cost of a Real Grover Oracle: Minecraft Seed Search from Software to Quantum Hardware
- **Authors**: Evan M. Reeves; Elias Sopkin; Thomas A. Searles
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue/conference**: arXiv preprint (quant-ph)
- **Date**: 2026-10-23 (v1)
- **Abstract**: This work estimates resources for a Grover oracle targeting Minecraft 1.13.1 seed recovery, combining a structure-placement predicate with a reversible inverse transform of the 32-bit residual search in the linear congruential generator. The authors verify reduced-width arithmetic, phase marking, uncomputation, and complete Grover loops against an independent Java reference, and audit production-width circuits structurally. They compare direct Fourier-basis constant arithmetic against register-to-register baselines and report hardware experiments on IBM processors and Quantinuum H2-1.
- **Key innovations**:
  - **Game/PCG-derived oracle construction**: frames Minecraft procedural seed recovery as a concrete quantum search workload with verifiable oracle components.
  - **Arithmetic specialization**: direct Fourier-basis constant arithmetic reduces placement-predicate width from 6n+3 to 4n+3 qubits and two-qubit gate scaling from Θ(n³) to O(n²) (author-reported structural/scaling result).
  - **Resource quantification**: representative nonzero-r folded residual-search construction reported as 275 circuit qubits, 48,896 CX gates, depth 4,482 versus 467 qubits, 2,038,804 CX gates, depth 186,328 for the baseline under stated accounting (author-reported).
  - **Hardware-aware findings**: reduced-width circuits executed in complete Grover loops on IBM/Quantinuum; specialized construction shows larger one-iteration marked-state probability increases than baseline, with substantial routing/execution sensitivity on IBM experiments (author-reported).
  - **PCG insight**: exposes width-recomputation tradeoffs in multi-placement conjunctions and candidate-reduction plateaus in exact enumeration.
- **Links**: [arXiv](https://arxiv.org/abs/2610.33139) | [PDF](https://arxiv.org/pdf/2610.33139)

---

## 3) Game Benchmarks and Agent Evaluation in Game Environments

### ABHBench: Evaluating Moral Decision-Making of Foundation Models from an Agentic Perspective
- **Title (EN)**: ABHBench: Evaluating Moral Decision-Making of Foundation Models from an Agentic Perspective
- **Authors**: Chaoran Li; Yukun Li; Zeyuan Zhao; Shao Zhang; Xihuai Wang; Ying Wen
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue/conference**: NeurIPS 2026 Track on Datasets and Benchmarks (camera-ready version), as stated on arXiv
- **Date**: 2026-11-06 (v1)
- **Abstract**: ABHBench evaluates moral decision-making of foundation models as situated, acting agents using *Detroit: Become Human*, an interactive narrative game. Models face branching first-person human-android dilemmas with visual observations, dialogue, memory, and action choices. Inspired by Asimov’s Three Laws, the framework measures Harmlessness, Obedience, and Self-preservation, plus Autonomy, Stability, and Certainty. Across 12 foundation models, the study finds substantial behavioral shifts under situated agentic context compared with text-only abstractions.
- **Key innovations**:
  - **First-person agentic evaluation in a commercial narrative game**: tests models as actors in branching scenarios rather than third-person judges of text vignettes.
  - **Multimodal situated setup**: includes visual observations, dialogue, memory, and action choices in interactive dilemmas.
  - **Moral/behavioral axes**: operationalizes Harmlessness, Obedience, Self-preservation, Autonomy, Stability, and Certainty.
  - **Reported findings**: 75% of models shift significantly between text-only abstraction and matched multimodal DBH scenarios; reasoning-enhanced models show no monotonic gains in consistency or human-oriented behavior (author-reported).
  - **Benchmark implication**: argues for evaluating moral/agentic behavior in situated contexts, relevant to NPC/interactive-game AI evaluation.
- **Links**: [arXiv](https://arxiv.org/abs/2611.09326) | [PDF](https://arxiv.org/pdf/2611.09326)

### Evaluating LLM-Generated World Models for Neuro-Symbolic Reasoning
- **Title (EN)**: Evaluating LLM-Generated World Models for Neuro-Symbolic Reasoning
- **Authors**: Souhaila Djaffal; Amna Jamal; Gagana Madhugiri Devaraja; Anidipta Pal; Jobst Heitzig
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue/conference**: arXiv preprint
- **Date**: 2026-11-10 (v1)
- **Abstract**: The paper studies whether LLMs can generate formal world models as partially observable stochastic games (POSGs) from open-ended natural-language situations and whether mechanical validity implies faithful representation. Using 44 scenarios spanning game, situational, and cultural settings, it evaluates mechanical validity, reference-relative structural agreement, and semantic criteria across 410 first-pass generations from five LLMs.
- **Key innovations**:
  - **Game-formalism target**: treats LLM-generated world models as POSGs, directly relevant to multi-agent/game reasoning and planning.
  - **Three-axis evaluation**: separates mechanical validity, structural agreement, and semantic criteria rather than conflating executability with correctness.
  - **Key empirical result**: in the reference-backed game track, 134/135 generated world models pass strict mechanical audit, but mean permutation-invariant structural F1 is 0.366 and only 28/134 mechanically valid models exactly match authored references (author-reported).
  - **Sensitivity finding**: explicitly naming a country changes generated structural representations for most LLMs with only small changes in automated semantic scores (author-reported).
  - **Implication for game AI**: executability is necessary but insufficient for downstream neuro-symbolic reasoning/planning over game-like decision structures.
- **Links**: [arXiv](https://arxiv.org/abs/2611.14419) | [PDF](https://arxiv.org/pdf/2611.14419)

---

## 4) LLM Game Agents and Social-Deduction Intelligence (Werewolf)

### Beyond What to Say: Proactive Utterance Timing with Inner Thoughts for Werewolf Agents
- **Title (EN)**: Beyond What to Say: Proactive Utterance Timing with Inner Thoughts for Werewolf Agents
- **Authors**: Yoshiki Tanaka; Shuya Uchiyama; Daichi Hamaguchi; Michimasa Inaba
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue/conference**: Accepted to the 4th International AIWolfDial Workshop at INLG 2026 (as stated on arXiv)
- **Date**: 2026-10-23 (v1)
- **Abstract**: This work addresses not only what an LLM Werewolf agent should say, but when it should speak in an adversarial, incomplete-information setting where both speech and silence are interpreted. Building on the Inner Thoughts framework, the authors adapt utterance-timing decisions for Werewolf by generating internal thoughts and evaluating their value for expression at each moment, yielding the Adversarial Inner Thoughts method for the AIWolfDial Anytime Utterance Track.
- **Key innovations**:
  - **Proactive timing as strategy**: treats speaking/silence decisions as first-class actions in social-deduction gameplay.
  - **Adversarial adaptation of Inner Thoughts**: redesigns a general dialogue timing mechanism for competitive Werewolf dynamics and incomplete information.
  - **Evaluation approach**: analyzes self-play logs and human evaluations to assess effectiveness in the shared-task setting (author-reported).
  - **Relevance**: contributes to autonomous gameplay/NPC-like conversational agency where timing can signal intent, alignment, or deception.
- **Links**: [arXiv](https://arxiv.org/abs/2610.32107) | [PDF](https://arxiv.org/pdf/2610.32107)

### Language as Trait, Politeness as Strategy: Controlled Tests of Linguistic Effects in LLM Social-Deduction Agents
- **Title (EN)**: Language as Trait, Politeness as Strategy: Controlled Tests of Linguistic Effects in LLM Social-Deduction Agents
- **Authors**: Yuchen Li; Lisa Liu; Runqi Zou; Shuxuan Kuang; Qingquan Zhang; Julian Togelius
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue/conference**: arXiv preprint
- **Date**: 2026-11-06 (v1)
- **Abstract**: Using the LURK Werewolf framework, this study isolates linguistic realization from speech-act content to test whether complexity/range and politeness strategy affect other agents’ judgments and actions. The authors rewrite only realizations, preserve game content, and replay each game day from saved checkpoints against re-sampled controls. Across 30 games and 4,335 replays, manipulations do not significantly change trust, and no vote/night-action effect survives multiple-comparison correction.
- **Key innovations**:
  - **Controlled causal-style intervention in Werewolf dialogue**: separates speech-act predicate from natural-language realization to test linguistic effects.
  - **Scale of replay evaluation**: 30 games and 4,335 checkpoint replays varying linguistic range and per-utterance politeness strategy.
  - **Negative-result insight**: neither manipulation changes trust; largest uncorrected effect is ~4 percentage-point change in other players’ votes when shifting range away from neutral paraphrase; in natural play 88% of face-threatening speech is bald on-record regardless of role (author-reported).
  - **Design implication**: suggests LLM social-deduction agents may be driven more by game content/strategy than by surface politeness or complexity in this setup.
- **Links**: [arXiv](https://arxiv.org/abs/2611.09768) | [PDF](https://arxiv.org/pdf/2611.09768)

### Do LLMs Trust the Accuser or the Accusation? Measuring Belief Shifts in Werewolf
- **Title (EN)**: Do LLMs Trust the Accuser or the Accusation? Measuring Belief Shifts in Werewolf
- **Authors**: Yu-Yu Yang; Ti-Rong Wu; Hung Guei; Hsing-Yu Chen; I-Chen Wu
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue/conference**: EMNLP 2026 Main Conference (accepted), as stated on arXiv
- **Date**: 2026-09-11 (v1)
- **Abstract**: This paper proposes a belief-shift benchmark for Werewolf that evaluates communication skills through belief updating rather than final outcomes alone. Using LLM-played games, the authors annotate suspicion/accusation messages and measure how a village-side observer model’s beliefs change after each message. They evaluate 40 open-weight LLM configurations on 1,224 annotated messages.
- **Key innovations**:
  - **Process-level evaluation**: measures belief updates induced by accusations/suspicion messages instead of relying only on win/loss outcomes.
  - **Source-vs-content analysis**: disentangles trust in the accuser from the content of the accusation in strategic communication.
  - **Reported findings**: larger models better distinguish true wolves from villagers from history, but accusations still strongly shift beliefs (more suspicion of accused, less of accuser), especially when accuser is trusted—even if wolf-aligned; larger models better resist accusations from distrusted accusers (author-reported).
  - **Benchmark contribution**: highlights remaining difficulty for open-weight LLMs (up to 120B evaluated) in integrating accusation content with source trust.
  - **Resources**: benchmark/code available at `https://rlg.iis.sinica.edu.tw/papers/werewolf-accusation-benchmark` (as stated on arXiv).
- **Links**: [arXiv](https://arxiv.org/abs/2609.12446) | [PDF](https://arxiv.org/pdf/2609.12446) | [Benchmark/Code](https://rlg.iis.sinica.edu.tw/papers/werewolf-accusation-benchmark)

### Emotion Dynamics in Social Deception Games: Analysis of Professional and Nonprofessional Players through Electrodermal Activity in Werewolf Games
- **Title (EN)**: Emotion Dynamics in Social Deception Games: Analysis of Professional and Nonprofessional Players through Electrodermal Activity in Werewolf Games
- **Authors**: Sho Mitarai; Chang Liu; Goshiro Yamamoto; Nagisa Munekata
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue/conference**: Published in 2025 (journal/conference venue not fully specified in arXiv metadata; verify from PDF)
- **Date**: 2026-08-05 (arXiv v1)
- **Abstract**: This study compares professional and non-professional players in Werewolf using electrodermal activity to capture physiological emotional responses and analyzes communication patterns during high-arousal periods. It finds distinct strategies: professionals maintain persuasion-based approaches under high arousal, while non-professionals shift toward information-focused communication, with professionals showing more stable emotional states.
- **Key innovations**:
  - **Physiological grounding for social-deception gameplay**: combines EDA measurements with communication-pattern analysis in Werewolf.
  - **Expertise-dependent behavior**: reports significant differences in expression patterns and emotional regulation between professional and non-professional players (author-reported).
  - **Relevance to game AI/NPC design**: provides human behavioral signals that can inform emotionally adaptive communication strategies for agents in deception-heavy game settings.
- **Links**: [arXiv](https://arxiv.org/abs/2608.04605) | [PDF](https://arxiv.org/pdf/2608.04605)

---

## Cross-Cutting Observations

- **Generalist gameplay is moving toward unified stacks**: Gamer combines large-scale interaction pretraining, long-horizon RL, and real-time serving for 2D/3D games, suggesting a convergence of foundation-model perception/reasoning with control interfaces.
- **Game evaluation is becoming more diagnostic**: OCTAVE’s capability-resolved requirements and ABHBench’s situated first-person game dilemmas both reveal failures hidden by aggregate scores or third-person judgment tasks.
- **World-model validity is more than executability**: POSG-generation results show high mechanical pass rates but low structural faithfulness, an important warning for model-based/neuro-symbolic game agents.
- **Social-deduction games stress communication pragmatics**: Werewolf studies separate timing, linguistic style, source trust, and emotional regulation, indicating that robust LLM game agents need calibrated belief updating and interaction policies beyond text generation quality.
- **PCG/game structure can drive systems research**: Minecraft seed-recovery as a Grover-oracle workload illustrates how procedural game content yields concrete, measurable constraints for specialized computation.

## Coverage Notes and Gaps

- **Deduplication**: excluded papers whose arXiv IDs already appear in previous `game-rl-daily` synthesis files in this wiki.
- **Topic coverage**: this digest has direct coverage for game foundation/generalist agents, PCG/game generation benchmarks, game-based agent benchmarks, world models in game/POSG settings, and LLM game/social-deduction agents. Classic environment-specific RL breakthroughs (e.g. new Atari/StarCraft/Dota/Go/poker/NetHack training results) were sparse among deduplicated recent API results retrieved in this run; proceedings-only results without arXiv metadata may be underrepresented because `websearch` was unavailable.
- **Affiliations/venues**: several entries lack structured affiliations in arXiv metadata and should be verified from PDFs; some venue labels are taken from arXiv comments/journal fields and may reflect acceptance status rather than final published versions.
- **Sources consulted (arXiv API, 2026-11-16)**: `all:"reinforcement learning" AND all:game`, `all:"game agent" AND (all:LLM OR all:"language model" OR all:VLM)`, `all:"world model" AND (all:game OR all:Minecraft OR all:Atari)`, `all:"game foundation model" OR (all:generalist AND all:game AND all:agent)`, `all:"procedural content generation" AND (all:game OR all:level)`, `all:"self-play" AND all:game`, `all:"game benchmark" OR (all:benchmark AND all:game AND all:agent)`, `(all:Minecraft OR all:StarCraft OR all:poker OR all:chess OR all:Go) AND (all:RL OR all:agent)`, `all:Werewolf AND all:agent`, plus individual abstract queries for featured papers.
