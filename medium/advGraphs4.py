from collections import defaultdict
from typing import List
import heapq

class CostConnectPoints:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                dst = abs(x1-x2) + abs(y1-y2)
                adj[i].append((dst, j))
                adj[j].append((dst, i))

        hp = [(0, 0)]
        visit = set()
        rs = 0
        while len(visit) < len(points):
            td, tn = heapq.heappop(hp)
            if tn in visit:
                continue
            visit.add(tn)
            rs += td

            for nd, nn in adj[tn]:
                heapq.heappush(hp, (nd, nn))

        return rs


class NetworkDelayTime:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((w, v))

        hp = [(0, k)]
        visit = set()
        rs = 0
        while hp:
            td, tn = heapq.heappop(hp)
            if tn in visit:
                continue
            visit.add(tn)
            rs = td

            for nd, nn in adj[tn]:
                heapq.heappush(hp, (td + nd, nn))

        return rs if len(visit) == n else -1


class CheapestPrice:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        dist = [INF] * n
        dist[src] = 0

        for _ in range(k+1):
            tmpDist = dist.copy()
            for u, v, w in flights:
                if dist[u] == INF:
                    continue
                tmpDist[v] = min(tmpDist[v], dist[u] + w)
            dist = tmpDist

        rs = dist[dst]
        return int(rs) if rs != INF else -1

