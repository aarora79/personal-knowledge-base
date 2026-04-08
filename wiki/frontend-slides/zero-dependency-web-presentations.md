---
title: Zero-Dependency Web Presentations
created: 2026-04-08
updated: 2026-04-08
sources: [raw/20260408-githubcom-zarazhangrui-frontend-slides-tree-main.md]
related: [anti-ai-slop-design](anti-ai-slop-design.md), [claude-code-skills-and-plugins](claude-code-skills-and-plugins.md)
tags: [web-presentations, zero-dependency, html-css-js, genai-applications, ai-generated-code]
---

# Zero-Dependency Web Presentations

Zero-dependency web presentations are self-contained HTML files that include all CSS styling and JavaScript behavior inline, requiring no external frameworks, build tools, or package managers to run. Each presentation is a single `.html` file that can be opened in any browser and will work identically years later, because it depends on nothing beyond the browser's built-in capabilities.

The frontend-slides project generates presentations following this principle. Each output is a standalone HTML file with inline CSS for styling (including animations, transitions, and responsive layouts) and inline JavaScript for slide navigation, keyboard controls, and interactive features. There is no npm, no React, no build step -- just one file that a browser renders.

This approach stands in contrast to modern web development's dependency-heavy culture, where a simple presentation might pull in a framework, a bundler, dozens of npm packages, and require a build pipeline. The zero-dependency philosophy argues that "dependencies are debt" -- a single HTML file from 2026 will still work in 2036, while a React project from 2019 may already be difficult to build.

The generated presentations include production-quality features: accessible markup, responsive design (phone through desktop), smooth CSS animations, keyboard navigation, and well-commented code that users can customize after generation.

## Key Points

- Presentations are single HTML files with all CSS and JS inlined
- No npm, no build tools, no frameworks required to view or host
- Files are inherently portable -- shareable as email attachments, hostable anywhere
- Long-term durability: depends only on browser standards, not on package ecosystems
- Generated code is well-commented for post-generation customization
- Responsive by default, working across phones, tablets, and desktops
- Can be deployed to Vercel or exported to PDF via included helper scripts

## Related Concepts

- [Anti-AI-Slop Design](anti-ai-slop-design.md) - Quality-focused design principles applied to these generated presentations
- [Claude Code Skills and Plugins](claude-code-skills-and-plugins.md) - The skill system that generates these presentations

## Sources

- raw/20260408-githubcom-zarazhangrui-frontend-slides-tree-main.md - Describes the zero-dependency architecture and philosophy of the frontend-slides project
