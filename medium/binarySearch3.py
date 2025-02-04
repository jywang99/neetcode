from collections import defaultdict
import math
from typing import List


class SearchMatrix:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        row = None
        while l <= r:
            m = l + (r - l) // 2
            if matrix[m][0] <= target and target <= matrix[m][-1]:
                row = matrix[m]
            if matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1

        if not row:
            return False

        l, r = 0, len(row)-1
        while l <= r:
            m = l + (r - l) // 2
            if row[m] == target:
                return True
            if row[m] > target:
                r = m - 1
            else:
                l = m + 1

        return False


class FindMinRotated:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] <= nums[r]:
                return nums[l]

            m = l + (r - l) // 2
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m
        raise Exception("WTF")


class Koko:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        rs = r

        while l <= r:
            m = l + (r - l) // 2
            t = 0
            for p in piles:
                t += math.ceil(p / m)
            if t <= h:
                rs = m
                r = m - 1
            else:
                l = m + 1

        return rs


class TimeMap:
    def __init__(self):
        self.data: dict[str, list[tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        recs = self.data[key]

        rs = ""
        l, r = 0, len(recs)-1
        while l <= r:
            m = l + (r - l) // 2
            if recs[m][0] <= timestamp:
                rs = recs[m][1]
                l = m + 1
            else:
                r = m - 1

        return rs

