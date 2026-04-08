---
title: "Source Summary: How I Finally Sorted My Claude Code Memory"
created: 2026-04-08
source: raw/20260408-youngleaderstech-p-how-i-finally-sorted-my-claude-code-memor.md
depth: 500
articles_created: [claude-code-memory-system.md, structured-memory-architecture.md, claude-code-hooks.md, domain-knowledge-lifecycle.md, context-window-budget-management.md]
---

# How I Finally Sorted My Claude Code Memory - Summary

This source is a practitioner's deep-dive into configuring Claude Code's persistent memory system, written by John Conneely (Young Leaders in Tech, #98, March 2026). It documents the journey from an unsorted accumulation of auto-memory entries to a structured, directory-based architecture with automatic context injection via hooks. The article builds on Pawel Huryn's original memory management prompt (from The Product Compass) and extends it with a tiered directory structure, a PreToolUse hook for automatic injection, and a domain knowledge lifecycle model.

## The Problem Space

Claude Code v2.1.59 (26 February 2026) shipped auto memory, which silently accumulates project notes in `~/.claude/projects/{mapped-path}/memory/`. Before this, practitioners relied on increasingly bloated `CLAUDE.md` files that loaded every session in full regardless of relevance. The auto memory feature introduced project-scoped MEMORY.md files, but with a critical constraint: only the first 200 lines are loaded at session start. This 200-line budget makes content placement a strategic decision -- the wrong content in the wrong file wastes scarce context window capacity.

The author identifies the core insight: "More memory is not the answer. Better architecture is." A flat memory file replicates the bloated CLAUDE.md antipattern. The solution is a structured directory hierarchy with selective, on-demand loading.

## Architecture

```
  +---------------------------+
  |    CLAUDE.md (unlimited)  |
  |  - Memory routing rules   |
  |  - Instructions           |
  |  - Auto-init template     |
  +-------------+-------------+
                |
   reads at session start
                |
  +-------------v-------------+
  |  memory.md (index)        |
  |  - Topic file table       |
  |  - Cross-memory sync rule |
  |  - Domain lifecycle docs  |
  +-------------+-------------+
                |
     loads on demand
                |
  +------+------+------+
  |      |      |      |
  v      v      v      v
general tools/ domain/ project
 .md    *.md   {name}/ MEMORY.md
                *.md   (200 lines)
```

The architecture separates concerns across four tiers: the index (read every session), general conventions (cross-project), tool-specific knowledge (per-integration), and domain knowledge (per-product area). Each tier loads only when relevant to the active session.

## The PreToolUse Hook

The automatic injection mechanism uses a two-file hook design registered in `~/.claude/settings.json`. A bash wrapper (`~5ms`) checks a PPID-based flag file and gates a Python script (`~80ms startup`) that reads project MEMORY.md and the global index, then outputs structured JSON injected into Claude's prompt context. The hook fires once per process context (including subagents), survives context compression, and uses `os.getppid()` as the session identifier since `CLAUDE_SESSION_ID` is not available in hook environments.

## Domain Knowledge Lifecycle

Domain files follow a three-stage graduation: **Staging** (knowledge accumulates as the practitioner works), **Promotion** (knowledge is packaged as a Claude Code skill via PR), and **Pointer** (the memory file becomes a 3-line redirect to the skill). This model keeps memory files lean while preserving domain expertise in increasingly structured, shareable forms.

## Key Implementation Details

- Routing rules (trigger tables) belong in CLAUDE.md, not MEMORY.md -- placing them in MEMORY.md wastes 10% of the 200-line budget on boilerplate
- Global memory pointers in project MEMORY.md should be 2-line stubs, not duplicated topic lists
- The "reorganize memory" command runs in plan mode to review changes before execution
- Version `~/.claude/` as a git repo for backup and change tracking
- The Atlassian MCP was banned by the author due to reliability issues and token consumption; replaced by ACLI and direct REST APIs

## What This Source Covers

- Claude Code auto memory feature (v2.1.59, February 2026) and its constraints
- Structured directory architecture for global and project memory
- PreToolUse hook implementation for automatic memory injection
- Domain knowledge lifecycle: staging, promotion, pointer
- The 200-line MEMORY.md budget and strategic content placement
- Practical lessons from configuring memory across multiple integrations (Jira, Snowflake, Confluence, Slack)

## Wiki Articles From This Source

- [Claude Code Memory System](claude-code-memory-system.md) - Auto memory feature, global vs project scopes, and the 200-line constraint
- [Structured Memory Architecture](structured-memory-architecture.md) - Directory-based organization with tools/, domain/, and general.md tiers
- [Claude Code Hooks](claude-code-hooks.md) - PreToolUse hook for automatic memory injection with PPID-based session tracking
- [Domain Knowledge Lifecycle](domain-knowledge-lifecycle.md) - Three-stage progression from staging to skill promotion to pointer
- [Context Window Budget Management](context-window-budget-management.md) - Strategic allocation of the 200-line MEMORY.md budget and content routing
