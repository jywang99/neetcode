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


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        waitlist = {}
        for i, n in enumerate(nums):
            if n in waitlist:
                return [waitlist[n], i]
            waitlist[target - n] = i
        raise Exception('WTF')

