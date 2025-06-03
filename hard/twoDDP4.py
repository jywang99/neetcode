from typing import List


class LongestIncreasingPath:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        dp = {}

        def recurse(r: int, c: int, prev: int) -> int:
            if c < 0 or c >= cols or r < 0 or r >= rows or matrix[r][c] <= prev:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

            rs = 0
            for dr, dc in dirs:
                rs = max(rs, recurse(r+dr, c+dc, matrix[r][c]))
            rs += 1

            dp[(r, c)] = rs
            return rs

        rs = 0
        for r in range(rows):
            for c in range(cols):
                rs = max(rs, recurse(r, c, -1))
        return rs

