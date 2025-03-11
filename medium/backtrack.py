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

        def recurse(i: int, total: int):
            if total == target:
                rs.append(cur.copy())
                return
            if i == len(candidates) or total > target:
                return

            cur.append(candidates[i])
            recurse(i, total + candidates[i])
            cur.pop()
            recurse(i+1, total)

        recurse(0, 0)
        return rs


class CombinationSum2:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        rs = []

        def recurse(i: int, cur: list[int], total: int):
            if total == target:
                rs.append(cur.copy())
                return
            if total > target or i == len(candidates):
                return

            cur.append(candidates[i])
            recurse(i+1, cur, total + candidates[i])
            cur.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            recurse(i+1, cur, total)

        recurse(0, [], 0)
        return rs


class Permute:
    def permute(self, nums: List[int]) -> List[List[int]]:
        rs = []
        def recurse(perm: List[int], picked: List[bool]):
            if len(perm) == len(nums):
                rs.append(perm.copy())
                return
            for i in range(len(nums)):
                if not picked[i]:
                    perm.append(nums[i])
                    picked[i] = True
                    recurse(perm, picked)
                    perm.pop()
                    picked[i] = False
        recurse([], [False] * len(nums))
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
        nrow, ncol = len(board), len(board[0])

        def recurse(row: int, col: int, wi: int):
            if wi == len(word):
                return True
            if col < 0 or col >= ncol or row < 0 or row >= nrow or board[row][col] != word[wi] or board[row][col] == "#":
                return False

            board[row][col] = "#"
            if recurse(row + 1, col, wi+1) or recurse(row - 1, col, wi+1) or recurse(row, col + 1, wi+1) or recurse(row, col - 1, wi+1):
                return True
            board[row][col] = word[wi]
            return False
        
        for row in range(nrow):
            for col in range(ncol):
                if recurse(row, col, 0):
                    return True
        return False


class PalindromePartition:
    def partition(self, s: str) -> List[List[str]]:
        def isPali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l+1, r-1
            return True

        rs = []

        def recurse(i: int, part: List[str]):
            if i >= len(s):
                rs.append(part.copy())
                return

            for j in range(i, len(s)):
                if isPali(i, j):
                    part.append(s[i:j+1])
                    recurse(j+1, part)
                    part.pop()

        recurse(0, [])
        return rs

