---
title: Boolean Satisfiability (SAT)
created: 2026-04-08
updated: 2026-04-08
sources: [raw/20260408-arxiv-2509-07367.md]
related: [satlution-framework](satlution-framework.md), [multi-armed-bandit-heuristic-tuning](multi-armed-bandit-heuristic-tuning.md)
tags: [sat-solving, np-complete, cdcl, computational-complexity, combinatorial-optimization]
---

# Boolean Satisfiability (SAT)

Boolean satisfiability (SAT) is the problem of determining whether there exists an assignment of truth values to variables that makes a given Boolean formula evaluate to true. First proven NP-complete by Stephen Cook in 1971, SAT is the canonical NP-complete problem and serves as a cornerstone of computational complexity theory, linking a wide array of decision problems to a unified theoretical framework.

Despite its worst-case intractability, practical SAT solving has achieved dramatic performance gains through decades of algorithmic innovation. The evolution began in the early 1990s with the **DPLL (Davis-Putnam-Logemann-Loveland)** backtracking framework. Breakthroughs around 2000 introduced **Conflict-Driven Clause Learning (CDCL)**, the algorithmic foundation of virtually all modern SAT solvers. CDCL extends DPLL with the ability to analyze conflicts during search, learn new clauses that prevent repeating failed assignments, and perform non-chronological backtracking. Additional key techniques include two-watched literals for efficient unit propagation, dynamic restart policies, clause deletion heuristics, bound variable elimination, and clause vivification.

The **SAT Competition**, held annually since 2002, serves as the central benchmarking platform for solver advances. It hosts diverse tracks (sequential, parallel, cloud) and attracts benchmark submissions from planning, industrial verification, and AI communities. Competition-winning solvers represent the culmination of expert-driven design, with each edition embodying the state-of-the-art. Key solver families include zChaff, MiniSat, Glucose, Lingeling/CaDiCaL, Kissat, and MapleSAT.

Performance is typically measured using the **PAR-2 (Penalized Average Runtime)** metric, which averages solver runtimes across benchmark instances with a 2x timeout penalty for unsolved instances (e.g., 10,000 seconds for a 5,000-second timeout). Lower PAR-2 indicates better performance. Correctness is validated through satisfying assignment verification for SAT results and DRAT (Deletion Resolution Asymmetric Tautology) proof checking for UNSAT results.

The SATLUTION framework demonstrated that LLM-based code evolution can surpass human-designed SAT solvers, achieving the lowest PAR-2 scores on both SAT Competition 2024 and 2025 benchmarks despite being trained only on 2024 data.

## Key Points
- First problem proven NP-complete (Cook, 1971); foundational to computational complexity
- CDCL is the core algorithm of modern SAT solvers, extending DPLL with clause learning
- SAT Competition (since 2002) is the primary benchmarking arena for solver innovation
- PAR-2 is the standard performance metric; DRAT proofs validate unsatisfiability claims
- Applications span hardware verification, software analysis, planning, and cryptography
- Designing champion solvers by hand yields diminishing returns, motivating autonomous approaches

## Related Concepts
- [SATLUTION Framework](satlution-framework.md) - LLM-evolved solvers that outperform human-designed SAT Competition winners
- [Multi-Armed Bandit Heuristic Tuning](multi-armed-bandit-heuristic-tuning.md) - bandit-based optimization of SAT solver heuristics

## Sources
- raw/20260408-arxiv-2509-07367.md - comprehensive overview of SAT solving history, CDCL, SAT Competition, and how SATLUTION advances the field
