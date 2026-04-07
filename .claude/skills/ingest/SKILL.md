---
name: ingest
description: Process all unprocessed raw files into wiki articles. Run this after adding files to raw/.
---

# Ingest Raw Files into Wiki

Process all unprocessed files in `raw/` and compile them into wiki articles.

## Step 0: Check depth level preference

Read `.claude/skills/add/config.json` to get the `depth_level` setting (100, 300, or 500).
If the file does not exist, default to 100.

## Step 1: Find unprocessed files

1. List all files in `raw/`
2. Read `changelog.md` to find which files have already been processed
3. Identify files in `raw/` that are NOT mentioned in `changelog.md`

If all files are already processed, tell the user "Nothing new to ingest." and stop.

## Step 2: Read existing wiki state

1. Read `wiki/index.md` to understand existing articles and categories
2. Scan `wiki/` for existing article folders and files

## Step 3: Process each new raw file

For each unprocessed raw file:

1. Read the full file
2. Derive a source slug from the raw filename (strip the YYYYMMDD- date prefix)
3. Create a source folder: `wiki/<source-slug>/`
4. Extract 3-10 key concepts
5. For each concept:
   - Check if a wiki article already exists anywhere in `wiki/`
   - If yes: update and expand the article, add new source to frontmatter, update the `updated` date
   - If no: create a new article inside `wiki/<source-slug>/`
6. Add backlinks in related articles (use relative paths between folders)
7. Create `wiki/<source-slug>/summary-<source-slug>.md` at the configured depth level

## Step 4: Rebuild context graph

Run `uv run python build_graph.py` to regenerate `wiki/graph.json` from article frontmatter.

## Step 5: Update index and log

1. Update `wiki/index.md`:
   - Add new articles under the appropriate category with clickable markdown links
   - Add summary link under "Source Summaries" section
   - Update the "Total articles" count and "Last updated" date

2. Append to `changelog.md`:
   ```
   ## [YYYY-MM-DD] ingest | <brief description>
   - Processed: raw/<filename1>, raw/<filename2>, ...
   - Folder: wiki/<source-slug>/
   - Created: <list of new wiki articles>
   - Summary: wiki/<source-slug>/summary-<source-slug>.md (depth: <level>)
   - Updated: <list of updated wiki articles>
   ```

## Source Summary format

The summary file name includes the folder name so it is identifiable even if downloaded
standalone. Depth level controls the writing style. Read depth from `.claude/skills/add/config.json`.

Naming: `wiki/<source-slug>/summary-<source-slug>.md`

### Depth levels
- **100** - Explain like I'm 12 (Feynman technique, analogies, 300-600 words)
- **300** - College level (technical but accessible, 500-800 words)
- **500** - Expert deep-dive (full technical detail, 800-1200 words)

### ASCII diagrams (required in every summary)

Every source summary must include at least one ASCII diagram, regardless of depth level.
Choose the most appropriate type(s) for the content:

- **Sequence diagram**: for protocols, request/response flows, multi-step interactions
- **Architecture/block diagram**: for system components, layers, data flow
- **Flowchart**: for decision logic, algorithms, processes

Keep diagrams readable (under 70 characters wide). At minimum one diagram per summary.

## Article format

Individual wiki articles go inside the source folder and are always written at a consistent
encyclopedia style regardless of summary depth level.

Use `[text](file.md)` markdown links for all cross-references so they are clickable.

Every article must have a `tags` field in its frontmatter with 3-7 lowercase-kebab-case tags.
Tags should include both concept-specific tags and broader topic tags that connect to the
larger category the article serves (e.g., `ai-agents`, `software-engineering-philosophy`).

## Important rules
- Never make things up. Every claim must trace to a file in raw/.
- Each source gets its own folder: wiki/<source-slug>/
- Summary naming: wiki/<source-slug>/summary-<source-slug>.md
- Article naming: wiki/<source-slug>/lowercase-kebab-case.md
- Use markdown links for all cross-references
- A single raw source may touch 10-15 wiki pages
- Keep article summaries between 200-500 words
- Summary length varies by depth level
- Concepts mentioned 3+ times across articles should get their own article
- Always update the index and changelog when done
