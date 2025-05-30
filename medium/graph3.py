from collections import defaultdict, deque
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


class CourseSchedule:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pres = defaultdict(list)
        for c, p in prerequisites:
            pres[c].append(p)

        visit = set()
        def recurse(c: int) -> bool:
            if c in visit:
                return False

            visit.add(c)
            for pre in pres[c]:
                if not recurse(pre):
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
        pres = [[] for _ in range(numCourses)]
        for c, p in prerequisites:
            pres[c].append(p)

        rs = []
        clear, cycle = set(), set()

        def recurse(c: int) -> bool:
            if c in clear:
                return True
            if c in cycle:
                return False

            cycle.add(c)
            for p in pres[c]:
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
            if v in visit:
                return True
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
        def recurse(v: int, prev: int):
            if v in visit:
                return
            visit.add(v)
            for nv in adj[v]:
                if nv == prev:
                    continue
                recurse(nv, v)

        rs = 0
        for v in range(n):
            if v not in visit:
                recurse(v, -1)
                rs += 1
        return rs


class FindRedundantConnection:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(len(edges) + 1)]

        cycle = set()
        def hasCycle(v: int, prev: int) -> bool:
            if v in cycle:
                return True
            cycle.add(v)
            for nv in adj[v]:
                if nv == prev:
                    continue
                if hasCycle(nv, v):
                    return True
            return False

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            cycle = set()
            if hasCycle(u, -1):
                return [u, v]
        raise Exception("WTF")

