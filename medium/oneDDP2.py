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

