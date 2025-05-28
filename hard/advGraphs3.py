from collections import defaultdict
from typing import List


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
                if recurse(dst):
                    return True
                adj[src].insert(i, dst)
                rs.pop()

            return False

        recurse("JFK")
        return rs

    def findItinerary2(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)

        rs = []
        def recurse(src):
            while adj[src]:
                dst = adj[src].pop()
                recurse(dst)
            rs.append(src)

        recurse("JFK")
        return rs[::-1]
        
