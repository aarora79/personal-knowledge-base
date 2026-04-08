---
title: Multi-Armed Bandit Heuristic Tuning
created: 2026-04-08
updated: 2026-04-08
sources: [raw/20260408-arxiv-2509-07367.md]
related: [satlution-framework](satlution-framework.md), [boolean-satisfiability](boolean-satisfiability.md)
tags: [multi-armed-bandit, heuristic-optimization, sat-solving, adaptive-algorithms, reinforcement-learning]
---

# Multi-Armed Bandit Heuristic Tuning

Multi-armed bandit (MAB) heuristic tuning is an approach to dynamically selecting and adapting solver heuristics at runtime using bandit algorithms. In the context of SAT solving, this technique emerged as one of the most consistently effective innovations discovered by the SATLUTION evolution process. Rather than statically configuring heuristic parameters, MAB-based tuning allows the solver to adaptively allocate effort across competing strategies based on their observed effectiveness during the solving process.

## Techniques Discovered by SATLUTION

The evolution process distilled several bandit-based techniques across multiple solver subsystems:

**Bandit-Tuned UIP Depth**: Modern CDCL solvers typically use 1-UIP (first Unique Implication Point) for clause learning. SATLUTION explored multi-UIP strategies that generate several UIP candidates (1-UIP, 2-UIP, last-UIP) and select based on clause-quality metrics (LBD/size). A lightweight bandit selects the UIP depth or candidate, with reward based on downstream clause utility such as propagation and shortening effects. This reduced the overhead of fixed multi-UIP by focusing effort where it pays off and stabilized performance across mixed instance families.

**Bandit-Tuned Vivification**: Clause vivification (strengthening learned clauses through unit propagation) exhibits a critical trade-off: aggressive vivification speeds UNSAT proofs through stronger clauses but can slow SAT search through overhead and over-tightening. SATLUTION discovered adaptive vivification tiers controlled by a bandit guided by an efficiency signal (literals removed per clauses checked), optionally with Adam-like updates. This reliably recovered UNSAT benefits while avoiding over-vivification on SAT-heavy cases.

**Reward Design and Update Mechanisms**: The evolution shifted reward signals from "variable coverage" proxies toward conflict- and propagation-centered signals that better correlate with PAR-2 performance. Simple UCB updates were replaced with history-aware and Adam-like updates for robustness under noisy, non-stationary feedback.

**Multi-Domain Bandit Control**: The most sophisticated technique coordinates several solver subsystems (vivification, restarts via VSIDS/CHB, UIP depth, clause reduction) through concurrent bandits with light cross-regularization. This produces balanced, self-tuned behavior that avoids over-optimizing one component at the expense of others.

**Adaptive Sliding Window**: Adjusts statistics windows and discounting based on variance and non-stationary signals to handle phase transitions between exploration and exploitation phases, reducing oscillations in policy.

## Key Points
- MAB algorithms dynamically select among competing heuristic strategies at runtime
- Applied across multiple SAT solver subsystems: UIP depth, vivification, restarts, clause reduction
- Adam-like update mechanisms improve learning under noisy, non-stationary feedback
- Multi-domain bandit control coordinates subsystems to avoid over-optimizing any single component
- Reward design critically shapes solver behavior (variable-coverage vs. conflict/propagation signals)
- These techniques emerged autonomously through LLM-guided evolution, not human design

## Related Concepts
- [SATLUTION Framework](satlution-framework.md) - the evolution framework that discovered these techniques
- [Boolean Satisfiability](boolean-satisfiability.md) - the problem domain where MAB tuning applies

## Sources
- raw/20260408-arxiv-2509-07367.md - Table 4 and discussion of distilled solver-design insights including multi-UIP, vivification, reward design, and multi-domain bandit control
