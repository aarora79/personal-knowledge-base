---
title: Agent-First Data Systems Architecture
created: 2026-04-08
updated: 2026-04-08
sources: [raw/20250901-agent-first-data-systems.md]
related: [agentic-speculation](agentic-speculation.md), [probes-and-briefs](probes-and-briefs.md), [probe-optimization](probe-optimization.md), [agentic-memory-store](agentic-memory-store.md), [branched-updates](branched-updates.md), [sleeper-agents](sleeper-agents.md), [Agent Evaluation Benchmarks](../arxiv-2510-11977/agent-evaluation-benchmarks.md)
tags: [agent-first-data-systems, data-systems-architecture, ai-agents, database-design, llm-workloads]
---

# Agent-First Data Systems Architecture

Agent-first data systems architecture is a proposed redesign of database systems to natively support LLM agent workloads, as described by Liu et al. (UC Berkeley, 2025). The architecture recognizes that LLM agents will become the dominant consumers of data systems, replacing the human-driven and application-driven query patterns that today's databases are optimized for.

The architecture consists of several interconnected layers. At the interface layer, agents submit probes -- requests that go beyond SQL to include natural language briefs about goals, phases, and approximation needs. An agentic interpreter within the database parses and routes these probes. The query processing layer includes a probe optimizer that performs satisficing (producing reasonable results without complete evaluation) and leverages multi-query optimization to exploit redundancy. The storage layer introduces an agentic memory store for persistent grounding information and a shared transaction manager for efficient branched updates.

A distinctive feature is the inclusion of LLM agents within the database itself. Sleeper agents are invoked on-demand to gather auxiliary information, provide grounding hints, and steer external agents toward more efficient probing strategies. This represents a shift from the passive query-answer paradigm to a proactive, collaborative model of agent-database interaction.

## Key Points

- **Probe interface**: Replaces pure SQL with probes containing SQL queries plus natural language briefs about intent, phase, and accuracy requirements
- **Agentic interpreter**: An in-database LLM component that parses probes and orchestrates execution across natural language and SQL queries
- **Probe optimizer**: Extends traditional query optimization with satisficing, cost-accuracy tradeoffs, and cross-probe redundancy elimination
- **Agentic memory store**: A persistent semantic cache storing prior probe results, data metadata, and column encodings to accelerate future exploration
- **Shared transaction manager**: Supports branched updates with efficient forking and rollback for speculative multi-agent writes
- **Sleeper agents**: In-database agents that proactively provide grounding feedback beyond direct query answers

## Related Concepts

- [Agentic Speculation](agentic-speculation.md) - the workload pattern this architecture is designed to support
- [Probes and Briefs](probes-and-briefs.md) - the interface layer of this architecture
- [Probe Optimization](probe-optimization.md) - the query processing layer
- [Agentic Memory Store](agentic-memory-store.md) - the storage layer's semantic cache
- [Branched Updates](branched-updates.md) - the transaction model for speculative writes
- [Sleeper Agents](sleeper-agents.md) - proactive in-database agents

## Sources

- raw/20250901-agent-first-data-systems.md - proposed the full architecture (Sec. 3) and detailed each layer in Sec. 4-6
