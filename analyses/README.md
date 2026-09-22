# Analyses

Single-document paper analyses written with the Feynman technique: what the paper claims, how it got there, what it leaves unresolved. One folder per paper, holding the analysis and the prompt that produced it.

These moved here from `my-ai-assets/prompts/understand-academic-paper/` on 2026-09-22. That repo keeps the tooling that makes them (`template.txt`, `generate_prompts.py`, the `understand-academic-paper` prompt); the outputs live here with the rest of the reading.

## How these differ from `wiki/`

| | `analyses/` | `wiki/` |
| --- | --- | --- |
| Shape | one document per paper | many short articles per source |
| Length | 1,200 to 2,500 words | 200 to 500 words each |
| Written by | the Feynman prompt template | the `/add` and `/ingest` skills |
| Cross-linked | no | yes, plus graph edges |
| Traces to `raw/` | not required | required, every claim |

An analysis is a standalone read. A wiki article is a node in the graph. A paper can have both, and four here already do.

## Contents

| Analysis | Source | Words | `wiki/` | `raw/` |
| --- | --- | --- | --- | --- |
| [agent-first-database-systems](agent-first-database-systems/analysis.md) | [link](https://arxiv.org/pdf/2509.00997) | 1,367 | [`agent-first-data-systems`](../wiki/agent-first-data-systems/) | `20250901-agent-first-data-systems.md` |
| [agentgym-rl-training-llm-agents](agentgym-rl-training-llm-agents/analysis.md) | [link](https://arxiv.org/pdf/2509.08755) | 1,408 | none | not clipped |
| [ai-model-collapse-recursive-training](ai-model-collapse-recursive-training/analysis.md) | [link](https://www.nature.com/articles/s41586-024-07566-y.pdf) | 1,306 | none | not clipped |
| [holistic-agent-leaderboard-hal](holistic-agent-leaderboard-hal/analysis.md) | [link](https://arxiv.org/pdf/2510.11977) | 2,461 | [`arxiv-2510-11977`](../wiki/arxiv-2510-11977/) | `20260408-arxiv-2510-11977.md` |
| [k2-think-parameter-efficient-reasoning](k2-think-parameter-efficient-reasoning/analysis.md) | [link](https://arxiv.org/pdf/2509.07604) | 1,217 | none | not clipped |
| [llm-physical-reasoning-3d-environment](llm-physical-reasoning-3d-environment/analysis.md) | [link](https://arxiv.org/pdf/2410.23242v2) | 1,572 | none | not clipped |
| [openai-why-language-models-hallucinate](openai-why-language-models-hallucinate/analysis.md) | [link](https://cdn.openai.com/pdf/d04913be-3f6f-4d2b-b283-ff432ef4aaa5/why-language-models-hallucinate.pdf) | 1,381 | none | not clipped |
| [parathinker-parallel-thinking-llm](parathinker-parallel-thinking-llm/analysis.md) | [link](https://www.arxiv.org/pdf/2509.04475) | 1,308 | none | not clipped |
| [satlution-autonomous-code-evolution](satlution-autonomous-code-evolution/analysis.md) | [link](https://arxiv.org/pdf/2509.07367) | 1,732 | [`arxiv-2509-07367`](../wiki/arxiv-2509-07367/) | `20260408-arxiv-2509-07367.md` |
| [the-nature-of-the-firm](the-nature-of-the-firm/analysis.md) | [link](https://onlinelibrary.wiley.com/doi/10.1111/j.1468-0335.1937.tb00002.x) | 1,483 | [`coase-nature-of-the-firm`](../wiki/coase-nature-of-the-firm/) | `20260408-coase-nature-of-the-firm.md` |

## Open: four papers written up twice

4 of these 10 papers also went through the `/add` pipeline into `wiki/`, so each has two independent write-ups that never saw each other:

- **agent-first-database-systems**, 1,367 words in one document, against `wiki/agent-first-data-systems/` at 8 files
- **holistic-agent-leaderboard-hal**, 2,461 words in one document, against `wiki/arxiv-2510-11977/` at 9 files
- **satlution-autonomous-code-evolution**, 1,732 words in one document, against `wiki/arxiv-2509-07367/` at 9 files
- **the-nature-of-the-firm**, 1,483 words in one document, against `wiki/coase-nature-of-the-firm/` at 7 files

Neither version is wrong. The analysis reads start to finish; the wiki articles slot into the graph. Reconciling means deciding per paper whether to keep both, fold the analysis in as the source summary, or drop one. Nothing has been deleted pending that call.

## The other 6 are not in the pipeline

6 papers have an analysis but were never clipped, so there is no `raw/` archive and no wiki articles. If any of them matter, `/add <url>` runs the full pipeline and the analysis here becomes a second view of the same source:

- agentgym-rl-training-llm-agents &middot; `/add https://arxiv.org/pdf/2509.08755`
- ai-model-collapse-recursive-training &middot; `/add https://www.nature.com/articles/s41586-024-07566-y.pdf`
- k2-think-parameter-efficient-reasoning &middot; `/add https://arxiv.org/pdf/2509.07604`
- llm-physical-reasoning-3d-environment &middot; `/add https://arxiv.org/pdf/2410.23242v2`
- openai-why-language-models-hallucinate &middot; `/add https://cdn.openai.com/pdf/d04913be-3f6f-4d2b-b283-ff432ef4aaa5/why-language-models-hallucinate.pdf`
- parathinker-parallel-thinking-llm &middot; `/add https://www.arxiv.org/pdf/2509.04475`

