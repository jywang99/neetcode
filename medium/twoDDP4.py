from typing import List


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


class CoinChange2:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        cache = { (len(coins), 0): 1 }

        def recurse(i: int, amt: int) -> int:
            k = (i, amt)
            if k in cache:
                return cache[k]
            if i >= len(coins):
                return 0

            rs = 0
            coin = coins[i]
            if amt - coin >= 0:
                rs += recurse(i, amt - coin)
            rs += recurse(i+1, amt)

            cache[k] = rs
            return rs

        return recurse(0, amount)


class FindTargetSumWays:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def recurse(i: int, t: int) -> int:
            if i == len(nums):
                return 1 if t == 0 else 0
            k = (i, t)
            if k in cache:
                return cache[k]

            n = nums[i]
            rs = recurse(i+1, t-n) + recurse(i+1, t+n)
            cache[k] = rs
            return rs

        return recurse(0, target)


class InterleavingString:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {}

        def recurse(i: int, j: int, k: int) -> bool:
            if k == len(s3):
                return i == len(s1) and j == len(s2)
            ck = (i, j)
            if ck in cache:
                return cache[ck]

            rs = False
            if i < len(s1) and s1[i] == s3[k]:
                rs = recurse(i+1, j, k+1)
            if not rs and j < len(s2) and s2[j] == s3[k]:
                rs = recurse(i, j+1, k+1)

            cache[ck] = rs
            return rs

        return recurse(0, 0, 0)

