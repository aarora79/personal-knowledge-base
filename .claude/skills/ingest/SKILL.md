---
name: ingest
description: Process all unprocessed raw files into wiki articles. Run this after adding files to raw/.
allowed-tools: Bash Read Edit Write Glob Grep
---

# Ingest Raw Files into Wiki

Process all unprocessed files in `raw/` and compile them into wiki articles.

## Step 1: Find unprocessed files

1. List all files in `raw/`
2. Read `changelog.md` to find which files have already been processed
3. Identify files in `raw/` that are NOT mentioned in `changelog.md`

If all files are already processed, tell the user "Nothing new to ingest." and stop.

## Step 2: Read existing wiki state

1. Read `wiki/index.md` to understand existing articles and categories
2. Scan `wiki/` for existing article files

## Step 3: Process each new raw file

For each unprocessed raw file:

1. Read the full file
2. Extract 3-10 key concepts
3. For each concept:
   - Check if a wiki article already exists in `wiki/`
   - If yes: update and expand the article, add new source to frontmatter, update the `updated` date
   - If no: create a new article following the format below
4. Add `[[backlinks]]` in related articles that reference these concepts

## Step 4: Update index and log

1. Update `wiki/index.md`:
   - Add new articles under the appropriate category
   - Update the "Total articles" count
   - Update the "Last updated" date

2. Append to `changelog.md`:
   ```
   ## [YYYY-MM-DD] ingest | <brief description>
   - Processed: raw/<filename1>, raw/<filename2>, ...
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
- Never make things up. Every claim must trace to a file in raw/.
- Wiki filenames: lowercase-kebab-case.md
- A single raw source may touch 10-15 wiki pages
- Keep summaries between 200-500 words
- Concepts mentioned 3+ times across articles should get their own article
- Always update the index and changelog when done
