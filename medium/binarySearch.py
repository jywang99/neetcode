from typing import List
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


class FindMin:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]

