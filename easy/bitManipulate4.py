from typing import List


class HammingWeight:
    def hammingWeight(self, n: int) -> int:
        rs = 0
        while n > 0:
            rs += n & 1
            n >>= 1
        return rs
        

class SingleNumber:
    def singleNumber(self, nums: List[int]) -> int:
        rs = 0
        for n in nums:
            rs ^= n
        return rs

