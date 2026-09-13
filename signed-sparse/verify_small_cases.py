"""Independent finite checks of the signed sparse charge-shift theorem."""

from itertools import combinations, combinations_with_replacement, product
from math import comb
import json


def is_bs(residues, modulus, sparsity):
    seen = set()
    for terms in combinations_with_replacement(residues, sparsity):
        value = sum(terms) % modulus
        if value in seen:
            return False
        seen.add(value)
    return True


def signed_inputs(m, sparsity):
    for r in range(min(m, sparsity) + 1):
        for support in combinations(range(m), r):
            for signs in product((-1, 1), repeat=r):
                yield tuple(zip(support, signs))


def check(residues, modulus, sparsity):
    if not is_bs(residues, modulus, sparsity):
        raise ValueError('The supplied residues are not a cyclic B_s set')
    shift = 2 * sparsity * (modulus - 1) + 1
    weights = [shift + a for a in residues]
    values = {}
    for state in signed_inputs(len(weights), sparsity):
        value = sum(weights[i] * sign for i, sign in state)
        if value in values:
            raise AssertionError((residues, modulus, sparsity, values[value], state))
        values[value] = state
    expected = sum(2**r * comb(len(weights), r)
                   for r in range(min(len(weights), sparsity) + 1))
    if len(values) != expected or expected > 2 * sparsity * max(weights) + 1:
        raise AssertionError('State count or counting lower bound failed')
    return len(values)


def main():
    cases = states = rejected = 0
    by_s = {}
    for s in (1, 2, 3):
        accepted = 0
        for n in range(2, 12):
            for m in range(1, min(4, n) + 1):
                for a in combinations(range(n), m):
                    if not is_bs(a, n, s):
                        rejected += 1
                        continue
                    states += check(a, n, s)
                    cases += 1
                    accepted += 1
        by_s[str(s)] = accepted

    # A modular B_2 set alone need not encode signed sparse vectors:
    # 1 = -1 + 2 for two distinct permitted states.
    if not is_bs((1, 2), 7, 2):
        raise AssertionError('Negative-control premise failed')
    if 1 != -1 + 2:
        raise AssertionError('Negative-control collision failed')
    negative_control_shifted_count = check((1, 2), 7, 2)

    # Search independently for a four-element B_3 example modulo 40.
    example = next((0,) + tail for tail in combinations(range(1, 40), 3)
                   if is_bs((0,) + tail, 40, 3))
    example_count = check(example, 40, 3)
    print(json.dumps({
        'result': 'PASS',
        'scope': 'Finite independent replay; the all-parameter proof is in THEOREM.md',
        'exhaustive_ranges': {'N': [2, 11], 'm': '1..min(4,N)', 's': [1, 2, 3]},
        'cyclic_bs_sets_checked': cases,
        'signed_states_checked': states,
        'accepted_sets_by_s': by_s,
        'non_bs_sets_rejected': rejected,
        'negative_control': {'unshifted_collision': '1 = -1 + 2',
                             'shifted_distinct_states': negative_control_shifted_count},
        'additional_example': {'N': 40, 's': 3, 'residues': example,
                               'distinct_signed_states': example_count},
    }, indent=2))


if __name__ == '__main__':
    main()
