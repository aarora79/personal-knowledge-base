---
title: Probes and Briefs
created: 2026-04-08
updated: 2026-04-08
sources: [raw/20250901-agent-first-data-systems.md]
related: [agentic-speculation](agentic-speculation.md), [agent-first-data-systems-architecture](agent-first-data-systems-architecture.md), [probe-optimization](probe-optimization.md), [sleeper-agents](sleeper-agents.md)
tags: [probes, query-interface, agent-database-interaction, natural-language-queries, ai-agents]
---

# Probes and Briefs

Probes and briefs are a proposed extension to the traditional SQL query interface, designed for agent-first data systems. A probe is a request from an agent to a data system that combines one or more SQL queries with a brief -- a natural language description of the probe's goals, intent, current phase, approximation needs, and priorities.

The term "probe" is used instead of "query" for two reasons. First, probes carry contextual information beyond the query itself: the agent can specify whether it is in a metadata exploration phase or solution formulation phase, the degree of accuracy required, the identity of the requesting agent, and overall task goals. Second, probes can request operations impossible in standard SQL, such as searching for tokens semantically similar to a phrase across any table, column, or row in the entire database.

Briefs enable the data system to make intelligent optimization decisions. For example, during an exploration phase, the system can return coarse-grained approximations rather than exact results. Across a batch of queries within a probe, the brief can specify pair-wise priorities, indicate that only k of n queries need full execution, or define termination criteria -- functions evaluated on partial result sets to determine when further execution is unnecessary.

## Key Points

- **Beyond SQL**: Probes extend SQL with natural language metadata about intent, phase, accuracy needs, and inter-query priorities
- **Phase awareness**: Agents declare whether they are exploring metadata or formulating solutions, allowing the database to adjust accuracy levels
- **Semantic search**: Probes support querying for semantically similar content across all tables, columns, and rows -- not just exact matches via LIKE
- **Batch optimization**: A single probe can contain multiple queries with specifications about which subset needs completion, enabling the database to choose the cheapest viable set
- **Termination criteria**: Agents can supply functions that evaluate partial results to signal early stopping, such as detecting when new results are too similar to previous ones
- **Flexible approximation**: Agents can specify varying accuracy requirements per query, allowing the database to allocate compute where it matters most

## Related Concepts

- [Agentic Speculation](agentic-speculation.md) - the workload pattern that necessitates probes over traditional queries
- [Agent-First Data Systems Architecture](agent-first-data-systems-architecture.md) - the system architecture where probes serve as the interface layer
- [Probe Optimization](probe-optimization.md) - how the database processes and optimizes incoming probes
- [Sleeper Agents](sleeper-agents.md) - in-database agents that provide feedback beyond probe answers

## Sources

- raw/20250901-agent-first-data-systems.md - introduced probes and briefs as the query interface for agent-first systems (Sec. 4.1)
