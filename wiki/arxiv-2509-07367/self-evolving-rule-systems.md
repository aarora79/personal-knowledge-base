---
title: Self-Evolving Rule Systems
created: 2026-04-08
updated: 2026-04-08
sources: [raw/20260408-arxiv-2509-07367.md]
related: [satlution-framework](satlution-framework.md), [verification-pipelines-for-code-evolution](verification-pipelines-for-code-evolution.md), [evolutionary-coding-agents](evolutionary-coding-agents.md)
tags: [rule-systems, self-evolution, agent-guardrails, llm-agents, code-evolution, knowledge-management]
---

# Self-Evolving Rule Systems

Self-evolving rule systems are structured guidance frameworks for LLM-based coding agents that combine static human-authored rules with dynamically generated rules that co-evolve alongside the code being developed. In the SATLUTION framework, the rule system proved critical to the efficiency and correctness of the solver evolution process, serving as both guardrails and institutional memory.

## Static Initialization Rules

The system begins with an explicit, static rulebase authored by human domain experts that formalizes constraints and knowledge the agents need. In SATLUTION, six categories of static rules were defined: (1) **Project Goal** defining the evolution objective; (2) **Domain Knowledge Initialization** embedding basic SAT heuristics like restart policies, preprocessing, and CDCL principles; (3) **Critical Correctness Rules** enforcing strict guarantees such as mandatory DRAT proof generation and zero tolerance for heuristic-only termination; (4) **Repository Structure and Tracking** mandating documentation artifacts (HYPOTHESIS.md, CHANGELOG.md, RESULTS.md); (5) **Pre-Evaluation Verification** defining the compilation and smoke test pipeline; and (6) **Evaluation Protocol** specifying how performance metrics are computed.

Ablation experiments demonstrated the importance of static rules: without them, agents explored plausible but misleading directions such as early termination heuristics that spuriously predict satisfiability, or edits that weakened proof obligations. In 20 cycles without static rules, 7 produced failures and 8 produced significant performance degradation.

## Dynamic Self-Evolved Rules

SATLUTION embeds rulebase self-evolving mechanisms in every iteration through two processes. **Rule compliance verification** enforces rules actively before proposals enter the verifier, checking for mandatory documentation, packaging correctness, and scanning for forbidden patterns across source files. **Automatic rule evolution** runs a post-mortem analyzer after each cycle that parses compile errors, verifier mismatches, and new failure signatures, then proposes rule patches. An update engine injects these as concrete diffs to the rule files.

The rule files (stored in `.cursor/rules/`) include: `00_rule_compliance_verification.md`, `01_pre_evaluation_testing.md`, `02_critical_correctness.md`, `03_mandatory_logging.md`, `04_forbidden_patterns.md`, and `05_automatic_rule_evolution.md`. These evolve across cycles and remain machine-actionable via compliance checker scripts.

Three categories of dynamically generated rules emerged: **forbidden rules** blocking known bad patterns, **champion rules** preserving strategies from top-performing solvers, and **failure rules** preventing repetition of past mistakes. This creates institutional memory that accumulates across evolution cycles.

## Key Points
- Static rules encode human domain knowledge and correctness constraints as a foundation
- Dynamic rules co-evolve with the solver, capturing learned patterns and failure modes
- Rule compliance verification converts rules from passive text into active gates
- Without static rules, agents produce noisy, unstable modifications with frequent failures
- Three dynamic rule types: forbidden (bad patterns), champion (proven strategies), failure (past mistakes)
- The combination of static scaffolding and self-evolved refinements proved essential for progress

## Related Concepts
- [SATLUTION Framework](satlution-framework.md) - the system where self-evolving rules were developed and tested
- [Verification Pipelines for Code Evolution](verification-pipelines-for-code-evolution.md) - the correctness checking that rules feed into
- [Evolutionary Coding Agents](evolutionary-coding-agents.md) - the agents guided by these rules

## Sources
- raw/20260408-arxiv-2509-07367.md - detailed description of static and dynamic rule systems, ablation results, and the rule evolution mechanism
