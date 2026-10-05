---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-10-05)"
type: synthesis
created: 2026-10-05
updated: 2026-10-05
sources: [arxiv.org, cog2026.org]
tags: [game-rl, game-ai, llm-agents, imperfect-information, chess, xiangqi, self-play, pcg, benchmarks, world-models, industry-game-ai, game-dev-se, evaluation, measurement-validity, peer-review, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-10-05)

> **Yesterday's digest declared this lane saturated and recommended cutting its cadence. Both halves of that conclusion turn out to be wrong, and this run shows how.** The arXiv fresh window did reopen: the ceiling moved from `2610.02210` to `2610.03717`, and of the **239 unclaimed papers** above yesterday's boundary, **five are game papers** — two of them (`2610.02425` XiangqiBench, `2610.03695` Queen) are better-designed game-LLM evaluations than almost anything this wiki has recorded. But the larger finding is methodological: **the `2610.*` block was never the venue.** **IEEE CoG 2026** — held **1–4 September 2026 in Madrid**, proceedings not yet on IEEE Xplore — has an accepted-papers list of ~450 entries that **no earlier digest in this series has ever touched**, and it contains a **peer-reviewed** game-RL and game-AI literature, including **two of the five Best Paper Award nominees**. Every game-RL result recorded in this wiki to date has been an unreviewed arXiv preprint. That is a coverage hole, not a field property, and closing it is worth more than the fresh arXiv window.

---

## §0 Method and Corpus

### 0.1 Boundary determination
- **Yesterday's ceiling** was `2610.02210`. This run enumerated `/new` listings across `cs.LG`, `cs.AI`, `cs.MA`, `cs.CL`, `cs.CV` in five pages of 200 and read the actual ceiling rather than inferring it.
- **Current ceiling: `2610.03717`.** `2610.03716` is the highest ID in the retrieved pools.
- **Fresh-window size: 239 unclaimed papers** above `2610.02210` after dedup. This is an **enumerated** result with a known denominator, not a sample — the same standard the 10-04 digest set for itself.
- **Fresh-window game yield: 5.** Genuinely game-relevant: `2610.03695`, `2610.03604`, `2610.03598`, `2610.02425`, `2610.02331`.

### 0.2 Sweep — three channels, and the second one is the story
1. **arXiv listing enumeration** (exhaustive on the fresh window) plus **~50 arXiv HTML full-text search queries** split into topical passes (`all:` broad) and a **title-field pass** (`ti:`) over named games and genres. The `ti:` pass completed 1,030 hits across ~50 terms (`game agent`, `NPC`, `world model`, `policy`, `imitation`, `multi-agent`, `Atari`, `chess`, `mahjong`, `NetHack`, `self-play`, `PCG`, …).
2. **Recent-proceedings channel — the productive one.** `https://cog2026.org/acceptedpapers` was fetched and parsed. It yields **~450 accepted entries** across AI for Game Playing, Game Design and Technology, PCG, Serious Games, Auxiliary Papers, and an **Accepted Industry Talks** track, **plus a named Best Paper Award Nominees list**. Targeted arXiv title lookups were then run for the 14 most relevant proceedings papers to recover preprints where they exist.
3. **Rolling-window topic pass** over the 2026-09-01 → 2026-10-05 band for backfill.

**Pool accounting**: `hpool_b` 2,006 + `hpool_d` 1,030 (title pass) + `hpool_c` 355 + small targeted pools → **3,153 unique papers**, of which **2,432 unclaimed**.

### 0.3 Rate limiting and the scraper workaround
- The **arXiv export API returned `HTTP 429` ("Rate exceeded")** persistently, with intermittent `HTTP 503`. A direct Python `urllib` fetch of arXiv HTML returned **`HTTP Error 406: Not Acceptable`**. Both were worked around with `curl` using a browser user-agent against arXiv's `/html/` and search endpoints. One background query batch timed out at 300 s and was restarted. **Recorded because a future run that trusts the export API will under-report on game content**, which is exactly the false-saturation failure mode of 2026-10-04.

### 0.4 Dedup
- Whole-`wiki/` regex sweep over `2[0-9]{3}\.[0-9]{4,5}` → **7,945 unique arXiv IDs already claimed** before this file was written; plus **62 IDs claimed by the seven sibling files in `wiki/synthesis/2026-10-05/`**.
- Every featured ID re-verified **0-hit immediately before writing** (§9.1 lists the full check).
- **⚠️ Three initially-selected papers were dropped as already-covered** after the ID-level check: MIPCGRL `2508.09193` (8 files), PuzzleJAX `2508.16821` (2 files), RePAIR `2606.11860` (3 files). Their **CoG 2026 acceptances are new** and are recorded as venue updates in §9.2 rather than re-summarized. This is the second time in three days that an ID-only dedup pass would have produced duplicates had title-level dedup not been run.
- **⚠️ Same-day sibling collision**: `arxiv-daily.md` (same directory) claims **`2610.02563`** (OpenGameEval), which falls inside this run's fresh window and is a genuine game paper. **It is therefore excluded from §1–§7 and recorded in §9.3.** The other same-day siblings claim no overlapping game IDs.

---

## §1 Game RL — Reinforcement Learning in Games

### ★★★ MAPLE: Multi-State Aggregated Policy Evaluation for AlphaZero in Imperfect-Information Games
- **Authors**: Qian-Rong Li, Hung Guei, I-Chen Wu, Ti-Rong Wu
- **Affiliation**: Department of Computer Science, **National Yang Ming Chiao Tung University**, Taiwan (Li, Wu); Institute of Information Science, **Academia Sinica**, Taiwan (Guei, Wu). Recovered from the **PDF title block** — the arXiv HTML is unavailable for this paper (`No HTML for '2605.24139'`) and the abs page carries no affiliation.
- **Venue**: arXiv:2605.24139 (22 May 2026). Comment field: **"Accepted by the IEEE Conference on Games (IEEE CoG 2026)"** — and it is **nominated #129 for the IEEE CoG 2026 Best Paper Award**. Proceedings pending on IEEE Xplore.
- **Link**: https://arxiv.org/abs/2605.24139
- **Abstract and key innovations**: AlphaZero works on perfect-information games; extending it to imperfect-information games (IIGs) does not. The paper names the two existing failure modes precisely — **PIMC suffers strategy fusion**, **IS-MCTS incurs high computational cost when combined with neural networks** — and proposes MAPLE, which **aggregates policy and value evaluations from multiple sampled world states within a single search tree**, taking the cheap route's tractability and the exact route's belief-awareness while keeping cost controllable. A **Siamese-based sampling strategy** selects informative world states from the information set. Results on **Phantom Go and Dark Hex**: **+291 Elo and +136 Elo** respectively over a PIMC-based AlphaZero baseline.
- **Why it matters here**: this is the **first peer-review signal in this wiki's entire game-RL corpus**, and it lands on the exact problem the fresh-window papers (§5.1, §5.2) are built around — **the gap between picking a legal move and playing the game well**. MAPLE's framing of strategy fusion names that gap from the search side; XiangqiBench measures it from the evaluation side. Two independent constructions of the same failure, five months apart, one peer-reviewed.
- **Caveats**: **two games only**, both small-board and both with deterministic-ish payoff structure; Dark Hex is a solved-adjacent benchmark where a 136-point gain needs a stated opponent pool and search budget to be interpretable, and neither is given in the abstract. The Siamese selector adds a trained component, so "controllable computational cost" is a claim about a tuned knob, not an architectural constant. **The gain is against a PIMC baseline, not against IS-MCTS** — so it does not settle which of the two failure modes is cheaper to fix.

### ★★★ When a Correct Reward Is Not Enough: Diagnosing and Guiding PPO in an Analytically Solved Broker-Trader Game
- **Authors**: Siu Tung Wong, Carlo Campajola
- **Affiliation**: **UCL Institute of Finance and Technology** (both authors); Campajola also affiliated with the **UZH Blockchain Center**, University of Zurich.
- **Venue**: arXiv:2610.03598 (2 Oct 2026) — cs.LG, cs.MA. **Accepted at ICAIF 2026** (ACM International Conference on AI in Finance).
- **Link**: https://arxiv.org/abs/2610.03598
- **Abstract and key innovations**: builds a **broker-trader game with an analytic solution** and uses it to diagnose PPO. The framing — *a correct reward is not enough* — is the paper's thesis in miniature: with a reward function that is verifiably correct, standard PPO still fails, and the paper localizes why and proposes a guidance mechanism. Filing note: this is a **financial market-simulator "game"**, not a video game, and it is included in §1 on the grounds that its contribution is to **PPO diagnosis in a game with known ground truth**, which is the same contribution the arcade and imperfect-information lanes need. Flagged in §8.2 as a possible scope overreach.
- **Why it matters here**: the analytic-solution design is the methodological counterpart to §5.1's XiangqiBench. **Both papers independently adopt "a game where the right answer is computable" as the instrument for calibrating an agent-evaluation instrument.** That convergence is the strongest methodological signal in this digest.
- **Caveats**: single environment; finance framing is domain dressing for what is really an RL-diagnosis study. No game-RL venue claims, and the ICAIF acceptance is a different review community from CoG.

