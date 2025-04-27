from typing import List


class UniquePaths:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        cache[(m-1, n-1)] = 1

        def recurse(i: int, j: int) -> int:
            if (i, j) in cache:
                return cache[(i, j)]
            if i == m or j == n:
                return 0
            cache[(i, j)] = recurse(i+1, j) + recurse(i, j+1)
            return cache[(i, j)]
        
        return recurse(0, 0)


class CommonSubsequence:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}

        def recurse(i: int, j: int) -> int:
            if (i, j) in cache:
                return cache[(i, j)]
            if i == len(text1) or j == len(text2):
                return 0
            rs = 0
            if text1[i] == text2[j]:
                rs = 1 + recurse(i+1, j+1)
            else:
                rs = max(recurse(i+1, j), recurse(i, j+1))
            cache[(i, j)] = rs
            return rs

        return recurse(0, 0)



class MaxProfit:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def recurse(i: int, buy: bool) -> int:
            if (i, buy) in cache:
                return cache[(i, buy)]
            if i >= len(prices):
                return 0

            rs = recurse(i+1, buy)
            if buy:
                rs = max(rs, recurse(i+1, False) - prices[i])
            else:
                rs = max(rs, recurse(i+2, True) + prices[i])

            cache[(i, buy)] = rs
            return rs

        return recurse(0, True)


class CoinChange2:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = { (len(coins)-1, 0): 1 }
        coins.sort()

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

            cache[(i, amt)] = rs
            return rs

        return recurse(0, amount)


class TargetSumWays:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = { (len(nums), 0): 1 }

        def recurse(i: int, t: int) -> int:
            k = (i, t)
            if k in cache:
                return cache[k]
            if i >= len(nums):
                return 0

            cache[k] = recurse(i+1, t-nums[i]) + recurse(i+1, t+nums[i])
            return cache[k]

        return recurse(0, target)


class InterleavingStrings:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        cache = {}
        def recurse(i: int, j: int, k: int) -> bool:
            if k == len(s3):
                return i == len(s1) and j == len(s2)
            if (i, j) in cache:
                return cache[(i, j)]

            rs = False
            if i < len(s1) and s1[i] == s3[k]:
                rs = recurse(i+1, j, k+1)
            if not rs and j < len(s2) and s2[j] == s3[k]:
                rs = recurse(i, j+1, k+1)

            cache[(i, j)] = rs
            return rs

        return recurse(0, 0, 0)

