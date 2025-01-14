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

