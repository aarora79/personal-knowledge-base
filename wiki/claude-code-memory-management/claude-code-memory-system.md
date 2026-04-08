---
title: Claude Code Memory System
created: 2026-04-08
updated: 2026-04-08
sources: [raw/20260408-youngleaderstech-p-how-i-finally-sorted-my-claude-code-memor.md]
related: [structured-memory-architecture](structured-memory-architecture.md), [context-window-budget-management](context-window-budget-management.md), [claude-code-hooks](claude-code-hooks.md), [../frontend-slides/claude-code-skills-and-plugins](../frontend-slides/claude-code-skills-and-plugins.md)
tags: [claude-code, memory-system, auto-memory, developer-experience, ai-tools, context-management]
---

# Claude Code Memory System

Claude Code's memory system is a file-based persistence mechanism that allows the AI assistant to retain knowledge across conversation sessions. Introduced as "auto memory" in version 2.1.59 (26 February 2026), the system enables Claude to write observations, preferences, and learned context to markdown files that are automatically loaded at the start of subsequent sessions.

The memory system operates at two scopes. **Global memory** resides at `~/.claude/memory/` and holds knowledge that applies across all projects -- tool configurations, workflow preferences, naming conventions, and credential patterns. **Project memory** resides at `~/.claude/projects/{mapped-path}/memory/MEMORY.md` and holds knowledge specific to a single repository -- active tickets, codebase patterns, domain-specific context. The project path is mapped by replacing directory separators with hyphens (e.g., `/Users/john/projects/my-app` becomes `-Users-john-projects-my-app`).

At session start, Claude reads the project `MEMORY.md` file automatically, but only the first 200 lines. This hard constraint, set by Anthropic rather than configurable by the user, makes the content placement within `MEMORY.md` a strategic decision. The global memory index (`memory.md`) serves as a routing table that points to topic-specific files loaded on demand.

Before auto memory shipped, practitioners relied on increasingly large `CLAUDE.md` files that loaded in full every session. This pattern -- appending knowledge directly into the instruction file -- created bloated documents where context loaded whether relevant or not. The memory system separates instructions (which belong in `CLAUDE.md`) from learned knowledge (which belongs in memory files), enabling selective loading based on session context.

The auto memory feature is enabled by default on personal Pro and Max plans. Enterprise plans may have auto-updates disabled; `claude doctor` can verify version and update status. Claude may silently accumulate memory entries even before the user configures a memory structure, as the feature begins writing notes immediately upon activation.

## Key Points

- Auto memory shipped in Claude Code v2.1.59 (26 February 2026)
- Two scopes: global (`~/.claude/memory/`) and project (`~/.claude/projects/{path}/memory/MEMORY.md`)
- Project MEMORY.md is auto-loaded at session start but truncated at 200 lines
- CLAUDE.md loads in full -- routing rules and instructions belong there, not in MEMORY.md
- Memory separates learned knowledge from static instructions, solving the bloated CLAUDE.md problem
- Enterprise plans may have auto-updates disabled; check with `claude doctor`
- Claude may already be accumulating memory entries silently before user configuration

## Related Concepts

- [Structured Memory Architecture](structured-memory-architecture.md) - Directory-based organization pattern for memory files
- [Context Window Budget Management](context-window-budget-management.md) - Strategic allocation of the 200-line MEMORY.md budget
- [Claude Code Hooks](claude-code-hooks.md) - Automatic memory injection via PreToolUse hooks
- [Claude Code Skills and Plugins](../frontend-slides/claude-code-skills-and-plugins.md) - The skill system that domain knowledge can be promoted into

## Sources

- raw/20260408-youngleaderstech-p-how-i-finally-sorted-my-claude-code-memor.md - Detailed walkthrough of discovering and configuring Claude Code's memory system, including the auto memory feature and its constraints
