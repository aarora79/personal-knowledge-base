---
title: Claude Code Hooks
created: 2026-04-08
updated: 2026-04-08
sources: [raw/20260408-youngleaderstech-p-how-i-finally-sorted-my-claude-code-memor.md]
related: [claude-code-memory-system](claude-code-memory-system.md), [context-window-budget-management](context-window-budget-management.md), [../frontend-slides/claude-code-skills-and-plugins](../frontend-slides/claude-code-skills-and-plugins.md)
tags: [claude-code, hooks, pretooluse, automation, context-injection, developer-experience]
---

# Claude Code Hooks

Claude Code hooks are user-defined scripts that execute automatically at specific lifecycle points during a Claude Code session. They enable automation that runs outside Claude's control flow -- triggered by the harness itself rather than by Claude deciding to act. Hooks can fire before a tool runs (`PreToolUse`), after a response, at session start, or at other defined events, and they can inject context, validate actions, or perform side effects.

The most documented hook pattern is the **PreToolUse memory injection hook**, a two-file design that automatically loads project memory and global memory index before the first tool call of each session. The architecture uses a shell wrapper (`pre-tool-memory.sh`, ~5ms overhead) gating a Python script (`pre-tool-memory.py`, ~80ms startup), so that after the initial injection, subsequent tool calls incur only the shell check cost.

The hook's once-per-session semantics are achieved via a flag file at `/tmp/claude-memory-loaded-{ppid}`. The parent process ID (`os.getppid()`) serves as the session identifier because `CLAUDE_SESSION_ID` is not available in the hook execution environment -- a non-obvious implementation detail documented through trial and error. Each subagent spawns with its own process, so the hook fires once per subagent context, ensuring newly spawned agents also receive memory context.

The hook output follows Claude Code's structured format: a JSON object with `hookSpecificOutput` containing `hookEventName` and `additionalContext`. The additional context string is injected into Claude's prompt, making it visible as system context rather than user input. This mechanism survives context compression in long sessions, ensuring memory remains available even after earlier messages are summarized.

Hooks are registered in `~/.claude/settings.json` under a `hooks` object, keyed by event name. Each event contains an array of matcher-hooks pairs, where the matcher determines which tool invocations trigger the hook and the hooks array specifies the commands to run with optional timeouts.

```json
"PreToolUse": [{
  "matcher": "*",
  "hooks": [{
    "type": "command",
    "command": "bash ~/.claude/hooks/pre-tool-memory.sh",
    "timeout": 5
  }]
}]
```

## Key Points

- Hooks are user-defined scripts triggered by Claude Code lifecycle events (PreToolUse, PostResponse, etc.)
- The PreToolUse memory hook injects project and global memory before the first tool call
- Two-file design: bash wrapper (~5ms) gates Python script (~80ms) for minimal overhead after first call
- `os.getppid()` is the correct session identifier; `CLAUDE_SESSION_ID` is not available in hooks
- Each subagent gets its own process, so hooks fire once per subagent context
- Hook output is structured JSON that injects context into Claude's prompt
- Injected context survives context compression in long sessions
- Hooks are registered in `~/.claude/settings.json` under the `hooks` key

## Related Concepts

- [Claude Code Memory System](claude-code-memory-system.md) - The memory system that hooks inject automatically
- [Context Window Budget Management](context-window-budget-management.md) - Why automatic injection is preferable to relying on Claude to read files
- [Claude Code Skills and Plugins](../frontend-slides/claude-code-skills-and-plugins.md) - Skills and hooks are complementary extension mechanisms

## Sources

- raw/20260408-youngleaderstech-p-how-i-finally-sorted-my-claude-code-memor.md - Full implementation walkthrough of the PreToolUse memory hook including the PPID discovery and two-file architecture
