from typing import List


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

