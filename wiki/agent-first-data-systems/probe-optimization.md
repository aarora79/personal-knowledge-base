---
title: Probe Optimization
created: 2026-04-08
updated: 2026-04-08
sources: [raw/20250901-agent-first-data-systems.md]
related: [agentic-speculation](agentic-speculation.md), [probes-and-briefs](probes-and-briefs.md), [agent-first-data-systems-architecture](agent-first-data-systems-architecture.md), [agentic-memory-store](agentic-memory-store.md)
tags: [probe-optimization, query-optimization, approximate-query-processing, multi-query-optimization, ai-agents, data-systems]
---

# Probe Optimization

Probe optimization refers to the query processing techniques proposed for agent-first data systems that go beyond traditional database optimization. Unlike conventional query optimizers that aim to execute each query completely and correctly, a probe optimizer's goal is to evaluate probes just enough for agents to make informed decisions about their next steps -- a strategy known as satisficing.

Probe optimization operates at two levels: intra-probe (within a single batch of queries) and inter-probe (across sequential interactions with an agent over multiple turns).

Intra-probe optimization addresses a given batch of probes. The optimizer first decides what to execute by reasoning about data and probe semantics, using the brief to understand the agent's goals. It can prune columns or entire queries deemed irrelevant to the agent's intent, compare probes within a batch to eliminate those whose results would be subsumed by others, and adjust accuracy levels based on the agent's declared phase. For execution, the optimizer exploits redundancy through multi-query optimization, approximate query processing, and caching of partial results. It can incrementally evaluate queries and dynamically re-prioritize which probes get higher accuracy first.

Inter-probe optimization leverages the full history of agent interactions. The optimizer can drop probes whose outputs provide no new information given prior answers, or choose to execute some queries completely rather than approximately if it predicts doing so will reduce future follow-up probes. It can also adopt an exploration-exploitation strategy, sometimes prioritizing underexplored solution spaces that might yield unexpected benefits.

## Key Points

- **Satisficing over completeness**: The optimization goal is producing sufficient answers, not complete ones, minimizing total time across all agent interactions
- **Semantic pruning**: Uses natural language briefs to prune irrelevant queries or columns before execution
- **Cost-accuracy tradeoffs**: Balances upfront computation cost against the risk of generating follow-up probes when answers are too approximate
- **Multi-query optimization**: Shares computation across probes that have overlapping sub-plans (80-90% redundancy observed in case studies)
- **Incremental evaluation**: Processes queries progressively, allowing the optimizer to re-evaluate decisions mid-execution
- **Exploration vs. exploitation**: Sometimes prioritizes deeper exploration of underexplored solution spaces rather than always satisficing quickly

## Related Concepts

- [Agentic Speculation](agentic-speculation.md) - the workload characteristics (redundancy, heterogeneity) that probe optimization exploits
- [Probes and Briefs](probes-and-briefs.md) - the input format that enables semantic optimization decisions
- [Agent-First Data Systems Architecture](agent-first-data-systems-architecture.md) - the system in which probe optimization is the query processing layer
- [Agentic Memory Store](agentic-memory-store.md) - stores prior results to avoid redundant computation across probes

## Sources

- raw/20250901-agent-first-data-systems.md - described intra-probe and inter-probe optimization strategies (Sec. 5)
