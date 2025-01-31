from typing import List


class EvalRPN:
    def is_integer(self, s: str):
        try:
            int(s)
            return True
        except ValueError:
            return False


    def evalRPN(self, tokens: List[str]) -> int:
        ns = []

        for t in tokens:
            if self.is_integer(t):
                ns.append(int(t))
                continue

            x, y = ns.pop(), ns.pop()
            match t:
                case "+":
                    ns.append(x + y)
                case "-":
                    ns.append(y - x)
                case "*":
                    ns.append(x * y)
                case "/":
                    ns.append(int(y / x))
                case _:
                    raise Exception("WTF")

        return ns[0]


class CarFleet:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, spd) for pos, spd in zip(position, speed)]
        cars.sort(reverse=True)

        cnt = 0
        prev_time: float|None = None
        for car in cars:
            time = (target - car[0]) / car[1]
            if prev_time and prev_time >= time:
                continue
            cnt += 1
            prev_time = time

        return cnt


class DailyTemperatures:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        rs = [0] * len(temperatures)
        stk = []
        for i, t in enumerate(temperatures):
            while stk and temperatures[stk[-1]] < t:
                j = stk.pop()
                rs[j] = i - j
            stk.append(i)
        return rs

