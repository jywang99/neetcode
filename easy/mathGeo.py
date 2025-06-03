from typing import List


class HappyNumber:
    def isHappy(self, n: int) -> bool:
        def nextNum(c: int) -> int:
            rs = 0
            while c:
                rs += (c % 10) ** 2
                c //= 10
            return rs

        s, f = n, n
        while True:
            s = nextNum(s)
            f = nextNum(nextNum(f))
            if f == 1:
                return True
            if s == f:
                return False


class PlusOne:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            if not carry:
                break
            v = carry + digits[i]
            digits[i] = v % 10
            carry = v // 10

        if carry:
            digits.insert(0, carry)

        return digits

