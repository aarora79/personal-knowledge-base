---
title: "Source Summary: Frontend Slides - A Claude Code Skill for Web Presentations"
created: 2026-04-08
source: raw/20260408-githubcom-zarazhangrui-frontend-slides-tree-main.md
depth: 100
articles_created: [claude-code-skills-and-plugins.md, progressive-disclosure-in-ai-tools.md, vibe-coding.md, zero-dependency-web-presentations.md, anti-ai-slop-design.md]
---

# Frontend Slides - Summary

Imagine you need to make a really cool slideshow for a presentation, but you're not a designer and you don't know CSS or JavaScript. Frontend Slides is like having an artist friend who lives inside Claude Code -- you tell it what your presentation is about, it shows you three different looks to pick from, and then it builds the whole thing for you as a single web page.

The really neat part? Everything it makes is just one HTML file. Think of it like writing a letter versus building a machine -- a letter (one HTML file) will still be readable in 50 years, but a machine with lots of parts (a project with dozens of dependencies) might break when any single part goes missing. Frontend Slides bets on simplicity.

## How It Works

The tool is a "skill" for Claude Code, which is like an app you install on your phone. You type `/frontend-slides`, describe what you want, and it walks you through the process:

```
  +------------------+     +------------------+     +------------------+
  |  You describe    |     |  Claude shows    |     |  Claude builds   |
  |  your content    |---->|  3 style options  |---->|  the full deck   |
  |  and feeling     |     |  to pick from    |     |  as one HTML file|
  +------------------+     +------------------+     +------------------+
         |                        |                        |
    "AI startup pitch"     "I like #2, the          Opens in your
    "Make it feel bold"     dark one with            browser, ready
                            neon accents"            to present
```

## The Clever Part: Progressive Disclosure

The skill doesn't dump all its instructions on Claude at once. That would be like giving someone a 1,000-page manual before they even know what job they're doing. Instead, it gives Claude a short map (about 180 lines), and Claude only reads the detailed files when it actually needs them -- like looking up a recipe only when it's time to cook that dish.

## Fighting "AI Slop"

You know how a lot of AI-generated images and designs look kind of the same? Purple gradients, generic layouts, safe and boring? That's what people call "AI slop." Frontend Slides fights this by offering 12 handpicked styles -- from "Terminal Green" (looks like a hacker's screen) to "Paper & Ink" (looks like a fancy book) -- so your presentation actually stands out instead of looking like every other AI-made thing.

## What This Source Covers

- How Claude Code skills and plugins work (install, invoke, architecture)
- Progressive disclosure as a design pattern for AI tool instructions
- The "vibe coding" philosophy -- building beautiful things without being a traditional engineer
- Zero-dependency web presentations that are just one HTML file
- Anti-AI-slop design: curated styles that avoid generic AI aesthetics

## Wiki Articles From This Source

- [Claude Code Skills and Plugins](claude-code-skills-and-plugins.md) - How the skill/plugin system works in Claude Code
- [Progressive Disclosure in AI Tools](progressive-disclosure-in-ai-tools.md) - Loading instructions on-demand instead of all at once
- [Vibe Coding](vibe-coding.md) - The philosophy of building by describing what you want, not how to code it
- [Zero-Dependency Web Presentations](zero-dependency-web-presentations.md) - Self-contained HTML files with no frameworks needed
- [Anti-AI-Slop Design](anti-ai-slop-design.md) - Curated design that avoids generic AI-generated aesthetics
