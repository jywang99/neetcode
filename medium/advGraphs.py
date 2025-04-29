from typing import List
from collections import defaultdict


class NetworkDelayTime:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        dst = { nn: float("inf") for nn in range(1, n+1) }
        def recurse(node: int, time: int):
            if time >= dst[node]:
                return

            dst[node] = time
            for nei, w in adj[node]:
                recurse(nei, time + w)

        recurse(k, 0)
        rs = max(dst.values())
        return rs if rs < float("inf") else -1
        
