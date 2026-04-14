---
title: TurboQuant
created: 2026-04-14
updated: 2026-04-14
sources: [raw/20260414-arxivorg-pdf-250419874.md]
related: [kv-cache-quantization](kv-cache-quantization.md), [random-rotation-quantization](random-rotation-quantization.md), [quantized-johnson-lindenstrauss-transform](quantized-johnson-lindenstrauss-transform.md), [vector-quantization-theory](vector-quantization-theory.md), [product-quantization-for-nearest-neighbor-search](product-quantization-for-nearest-neighbor-search.md)
tags: [vector-quantization, turboquant, kv-cache, llm-inference, near-optimal-distortion, online-quantization]
---

# TurboQuant

TurboQuant is a data-oblivious vector quantization algorithm developed by researchers at Google Research, New York University, and Google DeepMind that achieves near-optimal distortion rates for both mean-squared error (MSE) and inner product preservation across all bit-widths and dimensions. Unlike offline methods requiring data-specific calibration, TurboQuant operates online (without preprocessing), making it suitable for real-time applications like KV cache quantization in large language models.

The algorithm comprises two variants. **TurboQuant_mse** minimizes reconstruction MSE through a random rotation followed by optimal scalar quantization per coordinate. The random rotation induces a Beta distribution on each coordinate (converging to Gaussian in high dimensions), and crucially, makes distinct coordinates nearly independent. This independence allows applying precomputed Lloyd-Max quantizers to each coordinate independently while still achieving near-optimal vector-level distortion. The MSE distortion bound is sqrt(3*pi)/2 * 4^(-b) for bit-width b, within a constant factor (~2.7x) of the information-theoretic lower bound proved via Shannon's source coding theory and Yao's minimax principle.

**TurboQuant_prod** addresses the bias problem: MSE-optimal quantizers produce biased inner product estimates (e.g., a multiplicative bias of 2/pi at 1-bit). The solution is a two-stage algorithm that first applies TurboQuant_mse with bit-width b-1, then applies a 1-bit Quantized Johnson-Lindenstrauss (QJL) transform on the residual. This composition yields unbiased inner product estimation with near-optimal distortion.

Experimentally, TurboQuant achieves absolute quality neutrality with 3.5 bits per channel on KV cache quantization (matching full-precision performance on needle-in-a-haystack and LongBench tasks), marginal degradation at 2.5 bits, and outperforms product quantization in nearest neighbor search while reducing indexing time to virtually zero (0.001s vs. hundreds of seconds).

## Key Points

- Data-oblivious (online) algorithm: no preprocessing, calibration, or codebook learning required
- Two variants: TurboQuant_mse for reconstruction and TurboQuant_prod for unbiased inner products
- Near-optimal distortion within ~2.7x of the information-theoretic lower bound
- Accelerator-friendly: fully vectorizable, suitable for GPU execution
- Achieves 4-5x KV cache compression with no quality loss at 3.5 bits per channel
- Indexing time in NN search reduced to ~0.001s vs. 37-597s for PQ and RabitQ
- Precomputed codebooks for practical bit-widths enable efficient repeated invocations

## Related Concepts

- [KV Cache Quantization](kv-cache-quantization.md) - Primary application: compressing key-value caches in LLM inference
- [Random Rotation Quantization](random-rotation-quantization.md) - The core technique enabling coordinate-wise independence
- [Quantized Johnson-Lindenstrauss Transform](quantized-johnson-lindenstrauss-transform.md) - 1-bit residual quantizer providing unbiased inner products
- [Vector Quantization Theory](vector-quantization-theory.md) - Shannon's foundational framework for lossy compression
- [Product Quantization for Nearest Neighbor Search](product-quantization-for-nearest-neighbor-search.md) - Competing approach that TurboQuant outperforms

## Sources

- raw/20260414-arxivorg-pdf-250419874.md - Primary source: full algorithm description, theoretical analysis with distortion bounds and information-theoretic lower bounds, and experimental validation on KV cache and NN search tasks
