---
title: Agent Evaluation Infrastructure
created: 2026-04-08
updated: 2026-04-08
sources: [raw/20260408-arxiv-2510-11977.md]
related: [Holistic Agent Leaderboard](holistic-agent-leaderboard.md), [Agent Evaluation Benchmarks](agent-evaluation-benchmarks.md), [Agent Scaffolds](agent-scaffolds.md)
tags: [evaluation-infrastructure, distributed-systems, reproducibility, orchestration, litellm, weave, ai-agents]
---

# Agent Evaluation Infrastructure

Agent evaluation infrastructure refers to the standardized systems required to run reproducible, cost-controlled evaluations of AI agents at scale. The HAL project identified and addressed six major engineering requirements: comprehensive logging, scaffold support, benchmark integration, parallel execution, multiple execution environments, and one-command deployment. Prior to HAL, setting up a single benchmark could take a person-week of effort, and serial evaluation across models could take weeks.

The infrastructure challenges are fundamentally different from language model evaluation because agents navigate complex environments over extended time horizons, use tools from browsers to bash shells, consume hundreds of thousands of tokens per rollout, and can fail catastrophically or get trapped in loops.

## Key Points

- **Logging**: Integrated Weave for automatic telemetry across all major LLM libraries, with separate task IDs per benchmark task for granular tracking and unified cost tracking across providers
- **Scaffold support**: Minimal Python interface where scaffolds only expose a `run(input) -> dict(responses)` function, with isolated execution environments completely separate from benchmark infrastructure
- **Benchmark integration**: Common interface abstracting away benchmark-specific implementation details with standardized task data, evaluation logic, and scoring procedures — reduced setup time from weeks to hours
- **Parallel execution**: Orchestration layer managing hundreds of Azure VMs with batch processing and semaphore-based concurrency control, reducing evaluation time from weeks to hours
- **Cross-model compatibility**: LiteLLM integration for inference across major model providers, with numerous bug fixes contributed (e.g., GPT-5 initially lacked reasoning support, providers swap model weights without notice, aggregators like OpenRouter serve different quantizations for the same endpoint)
- **Three execution tiers**: Local for quick development, Docker for lightweight isolation, and Azure VMs for large-scale evaluation, all exposing a common interface
- A breaking OpenAI API update removed the `stop` keyword argument from o3 and o4-mini, breaking multiple agent scaffolds — highlighting the fragility of the current API ecosystem
- The entire Azure VM orchestration system was implemented from scratch as a significant engineering project

## Related Concepts

- [Holistic Agent Leaderboard](holistic-agent-leaderboard.md) - the framework this infrastructure supports
- [Agent Evaluation Benchmarks](agent-evaluation-benchmarks.md) - the benchmarks integrated into this infrastructure
- [Agent Scaffolds](agent-scaffolds.md) - the scaffold interface this infrastructure standardizes

## Sources

- raw/20260408-arxiv-2510-11977.md - infrastructure requirements and solutions (Table 2), engineering challenges, API compatibility issues (Section 2)
