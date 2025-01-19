from collections import defaultdict
from typing import List


class ContainsDuplicate:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


class IsAnagram:
    def isAnagram(self, s: str, t: str) -> bool:
        lcnt = defaultdict(int)
        for c in s:
            lcnt[c] += 1

        for c in t:
            if lcnt[c] == 0: return False
            lcnt[c] -= 1

        for v in lcnt.values():
            if v > 0: return False
        return True

