"""Greedy interval scheduling and dynamic programming for subsequences."""


def interval_sort(intervals):
    """Select a maximum number of non-overlapping, positive-length intervals."""
    intervals = sorted(intervals, key=lambda x: x[1])
    selected = []
    last_end = float('-inf')
    for interval in intervals:
        start = interval[0]
        end = interval[1]
        if start >= last_end:
            selected.append(interval)
            last_end = end
    return selected


def lcs(x, y):
    """Return the length of a longest common subsequence of x and y."""
    m = len(x)
    n = len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


def lis(arr):
    """Return the length of a longest strictly increasing subsequence."""
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp, default=0)
