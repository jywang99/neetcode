from typing import List


class TrappingRainWater:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        ml, mr = height[l], height[r]
        rs = 0
        while l < r:
            if height[l] < height[r]:
                l += 1
                ml = max(ml, height[l])
                rs += ml - height[l]
            else:
                r -= 1
                mr = max(mr, height[r])
                rs += mr - height[r]
        return rs
