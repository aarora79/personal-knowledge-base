---
title: KV Cache Quantization
created: 2026-04-14
updated: 2026-04-14
sources: [raw/20260414-arxivorg-pdf-250419874.md]
related: [turboquant](turboquant.md), [vector-quantization-theory](vector-quantization-theory.md), [random-rotation-quantization](random-rotation-quantization.md)
tags: [kv-cache, quantization, llm-inference, transformer, memory-optimization, long-context]
---

# KV Cache Quantization

KV cache quantization is the compression of key and value embedding vectors stored during autoregressive inference in decoder-based transformer models. During text generation, each previously generated token's key and value vectors must be retained in the KV cache for attention computation. The cache size scales linearly with both model size (number of layers and attention heads) and context length, creating a significant memory bottleneck that limits the maximum context length and increases inference latency.

The challenge is to reduce the KV cache size while preserving the Euclidean structure of the embedding vectors -- specifically their inner products and distances -- since attention computation relies on dot products between query vectors and cached key vectors. This makes it a vector quantization problem where the distortion metric must account for inner product preservation, not merely reconstruction error.

Several approaches exist for KV cache compression: architectural modifications that restructure the transformer to store fewer key-value pairs, token pruning/eviction methods that discard less critical tokens (e.g., SnapKV, PyramidKV), and direct quantization of the KV vectors. Among quantization approaches, offline methods like KIVI use scalar quantization without formal distortion guarantees, while online methods like PolarQuant and TurboQuant provide theoretical bounds on compression quality.

TurboQuant demonstrates that 3.5-bit KV cache quantization achieves absolute quality neutrality with full-precision inference on the needle-in-a-haystack benchmark (perfect retrieval up to 104k tokens) and LongBench tasks. At 2.5 bits, performance degrades only marginally. The approach handles outlier channels by splitting them into two groups and applying independent TurboQuant instances with different bit precisions (e.g., 3 bits for 32 outlier channels, 2 bits for 96 regular channels yields 2.5 effective bits). Notably, TurboQuant quantizes even during streaming generation, unlike KIVI and PolarQuant which leave generated tokens unquantized.

## Key Points

- KV cache size scales with model size x context length, creating the primary memory bottleneck in long-context LLM inference
- Inner product preservation is essential because attention relies on key-query dot products
- Online (data-oblivious) quantization is required since KV vectors arrive during streaming inference
- TurboQuant achieves quality neutrality at 3.5 bits (>4.5x compression)
- Outlier channels handled by split quantization with different bit precisions per group
- Competing approaches include token-level pruning (SnapKV, PyramidKV) and scalar quantization (KIVI)
- Evaluated on needle-in-a-haystack (up to 104k tokens) and LongBench with Llama-3.1-8B and Ministral-7B

## Related Concepts

- [TurboQuant](turboquant.md) - The near-optimal online quantization algorithm applied to KV cache compression
- [Vector Quantization Theory](vector-quantization-theory.md) - The theoretical framework underlying KV cache quantization
- [Random Rotation Quantization](random-rotation-quantization.md) - The core technique enabling efficient coordinate-wise compression

## Sources

- raw/20260414-arxivorg-pdf-250419874.md - KV cache quantization as a primary application of TurboQuant, with experimental results on needle-in-a-haystack and LongBench benchmarks
