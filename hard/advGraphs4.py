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
        
