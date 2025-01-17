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
        lcnt = defaultdict(int)
        for c in s:
            lcnt[c] += 1

        for c in t:
            if lcnt[c] == 0: 
                return False
            elif lcnt[c] == 1:
                del lcnt[c]
            else:
                lcnt[c] -= 1

        return len(lcnt) == 0


class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        waitlist = {}
        for i, n in enumerate(nums):
            if n in waitlist:
                return [waitlist[n], i]
            waitlist[target - n] = i
        raise Exception('WTF')


class GroupAnagrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]

        anas = defaultdict(list)
        for s in strs:
            anas[''.join(sorted(s))].append(s)
        
        return list(anas.values())


class TopKFrequent:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n_freq: dict[int, int] = defaultdict(int)
        for n in nums:
            n_freq[n] += 1

        freq_tups = list(n_freq.items())
        freq_tups = sorted(freq_tups, key = lambda tup : tup[1], reverse=True)
        return list(map(lambda tup : tup[0], freq_tups[:k]))


class ProductExceptSelf:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cnt = len(nums)

        pref = [0] * cnt
        for i in range(cnt):
            prev_prd, prev = 1, 1
            if i > 0:
                prev_prd = pref[i-1]
                prev = nums[i-1]
            pref[i] = prev_prd * prev

        suff = [0] * cnt
        for i in reversed(range(cnt)):
            prev_prd, prev = 1, 1
            if i < cnt - 1:
                prev_prd = suff[i+1]
                prev = nums[i+1]
            suff[i] = prev_prd * prev

        rs = [0] * cnt
        for i in range(cnt):
            rs[i] = pref[i] * suff[i]
        
        return rs


class ProductExceptSelfOptimal:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cnt = len(nums)
        rs = [0] * cnt
        
        pref = 1
        for i in range(cnt):
            rs[i] = pref
            pref *= nums[i]

        suff = 1
        for i in range(cnt-1, -1, -1):
            rs[i] *= suff
            suff *= nums[i]

        return rs


if __name__ == '__main__':
    print(ProductExceptSelfOptimal().productExceptSelf([1,2,3,4]))

