from typing import List
import math


class BianrySearch:
    def search(self, nums: List[int], target: int) -> int:
        def recurse(l: int, r: int) -> int:
            if l > r:
                return -1

            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                return recurse(m+1, r)
            return recurse(l, m-1)

        return recurse(0, len(nums)-1)

    def search_iter(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1


class SearchMatrix:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        row = None
        while l <= r:
            m = l + (r - l) // 2
            if matrix[m][0] <= target and matrix[m][-1] >= target:
                row = matrix[m]
                break
            elif matrix[m][0] > target:
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
            if nums[m] < nums[l]:
                r = m
            else:
                l = m + 1
        raise Exception("WTF")


class Koko:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        mk = r

        while l <= r:
            k = l + (r - l) // 2
            kh = 0
            for p in piles:
                kh += math.ceil(p / k)
            if kh > h:
                l = k + 1
            else:
                mk = k
                r = k - 1

        return mk

