from typing import List


class BinarySearch:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target:
            return 0

        def recurse(l: int, r: int) -> int:
            if l > r:
                return -1
            m = (l + r) //2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                return recurse(m+1, r)
            return recurse(l, m-1)

        return recurse(0, len(nums) - 1)

