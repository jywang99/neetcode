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

