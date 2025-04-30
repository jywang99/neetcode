from collections import defaultdict
from typing import List
import heapq


class NetworkDelayTime:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        hp = [(0, k)]
        visit = set()
        t = 0
        while hp:
            tw, tn = heapq.heappop(hp)
            if tn in visit:
                continue
            visit.add(tn)
            t = tw

            for nn, nw in adj[tn]:
                if nn not in visit:
                    heapq.heappush(hp, (tw + nw, nn))

        return t if len(visit) == n else -1


class CostConnectPoints:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = [[] for _ in range(N)]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dst = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dst, j])
                adj[j].append([dst, i])

        rs = 0
        visit = set()
        hp = [[0, 0]]
        while len(visit) < N:
            cost, i = heapq.heappop(hp)
            if i in visit:
                continue
            rs += cost
            visit.add(i)

            for nc, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(hp, [nc, nei])

        return rs


class CheapestFlights:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        prices = [INF] * n
        prices[src] = 0

        for _ in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights:
                if prices[s] == INF:
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices

        return -1 if prices[dst] == INF else int(prices[dst])

