---
title: Claude Code Skills and Plugins
created: 2026-04-08
updated: 2026-04-08
sources: [raw/20260408-githubcom-zarazhangrui-frontend-slides-tree-main.md]
related: [progressive-disclosure-in-ai-tools](progressive-disclosure-in-ai-tools.md), [vibe-coding](vibe-coding.md)
tags: [claude-code, ai-tools, plugin-architecture, developer-experience, genai-applications]
---

# Claude Code Skills and Plugins

Claude Code skills are modular, installable extensions that add specialized capabilities to the Claude Code CLI. A skill is invoked with a slash command (e.g., `/frontend-slides`) and provides Claude with domain-specific instructions, templates, and scripts that guide its behavior for a particular task. Skills can be distributed via a plugin marketplace or installed manually by copying files into a skills directory.

The skill system follows a file-based architecture where each skill is a folder containing a primary instruction file (`SKILL.md`) along with supporting assets loaded on demand. This design leverages Claude's ability to read and follow structured markdown instructions, essentially turning a set of documents into a capable, task-specific tool. Skills can include code templates, style references, extraction scripts, deployment helpers, and any other assets relevant to their domain.

## Key Points

- Skills are invoked via slash commands in the Claude Code CLI (e.g., `/frontend-slides`)
- Each skill is a folder with a primary `SKILL.md` file and optional supporting files
- Installation can be done via the plugin marketplace (`/plugin marketplace add`) or by manually copying files to `~/.claude/skills/`
- Skills transform Claude from a general-purpose assistant into a domain-specific tool by providing structured instructions and assets
- The plugin marketplace enables community distribution, with skills versioned and installable like packages
- Skills can include scripts (Python, Bash) for tasks beyond text generation, such as file extraction or deployment
- The architecture is zero-dependency from the user's perspective -- skills are just files, not installed packages

## Related Concepts

- [Progressive Disclosure in AI Tools](progressive-disclosure-in-ai-tools.md) - The architecture pattern used to structure skill files efficiently
- [Vibe Coding](vibe-coding.md) - The philosophy that motivates making creative tools accessible to non-engineers

## Sources

- raw/20260408-githubcom-zarazhangrui-frontend-slides-tree-main.md - Describes the frontend-slides skill architecture, installation methods, and plugin marketplace workflow