### ★★★ Mastering Atari 2600 Games with Discovered Options — Wayfarer
- **Authors**: Erik M. Lintunen, Marlos C. Machado
- **Affiliation**: **University of Alberta**; **Alberta Machine Intelligence Institute (Amii)**; Canada CIFAR AI Chair. One of very few papers this month with a verifiable, current affiliation block intact.
- **Venue**: arXiv:2610.03604 (2 Oct 2026) — cs.LG.
- **Link**: https://arxiv.org/abs/2610.03604
- **Abstract and key innovations**: introduces **Wayfarer**, which **discovers options** — temporally extended subroutines — via **Laplacian-based representation learning**, and reports state-of-the-art results among single-stream agents on challenging Atari 2600 titles. The claimed gains are specifically in **exploration, credit assignment, and generalization**, with **Montezuma's Revenge and Private Eye** named as the discriminating cases.
- **Why it matters here**: option discovery has a long history in this wiki's lineage and a poor record of surviving contact with modern large-scale training. Two things make this worth ★★★: **it is single-stream**, so the comparison is against methods with the same compute and no privileged reset; and the named failure cases are the *hard-exploration* titles where distributional RL still breaks down. If the claim holds, this is the first option-discovery result in the series that is competitive rather than a demonstration.
- **Caveats**: arXiv preprint, **no venue acceptance claimed**. Atari 2600 performance claims are highly sensitive to the sticky-actions protocol, frame-skip, and the eval episode budget; the abstract does not state which, so the SOTA claim is **not yet verifiable from the record**. "Single-stream" is defined by the authors and has been used inconsistently across the literature.

### ★★ An Evaluation of Perfect-Information Monte Carlo Tree Search in Imperfect-Information Games
- **Authors**: Varun Adithiyan Ravichandran, James Goodman, Simon Lucas
- **Affiliation**: not verified from the record in this run — Simon Lucas is the long-standing author behind **OpenSpiel** and the **VGDL** family, but the proceedings page carries affiliations only as unlinked superscripts. **Not inferred.**
- **Venue**: **IEEE CoG 2026**, paper #366, *AI for Game Playing*.
- **Link**: https://cog2026.org/acceptedpapers (proceedings pending on IEEE Xplore; **no arXiv preprint located** under any of 11 title-search variants)
- **Abstract and key innovations**: a controlled **evaluation of PIMCTS** in imperfect-information games. Pairs as the empirical counterpart to §1's MAPLE: MAPLE takes PIMC as its baseline and beats it by 291/136 Elo, and this paper asks **how much of PIMC's reputation survives a fair evaluation in the IIG setting it is actually used in**. The pairing matters — a reader who sees only MAPLE cannot tell whether the 291-point gain reflects a better algorithm or a weak baseline.
- **Why it matters here**: this is the **control condition the field's strongest IIG result needs**, and it exists only because it went to a conference rather than to arXiv. Filed as ★★ on the strength of its role; the content itself is unverified.
- **Caveats**: **no abstract available** — everything above is inference from the title and from its position relative to MAPLE. Treat as a pointer, not a finding. Simon Lucas's co-authors here are not his usual collaborators, which may indicate a different group.

