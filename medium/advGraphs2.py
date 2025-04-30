from collections import defaultdict
import heapq
from typing import List


class NetworkDelayTime:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((w, v))

        t = 0
        hp = [(0, k)]
        visit = set()
        while hp:
            tw, tn = heapq.heappop(hp)
            if tn in visit:
                continue
            visit.add(tn)
            t = tw

            for nw, nn in adj[tn]:
                if nn in visit:
                    continue
                heapq.heappush(hp, (tw + nw, nn))

        return t if len(visit) == n else -1


class CostConnectPoints:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        N = len(points)
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dst = abs(x2 - x1) + abs(y2 - y1)
                adj[i].append((dst, j))
                adj[j].append((dst, i))

        cost = 0
        visit = set()
        hp = [(0, 0)]
        while len(visit) < N:
            tc, tn = heapq.heappop(hp)
            if tn in visit:
                continue
            visit.add(tn)
            cost += tc

            for nc, nn in adj[tn]:
                heapq.heappush(hp, (nc, nn))

        return cost


class CheapestFlights:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        prices = [INF] * n
        prices[src] = 0

        for _ in range(k+1):
            newPrices = prices.copy()
            for s, d, p in flights:
                if prices[s] == INF:
                    continue
                nd = prices[s] + p
                if  nd < newPrices[d]:
                    newPrices[d] = nd
            prices = newPrices

        rs = prices[dst]
        return int(rs) if rs != INF else -1

