from collections import defaultdict
from typing import List


class GroupAnagrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anas = defaultdict(list)
        for s in strs:
            anas[''.join(sorted(s))].append(s)
        return list(anas.values())

