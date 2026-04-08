---
title: Agentic Speculation
created: 2026-04-08
updated: 2026-04-08
sources: [raw/20250901-agent-first-data-systems.md]
related: [agent-first-data-systems-architecture](agent-first-data-systems-architecture.md), [probes-and-briefs](probes-and-briefs.md), [probe-optimization](probe-optimization.md), [../ietf-draft-narajala-ans/agent-discovery](../ietf-draft-narajala-ans/agent-discovery.md)
tags: [agentic-speculation, ai-agents, data-systems, llm-workloads, query-optimization]
---

# Agentic Speculation

Agentic speculation is a term coined by Liu et al. (UC Berkeley, 2025) to describe the high-throughput, exploratory querying process that LLM agents employ when interacting with data systems. Unlike human-driven workloads that are intermittent and targeted, agentic speculation involves agents issuing hundreds or thousands of requests per second to explore data, discover metadata, formulate partial solutions, and validate results.

The concept captures a fundamental shift in how data systems are used. When an LLM agent is tasked with a data analysis problem, it lacks grounding -- an awareness of the underlying data and its characteristics. To compensate, agents engage in a tireless process of exploration that far exceeds what any human could perform. For example, agents tasked with analyzing coffee bean sales trends might issue enormous volumes of queries simply to discover relevant tables, understand column semantics, and iteratively refine their analysis approach.

## Key Points

- **Scale**: A single agent can issue hundreds to thousands of requests per second, and this scales linearly with the number of agents. Case studies on the BIRD text2SQL benchmark showed that success rates improve 14-70% as the number of parallel or sequential attempts increases.
- **Heterogeneity**: Agentic speculation is not uniform. It proceeds in phases -- from coarse-grained metadata exploration (table schemas, column statistics) to partial solution formulation and final validation. These phases overlap but show a clear temporal pattern.
- **Redundancy**: Across parallel agent attempts, only 10-20% of sub-plans are distinct. The remaining 80-90% represent overlapping computation that could be shared.
- **Steerability**: Providing grounding hints to agents reduces their total query count by over 20%, demonstrating that proactive feedback from data systems can make speculation more efficient.

## Related Concepts

- [Agent-First Data Systems Architecture](agent-first-data-systems-architecture.md) - the system architecture designed to support agentic speculation natively
- [Probes and Briefs](probes-and-briefs.md) - the interface through which agents express speculative queries
- [Probe Optimization](probe-optimization.md) - techniques for efficiently processing speculative workloads
- [Agent Discovery](../ietf-draft-narajala-ans/agent-discovery.md) - how agents find each other, a prerequisite for multi-agent speculation

## Sources

- raw/20250901-agent-first-data-systems.md - defined the concept and characterized its four properties through case studies on BIRD benchmark and multi-database agent tasks
