from collections import defaultdict
from typing import List, Tuple
import math


class SearchMatrix:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def recMtx(s: int, t: int) -> int:
            if s > t:
                return -1

            m = (s + t) // 2
            if matrix[m][0] <= target and target <= matrix[m][-1]:
                return m
            if matrix[m][0] > target:
                return recMtx(s, m-1)
            return recMtx(m+1, t)

        row = matrix[recMtx(0, len(matrix)-1)]

        def recRow(s: int, t: int) -> int:
            if s > t:
                return -1

            m = (s + t) // 2
            if row[m] == target:
                return m
            if row[m] > target:
                return recRow(s, m-1)
            return recRow(m+1, t)

        return recRow(0, len(row)-1) != -1


class MinEatingSpeed:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        record = r

        while l <= r:
            m = l + (r - l) // 2

            time = sum(map(lambda p: math.ceil(p / m), piles))
            if time <= h:
                record = m
                r = m - 1
            else:
                l = m + 1

        return record


class FindMinRotated:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]


class TimeMap:
    def __init__(self):
        self.records: dict[str, List[Tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.records[key].append(( timestamp, value ))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.records:
            return ""
        entries = self.records[key]

        rs = ""
        l, r = 0, len(entries)-1
        while l <= r:
            m = l + (r - l) // 2
            if entries[m][0] <= timestamp:
                rs = entries[m][1]
                l = m + 1
            else:
                r = m - 1

        return rs

