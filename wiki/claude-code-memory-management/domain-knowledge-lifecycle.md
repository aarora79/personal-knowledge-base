---
title: Domain Knowledge Lifecycle
created: 2026-04-08
updated: 2026-04-08
sources: [raw/20260408-youngleaderstech-p-how-i-finally-sorted-my-claude-code-memor.md]
related: [structured-memory-architecture](structured-memory-architecture.md), [claude-code-memory-system](claude-code-memory-system.md), [../frontend-slides/claude-code-skills-and-plugins](../frontend-slides/claude-code-skills-and-plugins.md)
tags: [domain-knowledge, knowledge-lifecycle, claude-code, knowledge-management, skills-promotion, ai-tools]
---

# Domain Knowledge Lifecycle

The domain knowledge lifecycle is a three-stage progression model for managing accumulated domain expertise within Claude Code's memory system. It describes how unstructured observations about a specific product area, codebase, or business process evolve from raw notes into a packaged, reusable skill that can be invoked across any project.

The three stages are:

**Stage 1: Staging.** Knowledge accumulates in `~/.claude/memory/domain/{name}/` as the practitioner works within a domain. Entries capture gotchas, edge cases, schema details, API behaviors, workarounds -- the granular, experience-derived context that takes weeks to build and that documentation typically fails to capture. At this stage, the knowledge is informal and append-only: date, what, why.

**Stage 2: Promotion.** When a domain file accumulates enough structured knowledge to stand on its own, it can be packaged as a Claude Code skill -- a reusable plugin invocable with a slash command across any project. The promotion decision is typically triggered by the domain file growing too large for its memory file budget, or by the knowledge becoming stable enough that it no longer changes session to session. A pull request is raised to either create a new skill or add the knowledge as an addendum to an existing skill.

**Stage 3: Pointer.** After promotion, the memory file does not retain the full knowledge. Instead, it becomes a pointer -- typically three lines directing Claude to the skill where the canonical knowledge now lives. The content lives in the skill; the memory file just says where to find it. When updates are needed to a promoted domain, they are noted in the memory file as issues to be created on the skill's repository, maintaining the single-source-of-truth principle.

This lifecycle addresses a fundamental tension in AI-assisted development: domain knowledge is the most valuable form of memory (it represents hard-won, experience-derived understanding that no documentation captures), but it also grows the fastest and risks overwhelming the memory budget. The lifecycle provides a graduation path that keeps memory files lean while preserving the knowledge in an increasingly structured, shareable, and reusable form.

The model also enables team knowledge sharing. At the staging phase, domain files can be synced with teammates so subject matter experts contribute their context directly. At the promotion phase, skills become distributable packages that encode collective domain expertise.

## Key Points

- Three stages: Staging (accumulation), Promotion (packaging as skill), Pointer (redirect to skill)
- Domain files capture the granular, experience-derived context that documentation misses
- Promotion is triggered when domain knowledge becomes stable or exceeds memory budget
- Post-promotion, the memory file becomes a 3-line pointer to the canonical skill
- Updates to promoted domains are noted as issues on the skill repository
- Enables team sharing: domain files can be synced, skills can be distributed
- Solves the tension between valuable domain knowledge and limited memory budget

## Related Concepts

- [Structured Memory Architecture](structured-memory-architecture.md) - The directory structure where domain files accumulate
- [Claude Code Memory System](claude-code-memory-system.md) - The underlying memory system with its 200-line project budget
- [Claude Code Skills and Plugins](../frontend-slides/claude-code-skills-and-plugins.md) - The skill system that domain knowledge graduates into

## Sources

- raw/20260408-youngleaderstech-p-how-i-finally-sorted-my-claude-code-memor.md - Describes the three-stage lifecycle and the author's experience promoting a product domain into a full skill
