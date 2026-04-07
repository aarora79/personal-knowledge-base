# Architecture

## Overview

This is an LLM-maintained knowledge base inspired by Andrej Karpathy's "LLM Knowledge Bases" concept. Instead of using RAG pipelines with vector databases, the system uses plain markdown files organized into a wiki structure. An LLM agent (Claude Code) acts as librarian and author -- reading raw source material and compiling it into structured, interlinked encyclopedia-style articles.

## How It Works

```
                   +------------------+
                   |   Web Articles   |
                   |   PDFs, YouTube  |
                   |   Papers, Docs   |
                   +--------+---------+
                            |
                   clip.sh (trafilatura / markitdown)
                            |
                            v
                   +------------------+
                   |     raw/         |  Append-only source documents
                   |  (never edited)  |  One file per source
                   +--------+---------+
                            |
                   LLM Agent (Claude Code) reads CLAUDE.md schema
                            |
                   "ingest" operation
                            |
                            v
                   +------------------+
                   |     wiki/        |  LLM-authored articles
                   |  index.md        |  One .md file per concept
                   |  concept-a.md    |  Interlinked with [[backlinks]]
                   |  concept-b.md    |
                   +------------------+
                            |
                   changelog.md tracks every run
```

## Components

### 1. raw/ (Source Documents)
- Append-only staging area for raw content
- Files are never edited after being added
- Naming: `YYYYMMDD-source-slug.md`
- Content arrives via `clip.sh` or manual file drops

### 2. wiki/ (LLM-Authored Articles)
- One markdown file per concept
- Naming: `lowercase-kebab-case.md`
- Each article has YAML frontmatter (title, created, updated, sources, related)
- Articles are interlinked using `[[wiki-link]]` syntax
- `wiki/index.md` is the master index organized by category

### 3. CLAUDE.md (Schema File)
- Operating instructions for the LLM agent
- Defines article format, naming conventions, and operations
- Read by the agent at the start of every session

### 4. clip.sh (Ingestion Script)
- Shell script that converts URLs to markdown files in `raw/`
- Uses two tools based on content type:

| Tool         | Best For                              | Limitations                        |
|--------------|---------------------------------------|------------------------------------|
| trafilatura  | Web articles, blog posts              | No JS rendering, no image download |
| markitdown   | PDFs, DOCX, YouTube, Wikipedia        | Noisy for web pages (no boilerplate removal) |

- Auto-detects YouTube and PDF URLs and routes to markitdown
- Everything else defaults to trafilatura
- Supports bulk ingestion from a text file of URLs

### 5. changelog.md (Run Log)
- Every ingest, lint, or update operation gets a timestamped entry
- Used to track which raw files have been processed

## Data Flow

### Adding Content
1. Find a URL (article, paper, video)
2. Run `./clip.sh <url>` to save it as markdown in `raw/`
3. Ask the LLM agent to "ingest" -- it reads new raw files and creates/updates wiki articles
4. Agent updates `wiki/index.md` and `changelog.md`

### Querying Knowledge
1. Ask the LLM agent a question
2. Agent reads `wiki/index.md` to find relevant articles
3. Agent reads those articles and follows backlinks for deeper context
4. Agent synthesizes an answer with citations to specific wiki files

### Maintaining Quality
1. Ask the LLM agent to "lint"
2. Agent scans for orphaned links, missing articles, and inconsistencies
3. Agent suggests new articles to fill gaps

## Design Decisions

### Why No RAG?
- At the scale of a personal knowledge base (hundreds of articles, not millions), plain markdown is simpler and more transparent
- Every claim can be traced to a specific source file
- Articles are human-readable and editable in any text editor
- No embedding infrastructure, vector database, or chunking pipeline needed
- The LLM built the wiki, so it understands the structure

### Why Two Ingestion Tools?
- trafilatura excels at extracting clean article content from web pages (strips navbars, ads, footers)
- markitdown handles non-HTML formats (PDF, DOCX, PPTX) and has specialized YouTube transcript extraction
- Neither tool downloads images -- they preserve image URLs as markdown references

### Why Append-Only raw/?
- Source material should never be modified after capture
- This creates an audit trail -- every wiki claim points back to the original source
- If a source is wrong, the wiki article gets updated but the raw file stays as-is for reference
