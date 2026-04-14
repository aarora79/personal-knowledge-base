---
title: Quantized Johnson-Lindenstrauss Transform
created: 2026-04-14
updated: 2026-04-14
sources: [raw/20260414-arxivorg-pdf-250419874.md]
related: [turboquant](turboquant.md), [random-rotation-quantization](random-rotation-quantization.md), [vector-quantization-theory](vector-quantization-theory.md)
tags: [qjl, johnson-lindenstrauss, inner-product, unbiased-estimation, 1-bit-quantization, sketching]
---

# Quantized Johnson-Lindenstrauss Transform

The Quantized Johnson-Lindenstrauss (QJL) transform is a 1-bit vector quantization method based on sketching techniques that provides unbiased estimates for inner product queries. Developed by Zandieh et al. (2024), QJL is a data-oblivious quantizer that compresses each coordinate to a single bit while maintaining unbiased inner product estimation -- a property that MSE-optimal quantizers cannot guarantee.

The QJL map Q_qjl: R^d -> {-1, +1}^d is defined as Q_qjl(x) = sign(S * x), where S is a d x d random matrix with i.i.d. standard Gaussian entries and the sign function is applied entry-wise. The dequantization map is Q_qjl^-1(z) = sqrt(pi/2) / d * S^T * z. The key properties are:

- **Unbiasedness**: E[<y, Q_qjl^-1(Q_qjl(x))>] = <y, x> for any vectors x on the unit sphere and any y.
- **Variance bound**: Var(<y, Q_qjl^-1(Q_qjl(x))>) <= pi/(2d) * ||y||^2, meaning the estimation error decreases with dimension d.

The unbiasedness property is critical because TurboQuant_mse (the MSE-optimal quantizer) introduces multiplicative bias in inner product estimation. At 1-bit, TurboQuant_mse has a bias factor of 2/pi (approximately 0.64), meaning inner products are systematically underestimated. This bias diminishes at higher bit-widths but does not disappear.

TurboQuant_prod addresses this by composing TurboQuant_mse with QJL in a two-stage algorithm: first apply TurboQuant_mse at bit-width b-1 to minimize the L2 norm of the residual, then apply QJL (1-bit per coordinate) to the residual vector. The composition works because: (1) TurboQuant_mse minimizes the residual magnitude, giving QJL a small-norm input, and (2) QJL's unbiasedness corrects the inner product bias from the first stage. The total bit budget remains b per coordinate.

The proof of unbiasedness in the composed system uses the law of total expectation conditioned on the MSE quantizer output, combined with QJL's standalone unbiasedness property. The inner product distortion of the composed system is bounded by sqrt(3*pi^2) * ||y||^2 / (d * 4^b), achieving near-optimal rates.

## Key Points

- QJL compresses each coordinate to 1 bit: Q_qjl(x) = sign(S * x) with Gaussian random matrix S
- Provides unbiased inner product estimates, unlike MSE-optimal quantizers
- Variance decreases as pi/(2d) * ||y||^2, improving with dimension
- MSE-optimal quantizers have multiplicative inner product bias (2/pi at 1-bit)
- TurboQuant_prod = TurboQuant_mse(b-1 bits) + QJL(1 bit on residual)
- The composition maintains unbiasedness while achieving near-optimal distortion
- Data-oblivious: requires no preprocessing or adaptation to input data

## Related Concepts

- [TurboQuant](turboquant.md) - Uses QJL as the second stage of its inner product-optimized variant
- [Random Rotation Quantization](random-rotation-quantization.md) - First stage that minimizes residual for QJL input
- [Vector Quantization Theory](vector-quantization-theory.md) - Theoretical framework for distortion bounds

## Sources

- raw/20260414-arxivorg-pdf-250419874.md - QJL definition (Definition 1), unbiasedness and variance proofs (Lemma 4), and composition with TurboQuant_mse (Theorem 2)
