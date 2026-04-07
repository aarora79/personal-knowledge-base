---
title: Programming as Theory Building
created: 2026-04-07
updated: 2026-04-07
sources: [raw/20260407-pablorauzyname-dev-naur1985programmingpdf.md]
related: [[tacit-knowledge-in-software]], [[program-lifecycle]], [[software-modification-challenges]], [[metaphor-driven-design]]
---

# Programming as Theory Building

"Programming as Theory Building" is a seminal 1985 essay by Peter Naur arguing that the essence of programming is not the production of source code and documentation, but rather the building of a *theory* in the minds of the programmers. Naur uses "theory" in the sense of philosopher Gilbert Ryle: a form of knowledge that enables a person not merely to do certain things, but to explain them, justify them, and respond intelligently to novel situations.

Naur's central claim is that a program is fundamentally a shared mental construct held by the programmers who built it. The code is merely a written representation of that theory, and it is inherently lossy -- you cannot fully reconstruct the program's theory from its source code and documentation alone. This stands in contrast to the "production view" of programming, which treats programming as the manufacture of program texts and associated documents.

Naur identifies three essential capabilities that a programmer possessing the theory of a program has, which transcend what documentation can capture:

1. **Explaining the world-mapping**: The programmer can explain how each part of the program relates to the real-world affairs it models, and conversely, how any aspect of the real world maps into the program text.

2. **Justifying design decisions**: The programmer can explain why each part of the program is what it is, providing rationale grounded in direct, intuitive knowledge rather than mechanically applied rules.

3. **Responding to modification demands**: The programmer can perceive the similarity between new requirements and existing program capabilities, and can design modifications that fit naturally within the program's existing structure.

The essay draws on real-world case studies to illustrate its points: a compiler team whose deep structural understanding could not be transferred through documentation alone, and a large real-time monitoring system whose maintenance depended entirely on programmers with years of continuous involvement. These cases demonstrate that even comprehensive documentation and personal guidance prove insufficient for transferring the full depth of design knowledge.

Naur's view has profound implications for software engineering practice, challenging assumptions about programmer replaceability, the sufficiency of documentation, and the viability of rigid programming methods as substitutes for genuine understanding.

## Key Points
- A program is a theory in the minds of programmers, not the source code itself
- Code and documentation are lossy representations of the underlying theory
- Programmers with the theory can explain, justify, and intelligently modify the program
- The theory cannot be captured by any set of rules or documentation
- This view challenges the "production" metaphor of programming as text manufacturing
- Naur draws on Ryle's distinction between intelligent behavior and intellectual (theory-holding) behavior
- The essay critiques programming methods as unable to substitute for genuine understanding
- Programmers should be treated as permanent, responsible professionals rather than replaceable components

## Related Concepts
- [[tacit-knowledge-in-software]] - Ryle's notion of theory as knowledge that cannot be fully articulated
- [[program-lifecycle]] - Naur's concepts of program life, death, and revival
- [[software-modification-challenges]] - Why program modifications are inherently difficult
- [[metaphor-driven-design]] - Using shared metaphors to communicate design theories

## Sources
- raw/20260407-pablorauzyname-dev-naur1985programmingpdf.md - Peter Naur's 1985 essay, the primary and defining source for this concept
