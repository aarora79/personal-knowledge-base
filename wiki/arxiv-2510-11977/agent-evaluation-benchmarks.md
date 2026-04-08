---
title: Agent Evaluation Benchmarks
created: 2026-04-08
updated: 2026-04-08
sources: [raw/20260408-arxiv-2510-11977.md]
related: [Holistic Agent Leaderboard](holistic-agent-leaderboard.md), [Agent Scaffolds](agent-scaffolds.md), [Agent Evaluation Infrastructure](agent-evaluation-infrastructure.md), [Agent-First Data Systems Architecture](../agent-first-data-systems/agent-first-data-systems-architecture.md)
tags: [benchmarks, agent-evaluation, swe-bench, gaia, tau-bench, ai-agents, evaluation-methodology, multi-agent-systems]
---

# Agent Evaluation Benchmarks

Agent evaluation benchmarks are standardized test suites designed to measure AI agent capabilities across specific domains. The HAL project evaluated 9 benchmarks spanning four major domains where agents are being developed and deployed: web navigation, software engineering, scientific research, and customer service.

The selection criteria prioritized benchmarks that evaluate genuine agent capabilities and represent tasks with high construct validity. These benchmarks differ by orders of magnitude in cost: ScienceAgentBench averages $13 per evaluation while Online Mind2Web averages over $450.

## Key Points

- **Web Navigation**: Online Mind2Web (dynamic web interface navigation), AssistantBench (multi-step web assistance), GAIA (web search combined with reasoning for complex questions)
- **Software Engineering**: SWE-bench Verified Mini (resolving real GitHub issues), USACO (competitive programming problems)
- **Scientific Research**: CORE-Bench Hard (reproducing computational research papers), ScienceAgentBench (data analysis and visualization), SciCode (implementing scientific algorithms)
- **Customer Service**: TAU-bench Airline (handling airline support with database queries)
- Benchmarks test diverse capabilities: navigating complex interfaces, writing correct code, conducting scientific analysis, and handling multi-turn interactions
- Prior work had significant gaps: only 2 of the 9 benchmarks were ever evaluated with the same agent scaffold for 4 or more models, making cross-model comparison difficult before HAL
- Cost variation across benchmarks spans orders of magnitude, making budget-aware benchmark selection essential for evaluation planning

## Related Concepts

- [Holistic Agent Leaderboard](holistic-agent-leaderboard.md) - the framework that standardizes evaluation across these benchmarks
- [Agent Scaffolds](agent-scaffolds.md) - the task-specific and generalist scaffolds paired with each benchmark
- [Agent Evaluation Infrastructure](agent-evaluation-infrastructure.md) - the engineering required to run evaluations at scale

## Sources

- raw/20260408-arxiv-2510-11977.md - benchmark selection criteria, domain categorization, and cost analysis from HAL paper Table 3
