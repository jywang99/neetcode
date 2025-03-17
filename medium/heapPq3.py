import heapq
from typing import List


class FindKthLargest:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]


class KClosest:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = [[-(x**2 + y**2), x, y] for [x, y] in points]
        heapq.heapify(hp)

        while len(hp) > k:
            heapq.heappop(hp)
        return [[x, y] for [_, x, y] in hp]

