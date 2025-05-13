from typing import List


class LargestRectangleArea:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        rs = 0
        for i, h in enumerate(heights):
            start = i
            while stk and stk[-1][1] > h:
                pi, ph = stk.pop()
                start = pi
                rs = max(rs, (i - pi) * ph)
            stk.append((start, h))

        i = len(heights)
        while stk:
            pi, ph = stk.pop()
            rs = max(rs, (i - pi) * ph)

        return rs

