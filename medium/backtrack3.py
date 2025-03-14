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

            for i in range(len(nums)):
                if picked[i]:
                    continue
                cur.append(nums[i])
                picked[i] = True
                recurse(cur, picked)
                cur.pop()
                picked[i] = False

        recurse([], [False]*len(nums))
        return rs


class SubsetsWithDup:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        rs = []
        nums.sort()

        def recurse(i: int, cur: List[int]):
            if i == len(nums):
                rs.append(cur.copy())
                return

            cur.append(nums[i])
            recurse(i+1, cur)
            cur.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            recurse(i+1, cur)

        recurse(0, [])
        return rs


class WordSearch:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nr, nc = len(board), len(board[0])

        def recurse(r: int, c: int, wi: int) -> bool:
            if wi == len(word):
                return True
            if r == nr or c == nc or r == -1 or c == -1 or board[r][c] != word[wi]:
                return False

            board[r][c] = "#"
            if recurse(r+1, c, wi+1) or recurse(r-1, c, wi+1) or recurse(r, c+1, wi+1) or recurse(r, c-1, wi+1):
                return True
            board[r][c] = word[wi]
            return False

        for r in range(nr):
            for c in range(nc):
                if recurse(r, c, 0):
                    return True
        return False


class PalindromePartition:
    def partition(self, s: str) -> List[List[str]]:
        def isPalin(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l+1, r-1
            return True

        rs = []

        def recurse(i: int, cur: List[str]):
            if i == len(s):
                rs.append(cur.copy())
                return
            for j in range(i, len(s)):
                if not isPalin(i, j):
                    continue
                cur.append(s[i:j+1])
                recurse(j+1, cur)
                cur.pop()

        recurse(0, [])
        return rs

