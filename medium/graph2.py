from collections import defaultdict, deque
from typing import List, Optional, Set, Tuple


class NumIslands:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
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


class AreaOfIsland:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
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
        if not node:
            return None

        clones = {}
        def recurse(n: Node) -> Node:
            if n in clones:
                return clones[n]
            
            cn = Node(n.val)
            clones[n] = cn
            for nei in n.neighbors:
                cn.neighbors.append(recurse(nei))

            return cn
        
        return recurse(node)


class IslandsAndTreasure:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows, cols = len(grid), len(grid[0])

        visit = set()
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visit.add((r, c))
                    q.append((r, c))

        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == -1 or (nr, nc) in visit:
                        continue
                    q.append((nr, nc))
                    visit.add((nr, nc))
            dist += 1


class OrangesRotting:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        rows, cols = len(grid), len(grid[0])

        q = deque()
        freshes = 0
        for r in range(rows):
            for c in range(cols):
                v = grid[r][c]
                if v == 2:
                    q.append((r, c))
                elif v == 1:
                    freshes += 1

        time = 0
        while q and freshes > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    freshes -= 1
            time += 1

        return time if freshes == 0 else -1


class PacificAtlantic:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def recurse(r: int, c: int, prevHeight: int, visit: Set[Tuple]):
            if r<0 or r>=rows or c<0 or c>=cols or (r, c) in visit or heights[r][c] < prevHeight:
                return
            visit.add((r, c))
            for dr, dc in dirs:
                recurse(r+dr, c+dc, heights[r][c], visit)

        for r in range(rows):
            recurse(r, 0, 0, pac)
            recurse(r, cols-1, 0, atl)

        for c in range(cols):
            recurse(0, c, 0, pac)
            recurse(rows-1, c, 0, atl)

        rs = []
        for t in pac.intersection(atl):
            rs.append([t[0], t[1]])
        return rs


class SurroundedRegions:
    def solve(self, board: List[List[str]]) -> None:
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        rows, cols = len(board), len(board[0])

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


class CourseSchedule:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pres = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            pres[c].append(p)

        visit = set()

        def recurse(c):
            if c in visit:
                return False
            if len(pres[c]) == 0:
                return True

            visit.add(c)
            for p in pres[c]:
                if not recurse(p):
                    return False
            visit.remove(c)

            pres[c] = []
            return True

        for c in range(numCourses):
            if not recurse(c):
                return False
        return True


class CourseSchedule2:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pres = defaultdict(list)
        for c, p in prerequisites:
            pres[c].append(p)

        rs = []
        visit, cycle = set(), set()
        def recurse(c) -> bool:
            if c in visit:
                return True
            if c in cycle:
                return False

            cycle.add(c)
            for p in pres[c]:
                if not recurse(p):
                    return False
            cycle.remove(c)
            visit.add(c)
            rs.append(c)
            return True

        for i in range(numCourses):
            if not recurse(i):
                return []

        return rs

