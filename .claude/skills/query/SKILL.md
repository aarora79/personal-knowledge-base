---
name: query
description: Query the knowledge base. Searches wiki articles and synthesizes an answer with references.
argument-hint: <question>

---

# Query the Knowledge Base

Answer the question: $ARGUMENTS

## Steps

1. Read `wiki/graph.json` to understand the knowledge graph structure (nodes, edges, tags)
2. Read `wiki/index.md` to find relevant articles by category
3. Search by tags: identify tags most relevant to the question, then find articles sharing those tags in graph.json
4. Use Grep to search `wiki/` for keywords related to the question
5. Read the most relevant wiki articles (up to 5)
6. If wiki articles reference raw/ sources and more detail is needed, read those too
7. Synthesize an answer grounded in the wiki content

## Tag-based search

The knowledge graph (`wiki/graph.json`) contains tags for every article. Use these to find
related content that keyword search might miss. For example, if the user asks about "how
agents verify each other", search for tags like `agent-identity`, `pki`, `trust` to find
relevant articles even if they don't contain those exact words.

When multiple articles share tags, they likely cover related aspects of the same topic.
Follow tag clusters to build a more complete answer.

## Rules
- Every claim in your answer must trace to a specific wiki article or raw source
- Cite sources at the end using markdown links to the wiki files
- If the knowledge base has no relevant content, say so clearly
- Do not make things up or add information beyond what is in the wiki
- Keep the answer concise and direct
