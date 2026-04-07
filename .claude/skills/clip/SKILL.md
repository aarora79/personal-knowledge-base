---
name: clip
description: Clip a URL into raw/ and then ingest it into the wiki. Accepts a URL and optional slug.
argument-hint: <url> [slug]
allowed-tools: Bash Read Edit Write Glob Grep
---

# Clip and Ingest a URL

Clip the URL $ARGUMENTS into the knowledge base and compile it into wiki articles.

## Step 1: Clip the URL into raw/

Run the clip script to download and convert the URL to markdown:

```
./clip.sh $ARGUMENTS
```

The script auto-detects content type:
- YouTube and PDF URLs use markitdown
- Everything else uses trafilatura

If clip.sh fails or returns empty content, try the alternate tool directly:
- For web articles: `uv run trafilatura -u "<url>" --output-format markdown`
- For PDFs/YouTube: `uv run markitdown "<url>"`

If both tools fail (e.g. scanned image PDFs), tell the user and suggest alternatives.

Verify the file was created and has content. Read the first 50 lines to confirm.

## Step 2: Ingest into wiki

Read the full raw file that was just created. Then:

1. Read `wiki/index.md` to understand existing articles
2. Read `changelog.md` to understand what has been done before
3. Extract 3-10 key concepts from the raw file
4. For each concept:
   - Check if a wiki article already exists in `wiki/`
   - If yes: update and expand the article, add new source to frontmatter
   - If no: create a new article following the format in CLAUDE.md
5. Add `[[backlinks]]` in related articles
6. Update `wiki/index.md` with any new articles
7. Append a new entry to `changelog.md`:
   ```
   ## [YYYY-MM-DD] ingest | <source description>
   - Processed: raw/<filename>
   - Created: <list of new wiki articles>
   - Updated: <list of updated wiki articles>
   ```

## Article format reminder

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
- Keep summaries between 200-500 words
- Always update the index and changelog
