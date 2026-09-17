# Sharp positional-encoding thresholds

For

\[
\Phi_B(r)=\sum_j r_j B^j
\]

on bounded integer coefficient vectors, this repository gives exact base thresholds for injectivity and zero detection, together with sparse analogues and an additive obstruction for repeated digit alphabets.

## Exact full-cube thresholds

Let `r∈[-A,A]^m` with `m>=2`.

### Injectivity

\[
\boxed{\Phi_B\text{ is injective on }[-A,A]^m\iff B>2A.}
\]

Hence the least integer base giving unique encoding of the full cube is exactly

\[
\boxed{2A+1}.
\]

### Zero detection

\[
\boxed{\Phi_B(r)=0\Rightarrow r=0\text{ for all }r\in[-A,A]^m\iff B>A.}
\]

The boundary failures have explicit two-coordinate carry witnesses. Independent exhaustive checks over small `A`, dimensions, and bases straddling the cutoffs found zero mismatches.

## Optimal coefficient size

If an integer scalarization `x↦w·x` is injective on `[-A,A]^m`, counting outputs gives

\[
\|w\|_1\ge \frac{(2A+1)^m-1}{2A}.
\]

Balanced positional weights

\[
(1,q,\ldots,q^{m-1}),\qquad q=2A+1,
\]

attain the minimum possible output span and `\ell_1` coefficient norm on the full cube.

## A universal two-digit Sidon obstruction

Large base does not cure every additive collision. For any `B>=2` and any two digits `a<b`,

\[
(aB+a)+(bB+b)=(aB+b)+(bB+a).
\]

Thus the four distinct two-digit words `aa,ab,ba,bb` always contain an additive rectangle. No fixed alphabet with at least two digits can make the complete family of two-digit positional words Sidon, regardless of the base.

See [`SIDON-DIGIT-OBSTRUCTION.md`](SIDON-DIGIT-OBSTRUCTION.md).

## Sparse encoding

The repository also develops sparse analogues:

- support-two signed encodings require largest weight `Ω(m²)` and admit `O(m²)` constructions;
- more generally, for fixed sparsity `s`, the optimal scale is

  \[
  \boxed{W(m,s)=\Theta_s(m^s)};
  \]

- moment encoding has an explicit sufficient base bound `B>4Asm^(2s-1)`;
- over a finite field with `p>max(m,2A)`, the first `2s` Vandermonde syndromes determine every `s`-sparse integer vector in the stated range.

The complete signed-sparse proof is in [`signed-sparse/THEOREM.md`](signed-sparse/THEOREM.md).

## Verification

The source collection contains 79 theorem cards, 63 with proof bodies. The two central full-cube thresholds and the Sidon obstruction also have independent finite regression checks.

Related Lean/application work lives in [`jaredwilder/lean-contributions/humu-finisher`](https://github.com/jaredwilder/lean-contributions/tree/main/humu-finisher).

Author: Jared Wilder. License: Apache-2.0.
