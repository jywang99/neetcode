from typing import List


class HouseRobber:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)

        def recurse(i: int) -> int:
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(nums[i] + recurse(i+2), recurse(i+1))
            return memo[i]

        return recurse(0)


class HouseRobber2:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.robLine(nums[1:]), self.robLine(nums[:-1]))

    def robLine(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        def recurse(i: int) -> int:
            if i >= len(nums):
                return 0
            if cache[i] == -1:
                cache[i] = max(nums[i] + recurse(i+2), recurse(i+1))
            return cache[i]
        return recurse(0)


class LongestPalindrome:
    def longestPalindrome(self, s: str) -> str:
        rs = ""
        ml = 0

        def update(i: int, j: int):
            nonlocal rs, ml
            if s[i] != s[j]:
                return
            while i >= 0 and j < len(s) and s[i] == s[j]:
                l =  j - i + 1
                if l > ml:
                    ml = l
                    rs = s[i:j+1]
                i -= 1
                j += 1

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

        def recurse(i: int):
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

            rs = 1e9
            for coin in coins:
                if amt - coin >= 0:
                    rs = min(rs, 1 + recurse(amt - coin))
            cache[amt] = rs
            return int(rs)

        cs = recurse(amount)
        return -1 if cs >= 1e9 else cs


class MaxProduct:
    def maxProduct(self, nums: List[int]) -> int:
        rs = nums[0]
        cmin, cmax = 1, 1

        for n in nums:
            nmax, nmin = cmax * n, cmin * n
            cmax = max(nmax, nmin, n)
            cmin = min(nmax, nmin, n)
            rs = max(rs, cmax)

        return rs


class WordBreak:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}

        def recurse(i: int) -> bool:
            if i >= len(s):
                return True
            if i in cache:
                return cache[i]

            rs = False
            for word in wordDict:
                if s[i:].startswith(word) and recurse(i+len(word)):
                    rs = True
                    break

            cache[i] = rs
            return rs
        
        return recurse(0)

