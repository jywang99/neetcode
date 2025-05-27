from collections import defaultdict
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
        
