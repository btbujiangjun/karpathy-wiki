---
title: "Structured Test-Time Learning"
type: method
created: 2026-05-24
updated: 2026-05-24
sources: [papers/sensi-llm-game-agents.md]
tags: [test-time-learning, llm-agents, curriculum, arc-agi]
---

A method for LLM agents to learn at test time via structured cognitive state management. Key components: two-player architecture (perception/action separation), state machine-driven curriculum, database-as-control-plane (cognitive state in SQLite), and LLM-as-judge with dynamic evaluation rubrics.

## Key Characteristics

- 50–94× sample efficiency improvement over comparable systems
- Database-as-control-plane enables explicit tracking of cognitive state
- Dynamic curriculum via state machine
- Honest reporting of negative results

## Source

[[sensi-llm-game-agents]] — [[2603.17683|arXiv]]
