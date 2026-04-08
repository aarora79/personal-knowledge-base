---
title: Sleeper Agents (Proactive Data Systems)
created: 2026-04-08
updated: 2026-04-08
sources: [raw/20250901-agent-first-data-systems.md]
related: [agent-first-data-systems-architecture](agent-first-data-systems-architecture.md), [probes-and-briefs](probes-and-briefs.md), [agentic-memory-store](agentic-memory-store.md), [agentic-speculation](agentic-speculation.md)
tags: [sleeper-agents, proactive-data-systems, agent-steering, grounding-feedback, ai-agents, data-systems]
---

# Sleeper Agents (Proactive Data Systems)

Sleeper agents are LLM-powered components proposed to reside within agent-first data systems, invoked on-demand to gather and provide information that goes beyond directly answering a query. They represent a shift from the passive query-answer paradigm to a proactive model where the data system actively steers external agents toward more efficient exploration.

The term "sleeper" reflects their activation pattern: they are dormant until a probe triggers them, at which point they work in parallel with normal query execution to gather auxiliary information returned alongside the probe's direct answers. This auxiliary information serves as a side-channel for grounding feedback.

Sleeper agents provide two categories of assistance. First, they supply auxiliary information such as related tables that could be joined with or replace the current analysis target (join discovery), explanations for unexpected results (why-not provenance -- e.g., informing an agent that state codes are stored as full names rather than two-letter abbreviations), and suggestions for alternative data paths. Second, they provide cost estimates and cost-based feedback, warning agents about expensive queries before execution, suggesting query modifications to reduce cost (e.g., narrowing geographic scope), recommending batch operations when sequential probes could be combined, and pointing agents toward pre-computed or recently-cached answers.

The paper cites empirical evidence that this approach works: providing grounding hints to agents in a multi-database task reduced total queries by over 20%, with some phases seeing reductions of 27-37%.

## Key Points

- **On-demand activation**: Sleeper agents are invoked when probes arrive, running in parallel with query execution
- **Side-channel feedback**: Provide information alongside (not instead of) direct query answers
- **Join discovery**: Suggest related tables that could enhance or replace the current analysis
- **Why-not provenance**: Explain why queries returned unexpected results (empty sets, wrong formats)
- **Cost-based steering**: Warn about expensive queries and suggest cheaper alternatives before execution
- **Empirical support**: Grounding hints reduced agent queries by 20-37% in case studies

## Related Concepts

- [Agent-First Data Systems Architecture](agent-first-data-systems-architecture.md) - sleeper agents are a key component of the architecture
- [Probes and Briefs](probes-and-briefs.md) - the input that triggers sleeper agent activation
- [Agentic Memory Store](agentic-memory-store.md) - sleeper agents may query and update the memory store
- [Agentic Speculation](agentic-speculation.md) - sleeper agents reduce the inefficiency of speculative exploration

## Sources

- raw/20250901-agent-first-data-systems.md - introduced sleeper agents for auxiliary information and cost-based feedback (Sec. 4.2)
