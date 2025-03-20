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
        

class FindKthLargest:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]


class KClosest:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [[-(x**2 + y**2), x, y] for [x, y] in points]
        heapq.heapify(points)
        while len(points) > k:
            heapq.heappop(points)
        return [[x, y] for [_, x, y] in points]

