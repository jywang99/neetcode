from typing import List


class HouseRobber:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)

        def recurse(i: int) -> int:
            if i >= len(nums):
                return 0
            if cache[i] == -1:
                cache[i] = max(nums[i] + recurse(i+2), recurse(i+1))
            return cache[i]
        
        return recurse(0)


class HouseRobber2:
    def robLine(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        def recurse(i: int) -> int:
            if i >= len(nums):
                return 0
            if cache[i] == -1:
                cache[i] = max(nums[i] + recurse(i+2), recurse(i+1))
            return cache[i]
        return recurse(0)

    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.robLine(nums[1:]), self.robLine(nums[:-1]))
        

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
        cache = { len(s): 1 }

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
        cache = { 0: 0 }

        def recurse(amt: int) -> int:
            if amt in cache:
                return cache[amt]
            rs = int(1e9)
            for coin in coins:
                if amt - coin >= 0:
                    rs = min(rs, 1 + recurse(amt - coin))
            cache[amt] = rs
            return rs
        
        cs = recurse(amount)
        return cs if cs < 1e9 else -1


class MaxProduct:
    def maxProduct(self, nums: List[int]) -> int:
        rs = nums[0]
        maxp, minp = 1, 1

        for n in nums:
            tmax, tmin = maxp * n, minp * n
            maxp = max(n, tmax, tmin)
            minp = min(n, tmax, tmin)
            rs = max(rs, maxp)

        return rs


class WordBreak:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ls = len(s)
        cache = { ls: True }

        def recurse(i: int) -> bool:
            if i in cache:
                return cache[i]
            rs = False
            for word in wordDict:
                if s[i:].startswith(word) and recurse(i + len(word)):
                    rs = True
                    break
            cache[i] = rs
            return rs

        return recurse(0)


class LengthOfLIS:
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

