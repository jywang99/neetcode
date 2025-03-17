import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k, self.heap = k, nums
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


class LastStoneWeight:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            s1, s2 = heapq.heappop(stones), heapq.heappop(stones)
            if s1 == s2:
                continue
            heapq.heappush(stones, -abs(s1 - s2))

        return -stones[0] if stones else 0


class KClosest:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = [[-(x**2 + y**2), x, y] for [x, y] in points]
        heapq.heapify(hp)

        while len(hp) > k:
            heapq.heappop(hp)

        return [[x, y] for [_, x, y] in hp]

