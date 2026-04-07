---
title: Metaphor-Driven Design
created: 2026-04-07
updated: 2026-04-07
sources: [raw/20260407-pablorauzyname-dev-naur1985programmingpdf.md]
related: [[programming-as-theory-building]], [[tacit-knowledge-in-software]]
---

# Metaphor-Driven Design

Metaphor-driven design is the practice of organizing a program's design around a single, shared metaphor that helps the entire team develop a coherent understanding of the system. The concept connects Peter Naur's Theory Building View of programming with practices from Extreme Programming (XP), as discussed in a later addendum to Naur's original 1985 essay.

Kent Beck suggested that it is useful for a design team to simplify a program's general design to match a single metaphor. Examples include: "This program really looks like an assembly line, with things getting added to a chassis along the line," or "This program really looks like a restaurant, with waiters and menus, cooks and cashiers."

The power of a good metaphor lies in the many associations it creates. If "assembly line" is the chosen metaphor, later programmers can make accurate guesses about the software's structure based on what they know about assembly lines, and find that their guesses are "close." This is precisely Naur's idea of passing along a theory of the design -- the metaphor serves as a compressed, shareable vehicle for the theory.

**Alignment through metaphor**: When 10 programmers work in parallel, each making design decisions and adding code independently, their individual theories will naturally diverge, leading to increasing complexity and incoherence. A shared metaphor counteracts this by aligning each person's guesses about the system's structure. The closer each person's guess is to the others', the greater the consistency in the final design. The metaphor acts as a coordination mechanism that doesn't require explicit rules or rigid process.

**Documentation and theory transfer**: The addendum connects metaphor to the question of what documentation should contain. Since documentation cannot say everything, its purpose is to help the next programmer build an accurate theory of the system. Experienced designers often start their documentation with three things: the metaphors, text describing the purpose of each major component, and drawings of the major interactions between components. These alone take a new team a long way toward constructing a useful theory.

Source code itself serves as a form of theory communication. Simple, consistent naming conventions help the next person build a coherent theory. When people talk about "clean code," a large part of what they mean is how easily the reader can build a coherent theory of the system.

## Key Points
- A shared metaphor helps teams develop coherent, aligned understanding of a system
- Good metaphors let programmers make accurate guesses about unfamiliar parts of the code
- Metaphors are a compressed vehicle for transmitting Naur's "theory" of a program
- Without shared theory, parallel development leads to increasing incoherence and "kludge"
- Effective documentation includes: metaphors, component purposes, and interaction diagrams
- Clean code is fundamentally about enabling readers to build a coherent theory of the system
- Multiple metaphors can be used when no single one covers the entire program
- The concept bridges Naur's 1985 philosophy with XP practices from the early 2000s

## Related Concepts
- [[programming-as-theory-building]] - The foundational view that metaphor-driven design operationalizes
- [[tacit-knowledge-in-software]] - Metaphors help transmit the tacit knowledge that documentation alone cannot capture

## Sources
- raw/20260407-pablorauzyname-dev-naur1985programmingpdf.md - The "Applying Theory Building" addendum discussing metaphors in the context of Extreme Programming and documentation practices
