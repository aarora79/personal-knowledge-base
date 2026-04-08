---
title: "Source Summary: SATLUTION - Autonomous Code Evolution Meets NP-Completeness"
created: 2026-04-08
source: raw/20260408-arxiv-2509-07367.md
depth: 500
articles_created: [satlution-framework.md, llm-code-evolution.md, boolean-satisfiability.md, self-evolving-rule-systems.md, repository-scale-code-evolution.md, verification-pipelines-for-code-evolution.md, evolutionary-coding-agents.md, multi-armed-bandit-heuristic-tuning.md]
---

# SATLUTION: Autonomous Code Evolution Meets NP-Completeness - Summary

This paper by Yu et al. (NVIDIA Research / University of Maryland, 2025) presents SATLUTION, the first framework to extend LLM-based code evolution from isolated algorithmic kernels to full repository-scale software engineering. Targeting Boolean Satisfiability (SAT) -- the canonical NP-complete problem and a cornerstone of both computational complexity theory and industrial applications -- SATLUTION orchestrates LLM agents to autonomously evolve SAT solver repositories under strict correctness guarantees and distributed runtime feedback. The evolved solvers decisively outperformed the human-designed winners of both SAT Competition 2024 and 2025.

## Architecture and Agent Framework

SATLUTION operates as a dual-agent iterative loop built on Claude models within the Cursor IDE. The **Planning Agent** performs high-level strategic reasoning: analyzing codebases, performance metrics, and past failures to formulate evolution plans. The **Coding Agent** executes these plans at the repository level -- editing source files across hundreds of C/C++ files, updating Makefile build systems, fixing compilation errors, and debugging memory faults. The agents operate under a Champion/Challenger model where successful variants replace incumbents.

```
  +------------------+       +------------------+       +------------------+
  |  Planning Agent  |       |  Coding Agent    |       |  Distributed     |
  |  (Claude LLM)   |       |  (Claude LLM)    |       |  Evaluator       |
  +--------+---------+       +--------+---------+       +--------+---------+
           |                          |                          |
           |  1. Evolution plan       |                          |
           |------------------------->|                          |
           |                          |                          |
           |                          |  2. Edit repository      |
           |                          |  (src/, Makefile, etc.)  |
           |                          |                          |
           |                          |  3. Submit for verify    |
           |                          |------------------------->|
           |                          |                          |
           |                          |  4. Stage 1: Compile +   |
           |                          |     smoke test (115 CNF) |
           |                          |                          |
           |                          |  5. Stage 2: DRAT proof  |
           |                          |     + SAT assignment     |
           |                          |     validation           |
           |                          |                          |
           |  6. Performance feedback |                          |
           |  (PAR-2, solved counts,  |<-------------------------|
           |   runtime distributions) |                          |
           |                          |                          |
           |  7. Reason + next plan   |                          |
           |<-------------------------|                          |
```

The framework was initialized with five diverse SAT solvers from the 2024 competition (kissat-sc2024, kissat-mab-dc, kissat-mab-binary, BreakID-Kissat, AMSAT), providing a portfolio of complementary algorithmic strategies. Portfolio/parallel solver construction was explicitly forbidden -- all evolved solvers adhere to sequential solver requirements.

## Self-Evolving Rule System

A critical architectural innovation is the rule system that combines static human-authored constraints with dynamically self-evolved rules. The static rulebase encodes domain knowledge (CDCL principles, restart policies), correctness constraints (mandatory DRAT proofs, no instance-specific optimizations), repository structure mandates, and evaluation protocols. Six rule files stored in `.cursor/rules/` cover compliance verification, pre-evaluation testing, critical correctness, mandatory logging, forbidden patterns, and automatic rule evolution.

Dynamic rules emerge through post-cycle analysis: a post-mortem analyzer parses compile errors, verifier mismatches, and new failure signatures, proposing rule patches injected as concrete diffs. Three categories of dynamic rules accumulate: **forbidden rules** (blocking known bad patterns), **champion rules** (preserving strategies from top performers), and **failure rules** (preventing repetition of past mistakes). Ablation studies confirmed that without static initialization rules, 35% of cycles produced failures and 40% produced degraded performance in a 20-cycle test.

