# Leetcode 198 - House Robber
# https://leetcode.com/problems/house-robber/description/

class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        dp = [0] * len(nums)

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]
    
"""
Time complexity: O(n)

Space complexity: O(n)

Approach:
- dp

TODO optimize space complexity to O(1)
"""