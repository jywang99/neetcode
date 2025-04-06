from collections import deque
from typing import List, Optional, Set, Tuple


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


class CloneGraph:
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


class IslandsAndTreasure:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dirs = ((1, 0), (-1, 0), (0, -1), (0, 1))
        rows, cols = len(grid), len(grid[0])

        q = deque()
        visit = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
        
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == -1 or (nr, nc) in visit:
                        continue
                    grid[nr][nc] = dist+1
                    visit.add((nr, nc))
                    q.append((nr, nc))
            dist += 1


class OrangesRotting:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        rows, cols = len(grid), len(grid[0])

        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                o = grid[r][c]
                if o == 2:
                    q.append((r, c))
                elif o == 1:
                    fresh += 1

        time = 0
        while q and fresh:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if nr<0 or nr>=rows or nc<0 or nc>=cols or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1


class PacificAtlantic:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def recurse(r: int, c: int, prevHeight: int, visit: Set[Tuple[int, int]]):
            if r<0 or r>=rows or c<0 or c>=cols or heights[r][c] < prevHeight or (r, c) in visit:
                return
            visit.add((r, c))
            for dr, dc in dirs:
                recurse(r+dr, c+dc, heights[r][c], visit)

        atl, pac = set(), set()
        for r in range(rows):
            recurse(r, 0, 0, pac)
            recurse(r, cols-1, 0, atl)
        for c in range(cols):
            recurse(0, c, 0, pac)
            recurse(rows-1, c, 0, atl)

        rs = []
        for r, c in atl.intersection(pac):
            rs.append([r, c])
        return rs


class SurroundedRegions:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def recurse(r: int, c: int):
            if r<0 or r>=rows or c<0 or c>=cols or board[r][c] != "O":
                return
            board[r][c] = "E"
            for dr, dc in dirs:
                recurse(r+dr, c+dc)

        for r in range(rows):
            recurse(r, 0)
            recurse(r, cols-1)
        for c in range(cols):
            recurse(0, c)
            recurse(rows-1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "E":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"

