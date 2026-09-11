# No fixed two-digit alphabet is Sidon in positional notation

**Author:** Jared Wilder  
**Public promotion:** 2026-09-11

## Theorem

Fix an integer base `B>=2`. Let `a<b` be two valid digits. Then the four distinct two-digit words

`aa`, `ab`, `ba`, `bb`

viewed as integers in base `B` satisfy

\[
(aB+a)+(bB+b)=(aB+b)+(bB+a)=(a+b)(B+1).
\]

Consequently, **no fixed digit alphabet containing two or more digits can be a Sidon set of two-digit positional words in any base.**

## Proof

The displayed identity is immediate by collecting the coefficients of `B` and the units digit. Because `a<b`, the four words `aa,ab,ba,bb` are distinct. Thus two distinct unordered pairs have the same sum, which violates the Sidon property.

The obstruction already occurs inside every two-element subalphabet, so enlarging the digit alphabet cannot repair it.

## Why this belongs here

This is the negative counterpart to the repository's sharp injective positional-encoding results. Large bases can make coefficient vectors uniquely decodable under bounded signed coefficients, but **a repeated fixed digit alphabet has an unavoidable additive rectangle**:

\[
aa+bb=ab+ba.
\]

So any attempt to obtain Sidon behavior from all two-digit words over a fixed alphabet fails for structural reasons, independently of how large the base is.

## Verification history

The release-day archive audit independently checked the identity for every base `2..15` and every two-digit subalphabet. The algebra above is the general proof; the finite check is regression evidence only.

No historical-priority claim is attached to this elementary identity.
