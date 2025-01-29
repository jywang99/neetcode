from typing import List


class MinStack:

    def __init__(self):
        self.stk = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        self.mins.append(min(self.mins[-1], val) if self.mins else val)

    def pop(self) -> None:
        self.stk = self.stk[:-1]
        self.mins = self.mins[:-1]

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.mins[-1]


class EvalRPN:
    def evalRPN(self, tokens: List[str]) -> int:
        ns: list[int] = []
        for t in tokens:
            match t:
                case "+":
                    ns.append(ns.pop() + ns.pop())
                case "-":
                    y, x = ns.pop(), ns.pop()
                    ns.append(x - y)
                case "*":
                    ns.append(ns.pop() * ns.pop())
                case "/":
                    y, x = ns.pop(), ns.pop()
                    ns.append(int(x / y))
                case _:
                    ns.append(int(t))
        return ns[0]


class GenerateParenthesis:
    def generateParenthesis(self, n: int) -> List[str]:
        rs: list[str] = []
        stk: list[str] = []

        def recurse(opens: int, closes: int):
            if opens == closes == n:
                rs.append("".join(stk))
                return

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


class CarFleet:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(reverse=True)
        
        jams = []
        for car in cars:
            t = (target - car[0]) / car[1]
            if not jams or jams[-1] < t:
                jams.append(t)

        return len(jams)


class DailyTemperatures:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        rs = [0] * len(temperatures)
        stk = []
        for i, t in enumerate(temperatures):
            while stk and temperatures[stk[-1]] < t:
                li = stk.pop()
                rs[li] = i - li
            stk.append(i)
        return rs

