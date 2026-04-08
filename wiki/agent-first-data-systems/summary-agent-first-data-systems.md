---
title: "Source Summary: Supporting Our AI Overlords - Redesigning Data Systems to be Agent-First"
created: 2026-04-08
source: raw/20250901-agent-first-data-systems.md
depth: 500
articles_created: [agentic-speculation.md, agent-first-data-systems-architecture.md, probes-and-briefs.md, probe-optimization.md, agentic-memory-store.md, branched-updates.md, sleeper-agents.md]
---

# Supporting Our AI Overlords: Redesigning Data Systems to be Agent-First - Summary

This paper by Liu et al. (UC Berkeley, 2025) presents a research vision for redesigning data systems around LLM agent workloads. The central thesis is that as LLM agents become the dominant consumers of data systems -- issuing orders of magnitude more requests than humans, with fundamentally different access patterns -- the traditional query-answer paradigm becomes a bottleneck. The paper introduces the concept of *agentic speculation* and proposes a layered architecture that exploits its characteristics.

## Agentic Speculation: Characterization

The authors define agentic speculation as the high-throughput, exploratory querying process agents use to compensate for their lack of data grounding. Through two case studies -- a text2SQL benchmark (BIRD) with GPT-4o-mini and Qwen2.5-Coder-7B, and a multi-database integration task with OpenAI o3 -- they identify four properties:

1. **Scale**: Success rates improve 14-70% with more parallel or sequential attempts. A single agent can theoretically issue hundreds of requests per second.
2. **Heterogeneity**: Agent traces show distinct phases -- metadata exploration, column statistics gathering, partial query formulation, and complete solution attempts -- that overlap temporally but follow a general progression.
3. **Redundancy**: Across 50 parallel attempts per problem, only 10-20% of sub-plans (subexpressions in query plans) are distinct, representing massive potential for computation sharing.
4. **Steerability**: Injecting grounding hints into prompts reduces total queries by 18-37% depending on phase, demonstrating that proactive feedback can substantially improve efficiency.

## Proposed Architecture

The agent-first data systems architecture spans three layers:

```
  +-------------------+     +-------------------+
  |  Field Agents     |     |  Agent-in-Charge  |
  |  (LLM workers)    |     |  (coordinator)    |
  +--------+----------+     +--------+----------+
           |  probes + briefs         |
           v                          v
  +-----------------------------------------------+
  |          AGENTIC INTERPRETER                   |
  |   (parses NL briefs, routes SQL + semantic)    |
  +----------------------+------------------------+
                         |
           +-------------+-------------+
           v                           v
  +------------------+      +--------------------+
  |  PROBE OPTIMIZER |      |  SLEEPER AGENTS    |
  |  - satisficing   |      |  - join discovery  |
  |  - MQO / AQP     |      |  - why-not prov.   |
  |  - intra/inter   |      |  - cost feedback   |
  +--------+---------+      +--------+-----------+
           |                          |
           v                          v
  +-----------------------------------------------+
  |              STORAGE LAYER                     |
  |  +------------------+  +--------------------+  |
  |  | Agentic Memory   |  | Shared Transaction |  |
  |  | Store (semantic   |  | Manager (branched  |  |
  |  |  cache + metadata)|  |  updates, CoW)     |  |
  |  +------------------+  +--------------------+  |
  +-----------------------------------------------+
```

### Interface Layer: Probes and Briefs

The paper replaces SQL queries with *probes* -- composite requests containing SQL statements plus a *brief* in natural language. The brief communicates the agent's phase (exploration vs. solution formulation), desired accuracy, priorities across queries, and termination criteria. This enables the data system to make optimization decisions impossible under pure SQL, such as returning coarse approximations during exploration or executing only k-of-n specified queries. The interface also introduces semantic search operators beyond LIKE that can match tokens across any table, column, or row by meaning rather than exact text.

### Query Processing: Probe Optimization

The probe optimizer pursues *satisficing* rather than complete execution -- producing results sufficient for the agent to decide its next step. Intra-probe optimization prunes semantically irrelevant queries using brief-derived intent, shares computation across redundant sub-plans via multi-query optimization (MQO), applies approximate query processing (AQP) with phase-aware accuracy levels, and supports incremental evaluation with dynamic re-prioritization. Inter-probe optimization across turns drops probes providing no marginal information over prior answers, strategically executes some queries completely when predicted to reduce future follow-ups, and adopts exploration-exploitation strategies to balance satisficing speed against discovery of unexpectedly useful results. Materialization and caching decisions are informed by query history and declared agent intent.

### Storage Layer: Memory and Transactions

The *agentic memory store* is a persistent semantic cache storing prior probe results, partial solutions, column encoding formats, missing value patterns, and partition metadata (date ranges, geographic granularity). Implementation combines table-embedded metadata with vector-indexed semantic similarity search. Key open challenges include staleness management (schema updates invalidating cached information) and multi-user access control (sharing grounding across agents serving different users creates privacy risks in aggregate).

For writes, *branched updates* support multi-world isolation where agents fork database state for speculative "what-if" explorations. Drawing on copy-on-write systems (Neon, Aurora, Tardis) and versioned databases (OrpheusDB), the authors envision "MVCC on steroids" -- thousands of near-identical snapshots with ultra-fast rollback. Neon reports agents create 20x more branches and 50x more rollbacks than humans. The reconciliation problem is harder than traditional branching because multiple agents' forks must merge with each other, not just the mainline.

### In-Database Sleeper Agents

Sleeper agents are dormant LLM components activated by incoming probes. They run in parallel with normal query execution and return auxiliary information via a side-channel: related tables (join discovery), explanations for unexpected results (why-not provenance), cost estimates and warnings, and suggestions to batch or restructure probes. This proactive behavior -- inspired by how a data engineer assists an analyst -- shifts the database from a passive oracle to an active collaborator.

## What This Source Covers

- Definition and empirical characterization of agentic speculation through case studies on BIRD and multi-database tasks
- Proposed architecture for agent-first data systems with three layers (interface, processing, storage)
- Probes and briefs as a beyond-SQL query interface with natural language intent specification
- Probe optimization via satisficing, MQO, AQP, and cross-turn inter-probe optimization
- Agentic memory store as a persistent semantic cache with staleness and access control challenges
- Branched updates with multi-world isolation for speculative writes at massive scale
- Sleeper agents as proactive in-database components for grounding feedback and cost steering

## Wiki Articles From This Source

- [Agentic Speculation](agentic-speculation.md) - the core concept of high-throughput exploratory querying by LLM agents
- [Agent-First Data Systems Architecture](agent-first-data-systems-architecture.md) - the proposed three-layer system redesign
- [Probes and Briefs](probes-and-briefs.md) - the beyond-SQL query interface with natural language intent
- [Probe Optimization](probe-optimization.md) - satisficing, multi-query optimization, and cross-turn strategies
- [Agentic Memory Store](agentic-memory-store.md) - persistent semantic cache for agent grounding
- [Branched Updates](branched-updates.md) - multi-world transactions for speculative agent writes
- [Sleeper Agents (Proactive Data Systems)](sleeper-agents.md) - in-database agents providing steering feedback
