import heapq
from typing import List
from collections import defaultdict


class ReconstructItinerary:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets):
            adj[src].append(dst)

        rs = ["JFK"]
        def recurse(src: str) -> bool:
            if len(rs) == len(tickets) + 1:
                return True
            if not adj[src]:
                return False

            for i, dst in enumerate(adj[src]):
                adj[src].pop(i)
                rs.append(dst)
                if recurse(dst): return True
                adj[src].insert(i, dst)
                rs.pop()

            return False
        
        recurse("JFK")
        return rs


class SwimInWater:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        n = len(grid)

        hp = [(grid[0][0], 0, 0)]
        visit = set([(0, 0)])
        while hp:
            t, r, c = heapq.heappop(hp)
            if r == n-1 and c == n-1:
                return t

            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if nr < 0 or nr >= n or nc < 0 or nc >= n or (nr, nc) in visit:
                    continue
                visit.add((nr, nc))
                heapq.heappush(hp, (max(t, grid[nr][nc]), nr, nc))

        raise Exception()

