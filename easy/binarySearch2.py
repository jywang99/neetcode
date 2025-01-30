from typing import List


class BinarySearch:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        def recurse(s: int, t: int) -> int:
            if s > t:
                return -1

            m = (s + t) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                return recurse(s, m-1)
            return recurse(m+1, t)

        return recurse(0, len(nums)-1)
        
