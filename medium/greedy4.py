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


class MergeTriplets:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        idcs = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i in range(3):
                if t[i] == target[i]:
                    idcs.add(i)

        return len(idcs) == 3


class PartitionLabels:
    def partitionLabels(self, s: str) -> List[int]:
        lasts = {}
        for i, c in enumerate(s):
            lasts[c] = i

        rs = []
        start, far = 0, 0
        for i, c in enumerate(s):
            far = max(far, lasts[c])
            if far == i:
                rs.append(i - start + 1)
                start = i+1
        return rs


class ValidString:
    def checkValidString(self, s: str) -> bool:
        om, ox = 0, 0
        for c in s:
            if c == "(":
                om, ox = om+1, ox+1
            elif c == ")":
                om, ox = om-1, ox-1
            else:
                om, ox = om-1, ox+1
            if ox < 0:
                return False
            if om < 0:
                om = 0
        return om == 0

