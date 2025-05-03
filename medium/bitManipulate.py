import math


class GetSum:
    def getSum(self, a: int, b: int) -> int:
        rs, cb = 0, 0

        for i in range(32):
            ab, bb = (a >> i) & 1, (b >> i) & 1
            rs |= (ab ^ bb ^ cb) << i
            cb = (ab & bb) | (ab & cb) | (bb & cb)
        if rs > 0x7FFFFFFF:
            rs = ~(rs ^ 0xFFFFFFFF)

        return rs


class ReverseInteger:
    def reverse(self, x: int) -> int:
        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1

        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0
            res = (res * 10) + digit

        return res

