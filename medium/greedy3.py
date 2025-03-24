from typing import List


class MaxSubArray:
    def maxSubArray(self, nums: List[int]) -> int:
        s, rs = 0, nums[0]
        for n in nums:
            if s < 0:
                s = 0
            s += n
            rs = max(rs, s)
        return rs

