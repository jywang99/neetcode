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
        rc, cc = len(board), len(board[0])

        def recurse(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= rc or c >= cc or board[r][c] == "#" or board[r][c] != word[i]:
                return False

            board[r][c] = "#"
            if recurse(r-1, c, i+1) or recurse(r+1, c, i+1) or recurse(r, c-1, i+1) or recurse(r, c+1, i+1):
                return True
            board[r][c] = word[i]
            return False
        
        for r in range(rc):
            for c in range(cc):
                if recurse(r, c, 0):
                    return True
        return False


class PalindromePartition:
    def partition(self, s: str) -> List[List[str]]:
        def isPali(i: int, j: int) -> bool:
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i+1, j-1
            return True

        rs = []

        def recurse(i: int, cur: List[str]):
            if i == len(s):
                rs.append(cur.copy())
                return

            for j in range(i, len(s)):
                if not isPali(i, j):
                    continue
                cur.append(s[i:j+1])
                recurse(j+1, cur)
                cur.pop()

        recurse(0, [])
        return rs


class LetterCombinations:
    LETTER_MAP = {
        "2": [ "a", "b", "c" ],
        "3": [ "d", "e", "f" ],
        "4": [ "g", "h", "i" ],
        "5": [ "j", "k", "l" ],
        "6": [ "m", "n", "o" ],
        "7": [ "p", "q", "r", "s" ],
        "8": [ "t", "u", "v", ],
        "9": [ "w", "x", "y", "z" ],
    }

    def letterCombinations(self, digits: str) -> List[str]:
        rs = []

        def recurse(i: int, cur: str):
            if i == len(digits):
                if cur:
                    rs.append(cur)
                return

            for c in self.LETTER_MAP[digits[i]]:
                cur += c
                recurse(i+1, cur)
                cur = cur[:-1]

        recurse(0, "")
        return rs

