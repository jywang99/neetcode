from collections import defaultdict
from typing import List, Set


class GroupAnagrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list[str])
        for s in strs:
            groups[''.join(sorted(s))].append(s)

        res: list[list[str]] = []
        for g in groups.values():
            res.append(g)
        return res


class IsValidSudoku:
    def isRangeValid(self, board: List[List[str]], yf: int, yt: int, xf: int, xt: int) -> bool:
        ns: Set[str] = set()
        for y in range(yf, yt):
            for x in range(xf, xt):
                n = board[y][x]
                if n == ".": continue
                if n in ns:
                    return False
                ns.add(n)
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        side = 9
        grid = 3

        for y in range(side):
            if not self.isRangeValid(board, y, y+1, 0, side):
                return False
        
        for x in range(side):
            if not self.isRangeValid(board, 0, side, x, x+1):
                return False

        for xf in range(0, side, grid):
            for yf in range(0, side, grid):
                if not self.isRangeValid(board, xf, xf+grid, yf, yf+grid):
                    return False

        return True

