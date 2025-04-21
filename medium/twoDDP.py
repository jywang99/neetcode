class UniquePaths:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[-1] * n for _ in range(m)]
        cache[m-1][n-1] = 1

        def recurse(i: int, j: int) -> int:
            if i >= m or j >= n:
                return 0
            if cache[i][j] != -1:
                return cache[i][j]
            rs = recurse(i+1, j) + recurse(i, j+1)
            cache[i][j] = rs
            return rs

        return recurse(0, 0)


class LongestCommonSubsequence:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}

        def recurse(i: int, j: int) -> int:
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(text1) or j >= len(text2):
                return 0
            rs = 0
            if text1[i] == text2[j]:
                rs = 1 + recurse(i+1, j+1)
            else:
                rs = max(recurse(i, j+1), recurse(i+1, j))
            cache[(i, j)] = rs
            return rs

        return recurse(0, 0)

