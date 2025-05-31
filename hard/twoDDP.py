from typing import List


class LongestIncreasingPath:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))

        cache = {}
        def recurse(r: int, c: int, prev: int) -> int:
            if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] <= prev:
                return 0
            ck = (r, c)
            if ck in cache:
                return cache[ck]

            v = matrix[r][c]
            rs = 0
            for dr, dc in dirs:
                rs = max(rs, recurse(r+dr, c+dc, v))
            rs += 1
            cache[ck] = rs
            return rs
        
        rs = 0
        for r in range(rows):
            for c in range(cols):
                rs = max(rs, recurse(r, c, -1))
        return rs
        

class DistinctSubsequences:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        def recurse(i: int, j: int) -> int:
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            ck = (i, j)
            if ck in cache:
                return cache[ck]

            rs = recurse(i+1, j)
            if s[i] == t[j]:
                rs += recurse(i+1, j+1)

            cache[ck] = rs
            return rs

        return recurse(0, 0)


class BurstBalloons:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}

        def recurse(l: int, r: int) -> int:
            if l > r:
                return 0
            ck = (l, r)
            if ck in dp:
                return dp[ck]

            rs = 0
            for i in range(l, r+1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += recurse(l, i-1) + recurse(i+1, r)
                rs = max(rs, coins)
            dp[ck] = rs

            return dp[ck]
        
        return recurse(1, len(nums)-2)


class RegularExpressionMatching:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        m, n = len(s), len(p)

        def recurse(i: int, j: int) -> bool:
            if j == n:
                return i == m
            if (i, j) in cache:
                return cache[(i, j)]

            ok = i < m and (s[i] == p[j] or p[j] == ".")
            if j+1 < n and p[j+1] == "*":
                cache[(i, j)] = recurse(i, j+2) or ok and recurse(i+1, j)
                return cache[(i, j)]

            if ok:
                cache[(i, j)] = recurse(i+1, j+1)
                return cache[(i, j)]

            cache[(i, j)] = False
            return False

        return recurse(0, 0)
        
