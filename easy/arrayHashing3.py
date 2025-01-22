from collections import defaultdict
from typing import List


class ContainsDuplicate:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


class IsAnagram:
    def isAnagram(self, s: str, t: str) -> bool:
        lcnt = defaultdict(int)
        for c in s:
            lcnt[c] += 1

        for c in t:
            if lcnt[c] == 0: return False
            lcnt[c] -= 1

        for v in lcnt.values():
            if v != 0: return False
        return True


class IsValidSudoku:
    def isValidArea(self, board: List[List[str]], sx: int, tx: int, sy: int, ty: int) -> bool:
        seen = set()
        for x in range(sx, tx):
            for y in range(sy, ty):
                n = board[y][x]
                if n == ".": continue
                if n in seen: return False
                seen.add(n)
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for y in range(9):
            if not self.isValidArea(board, 0, 9, y, y+1):
                return False

        for x in range(9):
            if not self.isValidArea(board, x, x+1, 0, 9):
                return False

        for x in range(1, 9, 3):
            for y in range(1, 9, 3):
                if not self.isValidArea(board, x-1, x+2, y-1, y+2):
                    return False

        return True


