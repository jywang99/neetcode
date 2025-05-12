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


class ReverseBits:
    def reverseBits(self, n: int) -> int:
        rs = 0
        for i in range(32):
            rs |= ((n >> i) & 1) << (31 - i)
        return rs


class CountBits:
    def countBits(self, n: int) -> List[int]:
        rs = [0]
        for i in range(1, n+1):
            rs.append(rs[i >> 1] + (i & 1))
        return rs


class MissingNumber:
    def missingNumber(self, nums: List[int]) -> int:
        rs = len(nums)
        for i, n in enumerate(nums):
            rs ^= i ^ n
        return rs

