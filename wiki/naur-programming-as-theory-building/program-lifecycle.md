---
title: Program Lifecycle (Life, Death, and Revival)
created: 2026-04-07
updated: 2026-04-07
sources: [raw/20260407-pablorauzyname-dev-naur1985programmingpdf.md]
related: [programming-as-theory-building](programming-as-theory-building.md), [tacit-knowledge-in-software](tacit-knowledge-in-software.md), [software-modification-challenges](software-modification-challenges.md)
tags: [program-lifecycle, team-continuity, knowledge-transfer, program-death, software-engineering-philosophy]
---

# Program Lifecycle (Life, Death, and Revival)

Peter Naur's Theory Building View of programming introduces a distinctive notion of program lifecycle defined not by whether the code executes, but by whether programmers possessing its theory remain in charge of it. This framework defines three states: program life, program death, and program revival.

**Program building** is the process by which a team of programmers constructs the theory of the program. This is synonymous with the programmers forming their deep understanding of how the program relates to real-world affairs, why design decisions were made, and how modifications should be incorporated.

**Program life** is the period during which a programmer team possessing the theory remains in active control of the program, retaining authority over all modifications. The program remains "alive" as long as its stewards can intelligently respond to demands for change.

**Program death** occurs when the programmer team possessing the theory is dissolved. A dead program may continue to execute and produce useful results, but its death becomes visible when demands for modifications can no longer be intelligently answered. The code still runs, but no one truly understands it at the level needed to evolve it coherently.

**Program revival** is the attempt to rebuild the theory of a program by a new programmer team. Naur argues this is strictly impossible in the full sense -- the revived theory will inevitably differ from the original, and may contain discrepancies with the program text. Revival is at best costly and at worst produces a theory fundamentally inconsistent with the existing code.

Naur's practical recommendation is striking: rather than attempting program revival, the existing program text should be discarded and the new team should solve the problem afresh. Building a theory to fit an existing, poorly understood program is more difficult and frustrating than building a new program from scratch, and the result is more likely to be viable.

For the extended life of a program, new programmers must work in close contact with existing team members who possess the theory. This is analogous to apprenticeship in crafts like music -- the student must practice under guidance, not merely study documentation. In programming, this means discussions about how the program relates to real-world situations, how unusual behaviors are handled, and how the program's theory accommodates change.

## Key Points
- Program life depends on the continued presence of programmers who hold the theory, not on code execution
- A "dead" program may still run perfectly but cannot be intelligently modified
- Program death becomes visible when modification demands cannot be competently addressed
- Program revival (rebuilding theory from documentation) is strictly impossible in full fidelity
- Naur recommends discarding dead program text and solving problems afresh over attempting revival
- Knowledge transfer requires apprenticeship-style close collaboration, not documentation study
- Team continuity and gradual onboarding of new members is essential for program longevity
- Similar challenges arise even in continuously maintained programs as team members are replaced

## Related Concepts
- [Programming as Theory Building](programming-as-theory-building.md) - The foundational view that defines this lifecycle framework
- [Tacit Knowledge in Software](tacit-knowledge-in-software.md) - The kind of knowledge whose loss causes program death
- [Software Modification Challenges](software-modification-challenges.md) - Dead programs accumulate incoherent modifications

## Sources
- raw/20260407-pablorauzyname-dev-naur1985programmingpdf.md - Naur's original formulation of program life, death, and revival, including the recommendation to discard dead programs rather than attempt revival
