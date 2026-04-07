---
title: "Source Summary: Programming as Theory Building (Peter Naur, 1985)"
created: 2026-04-07
source: raw/20260407-naur-programming-as-theory-building.md
depth: 500
articles_created: [programming-as-theory-building.md, tacit-knowledge-in-software.md, program-lifecycle.md, software-modification-challenges.md, metaphor-driven-design.md]
---

# Programming as Theory Building - Expert Summary

Peter Naur's 1985 essay, originally published in *Microprocessing and Microprogramming* and reprinted in his collection *Computing: A Human Activity* (1992), advances a thesis that fundamentally reframes what programming is. Naur argues that the primary product of programming is not source code, documentation, or any other artifact -- it is a **theory** held in the minds of the programmers. The term "theory" is used in Gilbert Ryle's philosophical sense (from *The Concept of Mind*, 1949): not a formal model or set of propositions, but a form of knowledge that enables intelligent performance -- the ability to do, explain, and adapt.

## The Ryle Foundation

Naur draws on Ryle's distinction between "knowing that" (propositional knowledge) and "knowing how" (practical mastery). Ryle argues that intelligent behavior is not reducible to following rules, because rule-following itself requires intelligence (leading to an infinite regress). Instead, intelligence is characterized by the capacity to build and hold a **theory** -- knowledge that enables a person to act appropriately in novel situations, explain their actions, and recognize similarities across contexts. Crucially, this knowledge is not fully articulable; it cannot be exhaustively encoded in rules or documents.

Naur maps this directly onto programming. A programmer who holds the theory of a program possesses three capabilities that transcend any documentation: (1) the ability to explain how the program's structure maps to the real-world domain it serves, including aspects that are deliberately excluded; (2) the ability to justify each part of the program text -- not just what it does, but *why* it was designed that way, which ultimately rests on the programmer's direct, intuitive knowledge; and (3) the ability to respond constructively to modification requests by perceiving the similarity between new requirements and the existing solution's conceptual structure.

## Empirical Grounding: Two Case Studies

Naur grounds his argument in two real-world cases. **Case 1** involves a compiler originally built by Group A for language L on computer X. Group B acquires full documentation, annotated source, and advisory support from Group A to build a compiler for language L+M on computer Y. Despite this extensive knowledge transfer, Group B's design proposals repeatedly fail to leverage deep structural facilities of the original compiler -- facilities that were documented but whose significance could only be appreciated by theory-holders. Over the following decade, as Group B's programmers modified the compiler without Group A's guidance, the originally powerful architecture degraded into an incoherent patchwork.

**Case 2** describes a large real-time industrial monitoring system where installation and fault-finding programmers, who had been continuously involved since the design phase, could diagnose faults by drawing on internalized knowledge of the system. External programmers with full documentation could not replicate this capability. Other programmer groups responsible for specific installations also found existing documentation inadequate, tracing their difficulties to the gap between documented knowledge and the installation team's tacit understanding.

## Program Life, Death, and Revival

The Theory Building View yields a precise taxonomy of program states. A program is **alive** when a team possessing its theory maintains active control, including the ability to make modifications that are coherent with the program's conceptual architecture. A program **dies** when the theory-holding team is dissolved -- even if the code continues to execute in production. The hallmark of death is that modification requests can no longer be answered intelligently: changes become structurally incoherent patches.

Naur argues that program **revival** -- reconstructing the theory from code and documentation alone -- is "strictly impossible." At best, a new team builds a *different* theory that may diverge from the original in ways that introduce subtle inconsistencies. He recommends that in most cases, discarding the existing code and building anew is preferable to revival, as constructing a theory to fit existing code is more difficult, frustrating, and time-consuming than building a fresh solution.

## Implications for Modification Costs and Flexibility

The essay directly challenges the assumption that software modification is inherently cheap because "it's just text manipulation." Naur argues this reasoning is flawed on two fronts. First, the analogy to modifying physical structures does not hold -- buildings are often demolished rather than modified because modification is more expensive than rebuilding. Second, built-in program flexibility (parameterization, plugin architectures) comes at substantial design, implementation, and testing cost for each axis of flexibility, and its usefulness depends on accurately predicting future requirements. The Theory Building View explains why modifications by programmers who lack the theory produce structurally unsound results: perceiving the relevant similarity between the existing solution and the new requirement is a theory-dependent act that cannot be reduced to documented criteria.

## Consequences for Methods and Programmer Status

Naur critiques the notion of programming "methods" as fixed sequences of prescribed actions. Drawing on Feyerabend's *Against Method* (1978) and Medawar's critique of scientific method, he argues that theory-building has no inherent ordering -- a person possessing a theory can produce various representations of it in any sequence, in response to demands. The Theory Building View also elevates the programmer from a replaceable production worker to a professional whose knowledge is the essential asset, analogous to engineers or lawyers whose value rests on intellectual proficiency rather than adherence to mechanical procedures.

## Program Lifecycle Diagram

```
  PROGRAM BUILDING
  (Team constructs theory)
         |
         v
  +------------------+
  |  PROGRAM LIFE    |
  |  Theory-holders  |
  |  in control      |
  +--------+---------+
           |
     Team dissolved?
      /          \
    No            Yes
     |              \
     v               v
  (continues)   +------------------+
                |  PROGRAM DEATH   |
                |  Code runs, but  |
                |  no one holds    |
                |  the theory      |
                +--------+---------+
                         |
                  Attempt revival?
                   /          \
                 No            Yes
                  |              \
                  v               v
            (discard &     +------------------+
             rebuild)      |  PROGRAM REVIVAL |
                           |  New theory !=   |
                           |  original theory |
                           |  (Naur: strictly |
                           |   impossible)    |
                           +------------------+
```

## Theory Transfer: What Works vs. What Fails

```
  +---------------------+     Documentation     +-------------------+
  |  Group A            |  ------------------>   |  Group B          |
  |  (Theory holders)   |     Source code        |  (New team)       |
  |                     |  ------------------>   |                   |
  |  - Can explain WHY  |     Personal advice    |  - Has all docs   |
  |  - Can justify      |  ------------------>   |  - Proposes bad   |
  |  - Can modify       |                        |    solutions      |
  |    coherently       |                        |  - Ignores deep   |
  +---------------------+                        |    structure      |
                                                 +-------------------+
         RESULT: Theory cannot be fully
         transferred through artifacts alone.
         Apprenticeship-style collaboration
         is the only effective mechanism.
```

## What This Source Covers
- Ryle's epistemology applied to programmer knowledge
- Theory as tacit, non-articulable knowledge distinct from documentation
- Three capabilities unique to theory-holding programmers
- Two empirical case studies (compiler development, industrial monitoring)
- Program life/death/revival as theory preservation/loss/reconstruction
- Critique of low-cost modification assumptions
- Built-in flexibility costs and theory-dependent similarity recognition
- Rejection of fixed programming methods
- Programmer status as professional vs. production worker

## Wiki Articles From This Source
- [Programming as Theory Building](programming-as-theory-building.md) - Naur's core thesis that programming is theory building, not code production
- [Tacit Knowledge in Software](tacit-knowledge-in-software.md) - How programmer knowledge transcends what documentation can capture
- [Program Lifecycle](program-lifecycle.md) - Life, death, and revival of programs based on whether theory-holders remain
- [Software Modification Challenges](software-modification-challenges.md) - Why modifying programs without the underlying theory causes decay
- [Metaphor-Driven Design](metaphor-driven-design.md) - Using shared metaphors to align design understanding across teams
