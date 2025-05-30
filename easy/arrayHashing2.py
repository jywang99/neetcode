from collections import defaultdict
from typing import List


class ContainsDuplicate:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen: return True
            seen.add(n)
        return False


class IsAnagram:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        lcnt = defaultdict(int)
        for c in s:
            lcnt[c] += 1

        for c in t:
            if lcnt[c] == 0: return False
            lcnt[c] -= 1

        for c in lcnt:
            if lcnt[c] != 0: return False
        return True


class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rs = {}
        for i, n in enumerate(nums):
            if n in rs:
                return [i, rs[n]]
            rs[target - n] = i
        raise Exception('WTF')


class LongestConsecutive:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        ml = 0

        for n in nset:
            if (n-1) in nset:
                continue
            l = 0
            while (n+l) in nset:
                l +=1
            ml = max(l, ml)

        return ml

