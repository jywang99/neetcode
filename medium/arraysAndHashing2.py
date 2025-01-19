from collections import defaultdict
from typing import List


class GroupAnagrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list[str])
        for s in strs:
            groups[''.join(sorted(s))].append(s)

        res: list[list[str]] = []
        for g in groups.values():
            res.append(g)
        return res

