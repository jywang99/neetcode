from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rs = []

        def recurse(i: int, cur: List[int]):
            if i == len(nums):
                rs.append(cur.copy())
                return
            
            cur.append(nums[i])
            recurse(i+1, cur)
            cur.pop()
            recurse(i+1, cur)

        recurse(0, [])
        return rs
        
