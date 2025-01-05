from collections import defaultdict
from typing import List


# 217. Contains Duplicate
class ContainsDuplicate:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for n in nums:
            if n in d:
                return True
            d[n] = True
        return False


# 242. Valid Anagram
class ValidAnagram:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1

        for c in t:
            if c not in d:
                return False
            if d[c] == 1:
                del d[c]
            else:
                d[c] -= 1

        return len(d) == 0


# 1. Two Sum
class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rs = {}
        for i, n in enumerate(nums):
            if n in rs:
                return [rs[n], i]
            rs[target - n] = i
        raise Exception('wtf')


# 49. Group Anagrams
class GroupAnagrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        
        anas = defaultdict(list)
        for s in strs:
            ss = ''.join(sorted(s))
            anas[ss].append(s)

        return list(anas.values())


# 347. Top K Frequent Elements
class TopKFrequent:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        val_freq: dict[int, int] = defaultdict(int)
        for val in nums:
            val_freq[val] += 1

        freq_vals: dict[int, List[int]] = defaultdict(list)
        for val, freq in val_freq.items():
            freq_vals[freq].append(val)

        rs: List[int] = []
        for freq in range(max(freq_vals.keys()), 0, -1):
            if freq not in freq_vals:
                continue

            for val in freq_vals[freq]:
                if len(rs) == k:
                    break
                rs.append(val)

            if len(rs) == k:
                break

        return rs


# # 238. Product of Array Except Self
# class ProductExceptSelf:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#

