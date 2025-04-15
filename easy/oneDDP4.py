from typing import List


class MinCostClimbingStairs:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * len(cost)
        def recurse(i: int) -> int:
            if i >= len(cost):
                return 0
            if cache[i] == -1:
                cache[i] = cost[i] + min(recurse(i+1), recurse(i+2))
            return cache[i]
        return min(recurse(0), recurse(1))
        

class ClimbStairs:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def recurse(i: int) -> int:
            if i >= n:
                return i == n
            if cache[i] == -1:
                cache[i] = recurse(i+1) + recurse(i+2)
            return cache[i]
        return recurse(0)

