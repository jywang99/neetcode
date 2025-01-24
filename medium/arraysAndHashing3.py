from collections import defaultdict
from typing import List


class GroupAnagrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anas = defaultdict(list)
        for s in strs:
            anas[''.join(sorted(s))].append(s)
        return list(anas.values())


class TopKFrequent:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nfreq: dict[int, int] = defaultdict(int)
        for n in nums:
            nfreq[n] += 1

        freqs: list[list[int]] = [[] for _ in range(len(nums) + 1)]
        for n, fq in nfreq.items():
            freqs[fq].append(n)

        rs = []
        for i in range(len(freqs)-1, -1, -1):
            ns = freqs[i]
            for n in ns:
                rs.append(n)
                if len(rs) == k: return rs

        return rs


class ProductExceptSelf:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cnt = len(nums)
        rs = [0] * cnt

        prd = 1
        for i, n in enumerate(nums):
            rs[i] = prd
            prd *= n

        prd = 1
        for i in range(len(nums)-1, -1, -1):
            rs[i] *= prd
            prd *= nums[i]

        return rs


class LongestConsecutive:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        mlen = 0
        for n in nset:
            if n-1 in nset:
                continue
            l = 1
            while n+l in nset:
                l += 1
            mlen = max(mlen, l)
        return mlen

