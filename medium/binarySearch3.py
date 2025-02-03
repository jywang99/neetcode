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

