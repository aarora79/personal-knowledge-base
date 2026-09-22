# Inbox

Links to read, and what has been done with each. This is the queue `clip.sh --bulk` and `/add` work from.

It arrived here from `my-ai-assets/prompts/understand-academic-paper/urls.txt` on 2026-09-22. The queue used to sit in that repo while the clipper that consumes it lived in this one, which is how four papers ended up written up twice.

## Adding a link

Paste it under **Unprocessed** with a date and one line on why it caught your eye. That costs seconds and is the whole point: a link can sit here for a month without being lost. Then pick how far it goes.

## What each column means

These are four products, not four rungs of one ladder. A paper can have an analysis and no wiki articles, or wiki articles and no analysis.

| Column | Directory | What it is | Cost |
| --- | --- | --- | --- |
| clipped | `raw/` | the fetched source, append-only, survives link rot | a minute, `./clip.sh <url>` |
| wiki | `wiki/<slug>/` | atomic articles, tags, graph edges | a few minutes, `/add <url>` |
| analysis | `analyses/<slug>/` | one Feynman-technique document, 1,200 to 2,500 words | a session, prompt template |
| explainer | `explainers/<slug>/` | publishable HTML page, inline SVG, runnable code | a real session, `explainer` skill |

## Processed

| Source | clipped | wiki | analysis | explainer |
| --- | --- | --- | --- | --- |
| [agent-first-database-systems](https://arxiv.org/pdf/2509.00997) | yes | `agent-first-data-systems` | `agent-first-database-systems` | no |
| [agentgym-rl-training-llm-agents](https://arxiv.org/pdf/2509.08755) | no | no | `agentgym-rl-training-llm-agents` | no |
| [ai-model-collapse-recursive-training](https://www.nature.com/articles/s41586-024-07566-y.pdf) | no | no | `ai-model-collapse-recursive-training` | no |
| [holistic-agent-leaderboard-hal](https://arxiv.org/pdf/2510.11977) | yes | `arxiv-2510-11977` | `holistic-agent-leaderboard-hal` | no |
| [k2-think-parameter-efficient-reasoning](https://arxiv.org/pdf/2509.07604) | no | no | `k2-think-parameter-efficient-reasoning` | no |
| [llm-physical-reasoning-3d-environment](https://arxiv.org/pdf/2410.23242v2) | no | no | `llm-physical-reasoning-3d-environment` | no |
| [openai-why-language-models-hallucinate](https://cdn.openai.com/pdf/d04913be-3f6f-4d2b-b283-ff432ef4aaa5/why-language-models-hallucinate.pdf) | no | no | `openai-why-language-models-hallucinate` | no |
| [parathinker-parallel-thinking-llm](https://www.arxiv.org/pdf/2509.04475) | no | no | `parathinker-parallel-thinking-llm` | no |
| [satlution-autonomous-code-evolution](https://arxiv.org/pdf/2509.07367) | yes | `arxiv-2509-07367` | `satlution-autonomous-code-evolution` | no |
| [the-nature-of-the-firm](https://onlinelibrary.wiley.com/doi/10.1111/j.1468-0335.1937.tb00002.x) | yes | `coase-nature-of-the-firm` | `the-nature-of-the-firm` | no |
| arxiv-2504-19874 | yes | `arxiv-2504-19874` | no | no |
| claude-code-memory-management | yes | `claude-code-memory-management` | no | no |
| frontend-slides | yes | `frontend-slides` | no | no |
| ietf-draft-narajala-ans | yes | `ietf-draft-narajala-ans` | no | no |
| klowden-tao-ai-mathematics | yes | `klowden-tao-ai-mathematics` | no | no |
| naur-programming-as-theory-building | yes | `naur-programming-as-theory-building` | no | no |

## Unprocessed

Nothing queued. Add links here as they come in:

```
- 2026-09-22 https://example.com/thing  why it caught your eye
```

