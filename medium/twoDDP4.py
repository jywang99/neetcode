class UniquePaths:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = { (m-1, n-1): 1 }

        def recurse(i: int, j: int) -> int:
            k = (i, j)
            if k in cache:
                return cache[k]
            if i >= m or j >= n:
                return 0

            rs = recurse(i+1, j) + recurse(i, j+1)
            cache[k] = rs
            return rs

        return recurse(0, 0)


class CommonSubsequence:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = { (len(text1), len(text2)): 0 }

        def recurse(i: int, j: int) -> int:
            if i == len(text1) or j == len(text2):
                return 0
            k = (i, j)
            if k in cache:
                return cache[k]

            rs = 0
            if text1[i] == text2[j]:
                rs = 1 + recurse(i+1, j+1)
            rs = max(rs, recurse(i+1, j), recurse(i, j+1))

            cache[k] = rs
            return rs

        return recurse(0, 0)

