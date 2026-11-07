import unittest
from itertools import combinations, product

from algorithms import interval_sort, lcs, lis


def subsequences(values):
    for length in range(len(values) + 1):
        yield from combinations(values, length)


class AlgorithmTests(unittest.TestCase):
    def test_interval_scheduling_maximizes_count(self):
        candidates = ((0, 4), (1, 2), (2, 4), (-1, 1), (1, 3), (4, 5))
        for sample in subsequences(candidates):
            def fits(intervals):
                ordered = sorted(intervals)
                return all(left[1] <= right[0] for left, right in zip(ordered, ordered[1:]))

            selected = interval_sort(sample)
            expected = max(len(group) for group in subsequences(sample) if fits(group))
            self.assertTrue(fits(selected))
            self.assertTrue(all(interval in sample for interval in selected))
            self.assertEqual(len(selected), expected)

    def test_lcs_matches_shared_subsequences(self):
        strings = [
            "".join(chars)
            for length in range(5)
            for chars in product("ab", repeat=length)
        ]
        all_subseqs = {word: set(subsequences(word)) for word in strings}
        for left, right in product(strings, repeat=2):
            expected = max(map(len, all_subseqs[left] & all_subseqs[right]))
            self.assertEqual(lcs(left, right), expected)

    def test_lis_matches_strictly_increasing_subsequences(self):
        for length in range(6):
            for values in product(range(3), repeat=length):
                expected = max(
                    len(group)
                    for group in subsequences(values)
                    if all(a < b for a, b in zip(group, group[1:]))
                )
                self.assertEqual(lis(values), expected)


if __name__ == "__main__":
    unittest.main()
