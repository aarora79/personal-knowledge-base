---
title: Agent Scaffolds
created: 2026-04-08
updated: 2026-04-08
sources: [raw/20260408-arxiv-2510-11977.md]
related: [Holistic Agent Leaderboard](holistic-agent-leaderboard.md), [Agent Evaluation Benchmarks](agent-evaluation-benchmarks.md), [Pareto Frontier in Agent Evaluation](pareto-frontier-in-agent-evaluation.md), [Agent Communication Protocols](../ietf-draft-narajala-ans/agent-communication-protocols.md), [Progressive Disclosure in AI Tools](../frontend-slides/progressive-disclosure-in-ai-tools.md)
tags: [agent-scaffolds, task-specific, generalist, smolagents, swe-agent, ai-agents, agent-architecture, multi-agent-systems]
---

# Agent Scaffolds

Agent scaffolds are the prompts, tools, and control logic that allow language models to solve agentic tasks. They represent the critical layer between a base language model and the environment, determining how the model perceives tasks, selects actions, and processes feedback. The HAL evaluation revealed that scaffold choice creates drastic differences in both cost and accuracy, often exceeding the impact of model selection.

The distinction between task-specific and generalist scaffolds is central to agent design. Task-specific scaffolds leverage domain knowledge and specialized tools (e.g., SWE-Agent provides a custom shell interface for code editing, CORE-Agent has prompts specifically directing reproducibility tasks). Generalist scaffolds use the same setup across benchmarks with general-purpose tools and prompts, built using frameworks like smolagents.

## Key Points

- **Task-specific scaffolds evaluated**: BrowserUse and SeeAct (web navigation), CORE-Agent (computational reproducibility), SWE-Agent (code editing), SAB Self-Debug (scientific tasks with iterative refinement), USACO Episodic+Semantic (competitive programming with memory retrieval), SciCode Tool Calling (code generation with external tools), HF Open Deep Research (web search and reasoning)
- **Generalist scaffold**: Built using the smolagents framework, evaluated on CORE-Bench Hard, TAU-bench Airline, and SWE-bench Verified Mini
- Task-specific agents consistently outperform generalist scaffolds: on CORE-Bench Hard (9 of 12 runs), SWE-bench Verified Mini (11 of 12 runs)
- Generalist scaffolds cost less in 20 of 24 model comparisons, but the accuracy penalty is substantial
- Scaffold choice creates a 9x cost difference for just 2 percentage points of accuracy difference (Online Mind2Web: SeeAct with GPT-5 costs $171 vs. Browser-Use with Claude Sonnet 4 costs $1,577)
- Model-scaffold interactions are complex: Claude models perform better with BrowserUse while OpenAI models achieve higher accuracy with SeeAct
- The TAU-bench Few Shot scaffold was found to contain data leakage through automated log analysis and was excluded from results

## Related Concepts

- [Holistic Agent Leaderboard](holistic-agent-leaderboard.md) - the framework enabling cross-scaffold comparisons
- [Agent Evaluation Benchmarks](agent-evaluation-benchmarks.md) - the benchmarks each scaffold is paired with
- [Pareto Frontier in Agent Evaluation](pareto-frontier-in-agent-evaluation.md) - how scaffold choice affects cost-accuracy tradeoffs

## Sources

- raw/20260408-arxiv-2510-11977.md - scaffold descriptions (Table 3), task-specific vs. generalist comparison, model-scaffold interaction analysis
