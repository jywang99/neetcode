from collections import deque
from typing import List, Optional, Set


class NumIslands:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def recurse(r: int, c: int):
            if r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                recurse(r + dr, c + dc)

        rs = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    recurse(r, c)
                    rs += 1
        return rs
        

class MaxAreaOfIsland:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows, cols = len(grid), len(grid[0])

        def recurse(r: int, c: int) -> int:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            s = 1
            for dr, dc in dirs:
                s += recurse(r+dr, c+dc)
            return s

        rs = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    rs = max(rs, recurse(r, c))
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
                    q.append((r, c))
                    visit.add((r, c))

        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if nr < 0 or nr == rows or nc < 0 or nc == cols or grid[nr][nc] == -1 or (nr, nc) in visit:
                        continue
                    visit.add((nr, nc))
                    q.append((nr, nc))
            dist += 1


class OrangesRotting:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows, cols = len(grid), len(grid[0])

        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        time = 0
        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != 1:
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
        pac, atl = set(), set()

        def recurse(r: int, c: int, prevHeight: int, visit: Set):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visit:
                return
            h = heights[r][c]
            if h < prevHeight:
                return
            visit.add((r, c))
            for dr, dc in dirs:
                recurse(r+dr, c+dc, h, visit)

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
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
                return
            board[r][c] = "E"
            for dr, dc in dirs:
                recurse(r+dr, c+dc)

        for r in range(rows):
            if board[r][0] == "O":
                recurse(r, 0)
            if board[r][cols-1] == "O":
                recurse(r, cols-1)

        for c in range(cols):
            if board[0][c] == "O":
                recurse(0, c)
            if board[rows-1][c] == "O":
                recurse(rows-1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "E":
                    board[r][c] = "O"


class CanFinish:
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
        pres = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            pres[c].append(p)

        rs = []
        visit, cycle = set(), set()

        def dfs(c):
            if c in cycle:
                return False
            if c in visit:
                return True

            cycle.add(c)
            for p in pres[c]:
                if not dfs(p):
                    return False

            cycle.remove(c)
            visit.add(c)
            rs.append(c)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return rs


class GraphValidTree:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False

        adj = [[] for _ in range(n)]
        for u, v in  edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def recurse(n: int, prev: int) -> bool:
            if n in visit:
                return False

            visit.add(n)
            for nei in adj[n]:
                if nei == prev:
                    continue
                if not recurse(nei, n):
                    return False
            return True

        return recurse(0, -1) and len(visit) == n 


class CountComponents:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = [False] * n
        def recurse(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    recurse(nei)

        rs = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                recurse(node)
                rs += 1
        return rs


class RedundantConnection:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        vs = len(edges)+1
        adj = [[] for _ in range(vs)]
        visit = set()

        def recurse(v: int, prev: int) -> bool:
            if v in visit:
                return True

            visit.add(v)
            for nv in adj[v]:
                if nv == prev:
                    continue
                if recurse(nv, v):
                    return True

            return False
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visit = set()

            if recurse(u, -1):
                return [u, v]
        
        return []

