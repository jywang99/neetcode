import heapq
from typing import List


class LastStoneWeight:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            s1, s2 = heapq.heappop(stones), heapq.heappop(stones)
            if s1 != s2:
                heapq.heappush(stones, -abs(s1-s2))
        return -stones[0] if stones else 0
        
