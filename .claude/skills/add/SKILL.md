---
name: add
description: Add a URL to the knowledge base. Clips it to raw/, then ingests it into wiki articles. One command does everything.
argument-hint: <url> [slug]
allowed-tools: Bash Read Edit Write Glob Grep
---

# Add Content to Knowledge Base

Add the URL $ARGUMENTS to the knowledge base. This runs two phases back to back.

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
3. Extract 3-10 key concepts from the raw file
4. For each concept:
   - Check if a wiki article already exists in `wiki/`
   - If yes: update and expand the article, add new source to frontmatter, update the `updated` date
   - If no: create a new article following the format below
5. Add `[[backlinks]]` in related articles that reference these concepts
6. Update `wiki/index.md`:
   - Add new articles under the appropriate category
   - Update the "Total articles" count
   - Update the "Last updated" date
7. Append to `changelog.md`:
   ```
   ## [YYYY-MM-DD] ingest | <source description>
   - Processed: raw/<filename>
   - Created: <list of new wiki articles>
   - Updated: <list of updated wiki articles>
   ```

## Article format

```markdown
---
title: <Concept Name>
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [raw/filename.md, ...]
related: [[other-article]], [[another-article]]
---

# <Concept Name>

<Encyclopedia-style summary, 200-500 words>

## Key Points
- ...

## Related Concepts
- [[linked-article]] - brief note on relationship

## Sources
- raw/filename.md - what this source contributed
```

## Important rules
- Never make things up. Every claim must trace to the raw file.
- Wiki filenames: lowercase-kebab-case.md
- A single raw source may touch 10-15 wiki pages
- Keep summaries between 200-500 words
- Concepts mentioned 3+ times across articles should get their own article
- Always update the index and changelog when done
