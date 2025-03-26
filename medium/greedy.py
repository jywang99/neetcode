from typing import Counter, List


class MaxSubArray:
    def maxSubArray(self, nums: List[int]) -> int:
        rs = nums[0]
        cur = 0

        for n in nums:
            if cur < 0:
                cur = 0
            cur += n
            rs = max(rs, cur)
        
        return rs
        

class JumpGame:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums)-2, -1, -1):
            if goal - i <= nums[i]:
                goal = i

        return goal == 0


class JumpGame2:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        rs = 0
        while r < len(nums)-1:
            far = 0
            for i in range(l, r+1):
                far = max(far, i + nums[i])
            l = r + 1
            r = far
            rs += 1
        return rs


class GasStation:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total, rs = 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                rs = i + 1
        return rs


class HandOfStraights:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        cnt = Counter(hand)
        for n in hand:
            start = n
            while cnt[start - 1]:
                start -= 1
            while start <= n:
                while cnt[start]:
                    for i in range(start, start + groupSize):
                        if not cnt[i]:
                            return False
                        cnt[i] -= 1
                start += 1
        return False


class MergeTriplets:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)

        return len(good) == 3

