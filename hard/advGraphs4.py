import heapq
from collections import defaultdict
from typing import List


class ReconstructItinerary:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)

        rs = []
        def recurse(src: str):
            while adj[src]:
                dst = adj[src].pop()
                recurse(dst)
            rs.insert(0, src)

        recurse("JFK")
        return rs
        

class SwimInRisingWater:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        rows, cols = len(grid), len(grid[0])

        hp = [(grid[0][0], 0, 0)]
        visit = set([(0, 0)])
        while hp:
            t, r, c = heapq.heappop(hp)
            if r == rows-1 and c == cols-1:
                return t

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols or (nr, nc) in visit:
                    continue
                visit.add((nr, nc))
                heapq.heappush(hp, (max(t, grid[nr][nc]), nr, nc))

        raise Exception()

