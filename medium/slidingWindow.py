class LongestSubstring:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ml = 0
        l = 0
        cset = set()
        for r in range(len(s)):
            c = s[r]
            while c in cset:
                cset.remove(s[l])
                l += 1
            cset.add(c)
            ml = max(ml, r - l + 1)
        return ml


class CharacterReplacement:
    def characterReplacement(self, s: str, k: int) -> int:
        rs = 0
        cset = set(s)
        for c in cset:
            matches = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    matches += 1

                while (r - l + 1) - matches > k:
                    if s[l] == c:
                        matches -= 1
                    l += 1

                rs = max(rs, r - l + 1)
        return rs

