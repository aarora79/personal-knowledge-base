---
title: Repository-Scale Code Evolution
created: 2026-04-08
updated: 2026-04-08
sources: [raw/20260408-arxiv-2509-07367.md]
related: [satlution-framework](satlution-framework.md), [llm-code-evolution](llm-code-evolution.md), [self-evolving-rule-systems](self-evolving-rule-systems.md), [verification-pipelines-for-code-evolution](verification-pipelines-for-code-evolution.md)
tags: [repository-scale, code-evolution, software-engineering, llm-agents, autonomous-coding]
---

# Repository-Scale Code Evolution

Repository-scale code evolution is the extension of LLM-based code self-improvement from isolated algorithmic kernels (single files, hundreds of lines) to full software repositories encompassing hundreds of files and tens of thousands of lines of code. This represents a qualitative leap in complexity compared to prior approaches like AlphaEvolve, which operated on self-contained code files.

The challenges of repository-scale evolution are fundamentally different from kernel-scale work. A full solver repository involves interconnected source files, header dependencies, build systems (Makefiles), linking configurations, and complex interactions between subsystems. Changes to one component can cause cascading effects: a modification to a heuristic function may break compilation, introduce memory safety issues, alter proof generation, or cause subtle performance regressions in unrelated solver phases. The coding agent must manage all of these concerns simultaneously.

SATLUTION addressed these challenges through several architectural decisions. Each solver variant follows a mandatory repository structure with `src/` for source code, `bin/` for compiled binaries, `build/` for build scripts, and documentation files tracking modifications and rationale. The framework enforces single-threaded C/C++ programs without external libraries, keeping the task focused on algorithmic innovation. Each iteration is stored in its own directory (SATLUTION_x/) with standardized layout, ensuring complete lineage and traceability.

Over approximately 70 evolution cycles, SATLUTION expanded the repository by more than 10,000 lines compared to initial baselines. The cumulative code modifications were so extensive and entangled that conducting controlled ablation studies of individual learned components became challenging. This highlights both the power and the difficulty of repository-scale evolution: the agent discovers synergistic combinations of improvements that would be difficult for humans to conceive or test in isolation.

A key finding was that the semi-automated approach proved more effective than fully autonomous operation. In fully automated "YOLO mode," agents struggled with deep memory errors like segmentation faults and SAT/UNSAT correctness violations. Human intervention remained critical for higher-level strategic direction, while the agents handled lower-level implementation effectively. This division of labor represents a practical balance for current LLM capabilities.

## Key Points
- Qualitative leap from single-file kernels to hundreds of files with build systems and interdependencies
- Mandatory repository structure ensures traceability and reproducible builds across evolution cycles
- Over 10,000 lines of cumulative code changes across 70 evolution cycles
- Semi-automated approach outperformed fully autonomous operation
- Human guidance for high-level strategy; agent handles low-level implementation
- Entangled improvements make individual ablation studies challenging

## Related Concepts
- [SATLUTION Framework](satlution-framework.md) - the first implementation of repository-scale evolution
- [LLM Code Evolution](llm-code-evolution.md) - the broader paradigm this extends
- [Self-Evolving Rule Systems](self-evolving-rule-systems.md) - the rules that make repo-scale evolution manageable
- [Verification Pipelines for Code Evolution](verification-pipelines-for-code-evolution.md) - correctness guarantees at repo scale

## Sources
- raw/20260408-arxiv-2509-07367.md - describes the challenges, architecture, and results of repository-scale evolution in SAT solving
