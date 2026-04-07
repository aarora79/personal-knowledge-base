# Personal Knowledge Base

An LLM-maintained knowledge base for Generative AI topics. Inspired by Andrej Karpathy's "LLM Knowledge Bases" concept -- raw source material goes in, and an LLM agent compiles and maintains an interlinked wiki of markdown articles.

No RAG. No vector databases. No embeddings. Just markdown files and an LLM acting as librarian.

## Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) package manager
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI (for the LLM agent operations)

## Setup

```bash
# Clone the repo
git clone <repo-url>
cd personal-knowledge-base

# Install dependencies
uv sync
```

## Project Structure

```
personal-knowledge-base/
├── CLAUDE.md        # Schema and instructions for the LLM agent
├── architecture.md  # System architecture and design decisions
├── changelog.md     # Log of every ingest/update run
├── clip.sh          # URL-to-markdown ingestion script
├── pyproject.toml   # Python dependencies (trafilatura, markitdown)
├── raw/             # Source documents (append-only, never edit)
│   └── YYYYMMDD-source-slug.md
└── wiki/            # LLM-authored articles (one per concept)
    └── index.md     # Master index of all articles
```

## Adding Content

### Clip a single URL

```bash
# Web article or blog post (uses trafilatura)
./clip.sh https://www.anthropic.com/news/contextual-retrieval

# YouTube video (auto-detected, uses markitdown for transcript)
./clip.sh https://youtu.be/Axd50ew4pco

# PDF document (auto-detected, uses markitdown)
./clip.sh https://arxiv.org/pdf/2501.00663

# Force markitdown for any URL
./clip.sh --markitdown https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)

# Custom slug for cleaner filename
./clip.sh https://some-long-url.com/article my-custom-slug
```

### Bulk clip from a file

Create a text file with one URL per line (lines starting with `#` are skipped):

```bash
# urls.txt
# RAG articles
https://www.anthropic.com/news/contextual-retrieval
https://docs.llamaindex.ai/en/stable/

# Agent frameworks
https://huyenchip.com//2025/01/07/agents.html
```

Then run:

```bash
./clip.sh --bulk urls.txt
```

### Drop files manually

You can also place markdown, PDF, or text files directly into `raw/` using the naming convention:

```
raw/YYYYMMDD-descriptive-slug.md
```

## Ingestion Tools

| Tool         | Best For                                | Image Download |
|--------------|----------------------------------------|----------------|
| trafilatura  | Web articles, blog posts (clean output)| No             |
| markitdown   | PDFs, DOCX, YouTube transcripts        | No             |

- **trafilatura** strips boilerplate (navbars, ads, footers) and extracts the main article content
- **markitdown** converts the full page/document to markdown, which can be noisy for web pages but handles non-HTML formats well
- Neither tool downloads images -- they preserve image URLs as markdown `![alt](url)` references

## Working with the LLM Agent

Once you have raw material in `raw/`, use Claude Code to compile it into wiki articles.

### Start a session

```bash
cd personal-knowledge-base
claude
```

The agent reads `CLAUDE.md` automatically to understand the schema and its role.

### Ingest new content

Tell the agent to process new raw files into wiki articles:

```
ingest
```

The agent will:
1. Scan `raw/` for unprocessed files (checking `changelog.md`)
2. Read each new file and extract key concepts
3. Create new wiki articles or update existing ones
4. Add backlinks between related articles
5. Update `wiki/index.md`
6. Log the run in `changelog.md`

### Query the knowledge base

Ask questions and the agent synthesizes answers from wiki articles:

```
What are the main approaches to RAG?
```

```
Compare agent frameworks discussed in the knowledge base
```

### Lint and health check

Ask the agent to find gaps and inconsistencies:

```
lint
```

The agent will:
1. Find orphaned references (links to articles that do not exist)
2. Identify concepts mentioned frequently that lack their own article
3. Flag conflicting claims between articles
4. Suggest new articles that would strengthen the knowledge base

## Wiki Article Format

Each article in `wiki/` follows this structure:

```markdown
---
title: Contextual Retrieval
created: 2026-04-07
updated: 2026-04-07
sources: [raw/20260407-anthropiccom-news-contextual-retrieval.md]
related: [[retrieval-augmented-generation]], [[embeddings]]
---

# Contextual Retrieval

Encyclopedia-style summary (200-500 words)...

## Key Points
- Point one
- Point two

## Related Concepts
- [[retrieval-augmented-generation]] -- parent concept
- [[embeddings]] -- used for contextual embeddings

## Sources
- raw/20260407-anthropiccom-news-contextual-retrieval.md -- Anthropic blog post
```

## Naming Conventions

| Item       | Convention                          | Example                                    |
|------------|-------------------------------------|--------------------------------------------|
| Raw files  | `YYYYMMDD-source-slug.md`          | `20260407-anthropiccom-contextual-retrieval.md` |
| Wiki files | `lowercase-kebab-case.md`           | `retrieval-augmented-generation.md`         |
| Links      | `[[article-name]]`                  | `[[contextual-retrieval]]`                  |

## Topic Coverage

This knowledge base focuses on Generative AI:

- LLM Fundamentals (transformers, attention, tokenization)
- Prompt Engineering
- Retrieval-Augmented Generation (RAG)
- AI Agents and Agentic Frameworks
- Fine-Tuning and Training
- Guardrails and Responsible AI
- Benchmarking and Evaluation
- GenAI Applications and Tools
- Cloud AI Services (Amazon Bedrock)

## Content Sources

The initial set of bookmarks comes from the [gu-dsan6725/bookmarks](https://github.com/gu-dsan6725/bookmarks) repository, which is a curated collection of GenAI resources covering LLM basics, RAG, agents, prompt engineering, fine-tuning, and more.

## References

- Karpathy's idea file: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- trafilatura docs: https://trafilatura.readthedocs.io
- markitdown repo: https://github.com/microsoft/markitdown
