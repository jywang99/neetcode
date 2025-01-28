from typing import List


class MinStack:

    def __init__(self):
        self.stk = []
        self.mins = []
        

    def push(self, val: int) -> None:
        self.stk.append(val)
        self.mins.append(min(val, self.mins[-1]) if self.mins else val)


    def pop(self) -> None:
        self.mins = self.mins[:-1]
        return self.stk.pop()
        

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]


class EvalRPN:
    OPS = ["+", "-", "*", "/"]


    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for t in tokens:
            match t:
                case "+":
                    stk.append(stk.pop() + stk.pop())
                case "-":
                    x, y = stk.pop(), stk.pop()
                    stk.append(y - x)
                case "*":
                    stk.append((stk.pop()) * stk.pop())
                case "/":
                    x, y = stk.pop(), stk.pop()
                    stk.append(int(float(y) / x))
                case _:
                    stk.append(int(t))
        
        return stk[0]


class GenerateParenthesis:
    def generateParenthesis(self, n: int) -> List[str]:
        rs = []
        stk = []

        def backtrack(opens: int, closes: int):
            if opens == closes == n:
                rs.append("".join(stk))
                return

            if opens < n:
                stk.append("(")
                backtrack(opens+1, closes)
                stk.pop()
            if closes < opens:
                stk.append(")")
                backtrack(opens, closes+1)
                stk.pop()

        backtrack(0, 0)
        return rs


class DailyTemperatures:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        rs = [0] * len(temperatures)
        stk: list[int] = []
        
        for i, t in enumerate(temperatures):
            while stk:
                if temperatures[stk[-1]] >= t:
                    break
                li = stk.pop()
                rs[li] = i - li
            stk.append(i)

        return rs


class CarFleet:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        stk = []
        for p, s in cars:
            t = (target - p) / s
            if stk and stk[-1] >= t:
                continue
            stk.append(t)
        return len(stk)

