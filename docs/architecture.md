# Architecture

## Overview

This is an LLM-maintained knowledge base inspired by Andrej Karpathy's "LLM Knowledge Bases" concept. Instead of RAG pipelines with vector databases, the system uses plain markdown files organized into a per-source wiki structure. An LLM agent (Claude Code) acts as librarian and author -- reading raw source material and compiling it into structured, interlinked encyclopedia-style articles. A knowledge graph connects concepts across sources via explicit cross-references and shared tags.

## System Diagram

```
  URL (article, PDF, YouTube)
    |
    v
  +------------------------------------------+
  |  clip.sh                                 |
  |  trafilatura (web) / markitdown (PDF/YT) |
  +------------------------------------------+
    |
    v
  +------------------------------------------+
  |  raw/                                    |  Append-only source documents
  |  YYYYMMDD-source-slug.md                 |  One file per source, never edited
  +------------------------------------------+
    |
    |  LLM Agent (Claude Code)
    |  reads CLAUDE.md schema + skills
    |  runs /add or /ingest
    |
    v
  +------------------------------------------+
  |  wiki/<source-slug>/                     |  Per-source folders
  |  ├── summary-<source-slug>.md            |  Depth-configured summary + ASCII diagrams
  |  ├── concept-one.md                      |  Wiki article with tags + backlinks
  |  ├── concept-two.md                      |  Cross-folder links via ../other-folder/
  |  └── ...                                 |
  +------------------------------------------+
    |                      |
    v                      v
  +-------------------+  +-------------------+
  |  wiki/index.md    |  |  changelog.md     |
  |  Master index     |  |  Every run logged |
  |  by category      |  |                   |
  +-------------------+  +-------------------+
    |
    v
  +------------------------------------------+
  |  build_graph.py                          |
  |  Scans frontmatter -> graph.json + HTML  |
  +------------------------------------------+
    |
    +--------------------+
    v                    v
  +------------------+ +------------------+
  | wiki/graph.json  | | wiki/graph.html  |
  | Nodes + edges    | | D3.js visual     |
  | (structured)     | | (self-contained) |
  +------------------+ +------------------+
```

## Components

### 1. raw/ (Source Documents)

- Append-only staging area for raw content
- Files are never edited after being added
- Naming: `YYYYMMDD-source-slug.md`
- Content arrives via `clip.sh`, `/add` skill, or manual file drops

### 2. wiki/<source-slug>/ (Per-Source Article Folders)

Each ingested source gets its own folder inside `wiki/`. The folder contains:

- **summary-<source-slug>.md** -- Source summary written at the configured depth level (100/300/500) with required ASCII diagrams (sequence, architecture, or flowchart)
- **concept-name.md** -- Individual wiki articles for each key concept (3-10 per source)

Example structure:
```
wiki/
├── index.md
├── graph.json
├── graph.html
├── arxiv-2510-11977/
│   ├── summary-arxiv-2510-11977.md
│   ├── holistic-agent-leaderboard.md
│   ├── agent-scaffolds.md
│   ├── pareto-frontier-in-agent-evaluation.md
│   └── ...
├── ietf-draft-narajala-ans/
│   ├── summary-ietf-draft-narajala-ans.md
│   ├── agent-name-service.md
│   └── ...
└── naur-programming-as-theory-building/
    ├── summary-naur-programming-as-theory-building.md
    ├── programming-as-theory-building.md
    └── ...
```

### 3. Article Format

Every wiki article has YAML frontmatter with:

- **title**: Concept name
- **created/updated**: ISO dates
- **sources**: List of raw files this article draws from
- **related**: Markdown links to related articles (same folder or cross-folder via `../`)
- **tags**: 3-7 lowercase-kebab-case tags (content-specific + broader topic)

Tags serve dual purpose: they describe the article's content and connect it to the larger topic taxonomy. The knowledge graph uses tags to auto-generate edges between articles in different source folders.

### 4. Source Summaries

Each source folder contains a summary written at the configured depth level:

| Level | Style | Words | Audience |
|-------|-------|-------|----------|
| 100 | Feynman technique, analogies, simple language | 300-600 | General |
| 300 | Technical but accessible, explains domain terms | 500-800 | College level |
| 500 | Full technical detail, algorithms, tradeoffs | 800-1200 | Expert |

Every summary includes at least one ASCII diagram (sequence, architecture block, or flowchart) regardless of depth level. The depth preference is stored in `.claude/skills/add/config.json`.

### 5. Knowledge Graph

The knowledge graph is maintained in `wiki/graph.json` and rebuilt programmatically by `build_graph.py` after every ingestion.

**Nodes** represent articles and summaries, each with:
- id, title, file path, tags, source_folder, type (article/summary)

**Edges** connect nodes via three relationship types:

| Edge Type | How Created | Purpose |
|-----------|-------------|---------|
| `related` | Explicit `related:` links in article frontmatter | Direct conceptual relationships |
| `shared-tag` | Auto-generated: articles in different folders sharing 2+ tags | Cross-source conceptual bridges |
| `source` | Auto-generated: each article linked to its folder's summary | Source provenance |

