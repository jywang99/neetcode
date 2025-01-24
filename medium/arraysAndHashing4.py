from collections import defaultdict
from typing import List


class GroupAnagrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anas = defaultdict(list)
        for s in strs:
            anas[''.join(sorted(s))].append(s)
        return list(anas.values())


class ProductExceptSelf:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rs = [0] * len(nums)

        prd = 1
        for i, n in enumerate(nums):
            rs[i] = prd
            prd *= n

        prd = 1
        for i in range(len(nums)-1, -1, -1):
            rs[i] *= prd
            prd *= nums[i]

        return rs


class TopKFrequent:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nfreq: dict[int, int] = defaultdict(int)
        for n in nums:
            nfreq[n] += 1
        ftups = sorted(nfreq.items(), key = lambda kvp : kvp[1], reverse = True)
        return list(map(lambda kvp : kvp[0], ftups[:k]))

