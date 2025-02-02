import math
from typing import List
from collections import defaultdict


class SearchMatrix:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def recMat(s: int, t: int) -> int:
            if s > t:
                return -1

            m = s + (t - s) // 2
            if matrix[m][0] <= target and target  <= matrix[m][-1]:
                return m
            if matrix[m][0] > target:
                return recMat(s, m-1)
            return recMat(m+1, t)

        idx = recMat(0, len(matrix)-1)
        if idx == -1:
            return False
        row = matrix[idx]

        def recRow(s: int, t: int) -> bool:
            if s > t:
                return False

            m = s + (t - s) // 2
            if row[m] == target:
                return True
            if row[m] > target:
                return recRow(s, m-1)
            return recRow(m+1, t)

        return recRow(0, len(row)-1)


class MinEatingSpeed:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        rk = r

        while l <= r:
            k = l + (r - l) // 2
            kh = 0
            for p in piles:
                kh += math.ceil(p / k)

            if kh > h:
                l = k + 1
            else:
                rk = k
                r = k - 1

        return rk


class FindMinRotated:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] <= nums[r]:
                return nums[l]

            m = l + (r - l) // 2
            if nums[m] < nums[l]:
                r = m
            else:
                l = m + 1
        raise Exception("WTF")


class TimeMap:
    def __init__(self):
        self.map: dict[str, list[tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        recs = self.map[key]
        l, r = 0, len(recs)-1
        rs = ""
        while l <= r:
            m = l + (r - l) // 2
            if recs[m][0] <= timestamp:
                rs = recs[m][1]
                l = m + 1
            else:
                r = m - 1
        
        return rs

