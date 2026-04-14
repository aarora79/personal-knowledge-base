---
title: Vector Quantization Theory
created: 2026-04-14
updated: 2026-04-14
sources: [raw/20260414-arxivorg-pdf-250419874.md]
related: [turboquant](turboquant.md), [random-rotation-quantization](random-rotation-quantization.md), [product-quantization-for-nearest-neighbor-search](product-quantization-for-nearest-neighbor-search.md)
tags: [vector-quantization, information-theory, shannon, distortion-rate, source-coding, lossy-compression]
---

# Vector Quantization Theory

Vector quantization (VQ) theory, rooted in Shannon's source coding work, addresses the fundamental problem of compressing high-dimensional Euclidean vectors by converting floating-point coordinates to low-bitwidth integers while minimizing distortion in geometric structure. The core objective is to design a quantization map Q: R^d -> {0,1}^B and a corresponding dequantization map Q^-1: {0,1}^B -> R^d that minimize expected distortion -- measured by mean-squared error (MSE) or inner product error -- for a given bit budget B = b*d, where b is the bits per coordinate.

Shannon's distortion-rate function establishes the information-theoretic lower bound on achievable distortion for any lossy compression scheme. The Shannon Lower Bound (SLB), derived from lossy source coding theory, states that for uniformly distributed random points on the unit hypersphere S^(d-1), the MSE distortion-rate function satisfies D(B) >= 2^(-2B/d), or equivalently D >= 1/4^b per coordinate. This bound uses Yao's minimax principle to relate worst-case randomized algorithms to optimal deterministic algorithms on random inputs, and the backward Gaussian test channel for the entropy calculation.

Key milestones in VQ theory include: Zador's 1963 high-resolution methods deriving limiting distortion-rate functions, Gersho's work on lattice vector quantization and high-resolution simplifications, and the Lloyd-Max algorithm for optimal scalar quantizer design. The Lloyd-Max algorithm solves a continuous 1-dimensional k-means problem, partitioning the input range into 2^b buckets with boundaries at midpoints between consecutive centroids, minimizing expected squared error under a known probability distribution.

The Panter-Dite high-resolution formula provides a distortion bound for fixed-rate scalar quantizers at higher bit-widths, yielding C(f_X, b) <= (1/12) * (integral of f_X(x)^(1/3) dx)^3 * 4^(-b). TurboQuant's distortion of sqrt(3*pi)/2 * 4^(-b) differs from the lower bound 1/4^b by a constant factor of approximately 2.7, with tighter constants at smaller bit-widths (factor ~1.45 at b=1).

## Key Points

- Shannon's source coding theory provides the information-theoretic lower bound on compression distortion
- The Shannon Lower Bound for unit hypersphere: D >= 1/4^b for bit-width b
- Proof technique combines Yao's minimax principle with Shannon's lossy source coding theorem
- Lloyd-Max algorithm yields optimal scalar quantizers for known distributions via continuous k-means
- Panter-Dite formula gives high-resolution distortion bounds for scalar quantizers
- TurboQuant achieves within ~2.7x of the information-theoretic optimum
- Online vs. offline distinction: online methods require no data-specific calibration

## Related Concepts

- [TurboQuant](turboquant.md) - Near-optimal vector quantizer that closely matches the theoretical lower bounds
- [Random Rotation Quantization](random-rotation-quantization.md) - Technique that reduces vector quantization to scalar quantization
- [Product Quantization for Nearest Neighbor Search](product-quantization-for-nearest-neighbor-search.md) - Applied VQ for nearest neighbor search

## Sources

- raw/20260414-arxivorg-pdf-250419874.md - Formal definition of VQ distortion measures, Shannon Lower Bound proof, Lloyd-Max codebook construction, and Panter-Dite formula application
