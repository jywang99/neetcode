from typing import List


class Subsets:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rs = []
        subset = []

        def recurse(i: int):
            if i == len(nums):
                rs.append(subset.copy())
                return

            subset.append(nums[i])
            recurse(i+1)
            subset.pop()
            recurse(i+1)

        recurse(0)
        return rs


class CombinationSum:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        rs = []
        cur = []

        def recurse(i: int, sm: int):
            if sm == target:
                rs.append(cur.copy())
                return
            if i == len(candidates) or sm > target:
                return

            cur.append(candidates[i])
            recurse(i, sm + candidates[i])
            cur.pop()
            recurse(i+1, sm)

        recurse(0, 0)
        return rs

