from typing import List
from collections import defaultdict
import heapq


class NetworkDelayTime:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((w, v))

        hp = [(0, k)]
        visit = set()
        t = 0
        while hp:
            tw, tn = heapq.heappop(hp)
            if tn in visit:
                continue
            visit.add(tn)
            t = tw

            for nw, nn in adj[tn]:
                heapq.heappush(hp, (tw + nw, nn))

        return t if len(visit) == n else -1


class CostConnectPoints:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                d = abs(x1-x2) + abs(y1-y2)
                adj[i].append((d, j))
                adj[j].append((d, i))

        hp = [(0, 0)]
        cost = 0
        visit = set()
        while len(visit) < len(points):
            tc, tn = heapq.heappop(hp)
            if tn in visit:
                continue
            visit.add(tn)
            cost += tc

            for nc, nn in adj[tn]:
                heapq.heappush(hp, (nc, nn))

        return cost

