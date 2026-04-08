---
title: Progressive Disclosure in AI Tools
created: 2026-04-08
updated: 2026-04-08
sources: [raw/20260408-githubcom-zarazhangrui-frontend-slides-tree-main.md]
related: [claude-code-skills-and-plugins](claude-code-skills-and-plugins.md), [../arxiv-2510-11977/agent-scaffolds](../arxiv-2510-11977/agent-scaffolds.md)
tags: [progressive-disclosure, ai-tool-design, prompt-engineering, context-window, harness-engineering]
---

# Progressive Disclosure in AI Tools

Progressive disclosure is an architecture pattern for structuring AI tool instructions where the primary file is a concise map of capabilities, and detailed reference material is loaded on demand only when needed. Rather than front-loading all instructions into a single massive prompt, the tool's knowledge is organized into focused files that are read at the phase of execution where they become relevant.

This pattern directly addresses the context window constraint of large language models. By keeping the always-loaded instruction file small (e.g., ~180 lines), the tool leaves room for user content and conversation context. Supporting files -- style references, code templates, animation patterns -- are pulled in only at the specific phase that requires them (e.g., style selection, code generation, deployment).

The concept draws from OpenAI's "harness engineering" principle, summarized as: "give the agent a map, not a 1,000-page instruction manual." The map tells the agent what resources exist and when to use them, while the detailed manuals sit on the shelf until called for.

## Key Points

- The primary instruction file acts as a routing map, not an exhaustive manual
- Supporting files are loaded on demand at the phase of execution where they are needed
- This conserves context window budget for actual user content and interaction
- The pattern was explicitly inspired by OpenAI's harness engineering concept
- In the frontend-slides skill, SKILL.md (~180 lines) routes to six supporting files across three generation phases
- Progressive disclosure reduces cognitive load on both the LLM and the user
- This pattern parallels software engineering concepts of lazy loading and separation of concerns

## Related Concepts

- [Claude Code Skills and Plugins](claude-code-skills-and-plugins.md) - The skill architecture where progressive disclosure is implemented
- [Agent Scaffolds](../arxiv-2510-11977/agent-scaffolds.md) - Task-specific vs. generalist scaffolds share similar design trade-offs around instruction scope

## Sources

- raw/20260408-githubcom-zarazhangrui-frontend-slides-tree-main.md - Describes the progressive disclosure architecture of the frontend-slides skill, with file-by-file loading breakdown
