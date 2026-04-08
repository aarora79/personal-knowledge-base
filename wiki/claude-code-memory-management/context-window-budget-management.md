---
title: Context Window Budget Management
created: 2026-04-08
updated: 2026-04-08
sources: [raw/20260408-youngleaderstech-p-how-i-finally-sorted-my-claude-code-memor.md]
related: [claude-code-memory-system](claude-code-memory-system.md), [structured-memory-architecture](structured-memory-architecture.md), [claude-code-hooks](claude-code-hooks.md), [../frontend-slides/progressive-disclosure-in-ai-tools](../frontend-slides/progressive-disclosure-in-ai-tools.md)
tags: [context-window, token-budget, claude-code, memory-optimization, prompt-engineering, ai-tools]
---

# Context Window Budget Management

Context window budget management refers to the strategic allocation of available context space within Claude Code's various loading mechanisms, treating each file's line count and content placement as a scarce resource to be optimized. The concept emerges from the practical constraint that Claude Code's project `MEMORY.md` file is truncated at 200 lines at session start, while `CLAUDE.md` loads in full, creating an asymmetric budget that demands careful content routing.

The central design principle is: **instructions belong in `CLAUDE.md`, learned knowledge belongs in memory files, and routing rules belong in `CLAUDE.md`.** This separation is non-obvious and the source documents a common mistake: placing routing rules (the trigger table that tells Claude which topic files to load for which context) inside `MEMORY.md`. Since the routing table consumed ~20 lines, it burned 10% of the 200-line budget on boilerplate that could live in `CLAUDE.md`, which has no line limit.

The budget management strategy operates at several levels:

**MEMORY.md (200 lines, auto-loaded, project-scoped):** Reserved exclusively for project-specific learned knowledge -- active tickets, codebase patterns, domain observations. Every line must earn its place. Global memory pointers are reduced to a 2-line stub ("Read ~/.claude/CLAUDE.md for memory rules and topic files") rather than duplicating the topic file list.

**CLAUDE.md (unlimited, fully loaded, instruction-scoped):** Houses memory management rules, routing logic, global memory topic file lists, and the repo memory auto-init template. Since it loads in full, there is no cost to placing routing infrastructure here.

**Global memory index (`memory.md`):** A routing table with one-line descriptions per topic file. Read every session but intentionally kept concise -- it tells Claude what exists, not what's in each file. Detailed knowledge lives in topic files loaded on demand.

**Topic files (loaded on demand):** The actual knowledge stores under `tools/`, `domain/`, and `general.md`. These have no inherent line limit but are subject to context window constraints when loaded. The structured architecture ensures only relevant files are loaded per session.

This budget-aware design mirrors the progressive disclosure pattern in Claude Code skill architecture, where the always-loaded file is a concise map and detailed reference material is loaded at the phase where it becomes relevant. Both patterns solve the same fundamental problem: LLM context windows are finite, and front-loading all available context wastes capacity that should be reserved for user interaction and task-specific content.

## Key Points

- Project MEMORY.md has a hard 200-line truncation at session start (set by Anthropic, not configurable)
- CLAUDE.md loads in full with no line limit -- routing rules and instructions belong here
- Common mistake: placing routing tables in MEMORY.md, wasting 10% of the budget on boilerplate
- Global memory pointers in project MEMORY.md should be 2-line stubs, not duplicated lists
- Topic files load on demand, keeping per-session context costs proportional to relevance
- The pattern parallels progressive disclosure in skill architecture
- Content placement is a strategic decision: wrong file = wasted budget or missed context

## Related Concepts

- [Claude Code Memory System](claude-code-memory-system.md) - The system whose constraints drive budget management decisions
- [Structured Memory Architecture](structured-memory-architecture.md) - The directory hierarchy that enables selective loading
- [Claude Code Hooks](claude-code-hooks.md) - PreToolUse hooks that inject memory, surviving context compression
- [Progressive Disclosure in AI Tools](../frontend-slides/progressive-disclosure-in-ai-tools.md) - The same budget-aware loading pattern applied to skill files

## Sources

- raw/20260408-youngleaderstech-p-how-i-finally-sorted-my-claude-code-memor.md - Documents the 200-line constraint discovery, the routing-table mistake, and the resulting content placement strategy