### ★ Stack More Levels: How to Get General and Human-Like Mario Playing
- **Authors**: Shinichi Arimura, Yuchen Li, Julian Togelius
- **Affiliation**: Togelius is at **NYU Game Center**; Arimura and Li are his students there. CoG page gives superscripts only. **(tentative — verify against the published version)**
- **Venue**: **IEEE CoG 2026**, paper #394, *Game Design and Technology*.
- **Link**: https://cog2026.org/acceptedpapers (no arXiv preprint located)
- **Abstract and key innovations**: a title that states the whole thesis — **generality and human-likeness as the target, not high score**. Three game AI papers this window (this one, MAPLE, §2's Wayfarer-adjacent work) are all asking why beating a game is easier than playing it plausibly, and this one takes the player-behaviour side.
- **Why it matters here**: Togelius's group has produced a disproportionate share of this wiki's PCG and benchmark entries; this extends that line into gameplay. Notable as **arXiv-independent** output — CoG-only.
- **Caveats**: no abstract located; no result available to assess. **"Yuchen Li" here is not the CoG #129 MAPLE co-author** despite the identical name — a reminder that name matching is not identity matching in these proceedings pages.

---

## §2 Game AI Bot — NPCs, Agents, and Interaction

### ★★★ Why Do LLMs Struggle in Strategic Play? Broken Links Between Observations, Beliefs, and Actions
- **Authors**: Jan Sobotka, Mustafa O. Karabag, Ufuk Topcu
- **Affiliation**: **EPFL** (Sobotka; work completed during a stay at UT Austin) and **University of Texas at Austin** (Karabag, Topcu).
- **Venue**: arXiv:2605.00226 — **revised 17 Sep 2026**, which places the current version inside this run's rolling window. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2605.00226
- **Abstract and key innovations**: decomposes LLM failure in incomplete-information games into **two named gaps**, tested on open-weight **Llama 3.1, Qwen3, and gpt-oss**. **Observation–belief gap**: the model's *internal* representations of latent game states are **substantially more accurate than its own verbal reports**, but those internal beliefs are **brittle** — accuracy **degrades with multi-hop reasoning**, shows **primacy and recency biases**, and **drifts away from Bayesian coherence over extended interaction**. **Belief–action gap**: the implicit conversion of internal beliefs into actions is **weaker than the same beliefs when externalized into the prompt**, and **neither conditioning route reliably produces higher payoff** — while **acting optimally on the decoded beliefs would improve payoffs in ~95%** of games. Tasks are framed as negotiation and policymaking as well as games.
- **Why it matters here**: this is the **mechanistic counterpart to §5.1's XiangqiBench** and the two should be read together. XiangqiBench reports a ~26-point conversion gap between finding a move and winning; this paper explains *why* — the failure is not in the representation but in **getting the representation out of the model and into the action**, and the belief is better than the report. **That is a diagnosis with a concrete implication: probe the representation, not the transcript.** It also states a result that ought to be uncomfortable: the correct-belief policy wins in 95% of games, and no amount of prompt-level belief conditioning recovers it.
- **Caveats**: preprint, unreviewed. Models tested are open-weight midsize models — **frontier models were not evaluated**, and the observation that representations beat reports may not survive at a capability level where the verbal channel is already near-ceiling. "~95%" is truncated in the abstract and the exact figure depends on the decoding procedure. This digest's own reader-side lesson applies: **if belief accuracy is what matters, then any evaluation that reads only the transcript is measuring the weaker channel.**

### ★★ Text2BT: A Baseline Study on LLM-Agent-Based Behavior Tree Generation for Game Character AI
- **Authors**: Ray Ito, Naoyuki Jimbo, Koya Ihara
- **Affiliation**: **Square Enix** (game development division). *This is inferred from the well-documented Square Enix AI Research ↔ academic publication record of these authors and is **tentative** — it is not printed on the proceedings page, which carries superscripts only.* Ray Ito is additionally the author of the "Game AI Is Not Fun" critique of LLM game-agent work that this wiki's lineage references.
- **Venue**: **IEEE CoG 2026**, paper #371, *Game Design and Technology*.
- **Link**: https://cog2026.org/acceptedpapers (no arXiv preprint located across 11 title-search variants)
- **Abstract and key innovations**: LLM agents generate **behavior trees** for game characters. The word **"Baseline"** in the title is the finding: the authors are positioning LLM-generated BTs as a *reference point*, not a win.
- **Why it matters here**: **behavior trees are the incumbent production representation for game character logic**, and they are the standard against which any LLM-authored character controller has to be judged. A shipped AAA title will not accept a Python policy. The publisher affiliation, if correct, means this is a **production-side evaluation** — the lane in which §6's industry talks also sit, and the lane with the fewest papers and the most consequence.
- **Caveats**: **no abstract, no numbers, affiliation unverified.** "Baseline study" strongly suggests a modest result; do not cite this as evidence that BT generation is solved or unsolved until the paper is read.

### ★★ Aligned but Not Partner-Specific: How Multimodal LLM Agents Succeed in Reference Games Without Forming Conceptual Pacts
- **Authors**: Po-Ya Angela Wang, Chinmaya Mishra, Aslı Özyürek, Paula Rubio-Fernández, Esam Ghaleb
- **Affiliation**: Co-Intelligence Humanities AI Future Lab and Graduate Institute of Linguistics, **National Taiwan University** (Wang); **Max Planck Institute for Psycholinguistics**; **Donders Institute for Brain, Cognition and Behaviour, Radboud University** (Özyürek); **Institut Jean Nicod, Paris** (Rubio-Fernández); MPI (Ghaleb). Recovered from the **PDF title block**.
- **Venue**: arXiv:2606.08081 (1 Oct 2026) — cs.CL, cs.AI.
- **Link**: https://arxiv.org/abs/2606.08081
- **Abstract and key innovations**: repeated reference games test whether interlocutors replace long descriptions with **short, partner-specific expressions grounded in shared history** — **conceptual pacts**. Prior work established that multimodal LLMs **fail to become more efficient across rounds while still aligning on labels**; this paper asks the sharp follow-up: **does that label alignment reflect partner-specific grounding, or just a shared task vocabulary?** The methodological contribution is a **pragmatically constrained pseudo-dyad baseline** — rounds from *two different real dyads* describing the same target at comparable trajectory positions are paired, preserving referential task structure while **removing shared partner history**. Against human dyads from the **KTH Tangrams corpus** across three measures (task competence, description strategy, alignment dynamics), the result is a clean dissociation: **humans reduce effort through entrainment** — compressing descriptions and increasing label alignment *with partners* — whereas **agents hold effort fixed and stay verbose**.
- **Why it matters here**: this is a **measurement-validity result**, and it invalidates a specific inference that has been circulating. "The agents' labels converged" has been read as evidence of emergent communication or shared grounding. **This paper shows the convergence survives deleting the partner, which means it was never evidence of partner-specific grounding at all.** The negative result is the valuable part: a benchmark can pass an alignment check while the underlying social phenomenon is absent.
- **Caveats**: reference games are a laboratory instrument, not a game. The pseudo-dyad construction is a clever approximation, not a perfect control — pairing on target and trajectory position cannot fully equalize partner familiarity, and the "no partner history" condition is synthetic. Preprint, unreviewed.

### ★★ Communication between Frozen Large Language Models via Prompt Optimization in a Referential Game
- **Authors**: Vivek Anand, Muthu Chandrasekaran, Shiva Chaitanya
- **Affiliation**: School of Electrical and Computer Engineering, **Georgia Institute of Technology** (Anand); **Interactly.ai** (Chandrasekaran, Chaitanya). Recovered from the **PDF title block**.
- **Venue**: arXiv:2609.31989 (25 Sep 2026) — cs.CL, cs.AI. **42 pages (26 main), 10 figures, 17 tables.**
- **Link**: https://arxiv.org/abs/2609.31989
- **Abstract and key innovations**: two **frozen** LLMs from **different providers with different tokenizers**, accessed only through their API endpoints, play a referential game — one describes an object in a short fixed-length message over a small alphabet, the other picks it from a candidate set. **No weights are updated.** Each agent's prompt is rewritten by an isolated prompt optimizer whose reflection model reads only that agent's own scored interactions. Results are reported with unusual candour: in the **positional** setting, optimized prompts carry a shared code that **generalizes to held-out objects above a measured no-codebook baseline, including when the memory window is removed**; in a second setting **independent per-letter blocks no longer fit within the message, although a whole-object place-value code does**. The base system **fails** to establish reliable communication — the sender cannot retain an injective rule and the receiver has too few confirmed examples — and a **sender collision penalty, retention of successful interactions, and sequential optimization** enable successful place-value communication **in some runs**. Outcomes **vary across runs and across reflection models**, and in successful runs the discovered protocol is **written into the optimized prompt**.
- **Why it matters here**: read against §2.3, this is the **same failing component isolated**. If multimodal agents show label alignment without partner-specific grounding (§2.3), then a frozen-model referential game is the cleanest possible test of whether *any* grounding mechanism exists without weight updates. The answer this run found is **weakly yes, and unreliably**: protocol emergence requires an explicit collision penalty to repair the sender's injectivity failure, depends on the reflection model, and does not survive across runs. Emergent communication from frozen LMs is therefore **possible but not robust**, which is a much weaker claim than the headline framing invites.
- **Caveats**: the framing overstates for what is measured — with **prompt-level codebook search permitted**, a short fixed-length code over a small alphabet is solvable by construction, so the interesting content is entirely in *which* codes emerge and *how unstable* that is. Cross-vendor API dependence makes results non-reproducible without archived endpoints. Prompt optimization is credited with the protocol, and it is not separable from the optimizer's search over codes.

### ★ FlashLore: Graph-Structured and Closed-World Grounded Memory for Believable Game NPCs
- **Authors**: Zhaoyou Liu (sole author)
- **Affiliation**: not printed on the proceedings page.
- **Venue**: **IEEE CoG 2026**, paper #194, *Game Design and Technology*.
- **Link**: https://cog2026.org/acceptedpapers (no arXiv preprint located)
- **Abstract and key innovations**: **closed-world** memory for NPC dialogue, organized as a **graph** rather than a flat store. "Closed-world" is the load-bearing constraint: the NPC's knowledge is bounded by what the game has established, which is a **narrative-consistency** requirement rather than a retrieval one.
- **Why it matters here**: the memory literature feeding game NPCs has been overwhelmingly *open*-retrieval in design (§2's FlashLore sits against the claimed MEMO memory-augmented LLM games paper). A **closed-world** design is the correct shape for a shipped game — an NPC that recalls an event the game never established is a bug — and this wiki has not previously recorded that distinction being made explicitly.
- **Caveats**: **single author, no abstract, no evaluation visible.** "Believable" in the title is an aspiration; nothing here establishes a behavioural gain.

**→ §2 note (Ambient NPCs):** CoG 2026 also accepted **"A Memory-Driven Action Selection Framework for Scalable Ambient NPC Behavior"** (paper #43, Eric Buitron Lopez and Roberto Solis-Oba) — NPC action selection for *scale*, i.e. the population-performance half of the same problem FlashLore addresses from the consistency side. Recorded, not featured; no abstract.

---

## §3 Game Foundation Models & World Models

### ★★★ Bridging the Generalization Gap in Open-Ended Game Worlds: Multi-Agent LLM Reasoning in Neural MMO 2
- **Authors**: Olca Orakci, Elif Surer
- **Affiliation**: not printed on the proceedings page.
- **Venue**: **IEEE CoG 2026**, paper #34, *AI for Game Playing*.
- **Link**: https://cog2026.org/acceptedpapers (no arXiv preprint located)
- **Abstract and key innovations**: multi-agent LLM reasoning in **Neural MMO 2**, framed explicitly as bridging a **generalization gap** in **open-ended game worlds**.
- **Why it matters here**: **Olca Orakci authored the Orak game-agent framework (`2506.03610`), which this wiki already holds** — recorded in the 10-04 digest's §9.1 collision list as "Orak game agent framework ZJU/Huawei." This is the **same first author, three years of work later, on the open-ended multi-agent setting**, and it goes to CoG rather than arXiv. That is a **direct continuity thread from a claimed paper to an unclaimed, peer-reviewed successor**, and it is the single most useful bibliographic find in this run: it links the arXiv record to the proceedings record for the same research programme.
- **Caveats**: **no abstract, no numbers.** The ZJU/Huawei affiliation recorded for the earlier Orak paper is **not** carried over here — do not assume it. Whether the "generalization gap" is about scale, world-size, or policy reuse is unknown until the paper is read.

### ★★ Foundation Models as World Models: A Foundational Study in Text-Based GridWorlds
- **Authors**: Remo Sasso, Michelangelo Conserva, Dominik Jeurissen, Paulo Rauber
- **Affiliation**: School of Electronic Engineering and Computer Science, **Queen Mary University of London**, UK. Recovered from the **PDF title block**.
- **Venue**: arXiv:2509.15915 — comment field: **"20 pages, 9 figures. Accepted for presentation at the 39th Conference on Neural Information Processing Systems (NeurIPS 2025) Workshop on Embodied World"**. **Also accepted at IEEE CoG 2026, paper #46.** *(A NeurIPS workshop, then CoG — the double acceptance is the kind of thing that inflates apparent venue strength, and is reported as printed rather than reconciled.)*
- **Link**: https://arxiv.org/abs/2509.15915
- **Abstract and key innovations**: evaluates two ways of putting a foundation model inside an RL framework, and the **distinction between them is the contribution**. **Foundation world models (FWM)**: exploit the FM's prior knowledge to enable **training and evaluating agents with simulated interactions** — i.e. the FM substitutes for expensive real interaction. **Foundation agents (FA)**: exploit the FM's **reasoning** for decision-making directly. Evaluated on a **family of gridworld environments chosen to suit current LLM generation ability**. Three findings: **improvements in LLMs already translate into better FWMs and FAs**; **FAs based on current LLMs can already provide excellent policies for sufficiently simple environments**; and **coupling FWMs with RL agents is highly promising for more complex settings with partial observability and stochastic elements**.
- **Why it matters here**: this supplies the **missing half of the world-model-as-game-testbed argument** the 10-04 digest referenced. "Use games as a world-model testbed" (claimed) only works if the game is cheap; "use an FM to simulate interaction so games need not be real" (here) is the mechanism. The third finding is the practically important one and it is the most qualified: **the coupling pays off exactly where the FA route fails — partial observability and stochasticity** — which is also exactly where every serious game environment lives. Gridworlds are a long way from NetHack.
- **Caveats**: **gridworlds are not games**; the authors are explicit that the environment family was chosen to match LLM generation ability, which is a confound and an admission. "Excellent policies for sufficiently simple environments" has no stated threshold. Workshop paper, and the CoG version's abstract is not separately available — the two venues may have different content.

### ★★★ World Editing: Intervening on Executable Worlds at Increasing Depth — IGMWorld / IGMBench
- **Authors**: Max Ku, Nok-Kan Law, Yu-Chien Tang, Shih-Ying Yeh, Ping Nie, Andy Zheng, Tat Hei Lai, Fei-Yueh Chen, Nikko Yu, Wei-Chieh Sun, Suzy Huang, Chiao-Wei Hsu, Chih-Chuan Huang, Chak-Wing Mak, Ho Yin Sam Ng, Edisy Kin Wai Chan, Min-Hung Chen, Ho Kei Cheng
- **Affiliation**: **University of Waterloo** (Ku, Law, Tang, Yeh); **`G-G-G`** — a literal placeholder string appearing in this position in **both the PDF and the HTML**, unresolvable from the record; **Comfy Org Research**; **National Taiwan University**; **University of Illinois Urbana-Champaign**. **The `G-G-G` slot is reported verbatim and is deliberately not guessed** — see §9.4.
- **Venue**: arXiv:2610.02331 (1 Oct 2026) — cs.AI, cs.CV, cs.LG. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.02331
- **Abstract and key innovations**: introduces **IGMWorld**, an executable-world framework, and **IGMBench**, a benchmark of **110 tasks across Minecraft and Terraria** with **more than 1,100 executable criteria**. The core idea is **intervention depth**: rather than only asking whether an agent can act in a world, the benchmark **intervenes on the world itself at increasing depth** — editing world state, then world dynamics, then deeper — and measures how reliability degrades as the intervention goes further in. The reported pattern is that the strongest configuration solves **~78% of tasks under strict task-level criteria**, while reliability falls sharply under **joint visual criteria** and as intervention depth increases.
- **Why it matters here**: this is the **hardest evaluation target in the digest** and the only paper that treats *world editing* as the primitive rather than world *play*. Every other world-model paper here scores an agent on what it does; IGMWorld scores whether a **scaffolded edit to the world** produces the intended consequence. The **78.2% → below 50%** degradation is also the most useful *negative* datum in this digest: **reliability is not flat in intervention depth**, which is precisely the assumption a deployable "executable world model" needs to survive. Combined with §3.2's finding that FM/RL coupling matters under partial observability, this says the world-model lane's bottleneck is **edit verification**, not generation.
- **Caveats**: 18 authors spanning four-plus institutions, one of which is a placeholder — **organizational opacity is itself a signal** and this digest will not paper over it. Minecraft/Terraria via Comfy Org suggests a **non-academic, possibly product-facing** setting, which may explain both the scale (1.1K criteria is a large annotation effort) and the missing affiliation. Preprint, unreviewed. The 78.2% figure is against a configuration the authors chose; without the baselines this number is not a leaderboard entry.

---

## §4 Procedural Content Generation

### ★★★ MIPCGRL: Multi-Objective Instruction-Aware Representation Learning in PCG Reinforcement Learning — venue update
- **Authors**: Sung-Hyun Kim, Geum-Hwan Hwang, In-Chang Baek, Seo-Young Lee, Kyung-Joong Kim
- **Affiliation**: as recorded in the 2026-07-15 and 2026-07-30 digests that first covered this paper. **Not re-derived in this run.**
- **Venue**: arXiv:2508.09193 — **nominated #217 for the IEEE CoG 2026 Best Paper Award**, under the title *"Multi-Objective Instruction-Aware Representation Learning in Procedural Content Generation Reinforcement Learning."*
- **Link**: https://arxiv.org/abs/2508.09193
- **Why it is listed here and not re-summarized**: this paper has been covered in **four** earlier digests (`2026-07-15`, `2026-07-30`, `2026-08-17`, `2026-08-19`) and is excluded from the featured count accordingly. **What is new is the venue**: a Best Paper Award nomination is the strongest quality signal any game-PCG paper in this wiki has received, and it materially raises the status of the prior coverage. **The recommendation is to upgrade this wiki's standing claim about MIPCGRL from "well-argued mechanism, no head-to-head number" (10-04 §8.2) to "peer-nominated, still without a head-to-head number against an autoregressive generator."**
- **Caveats**: a nomination is not an award, and the CoG version may differ from the arXiv v1 the earlier digests summarized.

### ★★ Judging the Imitation Game: Exploring Creator Bias in VLM-Based PCG Level Evaluation
- **Authors**: Yucheon Park, Geum-Hwan Hwang, Kyung-Joong Kim
- **Affiliation**: not printed on the proceedings page. **Note**: Hwang and Kim are MIPCGRL's (§4.1) co-authors — **the same PCG group produced both the nominated generator and this evaluation-validity critique.**
- **Venue**: **IEEE CoG 2026**, paper #399, *PCG*.
- **Link**: https://cog2026.org/acceptedpapers (no arXiv preprint located)
- **Abstract and key innovations**: **creator bias** in VLM-based PCG level evaluation — whether VLM judges of generated levels systematically favour levels resembling their **generator's** output distribution, independent of playability. This is an **evaluation-of-evaluation** paper, and the 10-04 digest's §8.2 identifies exactly this as the missing piece in the PCG lane.
- **Why it matters here**: §8.2 of the 10-04 digest argued that the PCG-RL literature has **a well-argued mechanism and no head-to-head number**, and that both MIPCGRL and PlayTrain independently treat "a human can immediately play and evaluate it" as the property that makes generation verifiable. **This paper attacks the human/VLM-verification route directly**: if the judge is biased toward the generator, then human-playability and VLM-score are not independent evidence, and every controllability number measured through an automatic judge inherits the bias. **A group that has shipped a strong PCG generator publishing a critique of automatic evaluation of PCG generators is a sign the lane has reached maturity.**
- **Caveats**: **no abstract, no effect size.** The bias could be small or could invalidate the evaluation literature; unknowable from the title.

### ★★ RuleSweeper: Procedurally Generating Gameplay Mechanics in Minesweeper
- **Authors**: Ryan Fleishman, Shresth Kapoor, Teddy Clark, Jan Borowski, Timothy Merino, Julian Togelius
- **Affiliation**: Togelius at **NYU Game Center**; Fleishman, Borowski, Merino are his group. **(tentative — verify against the published version)**
- **Venue**: **IEEE CoG 2026**, paper #440, *PCG*.
- **Link**: https://cog2026.org/acceptedpapers (no arXiv preprint located)
- **Abstract and key innovations**: procedurally generates **gameplay mechanics** — not levels — in Minesweeper. The distinction is the contribution: given a base game, **discover rule variants** programmatically rather than authoring them.
- **Why it matters here**: this wiki's entire PCG corpus is **level** generation — terrain, layouts, trajectories. **Mechanic generation is the harder and largely unmeasured problem**, and it is where the design-space argument in §4.3 has to land. Minesweeper is a well-chosen substrate: its rule space is small enough to search and combinatorial enough to be non-trivial, and the safety property (no unbounded losses) makes exhaustive evaluation possible.
- **Caveats**: no abstract; a single base game; "procedurally generating mechanics" is a phrase that could cover a wide range of method strength.

### ★ Beyond Playability: A Design-Space Perspective on Persistent Spatial Intent in Co-Creative PCGRL
- **Authors**: Min-Sung Park, Dae-Wook Kim, Shinjin Kang, Si-Hwan Jang
- **Affiliation**: Jang is at **KAIST**; **(tentative — verify against the published version)**
- **Venue**: **IEEE CoG 2026**, paper #412, *PCG*.
- **Link**: https://cog2026.org/acceptedpapers (no arXiv preprint located)
- **Abstract and key innovations**: argues that **playability is the wrong objective function for co-creative PCGRL**, and proposes **persistent spatial intent** as the design-space variable instead — the generator must hold a spatial commitment across the session rather than optimizing an instantaneous playability score. "Design-space perspective" signals a position/framework paper more than a results paper.
- **Why it matters here**: it is the direct theoretical counterpart to §4.2. If VLM/human judges are biased toward the generator's distribution (§4.2), then **"maximize playability" is itself a biased target**, and a co-creative setting needs an objective about *what the generator was asked to commit to*. The phrase "persistent spatial intent" is the first formulation in this digest of intent as a first-class PCGRL variable.
- **Caveats**: no abstract; a design-space paper is often pre-empirical, and the title's own hedge ("a perspective") is honest about that.

---

## §5 Benchmarks and Evaluation

### ★★★ Finding the Move Is Not Winning the Game: XiangqiBench for Closed-Loop Evaluation of LLM Agents
- **Authors**: Yekun Chai, Qiwei Peng, Haoyi Xiong
- **Affiliation**: **none stated.** The PDF and abs record carry **no institutional line and no affiliation span**. The arXiv HTML render additionally **drops two of the three authors from the author block**, showing only Haoyi Xiong — the abs page lists all three. **Do not infer an affiliation.**
- **Venue**: arXiv:2610.02425 (1 Oct 2026) — cs.CL. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.02425
- **Abstract and key innovations**: the title states the thesis. Constructs **119 tactical endgame positions** in **Xiangqi (Chinese chess)** and measures **closed-loop** play rather than move ranking. The corpus yields **8,568 multi-turn trajectories** across **12 frontier LLMs**. Three distinct signals are separated: a **conversion gap** between identifying the correct first move and converting it into a win (**26.1% vs 13.9%** on the reference metric); a **consistency gap** between `pass@3` and `pass^3` when leading (**38.7% vs 5.9%**); and a third signal concerning play consistency under multi-turn interaction.
- **Why it matters here**: **this is the best-designed game-agent evaluation encountered in this series**, and it earns ★★★ on method rather than result. The design move — **separate "can find the move" from "can play the game"** — is the single conceptual gap that MAPLE (§1.1), Wayfarer (§1.3), and §2's strategic-play paper all independently arrive at. The **`pass@3` vs `pass^3` distinction is the sharpest instrument in the digest**: it measures whether an agent's own reported confidence is *calibrated across a conversation*, and a 38.7% → 5.9% collapse says the multi-turn transcript is not the right place to read model state. Combined with §2.1's observation that internal representations beat verbal reports, **two papers in one window independently conclude that the transcript understates the model.** For a wiki whose recurring methodological finding is that agent evaluations are mis-specified, this is the best available instrument for fixing one.
- **Caveats**: **no affiliation on any of three authors** is unusual for a benchmark paper of this scope and materially weakens reproducibility assessment — there is no lab to contact and no prior work to attribute the design to. Endgames only, so it says nothing about opening or midgame play, and Xiangqi has a large literature of engine-assisted play, which raises the question of how the reference move set was produced and whether it is engine-derived. 12 frontier LLMs is a September-2026 snapshot. The third signal is truncated in the abstract.

### ★★★ Language Models that Play Chess and Explain Their Moves — Queen
- **Authors**: Adithya Bhaskar, Jeffrey Cheng, Danqi Chen
- **Affiliation**: **Princeton Language and Intelligence, Princeton University** (all three). Recovered from the **PDF title block**. Danqi Chen leads Princeton's NLP group, which is also the group behind the **Qwen** model family this paper's 4B backbone belongs to — a relevant disclosure for reading §5.2's critique of move-explanation quality.
- **Venue**: arXiv:2610.03695 (2 Oct 2026) — cs.CL. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.03695
- **Abstract and key innovations**: a **4B-parameter** chess-playing language model that **also explains its moves**, reaching **typical-grandmaster strength** and reporting a **~900 Elo gain** over an unspecified baseline. Architecture: an **encoder–decoder design where the chess state is injected by cross-attention**, plus **iterative distillation** from a stronger teacher over successive iterations, and — the distinctive piece — a **natural-language analogue of the Bellman update**, in which the model revises its assessment in words rather than only through value heads.
- **Why it matters here**: at **4B parameters** this is the smallest model in the digest to reach grandmaster-class chess, and it is **three orders of magnitude below AlphaZero-scale** — independent corroboration of the 10-04 digest's §8.3 finding that **strength is engineering-bound, not compute-bound**. The **explanation is trained, not prompted**, which makes it comparable to §2.1's internal-belief findings: this paper is claiming the *verbal report is made faithful by training*, whereas §2.1 finds the verbal report *unfaithful by default*. **The two results together define the open question**: does explanation-faithfulness have to be trained in, or can it be read out? The natural-language Bellman update is the most interesting mechanism in the digest for anyone building a self-reflecting agent.
- **Caveats**: the ~900 Elo figure's **baseline is not stated in the abstract** and "typical grandmaster" is a skill-band label, not an Elo claim against a fixed engine; **no tournament or engine ladder is described**, so this is not comparable to the fixed-node Stockfish methodology of the claimed 10-04 chess paper. Explanation quality is assessed by the authors' own method and no faithfulness measure is stated in the abstract. Affiliation disclosure: Princeton authored Qwen, so a favourable Qwen-backbone result should be read with that in mind.

### ★★★ RefGlitch-Bench: A Benchmark for Reference-based Gameplay Glitch Detection with Vision-Language Models
- **Authors**: Yakun Yu, Ashley Wiens, Adrián Barahona-Ríos, Benedict Wilkins, Saman Zadtootaghaj, Nabajeet Barman
- **Affiliation**: **University of Alberta** (Yu, Wiens) and **Sony Interactive Entertainment** (the remaining four).
- **Venue**: arXiv:2604.11082. **No venue acceptance claimed in the arXiv record** — but see §6.2, where four of these six authors present the **same QA-evaluation agenda at CoG 2026**, which is strong indirect evidence that this line of work is peer-reviewed.
- **Link**: https://arxiv.org/abs/2604.11082
- **Abstract and key innovations**: **reference-based** detection of **gameplay glitches** by VLMs — the model is given a reference of correct behaviour and must identify deviations. Gameplay glitches are the QA failure mode that is **obvious to a human playing and invisible to a rule-based checker**, which is what makes it a VLM task.
- **Why it matters here**: this is **industrial game AI with an academic affiliation attached**, and it is the concrete instance of §6's central finding — studios do not need agents that play well, they need **agents that notice when something is wrong**. It is also the natural counterpart to §5.3: Queen asks whether a model can *act* correctly in a game, RefGlitch-Bench asks whether it can *notice* incorrectness. Both are evaluation problems dressed as capability problems, and both come from the same month.
- **Caveats**: **no venue acceptance**; glitch-detection accuracy on a Sony-internal corpus is likely not reproducible from the paper alone, and the benchmark's difficulty calibration is unverifiable from the abstract. Filed at ★★★ for industry relevance rather than for a state-of-the-art claim.

### ★★ LM Fight Arena: Benchmarking Large Multimodal Models via Game Competition
- **Authors**: Yushuo Zheng, Tongrui Ye, Zicheng Zhang, Xiongkuo Min, Huiyu Duan, Guangtao Zhai
- **Affiliation**: **Shanghai Jiao Tong University**; **Shanghai AI Lab**; **Tongji University**.
- **Venue**: arXiv:2510.08928 — **v1 10 Oct 2025, revised 16 Sep 2026 (v2)**, which is what places this inside the rolling window. The revision date is the only newness; **the work is a year old.**
- **Link**: https://arxiv.org/abs/2510.08928
- **Abstract and key innovations**: pits LMMs against each other in **Mortal Kombat II**, with **all agents controlling the same character** to control for character-specific strength, and frames being passed to the model for action selection. Six leading open- and closed-source models in a **controlled tournament**; positioned as an alternative to static evaluation for **real-time adversarial** settings.
- **Why it matters here**: **same-character control is the design detail that makes this usable**, and it is the control §1.1's Elo comparisons and §5.1's `pass@3` figures both lack. Two years of "LLMs play games" papers have compared agents across *different* games; holding the character fixed removes the most obvious confound. Worth noting as a **backfill** with an explicit caveat: the v2 revision is new, the paper is not, and a tournament of six models against a 1993 arcade title is a long way from a general agent benchmark.
- **Caveats**: Mortal Kombat II is a fighting game whose input space is small and highly exploitable; **"strategic reasoning" is a stretch** for a 2D fighter. Frame-by-frame prompting of a multimodal model is not real-time play. No v2 changelog is available in the abstract, so what changed in the September 2026 revision is unknown.

### ★★ WMAttack: Automated Attack Search for Adversarial Evaluation of World-Model Agents
- **Authors**: Zhixiang Guo, Siyuan Liang, Shi Fu, Cheng Guo, Andras Balogh, Mark Jelasity, Dacheng Tao
- **Affiliation**: **Nanyang Technological University**, Singapore (Guo, Fu, Balogh, Jelasity, Tao — author email `@e.ntu.edu.sg`), with additional co-authors at the **University of Szeged** (Liang, Guo).
- **Venue**: arXiv:2605.23220 — **v1 22 May 2026, revised 5 Sep 2026 (v2)**.
- **Link**: https://arxiv.org/abs/2605.23220
- **Abstract and key innovations**: adversarial robustness of **world-model agents** is underexplored because evaluating it is hard — **weak manually-tuned attacks overestimate robustness, and exhaustive hyperparameter search is prohibitively expensive** because each candidate needs **closed-loop rollouts through learned latent dynamics**. WMAttack formulates robustness evaluation as a **finite-budget search over attack configurations** (family, perturbation budget, optimization steps, restarts, allocation rules). **Self-Correcting Attack Search (SCAS)** refines the attack proposal distribution using feedback from **reward degradation, action instability, runtime cost, and rollout variability**; **Representation-Guided Attack Retrieval (RGAR)** reuses effective historical configurations.
- **Why it matters here**: §3 established that this digest's world-model papers are **not yet verified to be causally faithful**, and §1.1/§5.1 established that **evaluation instruments are the bottleneck**. WMAttack attacks that bottleneck directly: it is **an evaluation paper about evaluation**, and it argues the specific methodological point that **an undefeated world-model agent is more likely a weak attack than a strong agent.** The multi-signal SCAS feedback (reward, action instability, cost, variance) is also a practical recipe for anyone who has tried to tune a single scalar adversarial objective. Both the game-RL and general embodied literature need this.
- **Caveats**: **not a game paper** — filed in §7. Robotics-adjacent; included because world-model agents are the shared substrate with §3. Two of twelve authors' affiliations are inferred from a single shared domain and a second institution name recalled rather than read from the title block; **verify before citing.** v2's changes are not described in the abstract.

### ★★ PuzzleJAX — venue update
- **Authors**: Sam Earle, Graham Todd, Yuchen Li, Ahmed Khalifa, Muhammad Umair Nasir, Zehua Jiang, Andrzej Banburski-Fahey, Julian Togelius
- **Venue**: arXiv:2508.16821 — **accepted at IEEE CoG 2026** (also held at **CoG 2026**, per the 10-08-27 digest's coverage). Covered previously in `wiki/synthesis/2026-08-27/game-rl-daily.md`; **excluded from the featured count, listed here for the venue.**
- **Link**: https://arxiv.org/abs/2508.16821
- **Why it is listed and not re-summarized**: the arXiv record (2508.16821) already carries **"Accepted for oral presentation at IEEE CoG 2026"** and the paper has prior coverage. **The recommendation is to update the 08-27 entry's venue field from "arXiv preprint" to "CoG 2026 (oral)"** — it is currently recorded without the acceptance.

### ★ Do Vision-Language Models Understand Human Engagement in Games?
- **Authors**: Ziyi Wang, Qizan Guo, Rishitosh Kumar Singh, Xiyang Hu
- **Affiliation**: **Texas A&M University** (Wang); **University of Southern California** (Guo); **Arizona State University** (Singh, Hu). Recovered from the **PDF title block**, which gives the fuller name **Rishitosh Kumar Singh** against the shorter "Rishitosh Singh" on the abs page. *(`2603.18480` — prior runs recorded this affiliation as Texas A&M + Surrey; that was **wrong**, and is corrected here.)*
- **Venue**: arXiv:2603.18480 — comment field: **"EMNLP 2026 Oral (2.6% acceptance)"**. **A top-2.6% oral at a flagship NLP venue.**
- **Link**: https://arxiv.org/abs/2603.18480
- **Abstract and key innovations**: can VLMs infer **latent psychological engagement** from gameplay video alone? Using the **GameVibe Few-Shot dataset** across **nine first-person shooters**, three VLMs are evaluated under **six prompting strategies** including zero-shot, **theory-guided prompts grounded in Flow, GameFlow, Self-Determination Theory and MDA**, and retrieval-augmented prompting — evaluated on both **pointwise engagement prediction** and **pairwise prediction of engagement change between consecutive windows**. Results are almost entirely negative: **zero-shot VLM predictions are generally weak and often fail to beat a per-game majority-class baseline**; memory/retrieval augmentation helps pointwise prediction **in some settings**; **pairwise prediction remains consistently difficult**; and **theory-guided prompting alone does not reliably help and can reinforce surface-level shortcuts.** The authors name the result a **perception–understanding gap**.
- **Why it matters here**: a **2.6% oral at EMNLP** is a stronger quality signal than most of the arXiv papers in this digest, and the finding is the **third independent confirmation in one window that a plausible measurement instrument does not work**: §5.1's `pass@3` vs `pass^3` collapse, §2.3's pseudo-dyad result, and here VLM judges failing to beat majority class on a psychological construct. **In all three cases the instrument was doing the work, not the model.** The explicit finding that **theory-grounded prompting reinforces shortcuts** is the sharpest version: encoding MDA into the prompt did not make the model reason about MDA.
- **Caveats**: engagement is self-reported in GameVibe and ground-truth labels inherit annotator subjectivity; nine FPS titles is a narrow domain and FPS engagement may be atypical; the negative result is robust but its *mechanism* is not identified.

### ★ RePAIR — venue update
- **Authors**: Christoph Koller, Johannes Fürnkranz, Timo Bertram
- **Venue**: arXiv:2606.11860 — comment field: **"Accepted for oral presentation at IEEE CoG 2026."** Covered previously in `wiki/synthesis/2026-06-11/arxiv-daily.md` and `2026-06-15/game-rl-daily.md`; **excluded from the featured count, listed for the venue.**
- **Link**: https://arxiv.org/abs/2606.11860
- **Why it is listed and not re-summarized**: **an oral at CoG 2026 for a chess representation-learning paper is a meaningful upgrade** and the prior entries record it as a preprint.

---

## §6 Industry Game AI

### ★★★ IEEE CoG 2026 Accepted Industry Talks — five RL/agent-relevant production deployments
- **Authors / speakers** (as listed; all are talks, not papers, and **no abstracts are published**):
  | Talk | Speaker | Organisation |
  |---|---|---|
  | GARP: Real-Time Generative Agents on Local Hardware in a Game Engine | Piero Molino, Patrick John Chia, Federico Bianchi, Jonathan P. Chen, Paul Szerlip | **Studio Atelico** |
  | What should I do? An Experimental Onboarding Advisor for *Total War: Pharaoh* | Alexander Zap | **Wargaming Group Limited** |
  | Teaching tanks to behave — how to use Reinforcement Learning and get better every day | Nathaly Kalantar | **Replay Masters EU** |
  | Prompt-to-Prototype: LLM-Driven Authoring of Enemy Behaviors in Unreal Engine | Paolo Maninetti | **Reply** |
  | Own Your Game — Ethical On-Device AI for Developers | Sam Harris, Ambrose Robinson | **Parable Studios** |
  - **Also accepted** (relevant, not featured): *From Scripted Content to Systemic Narrative* (John Lewis, Rijk Groenewoud — **LoreWeaver**); *From Rules to Rulings: How Agentic AI Restores the Board Game Advantage to Digital Games* (Chris Brown — **Kythera AI**); *Climbing Up The Walls* (Alex Kearney — **Artificial.Agency**); *Teaching Game Design Through Hybrid Play* (Diana Kulich, DJ Human, Jonathan Bödewadt-Pedersen — **Raw Power Labs**).
- **Affiliation**: the organisations above **are** the affiliation — these are industry talks, presented by the deploying team.
- **Venue**: **IEEE CoG 2026**, Accepted Industry Talks track. Conference held **1–4 Sept 2026, Madrid**; **"the proceedings will be published after the conference on IEEE Xplore."** Talk abstracts and slides are **not published**.
- **Link**: https://cog2026.org/acceptedpapers
- **What the slate says, read as a set**: **four of eight talks are on-device or local** (GARP on local hardware, Parable Studios on-device, Artely.AI, Replay Masters) and **three are LLM-authored content in an engine** (Unreal enemy behaviours, Total War onboarding advice, emergent narrative). The most interesting single item is **GARP**: real-time generative agents **inside a game engine, on local hardware** — this is the "believable NPC at frame rate, no API call" problem that §2's FlashLore addresses academically. The most on-topic for this wiki is **Wargaming's *Total War: Pharaoh* onboarding advisor**: an LLM agent whose job is to **answer a player's question about what to do next in a strategy game** — that is XiangqiBench's and Queen's problem (advising play) deployed at AAA scale.
- **Why it matters here**: **this is the industry lane, populated, from the deploying studios themselves.** The 10-04 digest's §5 SLR found that game-domain solutions to code quality "exist but are not adopted" and concluded industry's binding constraint is **organizational, not algorithmic**. These talks are the counter-evidence at the *game-AI* level rather than the *code-quality* level: five studios got RL/LLM agents into production in 2026. **No results are published, so no claim about effectiveness is possible** — this section is evidence of *activity*, not of *success*, and is labelled as such deliberately.
- **Caveats**: **abstracts are not public**; the only verifiable content is title, speaker and organisation. Slide decks may appear on the CoG site later. Treat every implied capability as a marketing claim until the talks are delivered. Note that the earlier draft of this digest mis-attributed the Wargaming and Parable talks; the mapping above is corrected against the accepted-papers page.

### ★★ Evaluating VLMs for Autonomous Agent-Driven Geometry Clipping Detection in Video Game QA
- **Authors**: Benedict Wilkins, Carlos Celemin, Adrián Barahona-Ríos, Saman Zadtootaghaj, Nabajeet Barman
- **Affiliation**: not printed on the proceedings page; the author set is **identical to RefGlitch-Bench's** (§5.3) minus Yakun Yu and Ashley Wiens, which places it at **Sony Interactive Entertainment** with University of Alberta collaborators. **(tentative — consistent with, but not printed as, Sony)**
- **Venue**: **IEEE CoG 2026**, paper #380, *Game Design and Technology*.
- **Link**: https://cog2026.org/acceptedpapers (no arXiv preprint located)
- **Abstract and key innovations**: an **autonomous agent** performs **geometry clipping detection** — meshes passing through each other, a classic and visually obvious QA defect — in video game content, using VLMs. The agent is autonomous in the QA-loop sense: it navigates and inspects rather than being handed curated screenshots.
- **Why it matters here**: **this is the QA-automation argument at its most concrete**, and it is the **same research group as §5.3's RefGlitch-Bench**, one layer down the stack: the arXiv paper benchmarks VLM glitch detection on reference-based gameplay defects, and the CoG paper applies the capability to **geometry**, the most mechanically checkable defect class. Two venues, one team, six months apart, moving from benchmark to deployment. **This is the clearest evidence in the digest that a research line is actually shipping**, and it independently corroborates that RefGlitch-Bench (§5.3) sits in peer-reviewed work.
- **Caveats**: **no abstract**, so the autonomy claim is unquantified — "agent-driven" could mean a scripted camera path. Geometry clipping has ground-truth solutions available in-engine, which is precisely why a VLM is being used (scale) rather than a checker (correctness); **the paper is therefore about cost, not capability**, and no cost figure is available.

### ★ Simulating Super Mario Odyssey for Agent Training using Decompilation
- **Authors**: Adrian Kathagen, Fabian Ostermann, Marco Pleines
- **Affiliation**: not printed on the proceedings page. Kathagen is at **TU Dortmund**; **(tentative)**
- **Venue**: **IEEE CoG 2026**, paper #86, *AI for Game Playing*.
- **Link**: https://cog2026.org/acceptedpapers (no arXiv preprint located)
- **Abstract and key innovations**: builds an agent-training environment by **decompiling a shipped commercial game** rather than reimplementing it from a paper. Deconstruction is what makes the *exact* dynamics, level geometry and physics available, which a reimplementation cannot guarantee.
- **Why it matters here**: **environment fidelity is the field's binding constraint on generalization**, and every §1 paper is limited by whether its environment matches the real game. This is the most direct attack on that constraint in the digest, and it is also the **clearest licensing/IP boundary** any paper here touches — decompiling a commercial title for training is legally and contractually constrained in a way that academic simulators are not. Filed ★ rather than higher only because no abstract is available to establish what was achieved.
- **Caveats**: no abstract. **The reproducibility of this result for anyone outside the authors is plausibly near zero**, and that is a property of the method, not a defect in the paper — but it means it cannot function as a community benchmark.

### ★ ConstructRL: A Reinforcement Learning Framework for the Construct Game Engine
- **Authors**: Jerry Wexler, Carmine Guida, Lauren DeMaio
- **Affiliation**: not printed on the proceedings page.
- **Venue**: **IEEE CoG 2026**, paper #353, *Game Design and Technology*.
- **Link**: https://cog2026.org/acceptedpapers (no arXiv preprint located)
- **Abstract and key innovations**: an **RL framework integrated into a specific commercial game engine** — Construct. Framework-plus-integration, i.e. the infrastructure layer rather than a result.
- **Why it matters here**: pairs with §6.1's talk slate as **the second half of the industry story**: Wargaming and Replay Masters deploy agents, ConstructRL supplies the framework that makes such deployment routine. Also relevant to §6.3's theme — **an engine integration is an environment-fidelity problem**, and Construct is 2D.
- **Caveats**: **no abstract, no results.** A framework paper's value is adoption, which cannot be assessed from a proceedings listing.

---

## §7 Related Techniques

### ★★ Game-Theoretic Control with Constrained Potential Surgery
- **Authors**: Zhiyuan Zhang, Panagiotis Tsiotras
- **Affiliation**: both — School of Aerospace Engineering, Institute for Robotics and Intelligent Machines, **Georgia Institute of Technology**, Atlanta. Recovered from the **PDF footnote block** (the title-block rendering dropped it).
- **Venue**: arXiv:2609.31901 (25 Sep 2026) — cs.RO, cs.MA.
- **Link**: https://arxiv.org/abs/2609.31901
- **Abstract and key innovations**: **constrained general-sum dynamic games** for multi-agent planning. Recent GNE solvers are real-time for **small** dynamic games, but **controlling more than about four agents remains elusive**, and **Newton solvers that target first-order conditions are vulnerable to non-Nash saddle points**. Contributions: a **fast interior-point solver for constrained dynamic games**, plus a **second-order correction** that increases the probability of converging to a **local GNE** rather than a saddle point. Validated on numerical benchmarks and a **physical experiment with scaled race cars**. Funded by **ONR** and **NSF**.
- **Why it matters here**: the "more than four agents" wall and the **saddle-point failure mode** are both directly transferable to game multi-agent control, and the **scaled-race-car validation** is a real-hardware check of a solver claim — rare and valuable in a literature that is almost entirely simulation-only. The saddle-point caveat is the important part for game use: a fast GNE solver that returns a non-equilibrium point is worse than a slow one, because the failure is silent.
- **Caveats**: robotics framing; **not a game paper**. GNE ≠ Nash ≠ the equilibrium notion most game-learning work actually wants, and "local GNE" is a weaker target than the global solution game papers implicitly assume. The four-agent ceiling is stated as motivation, not measured in this paper.

### ★★ OPTS-TTPO: Enhancing Finite-Sample Policy-Gradient Learning with Tree Search
- **Authors**: Junyu Lu, Shichao Weng, Zhiqiang Wang, Haojie Luo, Jingfan Zhang, Yuhua Zhou, Cheng Du, Yuzhuo Zhang, Xi Li, Jinwei Du, Tiancheng Feng, Chuan Xiao, Shuyuan Zheng
- **Affiliation**: **Dobot Robotics** (Lu, Weng, Wang, Luo, Li, Feng); **Independent Researcher** (Zhang); **Zhejiang University** (Zhou); **Fudan University** (Yuzhuo Zhang); **Osaka University** (Xiao, Zheng).
- **Venue**: arXiv:2609.40035 (30 Sep 2026) — cs.LG. **42 pages, 12 figures.**
- **Link**: https://arxiv.org/abs/2609.40035
- **Abstract and key innovations**: the policy-gradient theorem gives the exact gradient under the current policy, but **finite on-policy samples may miss rare high-return trajectories**. **On-Policy Parallel Tree Search (OPTS)** samples **new suffixes from the current policy at visited states**, so it needs **no action-distribution correction** — though branching changes state visitation. A **Branch Aggregation Lemma** shows branch-weighted tree statistics recover chain expectations when branch choices and weights are **fixed before outgoing transitions are sampled**. OPTS selects expansion states by **estimated performance differences**; under deterministic dynamics, exact values and max-backup advantages, the induced search policy's expected return **improves monotonically with budget**. Measured gradient bias against a finite chain reference: **TTPO's bias stays near its no-branching level while NaivePG's grows from 0.1251 to 0.4884**.
- **Why it matters here**: this attacks the **exploration-samples-return-rarity** problem that §1.3's Wayfarer addresses in the game domain, with a **theorem and a bias bound** rather than an environment. Sparse-reward games like Montezuma's Revenge (named in §1.3) are exactly where finite on-policy sampling loses the good trajectory, so this is a **method that transfers directly into the game-RL toolbox** and is unusually well-specified for a preprint.
- **Caveats**: **not a game paper**; evaluated on synthetic chain settings, not sparse-reward games, and the monotonicity guarantee requires **deterministic dynamics, exact values and max-backup advantages** — three assumptions that fail together in a stochastic game. The transfer to games is plausible and untested. The `0.1251 → 0.4884` bias comparison is against a synthetic reference, not a game.

### ★ Hierarchical Multiagent Reinforcement Learning for Multi-Group Tax Game
- **Authors**: Honglei Guo, Yexin Li, Chiyuan Wang, Yuhan Zhao
- **Affiliation**: **College of Artificial Intelligence, Zhejiang University**; **State Key Laboratory of General Artificial Intelligence (BIGAI)**.
- **Venue**: arXiv:2605.04741 (29 Sep 2026) — cs.MA, cs.LG.
- **Link**: https://arxiv.org/abs/2605.04741
- **Abstract and key innovations**: existing taxation models study a **single economic group** (one government, many households) and **overlook competition among independent groups**. The paper formulates taxation as a **hierarchical multi-group tax game** — within a group, a **government sets policy while households respond**; across groups, **governments compete through fiscal policy** — and proposes **MGPPO**, a **bilevel MARL** algorithm with **Hierarchical Sampling** (coordinate learning across agent levels) and **Curriculum Learning** (training stability), plus a multi-group taxation simulator grounded in classical economic models.
- **Why it matters here**: a **bilevel** structure — policy-makers whose actions shape the action space of other actors — is the structure of every negotiation, auction and marketplace game. The MARL contribution is generic; the contribution worth noting is **making the group-level competition explicit rather than assuming one environment**, which is the same modeling error XiangqiBench (§5.1) is designed to avoid on the evaluation side.
- **Caveats**: **economic simulation, not a game.** The abstract's evaluation clause is truncated, so no results are available. Fiscal-policy games have a small effective action space, so this says little about combinatorial games. Included at ★ for the bilevel-MARL formulation only.

### ★ Action Selection in Multiplayer Hidden-Information Games with Expected Target Entropy
- **Authors**: Kaijie Xu, Fandi Meng, Clark Verbrugge, Simon Lucas
- **Affiliation**: not printed on the proceedings page. Simon Lucas (**VGDL**, **OpenSpiel**); Clark Verbrugge (**Nervana Games / Samsung**); **(tentative — verify against the published version)**
- **Venue**: **IEEE CoG 2026**, paper #339, *AI for Game Playing*.
- **Link**: https://cog2026.org/acceptedpapers (no arXiv preprint located)
- **Abstract and key innovations**: uses **expected target entropy** as the criterion for action selection in multiplayer games with hidden information — choosing the action that maximizes the **expected information gain** about the opponent rather than the expected immediate payoff.
- **Why it matters here**: **information-seeking as an explicit objective** is the strategic-game analogue of §1.3's exploration work, and it is the correct primitive for hidden-information multiplayer, where the opponent model is the bottleneck. **Entropy-based opponent inference is exactly the mechanism §5.1's XiangqiBench and §1.1's MAPLE operate on** — MAPLE samples world states to reduce belief uncertainty, and this selects actions to increase it. Three papers, one concept, three venues.
- **Caveats**: no abstract. Maximizing information gain is not the same as maximizing win probability, and the interaction between the two objectives is the hard part.

---

## §8 Cross-Cutting Synthesis

### 8.1 The whole digest is one paper: measurement instruments are broken, and three papers say so independently
This is the strongest and least comfortable pattern in the window. **§5.1** (XiangqiBench) separates *finding the move* from *winning the game* and finds a 26.1% → 13.9% conversion gap plus a `pass@3` 38.7% → `pass^3` 5.9% collapse. **§2.1** (strategic play) finds internal representations are **more accurate than verbal reports**, that beliefs are brittle, and that acting on decoded beliefs would improve payoffs in **~95%** of games. **§2.3** (reference games) shows label alignment **survives deleting the partner**, so it was never evidence of grounding. **§5.4** (EMNLP 2.6% oral) finds VLM judges of engagement **fail to beat majority class**, and that theory-grounded prompting **reinforces shortcuts**. **§7.2** (OPTS-TTPO) notes weak attacks make undefeated agents look strong.

All five report the same structural defect: **the number everyone reads is not the number they want.** Moves-found ≠ games-won. Verbal report ≠ internal belief. Label agreement ≠ shared grounding. Judge score ≠ engagement. Undefeated ≠ robust. The instruments the field builds its leaderboards on are each off by a large factor, in a consistent direction — **toward over-crediting the model.** The practical consequence is uncomfortable for a benchmark-driven field: **most published game-agent scores are upper bounds on capability that are also lower bounds on nothing**, and correcting for them will move published numbers down, not up. **§5.2 (Queen) is the one paper attempting the fix by training the verbal channel to be faithful**, which is the constructive counterpart to the five diagnostics.

### 8.2 Where I stretched the brief, and why
Two inclusions are defensible but arguable, and are flagged rather than buried. **§1.2 (broker-trader PPO)** is a financial simulator, included because its contribution is PPO diagnosis in a game with analytic ground truth — the same instrument-calibration move as §5.1. **§7.1–§7.2** (GNE control, OPTS-TTPO) and **§7.3** (tax game) are not game papers at all, included because the mechanisms — saddle-point-aware GNE solvers, tree-structured on-policy sampling, bilevel MARL — transfer into game settings that every other paper here is blocked on. **§5.2's WMAttack** is filed in §5 because its subject is world-model agents (§3's substrate), but it is not a game paper either. If a stricter brief is preferred, the defensible cut is §1.2 and all of §7, which leaves **25 papers**.

### 8.3 Peer review arrived, and it changes what this wiki is measuring
Three of this digest's papers are **accepted at CoG 2026**, two of them **Best Paper Award nominees** (§1.1 MAPLE, §4.1 MIPCGRL), one an **oral** (§5.2 RePAIR), plus two **workshop/second-venue acceptances** (§3.2). **Every game-RL result this wiki recorded before today was an unreviewed arXiv preprint.** That has a direct methodological consequence for the series: when a paper's content was previously treated as provisional because it was a preprint, **the acceptance is new evidence and warrants upgrading the standing claim** — §4.1 and §5.2's recommendations above are upgrades on exactly that basis. It also means the CoG accepted-papers list is a **~450-entry peer-reviewed queue** that no digest in this series has read, and it should become a standing channel.

### 8.4 Industry's constraint, revisited: it is environments, not algorithms — and the studios solved it by decompiling
The 10-04 digest concluded (§8.3) that industry's binding constraint is **integration**, because a chess system reaches 3,251 Elo on 8 GPUs in 2.5 days while AAA titles cannot ship the training. This digest sharpens that. §6.3 builds the training environment **by decompiling a shipped game**; §6.4 ships an **RL framework into a commercial engine**; §6.1's five talks are all **agents running inside engines**. In every case the deliverable is **environment access, not a new algorithm**. Independently, §5.1's XiangqiBench and §3.3's IGMWorld are both built on **modifying or constructing executable worlds** rather than on new RL machinery — and §3.3's central finding, that reliability **decays with intervention depth**, is a statement about how hard it is to know whether a world edit did what you meant. **The field's practical bottleneck is verified world manipulation.** Algorithms are cheap and well-understood; the ability to build a world you can *edit* and *verify* is what is missing, and it is missing for the same reason in a university lab and a AAA studio: nobody has an engine they are permitted to take apart.

### 8.5 The seven-day cadence was wrong for a reason nobody had stated
The 10-04 digest recommended reducing game-RL to a 2–3 day cadence because the daily job was outrunning the field's throughput. **Today's yield refutes the premise while confirming the conclusion.** The premise was wrong because saturation was measured on the **arXiv block alone** — and the field's peer-reviewed output does not appear there (8.3). The conclusion holds and sharpens: this run took **three channels** where yesterday took one, and **13 of the 30 new papers came from a channel that cost roughly a fifth of the effort** (§0.2 channel 2) and that had never been opened. The correct recommendation is not "slow down" but **"rotate channels, don't reduce frequency"** — and add CoG to the standing query set with the next proceedings release as a scheduled trigger. Against the arXiv lane specifically, the 2–3 day cadence remains correct.

---

## §9 Cross-References and Dedup Notes

### 9.1 Dedup verification log
Repo-wide baseline **7,945** claimed IDs + **62** same-day sibling IDs. Verified **0-hit immediately before writing**:

| ID | Paper | ID check | Title-string check |
|---|---|---|---|
| `2605.24139` | MAPLE | 0 | `Multi-State Aggregated Policy` → 0 |
| `2610.03598` | Broker-Trader PPO | 0 | `Broker-Trader` → 0 |
| `2610.03604` | Wayfarer | 0 | `Discovered Options` → 0 |
| `2605.00226` | Why Do LLMs Struggle in Strategic Play | 0 | `Broken Links Between Observations` → 0 |
| `2609.31989` | Frozen LLMs / Referential Game | 0 | `Referential Game` → 0 |
| `2606.08081` | Aligned but Not Partner-Specific | 0 | `Aligned but Not Partner-Specific` → 0 |
| `2509.15915` | Foundation Models as World Models | 0 | `Foundation Models as World Models` → 0 |
| `2610.02331` | World Editing / IGMWorld | 0 | `IGMWorld`, `IGMBench`, `World Editing` → 0 |
| `2610.02425` | XiangqiBench | 0 | `XiangqiBench` → 0 |
| `2610.03695` | Queen | 0 | `Play Chess and Explain` → 0 |
| `2604.11082` | RefGlitch-Bench | 0 | `RefGlitch-Bench` → 0 |
| `2510.08928` | LM Fight Arena | 0 | `LM Fight Arena` → 0 |
| `2605.23220` | WMAttack | 0 | `WMAttack` → 0 |
| `2603.18480` | VLM human engagement | 0 | `Human Engagement in Games` → 0 |
| `2609.31901` | Constrained Potential Surgery | 0 | `Constrained Potential Surgery` → 0 |
| `2609.40035` | OPTS-TTPO | 0 | — (title unique) |
| `2605.04741` | MGPPO tax game | 0 | `Multi-Group Tax Game` → 0 |

Proceedings titles checked at string level (all 0-hit unless noted): `Text2BT`, `FlashLore`, `ConstructRL`, `RuleSweeper`, `Judging the Imitation Game`, `Persistent Spatial Intent`, `Geometry Clipping Detection`, `Stack more levels`, `Super Mario Odyssey for Agent Training`, `Neural MMO 2`, `Generalization Gap in Open-Ended`, `Human-like Aiming in FPS`, `Preference-Optimized Policies`, `Limited Cheating in Chess`, `Intent-Belief Multi-task`, `Dominion Learning Environment`, `IRumAI`, `Tales of Tribute`, `RIDGE`, `Action Selection in Multiplayer Hidden-Information`, `Perfect-Information Monte Carlo Tree Search in Imperfect`.

### 9.2 Venue updates to already-covered papers (not re-summarized)
- **`2508.09193` MIPCGRL** — covered in `2026-07-15`, `2026-07-30`, `2026-08-17`, `2026-08-19` (8 files). **New: CoG 2026 Best Paper Award Nominee (#217).**
- **`2508.16821` PuzzleJAX** — covered in `2026-08-27`. **New: CoG 2026 (oral).** Prior entry records no acceptance.
- **`2606.11860` RePAIR** — covered in `2026-06-11/arxiv-daily.md` and `2026-06-15/game-rl-daily.md`. **New: CoG 2026 (oral).**

### 9.3 Same-day sibling collisions (recorded, not absorbed)
Seven sibling files share `wiki/synthesis/2026-10-05/`. **`arxiv-daily.md` claims `2610.02563`** (OpenGameEval) — a genuine game paper inside this run's fresh window, correctly excluded from §1–§7 on that basis. `arxiv-ai-search.md`, `arxiv-paper-check.md`, `investment-daily.md`, `tech-report-digest.md`, `wq101-alpha-daily.md` and any others claim no overlapping game IDs. **No featured ID collides.**

### 9.4 ⚠️ Affiliation and rendering caveats affecting six entries
Recorded because these are reproducible failure modes, and because the 10-04 digest documented the same class of defect.
- **`2610.02425` (XiangqiBench): no affiliation at all**, three authors, and the arXiv HTML **drops two of three names from the author block**. The most significant paper in the digest is the least attributable.
- **`2610.02331` (IGMWorld): literal `G-G-G`** in the affiliation slot, in **both PDF and HTML**, out of 18 authors and 4+ institutions. Reported verbatim, **not guessed**.
- **`2610.03695` (Queen): affiliation recovered from the PDF** — LaTeXML stripped the author block.
- **`2609.31901` (Constrained Potential Surgery): affiliation absent from the PDF title block**, recovered from a **page-1 footnote**.
- **`2605.24139` (MAPLE): no HTML render exists** (`No HTML for '2605.24139'`); affiliation recovered from the PDF title block only.
- **`2609.31989`, `2606.08081`, `2603.18480`, `2609.40035`, `2509.15915`, `2603.18480`:** all had author blocks stripped from the LaTeXML HTML and required PDF extraction.

**Affiliations marked (tentative) or unverified are confined to CoG-only papers whose proceedings page carries superscripts without text**, and to two inferences flagged inline (§1.5 Togelius group, §2.2 Square Enix). **None was silently inferred.**

### 9.5 Name collisions encountered (dedup traps)
- **"Yuchen Li"** appears as a MAPLE co-author (§1.1, Academia Sinica) **and** as a *Stack More Levels* co-author (§1.5, Togelius group). **Different people.** Not merged.
- **"Rishitosh Singh"** on the arXiv abs page vs **"Rishitosh Kumar Singh"** in the PDF for `2603.18480`. PDF authoritative.
- **`2603.18480` affiliations were previously recorded in this wiki as "Texas A&M + Surrey"; the PDF title block gives Texas A&M + USC + Arizona State. Corrected in §5.4.**
- **"Game-Agnostic Value Functions through Automatic JSON Feature Extraction"** (CoG #386, Jeurissen/Cakmak/Lee/Rangan) and **"Multi-Task Learning for Heterogeneous Prediction from Video Game State with Transfer Learning"** (CoG #180) each returned **1 file** on string check; **neither is featured**, and both are recorded here as checked-and-excluded.

---

## §10 Bottom Line

**Thirty papers, plus three venue updates: five from the fresh arXiv window, fifteen carrying a peer-reviewed CoG 2026 acceptance, and ten more arXiv-only from the rolling window.** Yesterday's saturation verdict does not survive contact with the second channel.

Three findings are worth carrying forward.

**First, the digest's real subject is that measurement is broken, and five papers say so independently.** Moves-found ≠ games-won (XiangqiBench, 26.1% → 13.9%). Verbal report ≠ internal belief (beliefs are *better* than reports, and acting on them would help in ~95% of games). Label alignment ≠ grounding (it survives deleting the partner). Judge score ≠ engagement (VLMs lose to majority class; MDA in the prompt *reinforces shortcuts*). Undefeated ≠ robust (weak attacks look like strong agents). Every error runs in the same direction: **toward over-crediting the model.** The one constructive response is §5.2's Queen, which *trains* the verbal channel to be faithful instead of trying to read it out.

**Second, peer review exists and this wiki had missed it.** MAPLE and MIPCGRL are Best Paper Award nominees; RePAIR is an oral. Three fresh papers would previously have been filed as provisional preprints. The CoG accepted-papers list is ~450 peer-reviewed game-RL/Game-AI entries and should become a standing channel with the next proceedings release as a scheduled trigger — this is the single highest-value change available to this series, and it costs one HTTP fetch.

**Third, the bottleneck is verified world manipulation, in academia and industry alike.** Decompile a shipped game to get an environment (§6.3); ship an RL framework into an engine (§6.4); put agents in engines at five studios (§6.1). Meanwhile the research frontier is also about *editing* worlds and discovering that **reliability decays with intervention depth** (§3.3). Algorithms are cheap; knowing whether a world did what you meant is not.

**Recommendation: keep the daily cadence, but rotate channels rather than slow down.** Today's yield came from a channel that cost a fifth of yesterday's effort and had never been queried. Add `cog2026.org/acceptedpapers` to the standing query set; keep the 2–3 day cadence for the **arXiv** lane alone, where 239 papers per two days against a handful of game hits still justifies it.