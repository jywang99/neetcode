from collections import deque
from typing import List, Optional, Set, Tuple


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
        

class MaxAreaOfIsland:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        rows, cols = len(grid), len(grid[0])

        def recurse(r: int, c: int) -> int:
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            s = 1
            for dr, dc in dirs:
                s += recurse(r+dr, c+dc)
            return s
        
        rs = 0
        for r in range(rows):
            for c in range(cols):
                rs = max(rs, recurse(r, c))
        return rs


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class CloneGraph:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        doppel = {}

        def recurse(n: Node):
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
        inf = 2 ** 31 - 1
        rows, cols = len(grid), len(grid[0])
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if nr<0 or nr>=rows or nc<0 or nc>=cols or grid[nr][nc] != inf:
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = dist+1
            dist += 1


class OrangesRotting:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                v = grid[r][c]
                if v == 1:
                    fresh += 1
                elif v == 2:
                    q.append((r, c))

        time = 0
        while q and fresh:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if nr<0 or nr>=rows or nc<0 or nc>=cols or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
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

        pac, atl = set(), set()
        for r in range(rows):
            recurse(r, 0, 0, pac)
            recurse(r, cols-1, 0, atl)
        for c in range(cols):
            recurse(0, c, 0, pac)
            recurse(rows-1, c, 0, atl)
        
        rs = []
        for r, c in pac.intersection(atl):
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


class CanFinish:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for c, p in prerequisites:
            adj[c].append(p)

        cycle = set()
        def recurse(c: int) -> bool:
            if c in cycle:
                return False
            cycle.add(c)
            for p in adj[c]:
                if not recurse(p):
                    return False
            cycle.remove(c)
            adj[c] = []
            return True

        for c in range(numCourses):
            if not recurse(c):
                return False
        return True


class CourseSchedule2:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for c, p in prerequisites:
            adj[c].append(p)

        clear, cycle = set(), set()
        rs = []
        def recurse(c: int) -> bool:
            if c in cycle:
                return False
            if c in clear:
                return True

            cycle.add(c)
            for p in adj[c]:
                if not recurse(p):
                    return False
            cycle.remove(c)
            clear.add(c)
            rs.append(c)
            return True

        for c in range(numCourses):
            if not recurse(c):
                return []
        return rs


class GraphValidTree:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit, cycle = set(), set()
        def recurse(v: int, prev: int) -> bool:
            if v in cycle:
                return False
            cycle.add(v)
            for nv in adj[v]:
                if nv == prev:
                    continue
                if not recurse(nv, v):
                    return False
            cycle.remove(v)
            visit.add(v)
            return True
        
        return len(visit) == n if recurse(0, -1) else False


class CountComponents:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()

        def recurse(v: int):
            if v in visit:
                return
            visit.add(v)
            for nv in adj[v]:
                recurse(nv)

        rs = 0
        for v in range(n):
            if v not in visit:
                recurse(v)
                rs += 1
        return rs


class RedundantConnection:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(len(edges)+1)]
        cycle = set()

        def recurse(v: int, prev: int) -> bool:
            if v in cycle:
                return True
            cycle.add(v)
            for nv in adj[v]:
                if nv == prev:
                    continue
                if recurse(nv, v):
                    return True
            cycle.remove(v)
            return False

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            cycle = set()

            if recurse(u, -1):
                return [u, v]
            
        return []

