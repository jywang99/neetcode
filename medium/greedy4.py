from typing import Counter, List


class MaxSubArray:
    def maxSubArray(self, nums: List[int]) -> int:
        cur, rs = 0, nums[0]
        for n in nums:
            if cur < 0:
                cur = 0
            cur += n
            rs = max(rs, cur)
        return rs


class JumpGame:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0


class JumpGame2:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        rs = 0
        while r < len(nums)-1:
            far = r
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

        start, cur = 0, 0
        for i in range(len(gas)):
            if cur < 0:
                cur = 0
                start = i
            cur += (gas[i] - cost[i])
        
        return start


class NStraightHand:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        cnt = Counter(hand)
        for n in hand:
            start = n
            while cnt[start]:
                start -= 1
            while start <= n:
                while cnt[start]:
                    for i in range(start, start+groupSize):
                        if not cnt[i]:
                            return False
                        cnt[i] -= 1
                start += 1

        return True

