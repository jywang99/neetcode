from collections import defaultdict
import heapq
from typing import List


class ReconstructItinerary:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        rs = []
        def recurse(src: str) -> None:
            while adj[src]:
                dst = adj[src].pop()
                recurse(dst)
            rs.append(src)

        recurse("JFK")
        return rs[::-1]
        

class SwimInWater:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))
        visit = set()
        hp = [(grid[0][0], 0, 0)]
        visit.add((0, 0))

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

        return -1
        
