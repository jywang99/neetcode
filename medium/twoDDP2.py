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

