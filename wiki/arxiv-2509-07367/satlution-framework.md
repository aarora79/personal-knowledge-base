---
title: SATLUTION Framework
created: 2026-04-08
updated: 2026-04-08
sources: [raw/20260408-arxiv-2509-07367.md]
related: [llm-code-evolution](llm-code-evolution.md), [repository-scale-code-evolution](repository-scale-code-evolution.md), [self-evolving-rule-systems](self-evolving-rule-systems.md), [verification-pipelines-for-code-evolution](verification-pipelines-for-code-evolution.md), [boolean-satisfiability](boolean-satisfiability.md)
tags: [satlution, sat-solving, llm-agents, code-evolution, autonomous-coding, np-complete]
---

# SATLUTION Framework

SATLUTION is the first repository-scale, self-evolving coding framework that uses LLM-based agents to autonomously improve SAT solvers. Developed by researchers at NVIDIA Research and the University of Maryland, SATLUTION extends the concept of LLM-guided code evolution (pioneered by Google's AlphaEvolve) from single-file algorithm kernels to full solver repositories encompassing hundreds of files and tens of thousands of lines of C/C++ code.

The framework orchestrates two LLM-based stages in an iterative loop. In the **Planning stage**, a Claude model analyzes solver codebases, accumulated performance metrics, and prior failures to formulate an evolution plan for the next iteration. In the **Coding stage**, a second Claude model executes these plans by directly editing the solver repository, managing build configurations, fixing compilation errors, and debugging functional failures. Both agents operate within the Cursor IDE environment, leveraging its rule system for structured guidance.

SATLUTION was initialized with five high-performance SAT solvers from the SAT Competition 2024 (kissat-sc2024, kissat-mab-dc, kissat-mab-binary, BreakID-Kissat, and AMSAT) as a diverse seed portfolio. Over approximately 70 evolution cycles, the framework autonomously discovered solver improvements that surpassed human-designed state-of-the-art solvers. Notably, SATLUTION's evolved solvers outperformed both the 2024 and 2025 SAT Competition winners on their respective benchmarks, despite being trained exclusively on 2024 competition data.

The framework's key architectural components include a [self-evolving rule system](self-evolving-rule-systems.md) that provides structured guidance and co-evolves with the solver, a [two-stage verification pipeline](verification-pipelines-for-code-evolution.md) that ensures correctness through compilation checks, smoke tests, and formal proof validation, and a distributed evaluation harness running on 800 CPU nodes that provides near-immediate performance feedback.

## Key Points
- First framework to extend LLM-based code evolution to full repository scale (hundreds of files, tens of thousands of lines)
- Evolved SAT solvers that outperformed human-designed winners of SAT Competition 2025
- Trained exclusively on 2024 benchmark data but generalized to unseen 2025 benchmarks
- Uses a Planning Agent + Coding Agent architecture running on Claude models within Cursor
- Approximately 70 evolution cycles with strict correctness guarantees throughout
- Added over 10,000 lines of code compared to initial baselines across evolution

## Related Concepts
- [LLM Code Evolution](llm-code-evolution.md) - the broader paradigm SATLUTION extends
- [Repository-Scale Code Evolution](repository-scale-code-evolution.md) - the key scaling contribution
- [Self-Evolving Rule Systems](self-evolving-rule-systems.md) - the rule architecture that guides evolution
- [Verification Pipelines for Code Evolution](verification-pipelines-for-code-evolution.md) - correctness safeguards
- [Boolean Satisfiability](boolean-satisfiability.md) - the target problem domain

## Sources
- raw/20260408-arxiv-2509-07367.md - primary source describing the complete SATLUTION framework, architecture, results, and methods
