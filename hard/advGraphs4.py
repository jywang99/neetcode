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


class AlienDictionary:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { c: set() for w in words for c in w }
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            ml = min(len(w1), len(w2))
            if w1[:ml] == w2[:ml] and len(w1) > len(w2):
                return ""
            for j in range(ml):
                c1, c2 = w1[j], w2[j]
                if c1 != c2:
                    adj[c1].add(c2)
                    break

        visit = {}
        rs = []
        def recurse(c: str) -> bool:
            if c in visit:
                return visit[c]

            visit[c] = True
            for nc in adj[c]:
                if recurse(nc):
                    return True
            visit[c] = False

            rs.insert(0, c)
            return False
        
        for c in adj:
            if recurse(c):
                return ""

        return "".join(rs)

