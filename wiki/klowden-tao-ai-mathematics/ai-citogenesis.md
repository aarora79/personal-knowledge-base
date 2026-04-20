---
title: AI Citogenesis
created: 2026-04-20
updated: 2026-04-20
sources: [raw/20260420-arxivorg-html-260326524v1.md]
related: [faustian-bargain-of-ai](faustian-bargain-of-ai.md), [ai-and-mathematical-proof](ai-and-mathematical-proof.md)
tags: [ai-citogenesis, information-collapse, ai-research, citation-loops, provenance, responsible-ai]
---

# AI Citogenesis

AI Citogenesis describes the emergence of circular citation loops in which AI-generated summaries and analyses become treated as authoritative sources by subsequent AI research tools, creating feedback loops that can corrupt the knowledge ecosystem even in the absence of malicious intent. The term "citogenesis" was coined humorously by Randall Munroe in his xkcd comic #978 (2011), describing how an incorrect fact inserted into Wikipedia can get cited by a news article, which is then cited back on Wikipedia as a source, creating a self-reinforcing false citation.

Klowden and Tao give a concrete example they observed firsthand. Following the success of "deep research" AI tools in uncovering solutions to open mathematical problems buried in obscure literature, Tao helped launch an effort on an open problem site to systematically use these tools to report known literature on each problem, or the absence of such. This added real value to the site. However, the deep research tools began using these reports as an authoritative source for their own searches. The unintended consequence: summarizing these searches on the site interfered with any subsequent use of the tools to turn up genuinely new literature on those problems.

This is a subtle failure mode. No one acted maliciously. The AI tools were functioning as designed -- incorporating authoritative-looking sources into their answers. The human researchers were acting responsibly -- documenting known literature to make it accessible. But the interaction between these two legitimate activities created a closed loop that degraded the research ecosystem.

The phenomenon connects to broader concerns about AI-generated content in the information ecosystem:

**Model collapse.** AI models trained recursively on AI-generated data show documented performance degradation ("AI collapse"). Without sufficient genuine human content, models become ungrounded from reality. Mathematics, with its formal verification, may tolerate higher AI contamination than other domains, but is not immune.

**Erosion of provenance.** Training data origins become progressively obscured as AI-generated content mixes with human-generated content in subsequent training corpora. Distinguishing "what did a human actually discover" from "what was an AI's plausible guess" becomes increasingly difficult.

**Research integrity.** In a world where mathematical results can be mass-produced at automation speeds, the traditional social mechanisms that filter for significance (peer review, citation patterns, community consensus) may not operate fast enough. The authors note this as an illustration of the law of unintended consequences: past eras' slow-moving mathematical activity could self-correct over time, but that correction mechanism may break down under AI-generated volume.

The mitigation the authors propose: thorough vetting of provenance for cited information, even (especially) when that information comes from authoritative-looking AI sources. This places additional epistemic burden on researchers at exactly the moment when AI tools promise to reduce that burden.

## Key Points

- Circular citation loops form when AI tools treat AI-generated summaries as authoritative sources
- Term coined by Randall Munroe (xkcd #978, 2011) for Wikipedia citation cycles
- Can occur without malicious intent through interaction of legitimate activities
- Example: Tao's open problem site summaries became sources for the very AI tools they were meant to augment
- Related to "AI model collapse" from recursive training on generated data
- Erodes provenance and makes human vs. AI discoveries harder to distinguish
- Mitigation requires thorough vetting of information provenance
- Traditional self-correcting mechanisms (peer review, consensus) may not scale to AI-generated volume

## Related Concepts

- [Faustian Bargain of AI](faustian-bargain-of-ai.md) - The broader tradeoffs that citogenesis illustrates
- [AI and Mathematical Proof](ai-and-mathematical-proof.md) - How citation loops interact with proof validation

## Sources

- raw/20260420-arxivorg-html-260326524v1.md - Klowden and Tao on citogenesis in AI-augmented research (Section 4.8)
