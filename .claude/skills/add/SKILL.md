---
name: add
description: Add a URL to the knowledge base. Clips it to raw/, then ingests it into wiki articles. One command does everything.
argument-hint: <url> [slug]
---

# Add Content to Knowledge Base

Add the URL $ARGUMENTS to the knowledge base. This runs three phases.

## Phase 0: Check depth level preference

1. Read the config file at `.claude/skills/add/config.json`
2. If the file exists and has a `depth_level` field, use that as the default
3. Ask the user:

   "What depth level for the source summary?
   - **100** - Explain like I'm 12 (Feynman technique, analogies, no jargon)
   - **300** - College level (technical but accessible, assumes some background)
   - **500** - Expert deep-dive (full technical detail, assumes domain expertise)

   Current default: <value from config or 100>
   Press enter to use default, or type 100/300/500 to change."

4. If the user picks a new level, update `.claude/skills/add/config.json` with the new preference
5. If the user just presses enter or says "default", use the stored value

## Phase 1: Clip (download URL to raw/)

Run the clip script:

```
./clip.sh $ARGUMENTS
```

The script auto-detects content type:
- YouTube and PDF URLs use markitdown
- Everything else uses trafilatura

If clip.sh fails or returns empty content, try the alternate tool directly:
- For web articles: `uv run trafilatura -u "<url>" --output-format markdown`
- For PDFs/YouTube: `uv run markitdown "<url>"`

If both tools fail (e.g. scanned image PDFs), tell the user and stop.

Verify the file was created and has content. Read the first 50 lines to confirm.

## Phase 2: Ingest (compile raw file into wiki)

Read the full raw file that was just created. Then:

1. Read `wiki/index.md` to understand existing articles
2. Read `changelog.md` to understand what has been done before
3. Derive a source slug from the raw filename (strip the YYYYMMDD- date prefix)
4. Create a source folder: `wiki/<source-slug>/`
5. Extract 3-10 key concepts from the raw file
6. For each concept:
   - Check if a wiki article already exists anywhere in `wiki/`
   - If yes: update and expand the article, add new source to frontmatter, update the `updated` date
   - If no: create a new article inside `wiki/<source-slug>/`
7. Add backlinks in related articles (use relative paths between folders)
8. **Create `wiki/<source-slug>/summary-<source-slug>.md`** using the depth level from Phase 0
9. Update `wiki/index.md`:
   - Add new articles under the appropriate category with clickable links
   - Add summary link under "Source Summaries" section
   - Update the "Total articles" count and "Last updated" date
10. Rebuild the context graph: `uv run python build_graph.py`
11. Append to `changelog.md`:
    ```
    ## [YYYY-MM-DD] ingest | <source description>
    - Processed: raw/<filename>
    - Folder: wiki/<source-slug>/
    - Created: <list of new wiki articles>
    - Summary: wiki/<source-slug>/summary-<source-slug>.md (depth: <level>)
    - Updated: <list of updated wiki articles>
    ```

## Source Summary format

For each raw source, create `wiki/<source-slug>/summary.md`. The depth level controls
the writing style. All summaries link to every wiki article in the same folder.
Use markdown links for all references: `[article name](article-name.md)`.

Naming: `wiki/<source-slug>/summary.md`

```markdown
---
title: "Source Summary: <Source Title>"
created: YYYY-MM-DD
source: raw/filename.md
depth: <100|300|500>
articles_created: [wiki/article-one.md, wiki/article-two.md, ...]
---

# <Source Title> - Summary

<Summary content written at the chosen depth level>

## What This Source Covers
- <bullet summary of main topics>

## Wiki Articles From This Source
- [Article One](article-one.md) - one line description
- [Article Two](article-two.md) - one line description
```

### Depth level guidelines

**100 level (Explain like I'm 12)**
- 300-600 words
- Feynman technique: use analogies, everyday examples, simple language
- When you must use a technical term, explain it immediately in parentheses
- Example: "DNS is like a phone book for the internet"

**300 level (College level)**
- 500-800 words
- Assumes the reader knows basic CS/AI concepts
- Uses technical terms but explains domain-specific ones
- Covers architecture and design decisions, not just "what"
- Example: "ANS extends DNS-SD with PKI-based identity verification and capability-aware resolution"

**500 level (Expert deep-dive)**
- 800-1200 words
- Assumes deep domain expertise
- Full technical detail: algorithms, protocols, formal specifications
- Discusses trade-offs, limitations, and comparisons to alternatives
- Example: "The resolution algorithm performs version negotiation via semantic versioning ranges before cryptographic verification of the endpoint record using a two-phase signature and certificate chain validation"

### ASCII diagrams (required in every summary)

Every source summary must include at least one ASCII diagram, regardless of depth level.
Choose the most appropriate type(s) for the content:

- **Sequence diagram**: for protocols, request/response flows, multi-step interactions
- **Architecture/block diagram**: for system components, layers, data flow
- **Flowchart**: for decision logic, algorithms, processes

Use simple ASCII box-drawing characters. Example:

```
  +------------------+       +------------------+
  |   Requesting     |       |   Agent Name     |
  |     Agent        |       |   Service (ANS)  |
  +--------+---------+       +--------+---------+
           |                          |
           |  1. Resolve ANSName      |
           |------------------------->|
           |                          |
           |  2. Verify certificates  |
           |                          |
           |  3. Return endpoint      |
           |<-------------------------|
           |                          |
```

Keep diagrams readable (under 70 characters wide). Use them to reinforce the text,
not replace it. At minimum include one diagram per summary.

## Article format

Individual wiki articles are always written at a consistent encyclopedia style regardless
of the summary depth level.

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

### Tags guidelines

Every article must have a `tags` field in its frontmatter. Tags serve two purposes:
1. **Content-specific tags**: describe what this specific article covers (e.g., `pki`, `zero-knowledge-proofs`, `dns`)
2. **Broader topic tags**: connect the article to the larger topic it serves (e.g., `ai-agents`, `software-engineering-philosophy`, `multi-agent-systems`)

Use lowercase-kebab-case for all tags. Include 3-7 tags per article.
Reuse existing tags from other articles where possible to build a coherent tag taxonomy.

## Context Graph

After creating/updating articles, rebuild the context graph by running:

```
uv run python build_graph.py
```

This script scans all wiki articles, parses their frontmatter (related links, tags),
and generates `wiki/graph.json` with nodes and edges. The `/query` skill uses it for
tag-based search. The visual graph is viewable at `wiki/graph.html`.

## Important rules
- Never make things up. Every claim must trace to the raw file.
- Wiki filenames: lowercase-kebab-case.md
- Source summary filenames: wiki/summary-<slug>.md
- Use markdown links `[text](file.md)` for all cross-references so they are clickable
- A single raw source may touch 10-15 wiki pages
- Keep article summaries between 200-500 words
- Summary length varies by depth level (100: 300-600, 300: 500-800, 500: 800-1200)
- Concepts mentioned 3+ times across articles should get their own article
- Always update the index and changelog when done
