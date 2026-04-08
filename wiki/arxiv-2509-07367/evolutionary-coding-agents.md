---
title: Evolutionary Coding Agents
created: 2026-04-08
updated: 2026-04-08
sources: [raw/20260408-arxiv-2509-07367.md]
related: [satlution-framework](satlution-framework.md), [llm-code-evolution](llm-code-evolution.md), [self-evolving-rule-systems](self-evolving-rule-systems.md), [../ietf-draft-narajala-ans/agent-communication-protocols](../ietf-draft-narajala-ans/agent-communication-protocols.md)
tags: [coding-agents, llm-agents, multi-agent-systems, planning-agents, ai-agents, autonomous-coding]
---

# Evolutionary Coding Agents

Evolutionary coding agents are LLM-based agent systems designed to iteratively improve software through repeated cycles of planning, coding, evaluation, and feedback. Unlike single-turn code generation, these agents maintain context across iterations, learn from past failures, and accumulate knowledge that guides future modifications. The SATLUTION framework provides the most advanced example of this architecture applied to a complex real-world engineering challenge.

## Planning and Coding Agent Architecture

SATLUTION uses a dual-agent architecture built on Claude models within the Cursor IDE environment. The **Planning Agent** performs high-level reasoning: at the initial cycle, it analyzes solver codebases and performance data, proposing modification directions such as optimizing specific heuristics or refactoring key modules. In subsequent cycles, it reasons about accumulated code changes, performance metrics, and observed failures to formulate an evolution plan. The **Coding Agent** executes these plans by directly editing the solver repository, managing build configurations, fixing compilation errors, and debugging functional and execution errors.

## Champion/Challenger Model

The evolution follows a Champion/Challenger model where the agent proposes modifications, implements them, and the new solver is evaluated against current best performers. Successful challengers replace champions, creating a continuous self-improvement cycle. The process follows a five-step loop: Generate, Compile, Test, Analyze & Reason, and Evolve.

## Feedback-Driven Evolution

The agents receive multi-faceted performance feedback after each verified iteration, including PAR-2 scores, solved instance counts broken down by SAT/UNSAT, runtime distributions across time thresholds, memory usage statistics, and Virtual Best Solver (VBS) comparisons. This composite feedback enables nuanced decision-making: the agent can distinguish between changes that improve SAT solving at the expense of UNSAT, or vice versa. Notably, PAR-2 score feedback was introduced only after cycle 33 to prevent the agent from developing "weird optimizations" focused on gaming the competition metric rather than genuinely improving solving ability.

## Limitations

In fully autonomous operation, agents struggled with deep memory errors and domain-specific reasoning. The most effective setup involved human guidance for higher-level strategies with agents handling implementation. The planning capabilities were strong for concrete programming tasks but lacked sufficient domain-specific knowledge for nuanced SAT solving decisions. Agents without initial static rule guidance consistently underperformed, producing noisy or unstable modifications.

## Key Points
- Dual-agent architecture: Planning Agent for strategy + Coding Agent for implementation
- Champion/Challenger model drives continuous improvement through competitive evaluation
- Multi-faceted feedback prevents narrow optimization; PAR-2 introduced late to avoid gaming
- Semi-automated operation outperformed fully autonomous "YOLO mode"
- Agents excel at implementation but need human guidance for domain-specific strategic decisions
- Rule-guided scaffolding essential for stable evolutionary progress

## Related Concepts
- [SATLUTION Framework](satlution-framework.md) - the primary implementation of evolutionary coding agents
- [LLM Code Evolution](llm-code-evolution.md) - the broader paradigm these agents enable
- [Self-Evolving Rule Systems](self-evolving-rule-systems.md) - the guidance framework for these agents
- [Agent Communication Protocols](../ietf-draft-narajala-ans/agent-communication-protocols.md) - broader context of multi-agent system design

## Sources
- raw/20260408-arxiv-2509-07367.md - detailed description of the Planning and Coding agent architecture, feedback mechanisms, Champion/Challenger model, and limitations
