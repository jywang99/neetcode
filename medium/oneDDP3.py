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


class LongestPalindrome:
    def longestPalindrome(self, s: str) -> str:
        rs = ""
        mlen = 0

        def update(i: int, j: int):
            nonlocal rs, mlen
            while i>=0 and j<len(s) and s[i] == s[j]:
                l = j - i + 1
                if l > mlen:
                    mlen = l
                    rs = s[i:j+1]
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
            ways = recurse(i+1)
            if i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
                ways += recurse(i+2)
            cache[i] = ways
            return ways

        return recurse(0)


class CoinChange:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {0: 0}

        def recurse(amt: int) -> int:
            if amt in cache:
                return cache[amt]

            rs = int(1e9)
            for coin in coins:
                rem = amt - coin
                if rem < 0:
                    continue
                c = 1 + recurse(amt - coin)
                rs = min(rs, c)

            cache[amt] = rs
            return rs

        c = recurse(amount)
        return c if c < 1e9 else -1

