from typing import List


class MaxSubArray:
    def maxSubArray(self, nums: List[int]) -> int:
        cur, rs = 0, nums[0]
        for n in nums:
            if cur < 0:
                cur = 0
            cur += n
            rs = max(rs, cur)
        return rs

