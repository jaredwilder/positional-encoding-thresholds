# positional-encoding-thresholds

**79 cards on sharp thresholds for positional and sparse integer encoding — matched upper and lower
bounds, with the two central thresholds re-verified exhaustively here. 63 carry a proof body.**

Author: Jared Wilder. First public timestamp: 2026-09-11.

**The bank labels most of this as rediscovery, and so does this page.** Several cards say outright:
*"Classical balanced positional representation fact; exact sharp statement is an important campaign
asset"* and *"Elementary/classical arithmetic; rediscovered and sharpened inside the campaign.
**Historical novelty not claimed.**"

What is worth having is that the statements are sharp, the bounds are matched, and the thresholds
are exact rather than asymptotic.

---

## The two sharp thresholds, verified here

Write `Φ_B(r) = Σ_j r_j B^j`.

**CF-02 — injectivity.** For `m ≥ 2`, `Φ_B` is injective on `[−A,A]^m ∩ ℤ^m` **iff `B > 2A`**. The
least integer base is therefore exactly **`2A + 1`**.

**CF-01 — zero detection.** `Φ_B(r) = 0 ⟹ r = 0` for all such `r` **iff `B > A`**.

Both re-verified by exhaustive enumeration on 2026-09-11 across `A ∈ {1,2,3}`, `m ∈ {2,3}`, and
bases straddling each threshold — **46 cases, zero mismatches.** In every case the property flips
exactly at the stated boundary, which is what makes these thresholds and not estimates.

## Matched bounds

**Lower bound.** If `x ↦ w·x` is injective on `[−A,A]^m`, then

```
‖w‖₁  ≥  ((2A+1)^m − 1) / (2A)
```

The proof is a counting argument: the cube holds `(2A+1)^m` points while every output lands in an
interval containing `2A‖w‖₁ + 1` integers.

**Matching upper bound.** The balanced positional weights `(1, q, …, q^{m−1})` with `q = 2A+1`
**attain** the minimum possible output span and coefficient `ℓ₁` norm among integer linear
scalarizations injective on the full cube.

Lower bound and attaining construction, which is the pairing that makes a bound worth stating.

## Sparse encoding exponents

- Any positive-weight scalar encoding of every `x ∈ {−1,0,1}^m` with support at most two requires
  `max_i w_i ≥ m²/2`.
- The optimal largest-weight growth is **`Θ(m²)`**.
- In general, `W(m,s) = Θ_s(m^s)`.
- Moment encoding admits the explicit threshold `B > 4Asm^{2s−1}`.
- Finite-field syndrome injectivity holds for `p > max(m, 2A)`: the first `2s` Vandermonde
  syndromes determine every `s`-sparse integer vector.

The `Θ_s(m^s)` exponent closure and the counting lower bounds are the parts least likely to be
folklore.

## Scope

These are exact finite statements about integer encodings. Nothing here is a result about an Erdős
problem, and nothing was run through a proof assistant. The cards' own novelty posture is
reproduced above and should be believed: **this is sharpened classical material, not new
mathematics.**

The related 63-theorem finisher ledger, which uses CF-01 and CF-02 as ingredients and ships a replay
with negative controls, is in
[lean-contributions](https://github.com/jaredwilder/lean-contributions/tree/main/humu-finisher/ledger).

## License

Apache-2.0.
