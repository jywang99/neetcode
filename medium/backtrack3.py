from typing import List


class Subsets:
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
        

class CombinationSum:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        rs = []

        def recurse(i: int, cur: List[int], total: int):
            if total == target:
                rs.append(cur.copy())
                return
            if i == len(candidates) or total > target:
                return

            cur.append(candidates[i])
            recurse(i, cur, total + candidates[i])
            cur.pop()
            recurse(i+1, cur, total)

        recurse(0, [], 0)
        return rs
        
