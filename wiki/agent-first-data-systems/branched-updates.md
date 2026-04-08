---
title: Branched Updates
created: 2026-04-08
updated: 2026-04-08
sources: [raw/20250901-agent-first-data-systems.md]
related: [agent-first-data-systems-architecture](agent-first-data-systems-architecture.md), [agentic-speculation](agentic-speculation.md), [agentic-memory-store](agentic-memory-store.md)
tags: [branched-updates, multi-world-transactions, copy-on-write, database-transactions, ai-agents, speculative-execution]
---

# Branched Updates

Branched updates refer to a proposed transaction model for agent-first data systems that supports multi-world isolation -- the ability for multiple agents to independently fork database state, run speculative updates, and roll back all but the chosen branch. This model addresses the observation that LLM agents performing data transformations explore multiple "what-if" hypotheses simultaneously, creating far more branches and rollbacks than human users.

Empirical data from Neon (a serverless Postgres provider) shows that agents create 20x more branches and perform 50x more rollbacks relative to humans. Traditional transaction models operate within a linear thread of execution with isolation guaranteeing that concurrent writes do not interfere. Agentic speculation requires a fundamentally different model where each branch is logically isolated but may physically overlap, since most branches (often 90% identical data, same schema) differ only slightly.

The paper draws inspiration from branching consistency models developed during the weak consistency era, including Bayou, Dynamo, and Tardis, as well as versioned databases like OrpheusDB. However, agentic workloads go further: multiple agents may create forks that must eventually reconcile not just with the mainline but with each other, requiring new models of multi-agent, multi-version isolation.

Efficient implementation demands copy-on-write approaches that lazily clone state, but at a scale far beyond current systems. The authors envision new concurrency mechanisms analogous to "MVCC on steroids" -- supporting thousands of near-identical snapshots with ultra-fast rollbacks (fast aborts for failed branches) while preserving logical isolation to prevent cross-contamination.

## Key Points

- **Multi-world isolation**: Each speculative branch is logically isolated but physically shares overlapping data with other branches
- **Scale difference**: Agents create 20x more branches and 50x more rollbacks than humans (Neon data)
- **Copy-on-write**: Lazy cloning of state is necessary but current implementations are insufficient for agentic scale
- **Multi-agent reconciliation**: Branches from different agents must reconcile with each other, not just with the mainline
- **Ultra-fast rollbacks**: Unlike traditional systems where rollbacks are rare, agentic workloads require near-instantaneous abort of failed branches
- **MVCC on steroids**: The envisioned concurrency mechanism for forking thousands of near-identical snapshots

## Related Concepts

- [Agent-First Data Systems Architecture](agent-first-data-systems-architecture.md) - branched updates are the transaction component of the architecture
- [Agentic Speculation](agentic-speculation.md) - the speculative workload that produces the branching pattern
- [Agentic Memory Store](agentic-memory-store.md) - provides grounding that can reduce unnecessary branching

## Sources

- raw/20250901-agent-first-data-systems.md - proposed branched updates with multi-world isolation and referenced Neon empirical data (Sec. 6.2)
