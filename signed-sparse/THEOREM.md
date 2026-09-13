# Optimal integer weights for signed sparse vectors

For fixed sparsity `s >= 1`, the smallest possible largest positive integer
weight that injectively encodes all signed `s`-sparse vectors in `m` coordinates
grows as **Theta_s(m^s)**. Both directions hold for all sufficiently large `m`.

This expands estate cards **SGN-04, SGN-05, SGN-06** into a complete argument.
The cyclic B_s construction used below is classical Bose–Chowla; historical
priority of the signed formulation is not asserted. The finite replay is a
separate check of small instances, not the proof of the asymptotic theorem.

## Precise statement

Let `D(m,s) = {x in {-1,0,1}^m : |supp(x)| <= s}`, and let `W(m,s)` be the
minimum of `max_i w_i` over positive integer weights for which
`x -> sum_i x_i w_i` is injective on `D(m,s)`. For integers `m >= s >= 1`,

```text
W(m,s) >= ceil((sum_{r=0}^s 2^r binom(m,r) - 1)/(2s)).
```

For `s=1`, exactly `W(m,1)=m`. For `s>=2`, choose the smallest power of two
`q >= m`. There exist weights with

```text
max_i w_i <= (2s+1)(q^s-2)+1 < (2s+1)(2m)^s.
```

Consequently `W(m,s)=Theta_s(m^s)` for each fixed positive `s`. The constants
may depend on `s`; the result does not assert optimal leading constants.
In particular, the signed support-three exponent is exactly three.

## Counting lower bound

There are `sum_{r=0}^s 2^r binom(m,r)` input vectors. If every weight is at
most `W`, each encoded integer lies in `[-sW,sW]`, containing `2sW+1`
integers. Injectivity gives the displayed lower bound. For fixed `s`, its
leading term is `2^(s-1)m^s/(s s!)`. When `s=1`, weights `1,...,m` encode
`0, +/-e_1,...,+/-e_m` distinctly and attain the lower bound.

## Charge shift lemma (SGN-04)

A cyclic **B_s set** modulo `N` is a set of distinct residues whose sums of
exactly `s` terms, **with repetition allowed**, determine their multisets
uniquely. Take representatives `a_1,...,a_m` in `[0,N-1]`. Set

```text
L = 2s(N-1)+1,       w_i = L+a_i.
```

Suppose two vectors `x,y` in `D(m,s)` have the same encoding. Then

```text
L sum_i (x_i-y_i) = -sum_i (x_i-y_i)a_i.
```

The absolute value on the right is at most `2s(N-1) < L`. The left side is
an integer multiple of `L`, so both sides vanish. In particular, the two
vectors have the same total signed coefficient (their charge).

Move positive terms of `x` and negative terms of `y` to one side, and the
remaining terms to the other. Equal charge makes their lengths equal,
say `k`. The combined length is `|supp(x)|+|supp(y)| <= 2s`, so `k<=s`.
An index can occur twice on a side, which is why repetitions matter.

The two length-`k` sums are congruent modulo `N`. If `k=0`, both vectors
are zero. Otherwise append the same `s-k` copies of any one `a_i` to
both sides. The B_s property makes the resulting multisets equal. Cancel
the padding and compare each index's multiplicity: `x_i-y_i=0` for every
`i`. This proves injectivity for every permitted `m,s,N`.

## Upper bound and classical input (SGN-05)

Bose–Chowla Theorem 1 supplies a cyclic B_s set of size `q` modulo
`N=q^s-1`, for a prime power `q` and `s>=2`. Any `m` of its elements retain
the B_s property. Applying the charge shift gives
`max w_i <= (2s+1)(N-1)+1`. Powers of two give `m<=q<2m`, proving the
upper bound stated above. Together with counting, this closes the exponent.

Reference: R. C. Bose and S. Chowla, *Theorems in the additive theory of
numbers*, Commentarii Mathematici Helvetici 37 (1962/63), 141–147,
[DOI](https://doi.org/10.1007/BF02566968). Theorem 1 is also available in the
[authors' 1960 report, printed page 2](https://www.cs.umd.edu/~gasarch/COURSES/858/S13/BoseChowla.pdf).

## Independent replay

Run `python signed-sparse/verify_small_cases.py` from the repository root.
It independently generates all signed inputs, tests the cyclic B_s
hypothesis, and checks injectivity of shifted weights for every eligible
small set in the specified exhaustive ranges. It also checks a larger
explicit example and an unshifted collision as a negative control.

The checker uses only Python's standard library. It does not certify all
parameters, optimal leading constants, a Lean formalization, or priority.
See `REPLAY-2026-09-13.json` for the exact checked ranges and counts.

## Source provenance

The recovered ZIP `THEOREM-RECIPE-FORGE-R1-2026-08-05.zip` contains
`THEOREM-BANK-PATCH.json` (4,212 bytes), SHA-256
`83ad9b331e5b9011f3309df3cb51c2828c5507211a2ed0faf775d2744e7e0f81`.
`source-cards.json` preserves the three selected mathematical objects with
that provenance; their status fields are original source labels. The
statements already appear in `cards/cards.jsonl`. This publication adds a
full proof and replay rather than counting them as new estate results.
