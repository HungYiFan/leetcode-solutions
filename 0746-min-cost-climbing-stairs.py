# Leetcode 746 - Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/description/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
    
    # dp[i] = min(dp(i-1) + cost[i-1], dp[i-2] + cost[i-2])

        dp = [0] * (len(cost) + 1)

        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        return dp[-1]

""""
Time complexity: O(n)
- loop runs from 2 -> len(cost)

Space complexity: O(n)
- dp array of size n+1

Approach:
- bottom-up dp

TODO since it's always using the last two value only, the space complexity can be reduce to O(1)

"""