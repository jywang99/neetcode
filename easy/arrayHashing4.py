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


class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rs = {}
        for i, n in enumerate(nums):
            if n in rs:
                return [ rs[n], i ]
            rs[target - n] = i
        raise Exception('WTF')


class GroupAnagrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anas = defaultdict(list)
        for s in strs:
            anas[''.join(sorted(s))].append(s)
        return list(anas.values())

