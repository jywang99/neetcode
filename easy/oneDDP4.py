from typing import List


class MinCostClimbingStairs:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * len(cost)
        def recurse(i: int) -> int:
            if i >= len(cost):
                return 0
            if cache[i] == -1:
                cache[i] = cost[i] + min(recurse(i+1), recurse(i+2))
            return cache[i]
        return min(recurse(0), recurse(1))
        

class ClimbStairs:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def recurse(i: int) -> int:
            if i >= n:
                return i == n
            if cache[i] == -1:
                cache[i] = recurse(i+1) + recurse(i+2)
            return cache[i]
        return recurse(0)


class LongestPalindrome:
    def longestPalindrome(self, s: str) -> str:
        mlen, pal = 0, ""

        def update(i: int, j: int):
            nonlocal mlen, pal
            while i>=0 and j<len(s) and s[i] == s[j]:
                l = j - i + 1
                if l > mlen:
                    mlen = l
                    pal = s[i:j+1]
                i, j = i-1, j+1

        for i in range(len(s)):
            update(i, i)
            if i+1 < len(s):
                update(i, i+1)

        return pal

