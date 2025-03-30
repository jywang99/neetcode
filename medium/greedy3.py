from typing import Counter, List


class MaxSubArray:
    def maxSubArray(self, nums: List[int]) -> int:
        s, rs = 0, nums[0]
        for n in nums:
            if s < 0:
                s = 0
            s += n
            rs = max(rs, s)
        return rs


class JumpGame:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0


class JumpGame2:
    def jump(self, nums: List[int]) -> int:
        rs = 0
        l, r = 0, 0
        while r < len(nums)-1:
            far = 0
            for i in range(l, r+1):
                far = max(far, i + nums[i])
            l = r + 1
            r = far
            rs += 1
        return rs


class GasStations:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        tank, rs = 0, 0
        for i in range(len(gas)):
            if tank < 0:
                tank = 0
                rs = i
            tank += gas[i] - cost[i]
        
        return rs


class StraightHand:
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
                    for i in range(start, start + groupSize):
                        if not cnt[i]:
                            return False
                        cnt[i] -= 1
                start += 1
        return True


class MergeTriplets:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        idc = set()
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i in range(0, 3):
                if t[i] == target[i]:
                    idc.add(i)
        return len(idc) == 3

class PartitionLabels:
    def partitionLabels(self, s: str) -> List[int]:
        lasts = {}
        for i, c in enumerate(s):
            lasts[c] = i

        start, end = 0, 0
        rs = []
        for i, c in enumerate(s):
            end = max(end, lasts[c])
            if i == end:
                rs.append(end - start + 1)
                start = i+1

        return rs
