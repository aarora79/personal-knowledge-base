---
title: Product Quantization for Nearest Neighbor Search
created: 2026-04-14
updated: 2026-04-14
sources: [raw/20260414-arxivorg-pdf-250419874.md]
related: [turboquant](turboquant.md), [vector-quantization-theory](vector-quantization-theory.md), [kv-cache-quantization](kv-cache-quantization.md)
tags: [product-quantization, nearest-neighbor-search, vector-database, retrieval, indexing, rag]
---

# Product Quantization for Nearest Neighbor Search

Product quantization (PQ) is a family of vector compression techniques used in nearest neighbor (NN) search to reduce the memory footprint of high-dimensional vector databases while enabling efficient approximate inner product computation with query vectors. PQ is a cornerstone technique in vector databases that underpin retrieval-augmented generation (RAG) and information retrieval systems.

Traditional PQ algorithms divide each high-dimensional vector into subvectors, then learn a codebook for each subspace using k-means clustering during an indexing phase. At query time, inner products between the query and database vectors are approximated using precomputed distances to codebook centroids. This approach is data-dependent: it requires heavy preprocessing on the dataset to learn codebooks, and the codebook size grows exponentially with bit-width, creating storage overhead.

RabitQ, a more recent approach, eliminates k-means preprocessing by projecting a uniform grid onto the unit sphere and using binary search to find the nearest projection. While removing the codebook learning step, RabitQ's grid projection and binary search are computationally slow and lack vectorization, making them inefficient on GPU accelerators.

TurboQuant provides a compelling alternative: its data-oblivious design requires no indexing-phase preprocessing (no k-means, no grid projection), reducing indexing time to virtually zero. Experimental results on DBpedia (1536-d and 3072-d OpenAI embeddings) and GloVe (200-d) datasets show that TurboQuant consistently outperforms PQ in recall@k while being orders of magnitude faster at indexing. At 4-bit quantization, TurboQuant's indexing time is ~0.001s compared to 37s for PQ and 597s for RabitQ on 200-d data, with the gap widening at higher dimensions (0.002s vs. 494s vs. 3957s at 3072-d).

The key trade-off: PQ can adapt to data distribution via learned codebooks, potentially achieving better compression for well-clustered data. But TurboQuant's data-oblivious approach provides theoretical distortion guarantees that hold for any input distribution, and its lack of preprocessing makes it the only viable option for dynamic datasets where vectors are added in real-time.

## Key Points

- PQ is the standard compression technique for vector databases used in RAG and information retrieval
- Traditional PQ requires k-means codebook learning -- offline, data-dependent, and slow
- Codebook size grows exponentially with bit-width, adding storage overhead
- RabitQ eliminates k-means but uses slow grid projection unsuitable for GPUs
- TurboQuant reduces indexing time by 5-6 orders of magnitude vs. PQ and RabitQ
- TurboQuant outperforms PQ in recall@k across multiple datasets and dimensions
- Data-oblivious design enables real-time indexing of dynamic datasets
- Evaluated on DBpedia (OpenAI embeddings, 1536-d and 3072-d) and GloVe (200-d)

## Related Concepts

- [TurboQuant](turboquant.md) - The online quantizer that outperforms PQ in both recall and indexing speed
- [Vector Quantization Theory](vector-quantization-theory.md) - Theoretical foundations shared by PQ and TurboQuant
- [KV Cache Quantization](kv-cache-quantization.md) - A parallel application domain for the same quantization techniques

## Sources

- raw/20260414-arxivorg-pdf-250419874.md - Comparison of TurboQuant vs. PQ and RabitQ on recall@k and indexing time across multiple datasets (Section 4.4, Table 2)
