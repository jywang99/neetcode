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


class JumpGame:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0


class JumpGame2:
    def jump(self, nums: List[int]) -> int:
        rs = 0
        l, r = 0, 0
        while r < len(nums)-1:
            far = 0
            for i in range(l, r+1):
                far = max(far, i + nums[i])
            l = r + 1
            r = far
            rs += 1
        return rs

