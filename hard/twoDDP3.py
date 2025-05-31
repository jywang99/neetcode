from typing import List


class LongestIncreasingPath:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        rows, cols = len(matrix), len(matrix[0])
        cache = {}

        def recurse(r: int, c: int, prev: int) -> int:
            if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] <= prev:
                return 0
            if (r, c) in cache:
                return cache[(r, c)]

            rs = 0
            for dr, dc in dirs:
                rs = max(rs, recurse(r+dr, c+dc, matrix[r][c]))
            rs += 1
            cache[(r, c)] = rs

            return rs
        
        rs = 0
        for r in range(rows):
            for c in range(cols):
                rs = max(rs, recurse(r, c, -1))
        return rs
        
