from typing import List


class LongestConsecutive:
    def longestConsecutive(self, nums: List[int]) -> int:
        ml = 0
        ns = set(nums)

        for n in ns:
            if (n-1) in ns:
                continue
            l = 1
            while (n+l) in ns:
                l += 1
            ml = max(l, ml)
            
        return ml
        
