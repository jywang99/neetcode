from collections import defaultdict


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


class CheckInclusion:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # alphabet counts in the window
        s1c = [0] * 26 # stays the same
        s2c = [0] * 26 # updated in below loop
        for i in range(len(s1)):
            s1c[ord(s1[i]) - ord("a")] += 1
            s2c[ord(s2[i]) - ord("a")] += 1

        # matches in the window
        matches = 0
        for i in range(26):
            matches += (1 if s1c[i] == s2c[i] else 0)

        # move a fix-sized window from left to right
        # update alphabet counts, update matches according to the counts
        l = 0
        for r in range(len(s1), len(s2)):
            # all letter counts match = done
            if matches == 26:
                return True

            # handle right pointer
            ai = ord(s2[r]) - ord("a")
            # update count
            s2c[ai] += 1
            if s1c[ai] == s2c[ai]:
                # became the same for this letter
                matches += 1
            elif s1c[ai] + 1 == s2c[ai]:
                # was the same before, now different
                matches -= 1

            # handle left pointer
            ai = ord(s2[l]) - ord("a")
            s2c[ai] -= 1
            if s1c[ai] == s2c[ai]:
                matches += 1
            elif s1c[ai] - 1 == s2c[ai]:
                matches -= 1
            
            # increment so that window size is the same
            l += 1

        # counts match for all letters or not
        return matches == 26

