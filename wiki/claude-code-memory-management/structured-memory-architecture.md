---
title: Structured Memory Architecture
created: 2026-04-08
updated: 2026-04-08
sources: [raw/20260408-youngleaderstech-p-how-i-finally-sorted-my-claude-code-memor.md]
related: [claude-code-memory-system](claude-code-memory-system.md), [domain-knowledge-lifecycle](domain-knowledge-lifecycle.md), [context-window-budget-management](context-window-budget-management.md), [../frontend-slides/progressive-disclosure-in-ai-tools](../frontend-slides/progressive-disclosure-in-ai-tools.md)
tags: [memory-architecture, structured-knowledge, claude-code, knowledge-management, developer-experience, ai-tools]
---

# Structured Memory Architecture

Structured memory architecture is a directory-based organization pattern for Claude Code's persistent memory that replaces flat, monolithic memory files with a categorized hierarchy of topic-specific files. Rather than accumulating all learned context in a single `memory.md` or `CLAUDE.md`, the architecture segments knowledge into purpose-built directories that are loaded selectively based on session context.

The canonical structure, as refined by practitioner John Conneely building on Pawel Huryn's initial prompt, organizes global memory into three tiers:

```
~/.claude/memory/
  memory.md          # Index file (read every session)
  general.md         # Cross-project conventions
  tools/
    snowflake.md     # Tool-specific knowledge
    atlassian.md
    slack.md
  domain/
    {product}/       # Domain-specific knowledge
    {project}/
```

The **index file** (`memory.md`) is read at every session start and contains a table of all topic files with one-line descriptions and last-updated dates. It serves as a routing mechanism -- Claude scans it to determine which topic files are relevant to the current session and loads only those. This is analogous to the progressive disclosure pattern used in Claude Code skills, where the primary file is a concise map that points to detailed reference material loaded on demand.

**`general.md`** holds cross-project knowledge: naming conventions, workflow preferences, date formats, writing style. It is the knowledge that applies regardless of which project or domain is active.

**`tools/`** contains per-tool knowledge files documenting integration-specific configuration, authentication patterns, workarounds, and gotchas. This solves a common problem where the same tool fix must be applied across dozens of agents, skills, and workflows -- with a centralized tool file, the knowledge exists in one place and is referenced everywhere.

**`domain/`** is the most strategically important tier. Domain files accumulate hard-won context about specific product areas, codebases, or business processes -- the gotchas, edge cases, and implicit knowledge that takes weeks to build. Domain files are designed to be shareable: subject matter experts can contribute context directly, making them a living knowledge source rather than static documentation. When a domain file grows large enough, it can be promoted into a full Claude Code skill (see Domain Knowledge Lifecycle).

The key insight driving this architecture is that "more memory is not the answer -- better architecture is." A flat memory file replicates the bloated `CLAUDE.md` antipattern: everything loads every session whether needed or not. The structured approach ensures the right knowledge loads at the right time.

## Key Points

- Replaces flat memory files with a categorized directory hierarchy
- Index file (`memory.md`) serves as a routing table read every session
- Topic files loaded selectively based on session context
- Three tiers: general (cross-project), tools (per-integration), domain (per-product/area)
- Domain files designed for sharing -- SMEs can contribute context directly
- Solves the "same fix in twenty places" problem by centralizing tool knowledge
- Parallels the progressive disclosure pattern used in Claude Code skill architecture
- The prompt to set it up is designed to be copy-paste: "drop it in, done"

## Related Concepts

- [Claude Code Memory System](claude-code-memory-system.md) - The underlying auto memory feature this architecture builds on
- [Domain Knowledge Lifecycle](domain-knowledge-lifecycle.md) - How domain files graduate into skills
- [Context Window Budget Management](context-window-budget-management.md) - Why selective loading matters
- [Progressive Disclosure in AI Tools](../frontend-slides/progressive-disclosure-in-ai-tools.md) - The same on-demand loading pattern applied to skill instruction files

## Sources

- raw/20260408-youngleaderstech-p-how-i-finally-sorted-my-claude-code-memor.md - Describes the directory structure, rationale for each tier, and the refinement journey from flat memory to structured architecture
