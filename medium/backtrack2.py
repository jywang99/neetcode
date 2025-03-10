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


class CombinationSum2:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        rs = []
        candidates.sort()

        def recurse(i: int, cur: List[int], total: int):
            if total == target:
                rs.append(cur.copy())
                return
            if i == len(candidates) or total > target:
                return

            cur.append(candidates[i])
            recurse(i+1, cur, total + candidates[i])
            cur.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            recurse(i+1, cur, total)

        recurse(0, [], 0)
        return rs


class Permute:
    def permute(self, nums: List[int]) -> List[List[int]]:
        rs = []

        def recurse(cur: List[int], picked: List[bool]):
            if len(cur) == len(nums):
                rs.append(cur.copy())
                return

            for j in range(len(nums)):
                if picked[j]:
                    continue
                cur.append(nums[j])
                picked[j] = True
                recurse(cur, picked)
                cur.pop()
                picked[j] = False

        recurse([], [False] * len(nums))
        return rs

