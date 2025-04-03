from typing import List


class NumIslands:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        rows, cols = len(grid), len(grid[0])

        def recurse(r: int, c: int):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return 0

            grid[r][c] = "0"
            for dr, dc in dirs:
                recurse(r+dr, c+dc)
        
        rs = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    recurse(r, c)
                    rs += 1
        return rs
        
