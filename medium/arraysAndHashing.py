from collections import defaultdict
from typing import List


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


class IsValidSudoku:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            cset = set()
            for c in row:
                if c in cset: return False
                if c != '.': cset.add(c)

        for x in range(9):
            cset = set()
            for y in range(9):
                c = board[y][x]
                if c in cset: return False
                if c != '.': cset.add(c)

        for cx in range(1, 8, 3): 
            for cy in range(1, 8, 3):
                cset = set()
                for x in range(cx-1, cx+2):
                    for y in range(cy-1, cy+2):
                        c = board[y][x]
                        if c in cset: return False
                        if c != '.': cset.add(c)

        return True


class LongestConsecutive:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        cnt = 0

        for n in nset:
            if (n-1) in nset:
                continue

            slen = 1
            while (n + slen) in nset:
                slen += 1
            cnt = max(cnt, slen)

        return cnt

