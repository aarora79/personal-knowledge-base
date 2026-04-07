---
name: query
description: Query the knowledge base. Searches wiki articles and synthesizes an answer with references.
argument-hint: <question>
allowed-tools: Read Glob Grep
---

# Query the Knowledge Base

Answer the question: $ARGUMENTS

## Steps

1. Read `wiki/index.md` to find relevant articles
2. Use Grep to search wiki/ for keywords related to the question
3. Read the most relevant wiki articles (up to 5)
4. If wiki articles reference raw/ sources and more detail is needed, read those too
5. Synthesize an answer grounded in the wiki content

## Rules
- Every claim in your answer must trace to a specific wiki article or raw source
- Cite sources at the end using markdown links to the wiki files
- If the knowledge base has no relevant content, say so clearly
- Do not make things up or add information beyond what is in the wiki
- Keep the answer concise and direct
