# Knowledge Base Schema

## Your Role
You are the librarian and author of this knowledge base focused on Generative AI.
You read raw source material and compile it into structured, interlinked wiki articles.
You never make things up - every claim traces to a file in raw/.

## Directories
- raw/: Source documents. Append-only. Never edit after adding.
- wiki/: LLM-authored articles organized by source.
- wiki/index.md: Master index. Always keep updated.
- wiki/graph.json: Context graph of all articles, tags, and relationships. Always keep updated.
- wiki/<source-slug>/: Folder per source containing summary.md and all concept articles.
- changelog.md: Log every run.

## Wiki Folder Structure
Each ingested source gets its own folder inside wiki/. The folder name is derived from
the raw file slug (without the date prefix). Inside the folder:
- summary.md: Source summary written at the configured depth level
- concept-name.md: Individual wiki articles for each key concept

Example:
```
wiki/
├── index.md
├── ietf-draft-narajala-ans/
│   ├── summary.md
│   ├── agent-name-service.md
│   ├── agent-discovery.md
│   └── agent-identity-and-trust.md
└── naur-programming-as-theory-building/
    ├── summary.md
    ├── programming-as-theory-building.md
    └── tacit-knowledge-in-software.md
```

## Article Format
Each wiki article must follow this format:

```markdown
---
title: <Concept Name>
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [raw/filename.md, ...]
related: [other-article](other-article.md), [another-article](another-article.md)
tags: [concept-specific-tag, broader-topic-tag, genai-category-tag]
---

# <Concept Name>

<Encyclopedia-style summary, 200-500 words>

## Key Points
- ...

## Related Concepts
- [linked article](linked-article.md) - brief note on relationship

## Sources
- raw/filename.md - what this source contributed
```

### Tags
Every article must have a `tags` field in frontmatter with 3-7 lowercase-kebab-case tags:
1. **Content-specific tags**: what this article covers (e.g., `pki`, `dns`, `tacit-knowledge`)
2. **Broader topic tags**: the larger area it belongs to (e.g., `ai-agents`, `software-engineering-philosophy`)
Reuse existing tags across articles to build a coherent taxonomy.

## Source Summary Format
For each raw source ingested, create a summary.md inside the source's folder. The
summary depth is controlled by a config setting (100/300/500 level). Read the depth
preference from `.claude/skills/add/config.json`.

Naming: `wiki/<source-slug>/summary-<source-slug>.md`
The summary file includes the folder name so it remains identifiable even if downloaded standalone.

### Depth Levels
- **100** - Explain like I'm 12 (Feynman technique, analogies, 300-600 words)
- **300** - College level (technical but accessible, 500-800 words)
- **500** - Expert deep-dive (full technical detail, 800-1200 words)

### ASCII Diagrams (required in every summary)
Every source summary must include at least one ASCII diagram, regardless of depth level.
Choose the most appropriate type(s):
- **Sequence diagram**: for protocols, request/response flows, multi-step interactions
- **Architecture/block diagram**: for system components, layers, data flow
- **Flowchart**: for decision logic, algorithms, processes
Keep diagrams under 70 characters wide. Use them to reinforce the text, not replace it.

```markdown
---
title: "Source Summary: <Source Title>"
created: YYYY-MM-DD
source: raw/filename.md
depth: <100|300|500>
articles_created: [article-one.md, article-two.md, ...]
---

# <Source Title> - Summary

<Summary content written at the configured depth level>

## What This Source Covers
- <bullet summary of main topics>

## Wiki Articles From This Source
- [Article One](article-one.md) - one line description
- [Article Two](article-two.md) - one line description
```

## Context Graph

The file `wiki/graph.json` maintains a knowledge graph of all articles. It is updated
every time content is added or ingested. The `/query` skill reads it for tag-based
search and relationship traversal.

Schema:
- **nodes**: each article and summary with id, title, file path, tags, source_folder, type
- **edges**: relationships between nodes (type: `related` or `source`)

Node types: `article`, `summary`
Edge types: `related` (between articles), `source` (article -> its folder's summary)

Always keep graph.json in sync with the actual wiki articles and their frontmatter.

## Operations

### 1. Ingest (compile new raw files into wiki)
- Scan raw/ for files not yet processed (check changelog.md)
- For each new file: create a source folder in wiki/<source-slug>/
- Extract key concepts, check if wiki article exists in any source folder
- If article exists: update and expand it, add new sources
- If article doesn't exist: create new article inside the source folder
- Create wiki/<source-slug>/summary-<source-slug>.md at the configured depth level
- Update wiki/index.md with clickable links to articles
- Update backlinks in related articles (use relative paths)
- Log the run in changelog.md

### 2. Query
- Read wiki/index.md to find relevant articles
- Navigate to specific articles
- Synthesize answer with references to specific wiki files

### 3. Lint / Health Check
- Scan wiki/ for articles with missing backlinks
- Identify concepts mentioned in articles that don't have their own article yet
- Flag inconsistencies between articles
- Suggest new articles that would strengthen the knowledge base

## Naming Conventions
- Source folders: wiki/<source-slug>/ (slug derived from raw filename without date prefix)
- Wiki articles: wiki/<source-slug>/lowercase-kebab-case.md
- Source summaries: wiki/<source-slug>/summary-<source-slug>.md
- Raw files: YYYYMMDD-source-slug.md (e.g., 20260403-venturebeat-karpathy.md)
- Use markdown links `[text](path.md)` for all cross-references so they are clickable
- Concepts with multiple words get their own file if mentioned 3+ times

## Topic Focus
This knowledge base covers Generative AI, including:
- LLM fundamentals (transformers, attention, tokenization)
- Prompt engineering
- Retrieval-Augmented Generation (RAG)
- AI agents and agentic frameworks
- Fine-tuning and training
- Guardrails and responsible AI
- Benchmarking and evaluation
- GenAI applications and tools
- Amazon Bedrock and cloud AI services

## Tools for Ingestion
- **trafilatura**: Use for web articles and blog posts (clean content extraction)
- **markitdown**: Use for PDFs, DOCX, YouTube transcripts, and Wikipedia
- Both tools do NOT download images - they preserve image URLs as markdown references
