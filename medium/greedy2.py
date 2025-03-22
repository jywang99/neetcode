from typing import List


class MaxSubArray:
    def maxSubArray(self, nums: List[int]) -> int:
        rs, cur = nums[0], 0
        for n in nums:
            if cur < 0:
                cur = 0
            cur += n
            rs = max(rs, cur)
        return rs

