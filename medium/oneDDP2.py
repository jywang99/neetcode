from typing import List


class HouseRobbing:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)

        def maximize(i: int) -> int:
            if i >= len(nums):
                return 0
            if cache[i] == -1:
                cache[i] = max(nums[i] + maximize(i+2), maximize(i+1))
            return cache[i]
        
        return maximize(0)
        

class HouseRobbing2:
    def robLine(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)

        def recurse(i: int) -> int:
            if i >= len(nums):
                return 0
            if memo[i] == -1:
                memo[i] = max(nums[i] + recurse(i+2), recurse(i+1))
            return memo[i]
        
        return recurse(0)

    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.robLine(nums[1:]), self.robLine(nums[:-1]))


class LongestPalindrome:
    def longestPalindrome(self, s: str) -> str:
        rs = ""
        plen = 0

        def update(i: int, j: int):
            nonlocal rs, plen
            while i>=0 and j<len(s) and s[i] == s[j]:
                l = j - i + 1
                if l > plen:
                    rs = s[i:j+1]
                    plen = l
                i, j = i-1, j+1

        for i in range(len(s)):
            update(i, i)
            if i+1 < len(s):
                update(i, i+1)

        return rs


class CountSubstrings:
    def countSubstrings(self, s: str) -> int:
        rs = 0
        def update(i: int, j: int):
            nonlocal rs
            while i>=0 and j<len(s) and s[i] == s[j]:
                rs += 1
                i, j = i-1, j+1

        for i in range(len(s)):
            update(i, i)
            if i+1 < len(s):
                update(i, i+1)

        return rs


class NumDecodings:
    def numDecodings(self, s: str) -> int:
        cache = {len(s): 1}

        def recurse(i: int) -> int:
            if i in cache:
                return cache[i]
            if s[i] == "0":
                return 0

            rs = recurse(i+1)
            if i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
                rs += recurse(i+2)
            cache[i] = rs
            return rs
        
        return recurse(0)


class CoinChange:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def recurse(amt: int) -> int:
            if amt == 0:
                return 0
            if amt in cache:
                return cache[amt]

            rs = 1e5
            for coin in coins:
                if amt - coin >= 0:
                    rs = min(rs, 1 + recurse(amt - coin))
            cache[amt] = rs
            return int(rs)
        
        cs = recurse(amount)
        return cs if cs < 1e5 else -1


class WordBreak:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {len(s): True}

        def recurse(i: int) -> bool:
            if i in cache:
                return cache[i]
            for word in wordDict:
                if s[i:].startswith(word) and recurse(i + len(word)):
                    cache[i] = True
                    return True
            cache[i] = False
            return False

        return recurse(0)


class LongestIncreasing:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = { len(nums)-1: 1 }

        def recurse(i: int) -> int:
            if i in cache:
                return cache[i]

            rs = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    rs = max(rs, 1 + recurse(j))

            cache[i] = rs
            return rs

        return max(recurse(i) for i in range(len(nums)))


class CanPartition:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) / 2

        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            ndp = set()
            for d in dp:
                ndp.add(d)
                nd = d + nums[i]
                if nd == target:
                    return True
                ndp.add(nd)
            dp = ndp

        return False


class MaxProduct:
    def maxProduct(self, nums: List[int]) -> int:
        pmax, pmin = 1, 1
        rs = nums[0]

        for n in nums:
            nmax, nmin = pmax * n, pmin * n
            pmax = max(n, nmax, nmin)
            pmin = min(n, nmax, nmin)
            rs = max(rs, pmax)

        return rs