## Verification Pipeline

Each iteration passes through a two-stage verification pipeline before receiving performance feedback. Stage 1 performs compilation checking and runs 115 trivial CNF smoke tests, catching crashes, segfaults, and obvious incorrect results. Stage 2 performs full correctness validation: SAT results require verified satisfying assignments; UNSAT results require externally validated DRAT proofs. No solver passing both stages ever produced a misclassification on competition benchmarks. Across 70 cycles, the pipeline automatically detected and pruned 11 variants with segmentation faults, 4 with proof validation failures, and 9 with significant performance regressions.

## Performance Feedback and Reward Design

The distributed evaluator runs on 800 CPU nodes in parallel, providing near-immediate feedback on the full 400-instance SAT Competition 2024 benchmark. Metrics include PAR-2 scores (overall, SAT-only, UNSAT-only), solved instance counts across multiple time thresholds (300s, 600s, 1000s, 2000s, 3000s, 4500s), Virtual Best Solver (VBS) match rates, and memory usage statistics. Notably, PAR-2 feedback was withheld until cycle 33 to prevent the agent from developing degenerate optimizations focused on gaming the metric rather than genuinely improving solving performance. The composite feedback design proved essential for balanced improvement across both SAT and UNSAT instance categories.

## Results and Learned Techniques

Over approximately 70 evolution cycles, SATLUTION produced solvers achieving the lowest PAR-2 scores across all entrants in both SAT Competition 2024 and 2025 benchmarks. The top-3 evolved solvers solved 347, 345, and 344 instances on the 2025 benchmark, compared to 334 and 331 for the gold and silver human-designed winners. The evolution trajectory showed rapid improvement in cycles 1-10, continued gains through cycle 50 (surpassing the 2025 winner), and final convergence around cycle 70 with over 10,000 lines of cumulative code changes.

Key solver-design techniques discovered include: multi-UIP clause learning with bandit-based depth selection, adaptive vivification with bandit control to balance SAT/UNSAT trade-offs, conflict- and propagation-aware reward signals with Adam-like updates, multi-domain bandit control coordinating subsystems (vivification, restarts, UIP depth, clause reduction), BreakID symmetry integration, and compressed watch list architectures for memory efficiency.

## Limitations

The framework performed best in semi-automated mode with human guidance for high-level strategy. Fully autonomous "YOLO mode" struggled with deep memory errors and domain-specific reasoning. The agents lacked sufficient domain knowledge at the idea level for nuanced SAT solving decisions. The entangled nature of cumulative modifications (10,000+ lines across hundreds of files) made controlled ablation studies of individual components impractical.

## What This Source Covers
- Repository-scale LLM-based code evolution architecture and agent framework
- Self-evolving rule systems combining static and dynamic constraints
- Two-stage verification pipelines with formal proof validation (DRAT)
- Distributed performance evaluation and reward signal design for solver evolution
- Comprehensive SAT Competition 2024/2025 benchmark results
- Distilled solver-design techniques: multi-UIP, bandit-tuned vivification, multi-domain bandit control
- Comparison with AlphaEvolve and discussion of current limitations

## Wiki Articles From This Source
- [SATLUTION Framework](satlution-framework.md) - the overall self-evolving coding framework for SAT solving
- [LLM Code Evolution](llm-code-evolution.md) - the broader paradigm of using LLMs to iteratively evolve code
- [Boolean Satisfiability](boolean-satisfiability.md) - the canonical NP-complete problem and SAT solving history
- [Self-Evolving Rule Systems](self-evolving-rule-systems.md) - static + dynamic rule architectures for agent guidance
- [Repository-Scale Code Evolution](repository-scale-code-evolution.md) - extending code evolution to full repositories
- [Verification Pipelines for Code Evolution](verification-pipelines-for-code-evolution.md) - two-stage correctness checking
- [Evolutionary Coding Agents](evolutionary-coding-agents.md) - Planning + Coding agent architecture
- [Multi-Armed Bandit Heuristic Tuning](multi-armed-bandit-heuristic-tuning.md) - bandit-based optimization of solver heuristics
