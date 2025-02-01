import math
from typing import List


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