The `shared-tag` edges are what connect otherwise isolated per-source clusters. For example, an article about "Agent Scaffolds" (from the HAL paper) and "Agent Communication Protocols" (from the IETF ANS draft) both carry `ai-agents` and `multi-agent-systems` tags, creating an automatic bridge.

`wiki/graph.html` is a self-contained D3.js force-directed visualization with the graph data embedded inline (no server required). It supports filtering by source folder, tag, and edge type, with hover-to-highlight and click-to-open.

### 6. CLAUDE.md (Schema File)

Operating instructions for the LLM agent:
- Article format, naming conventions, and tag guidelines
- Source summary format and depth levels
- Knowledge graph schema
- Operations: ingest, query, lint

### 7. clip.sh (Ingestion Script)

Shell script that converts URLs to markdown files in `raw/`:

| Tool | Best For | Routing |
|------|----------|---------|
| trafilatura | Web articles, blog posts (clean output) | Default for web URLs |
| markitdown | PDFs, DOCX, YouTube transcripts | Auto-detected by URL pattern |

Supports `--bulk` mode for batch ingestion from a text file.

### 8. Skills (.claude/skills/)

Claude Code skills define the agent's operations:

| Skill | Trigger | What It Does |
|-------|---------|--------------|
| `/add <url>` | User provides URL | Clips URL to raw/, ingests into wiki, rebuilds graph |
| `/ingest` | User has new files in raw/ | Batch processes all unprocessed raw files |
| `/query <question>` | User asks a question | Searches graph.json by tags, reads articles, synthesizes answer |
| `/lint` | User requests health check | Checks broken links, missing backlinks, folder structure, stale references |

### 9. build_graph.py

Python script that programmatically generates the knowledge graph:

1. Scans all `wiki/<source-slug>/*.md` files
2. Parses YAML frontmatter (title, tags, related links)
3. Builds nodes for each article and summary
4. Builds edges from explicit `related:` links, shared tags (2+ tags across folders), and source links
5. Writes `wiki/graph.json` (structured data) and `wiki/graph.html` (self-contained visualization)

### 10. changelog.md (Run Log)

Every ingest or update operation gets a timestamped entry recording:
- Which raw files were processed
- Which source folder was created
- Which articles were created or updated
- Summary depth level used

## Data Flow

### Adding Content (/add)

1. User runs `/add <url>`
2. `clip.sh` downloads the URL to `raw/YYYYMMDD-source-slug.md`
3. LLM reads the raw file and extracts 3-10 key concepts
4. LLM creates `wiki/<source-slug>/` with individual articles and a depth-configured summary
5. LLM adds cross-references between new articles and existing ones (including cross-folder backlinks)
6. `build_graph.py` regenerates `wiki/graph.json` and `wiki/graph.html`
7. LLM updates `wiki/index.md` and appends to `changelog.md`

### Querying Knowledge (/query)

1. Agent reads `wiki/graph.json` to find articles matching tags or keywords
2. Agent reads `wiki/index.md` for category-level navigation
3. Agent reads relevant articles and follows cross-references for deeper context
4. Agent synthesizes an answer with citations to specific wiki files

### Maintaining Quality (/lint)

1. Scans for broken markdown links (links to files that don't exist)
2. Detects legacy `[[wikilink]]` syntax (should be `[text](file.md)`)
3. Validates folder structure (each source folder should have a summary)
4. Identifies stale backlinks and missing cross-references
5. Suggests new articles for concepts mentioned 3+ times without their own article

## Design Decisions

### Why No RAG?

- At the scale of a personal knowledge base (tens of sources, hundreds of articles), plain markdown is simpler and more transparent
- Every claim can be traced to a specific source file in `raw/`
- Articles are human-readable and editable in any text editor
- No embedding infrastructure, vector database, or chunking pipeline needed
- The LLM built the wiki, so it understands the structure

### Why Per-Source Folders?

- Each ingested source gets its own namespace, preventing article name collisions
- Source summaries live alongside their articles for easy navigation
- Cross-folder links (`../other-folder/article.md`) make inter-source relationships explicit
- The folder structure maps directly to the knowledge graph's source_folder attribute

### Why a Knowledge Graph?

- Tags alone are not visible as connections -- the graph materializes tag relationships as edges
- Cross-source conceptual bridges (shared-tag edges) emerge automatically without manual linking
- The graph enables tag-based search in the `/query` skill
- The HTML visualization provides an intuitive overview of the entire knowledge base

### Why Two Ingestion Tools?

- trafilatura excels at extracting clean article content from web pages (strips navbars, ads, footers)
- markitdown handles non-HTML formats (PDF, DOCX, PPTX) and has specialized YouTube transcript extraction
- Neither tool downloads images -- they preserve image URLs as markdown references

### Why Append-Only raw/?

- Source material should never be modified after capture
- This creates an audit trail -- every wiki claim points back to the original source
- If a source is wrong, the wiki article gets updated but the raw file stays as-is for reference

### Why Configurable Depth Levels?

- Different users need different levels of detail from the same source
- Level 100 (Feynman) is useful for onboarding or sharing with non-experts
- Level 500 (expert) preserves full technical detail for deep reference
- The depth applies only to source summaries; individual wiki articles are always written at a consistent encyclopedia style
