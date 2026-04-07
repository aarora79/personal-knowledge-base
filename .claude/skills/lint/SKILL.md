---
name: lint
description: Run a health check on the wiki. Find broken links, missing articles, inconsistencies, and suggest improvements.
allowed-tools: Bash Read Edit Write Glob Grep
---

# Lint the Knowledge Base

Run a comprehensive health check on the wiki and report findings.

## Check 1: Orphaned references

Scan all wiki articles for `[[links]]` that point to articles that do not exist in `wiki/`.

Report each broken link with the file it appears in:
```
BROKEN LINK: [[missing-article]] in wiki/some-article.md
```

## Check 2: Missing articles

Scan all wiki articles for concepts or terms that appear 3+ times across different articles but do not have their own wiki article yet.

Report each:
```
MISSING ARTICLE: "<concept>" mentioned in N articles but has no wiki page
```

## Check 3: Index consistency

Compare `wiki/index.md` against actual files in `wiki/`:
- Articles listed in index but file does not exist
- Articles that exist as files but are not listed in the index

Report each:
```
INDEX STALE: wiki/<file>.md exists but not in index
INDEX GHOST: wiki/<file>.md listed in index but file missing
```

## Check 4: Source traceability

Check that every wiki article has at least one source in its frontmatter that exists in `raw/`.

Report:
```
NO SOURCE: wiki/<file>.md has no sources listed
MISSING SOURCE: wiki/<file>.md references raw/<file>.md which does not exist
```

## Check 5: Stale backlinks

Check that `related: [[...]]` entries in frontmatter point to articles that actually exist.

Report:
```
STALE BACKLINK: wiki/<file>.md links to [[missing]] which does not exist
```

## Summary

After all checks, produce a summary:

```
HEALTH CHECK SUMMARY
--------------------
Total wiki articles: N
Broken links: N
Missing articles suggested: N
Index issues: N
Source issues: N
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
- Add missing articles to the index
- Remove ghost entries from the index
- Update the article count and date in the index
