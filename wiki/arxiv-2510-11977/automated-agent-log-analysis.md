---
title: Automated Agent Log Analysis
created: 2026-04-08
updated: 2026-04-08
sources: [raw/20260408-arxiv-2510-11977.md]
related: [Holistic Agent Leaderboard](holistic-agent-leaderboard.md), [Agent Shortcuts and Gaming](agent-shortcuts-and-gaming.md), [Agent Evaluation Benchmarks](agent-evaluation-benchmarks.md)
tags: [log-analysis, docent, agent-behavior, evaluation-methodology, rubric-analysis, ai-agents, observability]
---

# Automated Agent Log Analysis

Automated agent log analysis uses language models to systematically inspect agent execution traces at scale, identifying behaviors that accuracy metrics alone cannot capture. The HAL project employed Docent, an LLM-based transcript analysis tool, to examine 1,634 transcripts from 36 model-scaffold pairs across three benchmarks (AssistantBench, SciCode, and CORE-Bench), revealing critical failure modes, shortcuts, and reliability issues.

The approach is considered a cornerstone of agent evaluation because agents with identical accuracy scores can exhibit vastly different behaviors and risk profiles. A web agent that abstains from answering and one that leaks credit card information both receive a score of zero, but their real-world consequences differ enormously.

## Key Points

- **Docent rubrics** systematically categorize six behavioral dimensions: instruction violations, tool use failures, self-correction, verification, environmental barriers, and shortcuts/gaming
- **Self-correction matters**: When agents successfully fix tool call or instruction-following errors mid-run, they are 1.5x to 4x more likely to succeed at the task
- **Verification boosts success**: Agents that take explicit verification actions (constructing unit tests, producing artifacts, cross-referencing search results) are 13% to 87% more likely to succeed
- **Tool use is fragile**: On SciCode and CORE-Bench, agents almost never completed a run without at least one tool calling failure, even when ultimately succeeding
- **Instruction violations are pervasive**: On failed tasks in AssistantBench and CORE-Bench, agents violated an explicit benchmark instruction in their final answer over 60% of the time
- **Environmental barriers**: Agents encountered at least one environmental barrier (crashing browser, unavailable file, unavailable import) in roughly 40% of failed tasks
- **Scaffold design bugs uncovered**: Log analysis of TAU-bench revealed that the few-shot scaffold included actual benchmark examples in its few-shot data, constituting data leakage — discovered only after expensive evaluations were completed
- Automated log analysis validated via manual examination of flagged agent logs to confirm Docent's precision

## Related Concepts

- [Holistic Agent Leaderboard](holistic-agent-leaderboard.md) - integrates automated log analysis as a core evaluation component
- [Agent Shortcuts and Gaming](agent-shortcuts-and-gaming.md) - specific shortcut behaviors uncovered through log analysis
- [Agent Evaluation Benchmarks](agent-evaluation-benchmarks.md) - benchmarks where log analysis was applied

## Sources

- raw/20260408-arxiv-2510-11977.md - Docent analysis methodology, rubric design, behavioral findings across benchmarks (Section 4.2, Figure 4)
