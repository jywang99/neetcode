from typing import List


class IsValid:
    PAIRS = { "{": "}", "(": ")", "[": "]" }

    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c in self.PAIRS:
                stk.append(c)
                continue

            if not stk:
                return False
            if self.PAIRS[stk.pop()] != c:
                return False

        return len(stk) == 0


class MinStack:
    def __init__(self):
        self.stk = []
        self.mins = []
        

    def push(self, val: int) -> None:
        self.stk.append(val)
        self.mins.append(min(self.mins[-1], val) if self.mins else val)
        

    def pop(self) -> None:
        self.stk.pop()
        self.mins.pop()
        

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]


class GenerateParenthesis:
    def generateParenthesis(self, n: int) -> List[str]:
        rs = []
        stk = []

        def recurse(opens: int, closes: int):
            if opens == closes == n:
                rs.append("".join(stk))

            if opens < n:
                stk.append("(")
                recurse(opens+1, closes)
                stk.pop()
            if closes < opens:
                stk.append(")")
                recurse(opens, closes+1)
                stk.pop()
        
        recurse(0, 0)
        return rs

