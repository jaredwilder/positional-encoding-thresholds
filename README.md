# Sharp positional-encoding thresholds

**A 79-card theorem bank on exact thresholds for positional and sparse integer encoding, with matched upper/lower bounds, independent exhaustive checks of the two central cutoff theorems, and a universal additive obstruction for fixed digit alphabets. 63 cards contain proof bodies.**

Author: Jared Wilder. First public timestamp: 2026-09-11.

The core results are exact finite arithmetic statements. Much of the basic positional material is classical or rediscovered; historical novelty is therefore treated separately from the mathematical sharpness of the thresholds.

## Two exact cutoff theorems

For

`Phi_B(r)=sum_j r_j B^j`

on integer vectors `r in [-A,A]^m` with `m>=2`:

### Injectivity

`Phi_B` is injective on the full cube **if and only if `B>2A`**.

Hence the least integer base is exactly

`2A+1`.

### Zero detection

`Phi_B(r)=0` implies `r=0` for every vector in the cube **if and only if `B>A`**.

Both thresholds were independently exhaustively checked during the release for `A in {1,2,3}`, `m in {2,3}`, and bases straddling the predicted boundary: **46 cases, zero mismatches**.

## A universal Sidon obstruction

There is also an exact negative theorem that no choice of large base can evade. For any base `B>=2` and any two digits `a<b`,

`(aB+a)+(bB+b)=(aB+b)+(bB+a)`.

Thus the four distinct words `aa,ab,ba,bb` contain an additive collision. **No fixed digit alphabet with at least two digits can make all two-digit positional words Sidon in any base.**

The complete statement and proof are in [`SIDON-DIGIT-OBSTRUCTION.md`](SIDON-DIGIT-OBSTRUCTION.md).

This sharply separates two phenomena: sufficiently large positional weights give unique decoding of bounded coefficient vectors, while unrestricted two-digit word families over a repeated alphabet always contain an additive rectangle.

## Optimal coefficient size

If an integer linear scalarization

`x -> w.x`

is injective on `[-A,A]^m`, then counting possible outputs gives

`||w||_1 >= ((2A+1)^m - 1)/(2A)`.

Balanced positional weights

`(1,q,...,q^(m-1))`, with `q=2A+1`,

attain the minimum possible output span and coefficient `l1` norm on the full cube.

Thus the elementary counting lower bound is paired with an explicit attaining construction.

## Sparse encoding

The bank also records higher-dimensional sparse analogues:

- any positive-weight scalar encoding of every vector in `{-1,0,1}^m` with support at most two requires `max_i w_i >= m^2/2`;
- the optimal largest-weight growth for support two is `Theta(m^2)`;
- more generally `W(m,s)=Theta_s(m^s)` for fixed sparsity `s`;
- moment encoding has an explicit sufficient base threshold `B>4Asm^(2s-1)`;
- over a finite field, if `p>max(m,2A)`, the first `2s` Vandermonde syndromes determine every `s`-sparse integer vector in the stated range.

The sparse exponent closures and matched growth bounds are the most structurally interesting part of the bank beyond the elementary full-cube threshold.

## Relationship to the Lean finisher work

A related **63-theorem finisher ledger** uses the two cutoff lemmas as ingredients and is published under

`jaredwilder/lean-contributions/humu-finisher/ledger`.

This repository is the ordinary mathematical home for the encoding thresholds; the Lean project records a separate formal/application layer.

## Evidence and literature status

Of the 79 cards, 63 contain proof bodies. The two central cutoff theorems also have independent finite boundary checks as described above. The Sidon obstruction has a one-line general proof and was additionally regression-checked across small bases during the release audit.

Several positional-representation statements are classical or elementary rediscoveries, and this repository makes no blanket novelty claim for them. That literature status does not affect the exactness of the statements or the usefulness of the sharp thresholds.

No blanket proof-assistant certification is claimed for this theorem bank.

## License

Apache-2.0.
