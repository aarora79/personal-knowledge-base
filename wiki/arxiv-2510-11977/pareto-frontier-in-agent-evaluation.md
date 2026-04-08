---
title: Pareto Frontier in Agent Evaluation
created: 2026-04-08
updated: 2026-04-08
sources: [raw/20260408-arxiv-2510-11977.md]
related: [Holistic Agent Leaderboard](holistic-agent-leaderboard.md), [Agent Scaffolds](agent-scaffolds.md), [Reasoning Effort Tradeoffs](reasoning-effort-tradeoffs.md)
tags: [pareto-frontier, cost-accuracy, agent-evaluation, model-selection, inference-cost, ai-agents, benchmarking]
---

# Pareto Frontier in Agent Evaluation

The Pareto frontier in agent evaluation identifies the set of model-scaffold configurations that achieve the best accuracy for a given cost budget, where no configuration can improve accuracy without increasing cost. HAL's systematic computation of Pareto frontiers across 9 benchmarks revealed that the frontier is typically both steep and sparse, meaning most models are dominated by cheaper alternatives that achieve comparable accuracy.

This analysis challenges the assumption that the most expensive models are the best choice. In only 1 of 9 benchmarks does the most costly model appear on the Pareto frontier, despite costing an order of magnitude more than mid-tier options (Claude Opus 4.1 at $15/$75 per million tokens vs. GPT-5 at $1.25/$10).

## Key Points

- **Steep frontier**: The most expensive model is on the Pareto frontier in only 1 of 9 benchmarks, indicating diminishing returns at high cost levels
- **Sparse frontier**: On average, less than one-third of tested models are on the frontier for a given benchmark
- **Top Pareto models**: Gemini 2.0 Flash (7 of 9 benchmarks), GPT-5 (4 of 9), and o4-mini Low (4 of 9) — these differ in cost by an order of magnitude
- **Worst Pareto performers**: DeepSeek R1 (0 of 9), Claude-3.7 Sonnet High (1 of 9)
- Token usage vs. dollar cost frontiers tell different stories: Claude Opus 4.1 appears on the token-usage Pareto frontier in 3 of 8 benchmarks but the dollar-cost frontier only once, because model prices change frequently (e.g., o3's price dropped 80% since initial release)
- On 6 of 9 benchmarks, there is a positive correlation between token usage and accuracy, indicating inference-time scaling has not yet yielded dramatic efficiency gains for long-horizon tasks
- HAL plots the convex hull because one can interpolate between agents by randomly selecting between them to achieve intermediate cost-accuracy points

## Related Concepts

- [Holistic Agent Leaderboard](holistic-agent-leaderboard.md) - the framework that enables systematic Pareto analysis
- [Agent Scaffolds](agent-scaffolds.md) - scaffold choice dramatically affects position on the Pareto frontier
- [Reasoning Effort Tradeoffs](reasoning-effort-tradeoffs.md) - higher reasoning effort shifts models along the cost axis without guaranteed accuracy gains

## Sources

- raw/20260408-arxiv-2510-11977.md - Pareto frontier analysis across 9 benchmarks (Figure 2), token vs. cost frontiers, model pricing comparisons
