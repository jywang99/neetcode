from typing import List


class HappyNumber:
    def isHappy(self, n: int) -> bool:
        def getNext(n: int) -> int:
            rs = 0
            while n:
                rs += (n % 10) ** 2
                n //= 10
            return rs

        s, f = n, getNext(n)
        while s != f and f != 1:
            s = getNext(s)
            f = getNext(getNext(f))

        return f == 1


class PlusOne:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            v = digits[i] + carry
            digits[i] = v % 10
            carry = v // 10
        if carry:
            digits.insert(0, carry)
        return digits

