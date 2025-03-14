import heapq
from typing import List


class KClosest:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = [[-x**2 + -y**2, x, y] for [x, y] in points]
        heapq.heapify(hp)

        while len(hp) > k:
            heapq.heappop(hp)

        return [[x, y] for [_, x, y] in hp]


class FindKthLargest:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        for _ in range(k-1):
            heapq.heappop(nums)
        return -nums[0]

