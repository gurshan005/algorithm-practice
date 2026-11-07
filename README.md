# Algorithm practice

Three Python implementations from my algorithm-design practice, with exhaustive checks on small inputs.

| Function | Result | Time | Extra space |
| --- | --- | --- | --- |
| `interval_sort(intervals)` | A maximum-size set of non-overlapping intervals, chosen by earliest finish. Intervals have positive duration and can touch at an endpoint. | O(n log n) | O(n) |
| `lcs(x, y)` | Length of a longest common subsequence of two sequences. | O(mn) | O(mn) |
| `lis(arr)` | Length of a longest strictly increasing subsequence. Duplicate values cannot extend it. | O(n²) | O(n) |

```python
from algorithms import interval_sort, lcs, lis

assert interval_sort([(0, 4), (1, 2), (2, 4)]) == [(1, 2), (2, 4)]
assert lcs("CABLE", "TABLE") == 4
assert lis([3, 1, 2, 2, 4]) == 3
```

Run `python3 -m unittest -v` from this directory. The tests compare each algorithm with an exhaustive search across 64 interval sets, 961 sequence pairs, and 364 integer sequences.
