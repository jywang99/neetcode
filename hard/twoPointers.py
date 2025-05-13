from typing import List


class TrappingRainWater:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmax, rmax = [0] * n, [0] * n
        mh = 0
        for i, h in enumerate(height):
            mh = max(mh, h)
            lmax[i] = mh
        mh = 0
        for i in range(n-1, -1, -1):
            h = height[i]
            mh = max(mh, h)
            rmax[i] = mh

        rs = 0
        for i, h in enumerate(height):
            gain = min(rmax[i], lmax[i]) - h
            if gain > 0:
                rs += gain
        return rs
        
