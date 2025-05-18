from typing import List


class TrappingRainWater:
    def trap(self, height: List[int]) -> int:
        rs = 0
        l, r = 0, len(height)-1
        lmax, rmax = height[l], height[r]
        while l < r:
            if height[l] < height[r]:
                l += 1
                lmax = max(lmax, height[l])
                rs += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                rs += rmax - height[r]
        return rs
        
