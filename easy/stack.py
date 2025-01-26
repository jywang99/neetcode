from typing import List


class ValidParen:
    PAIRS = { "{": "}", "[": "]", "(": ")" }
    OPENS = PAIRS.keys()

    def isValid(self, s: str) -> bool:
        open: List[str] = []
        for c in s:
            if c in self.OPENS:
                open.append(c)
                continue

            if len(open) == 0:
                return False

            o = open.pop()
            if self.PAIRS[o] != c:
                return False

        return len(open) == 0

