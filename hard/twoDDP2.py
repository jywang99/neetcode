from typing import List


class LongestIncreasingPath:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        rows, cols = len(matrix), len(matrix[0])

        cache = {}
        def recurse(r: int, c: int, prev: int) -> int:
            if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] <= prev:
                return 0
            ck = (r, c)
            if ck in cache:
                return cache[ck]
            rs = 0
            for dr, dc in dirs:
                rs = max(rs, recurse(r+dr, c+dc, matrix[r][c]))
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
        cache = {}

        def recurse(l: int, r: int) -> int:
            if l > r:
                return 0
            if (l, r) in cache:
                return cache[(l, r)]

            rs = 0
            for i in range(l, r+1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += recurse(l, i-1) + recurse(i+1, r)
                rs = max(rs, coins)

            cache[(l, r)] = rs
            return rs

        return recurse(1, len(nums)-2)


class RegularExpressionMatching:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def recurse(i: int, j: int) -> bool:
            if j == len(p):
                return i == len(s)
            if (i, j) in cache:
                return cache[(i, j)]

            ok = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j+1 < len(p) and p[j+1] == "*":
                cache[(i, j)] = recurse(i, j+2) or ok and recurse(i+1, j)
                return cache[(i, j)]

            if ok:
                cache[(i, j)] = recurse(i+1, j+1)
                return cache[(i, j)]

            cache[(i, j)] = False
            return False

        return recurse(0, 0)

