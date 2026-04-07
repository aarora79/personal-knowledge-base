---
name: lint
description: Run a health check on the wiki. Find broken links, missing articles, inconsistencies, and suggest improvements.

---

# Lint the Knowledge Base

Run a comprehensive health check on the wiki and report findings.

## Check 1: Broken markdown links

Scan all wiki articles for `[text](path.md)` links that point to files that do not exist.

Report each broken link with the file it appears in:
```
BROKEN LINK: [text](path.md) in wiki/<source-slug>/some-article.md
```

## Check 2: Legacy wikilink syntax

Scan all wiki articles for `[[link]]` syntax which should be replaced with clickable
markdown links `[text](path.md)` using relative paths between folders.

Report each:
```
LEGACY LINK: [[article-name]] in wiki/<source-slug>/some-article.md — convert to [text](path.md)
```

## Check 3: Missing articles

Scan all wiki articles for concepts or terms that appear 3+ times across different articles but do not have their own wiki article yet.

Report each:
```
MISSING ARTICLE: "<concept>" mentioned in N articles but has no wiki page
```

## Check 4: Index consistency

Compare `wiki/index.md` against actual files in `wiki/`:
- Articles listed in index but file does not exist
- Articles that exist as files but are not listed in the index
- Summary files listed but not present

Report each:
```
INDEX STALE: wiki/<source-slug>/<file>.md exists but not in index
INDEX GHOST: wiki/<source-slug>/<file>.md listed in index but file missing
```

## Check 5: Source traceability

Check that every wiki article has at least one source in its frontmatter that exists in `raw/`.

Report:
```
NO SOURCE: wiki/<source-slug>/<file>.md has no sources listed
MISSING SOURCE: wiki/<source-slug>/<file>.md references raw/<file>.md which does not exist
```

## Check 6: Folder structure

Check that each source folder in `wiki/` contains:
- A summary file named `summary-<folder-name>.md`
- At least one article file

Report:
```
MISSING SUMMARY: wiki/<source-slug>/ has no summary-<source-slug>.md
EMPTY FOLDER: wiki/<source-slug>/ has no article files
```

## Check 7: Stale backlinks

Check that `related:` entries in frontmatter point to articles that actually exist.

Report:
```
STALE BACKLINK: wiki/<source-slug>/<file>.md links to a non-existent article
```

## Summary

After all checks, produce a summary:

```
HEALTH CHECK SUMMARY
--------------------
Total wiki articles: N
Total source folders: N
Broken links: N
Legacy wikilinks: N
Missing articles suggested: N
Index issues: N
Source issues: N
Folder structure issues: N
Stale backlinks: N
```

## Suggestions

Based on findings, suggest up to 5 new articles that would most strengthen the knowledge base. Prioritize:
1. Concepts referenced by many articles but lacking their own page
2. Bridging articles that would connect isolated clusters
3. Foundational concepts assumed but not explained

Format:
```
SUGGESTED ARTICLES
1. <concept-name>.md - <why it would help>
2. ...
```

## Auto-fix option

After reporting, ask the user if they want to auto-fix:
- Convert legacy `[[wikilinks]]` to markdown links with relative paths
- Add missing articles to the index
- Remove ghost entries from the index
- Update the article count and date in the index
