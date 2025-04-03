from collections import deque
from typing import List, Optional


class NumIslands:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        rows, cols = len(grid), len(grid[0])

        def recurse(r: int, c: int):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return
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


class MaxAreaOfIsland:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        rows, cols = len(grid), len(grid[0])

        def recurse(r: int, c: int) -> int:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            sz = 1
            for dr, dc in dirs:
                sz += recurse(r+dr, c+dc)
            return sz

        rs = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    sz = recurse(r, c)
                    rs = max(rs, sz)
        return rs


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        doppel = {}

        def recurse(n: Node) -> Node:
            if n in doppel:
                return doppel[n]
            
            nc = Node(n.val)
            doppel[n] = nc
            for nei in n.neighbors:
                neic = recurse(nei)
                nc.neighbors.append(neic)

            return nc
        
        return recurse(node) if node else None

