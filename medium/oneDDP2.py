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
        
