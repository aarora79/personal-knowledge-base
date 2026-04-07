---
title: Tacit Knowledge in Software Development
created: 2026-04-07
updated: 2026-04-07
sources: [raw/20260407-pablorauzyname-dev-naur1985programmingpdf.md]
related: [programming-as-theory-building](programming-as-theory-building.md), [program-lifecycle](program-lifecycle.md), [software-modification-challenges](software-modification-challenges.md)
tags: [tacit-knowledge, epistemology, gilbert-ryle, knowledge-transfer, documentation, software-engineering-philosophy]
---

# Tacit Knowledge in Software Development

Tacit knowledge in software development refers to the deep, intuitive understanding that programmers hold about a system -- knowledge that cannot be fully expressed in documentation, specifications, or formalized rules. Peter Naur grounded this concept in the philosophy of Gilbert Ryle, whose "The Concept of Mind" (1949) distinguishes between merely intelligent behavior (doing things well) and intellectual activity (having a theory that enables explanation, argumentation, and adaptation).

In Ryle's framework, a theory is not confined to abstract or general principles. Having Newton's theory of mechanics, for example, means not just knowing the central laws but understanding how they apply to specific phenomena like pendulums and planetary motion, and being able to recognize similar phenomena in novel situations. Crucially, this recognition of similarity between situations cannot be reduced to rules or criteria -- just as the similarity between human faces, musical tunes, or tastes of wine cannot be formally specified.

Naur applies this directly to programming. The programmer who possesses the theory of a program holds knowledge that necessarily transcends all documented products. This knowledge manifests in three dimensions: the ability to explain how the program maps to real-world affairs, the ability to justify each design decision, and the ability to perceive how new requirements relate to existing program capabilities. None of these can be fully captured in any written form because they depend on recognizing similarities that resist formal specification.

This has direct practical consequences. In one of Naur's case studies, a group of programmers (Group B) received full documentation and personal advice from the original team (Group A) for a compiler extension project. Despite this extensive knowledge transfer, Group B repeatedly proposed solutions that ignored structural facilities thoroughly documented in the compiler's design materials. Group A could instantly spot these problems and propose simpler solutions within the existing structure. The theory was immediately present to Group A but inaccessible to Group B through documentation alone.

Ryle further notes that intelligent behavior is not dependent on following rules -- the very act of following rules can itself be done more or less intelligently, leading to an infinite regress. This insight undermines the premise that programming methods (understood as sets of procedural rules) can substitute for genuine understanding.

## Key Points
- Ryle distinguishes intelligent behavior (doing things well) from intellectual activity (having a theory)
- A theory includes knowing how abstract principles apply to specific real-world situations
- Recognition of similarity between situations cannot be reduced to formal rules or criteria
- Programmer knowledge necessarily transcends what documentation can capture
- Even highly motivated teams with full documentation fail to absorb tacit design knowledge
- The infinite regress argument: following rules itself requires intelligence, so rules cannot be the basis of intelligence
- Popper's "unembodied World 3 objects" provides philosophical grounding for Ryle's notion of theory

## Related Concepts
- [Programming as Theory Building](programming-as-theory-building.md) - The broader framework in which tacit knowledge plays a central role
- [Program Lifecycle](program-lifecycle.md) - Tacit knowledge loss is what causes program "death"
- [Software Modification Challenges](software-modification-challenges.md) - Modifications require tacit knowledge of structural similarity

## Sources
- raw/20260407-pablorauzyname-dev-naur1985programmingpdf.md - Naur's application of Ryle's philosophy to programming, including the compiler case study demonstrating tacit knowledge failure
