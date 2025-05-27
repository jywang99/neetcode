from typing import List
import heapq


class MinInterval:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        rs = {}

        hp = []
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(hp, (r - l + 1, r))
                i += 1

            while hp and hp[0][1] < q:
                heapq.heappop(hp)
            rs[q] = hp[0][0] if hp else -1

        return [rs[q] for q in queries]
        
