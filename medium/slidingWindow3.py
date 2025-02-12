class LongestNoRepeat:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rs = 0
        cset = set()
        l = 0
        for c in s:
            while c in cset:
                cset.remove(s[l])
                l += 1
            cset.add(c)
            rs = max(rs, len(cset))
        return rs


class CheckInclusion:
    def getCharIdx(self, c: str) -> int:
        return ord(c) - ord("a")

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1c, s2c = [0]*26, [0]*26
        for i in range(len(s1)):
            s1c[self.getCharIdx(s1[i])] += 1
            s2c[self.getCharIdx(s2[i])] += 1

        matches = 0
        for i in range(26):
            if s1c[i] == s2c[i]:
                matches += 1

        l = 1
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            ai = self.getCharIdx(s2[l-1])
            s2c[ai] -= 1
            if s2c[ai] == s1c[ai]:
                matches += 1
            elif s2c[ai] + 1 == s1c[ai]:
                matches -= 1
            l += 1

            ai = self.getCharIdx(s2[r])
            s2c[ai] += 1
            if s2c[ai] == s1c[ai]:
                matches += 1
            elif s2c[ai] - 1 == s1c[ai]:
                matches -= 1

        return matches == 26

