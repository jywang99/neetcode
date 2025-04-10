from typing import List


class ClimbStairs:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * n

        def recurse(i: int) -> int:
            if i >= n:
                return i == n
            if memo[i] != -1:
                return memo[i]
            memo[i] = recurse(i+1) + recurse(i+2)
            return memo[i]

        return recurse(0)


class CostClimbingStairs:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * len(cost)
        
        def recurse(i: int) -> int:
            if i >= len(cost):
                return 0
            if memo[i] == -1:
                memo[i] = cost[i] + min(recurse(i+1), recurse(i+2))
            return memo[i]

        return min(recurse(0), recurse(1))

