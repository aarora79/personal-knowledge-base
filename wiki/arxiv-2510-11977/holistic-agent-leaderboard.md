---
title: Holistic Agent Leaderboard (HAL)
created: 2026-04-08
updated: 2026-04-08
sources: [raw/20260408-arxiv-2510-11977.md]
related: [Agent Evaluation Benchmarks](agent-evaluation-benchmarks.md), [Agent Scaffolds](agent-scaffolds.md), [Pareto Frontier in Agent Evaluation](pareto-frontier-in-agent-evaluation.md), [Automated Agent Log Analysis](automated-agent-log-analysis.md), [Agent Evaluation Infrastructure](agent-evaluation-infrastructure.md), [Agent Discovery](../ietf-draft-narajala-ans/agent-discovery.md)
tags: [hal, agent-evaluation, leaderboard, benchmarking, reproducibility, ai-agents, multi-agent-systems]
---

# Holistic Agent Leaderboard (HAL)

The Holistic Agent Leaderboard (HAL) is a unified evaluation framework developed by researchers at Princeton University and collaborating institutions to address fundamental infrastructure gaps in AI agent evaluation. Unlike existing frameworks that focus on single benchmarks or accuracy-only metrics, HAL provides standardized, reproducible, cost-controlled agent benchmarking with automated log analysis across multiple domains.

HAL was validated through 21,730 agent rollouts spanning 9 benchmarks and 9 models across four domains (coding, web navigation, scientific research, and customer service), at a total compute cost of approximately $40,000. The framework introduces three-dimensional analysis spanning models, scaffolds, and benchmarks, revealing previously hidden interactions between these factors.

## Key Points

- HAL addresses 8 specific challenges in agent evaluation: non-standardized infrastructure, slow serial execution, manual leaderboard updates, missing cost reporting, single-benchmark evaluations, lack of scaffold comparisons, shortcut detection, and catastrophic action identification
- The harness accepts any agent exposing a minimal Python API (`run(input) -> dict`) and orchestrates evaluation across diverse benchmarks through distributed execution on hundreds of Azure VMs
- Integrates Weave for comprehensive logging, LiteLLM for cross-model compatibility, and supports local, Docker, and Azure VM execution environments
- Produces Pareto frontiers of accuracy versus cost (both dollar and token), enabling practitioners to select agents based on real-world constraints
- All 2.5 billion tokens of agent logs are publicly shared on HuggingFace to incentivize research into agent behavior
- HAL is the official evaluation harness for CORE-Bench Hard and ScienceAgentBench

## Related Concepts

- [Agent Evaluation Benchmarks](agent-evaluation-benchmarks.md) - the 9 benchmarks HAL evaluates across four domains
- [Agent Scaffolds](agent-scaffolds.md) - task-specific and generalist scaffolds compared in HAL
- [Pareto Frontier in Agent Evaluation](pareto-frontier-in-agent-evaluation.md) - cost-accuracy tradeoff analysis enabled by HAL
- [Automated Agent Log Analysis](automated-agent-log-analysis.md) - Docent-based log inspection integrated into HAL
- [Agent Evaluation Infrastructure](agent-evaluation-infrastructure.md) - the engineering challenges HAL addresses

## Sources

- raw/20260408-arxiv-2510-11977.md - primary source; Kapoor, Stroebl et al. "Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation" (2025)
