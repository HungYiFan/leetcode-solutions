# Leetcode 213 - Robber House ||
# https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp_1, dp_2 = [0] * (len(nums) - 1), [0] * (len(nums) - 1)

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) == 3:
            return max(nums[0], nums[1], nums[2])

        dp_1[0], dp_1[1], dp_2[0], dp_2[1] = nums[0], max(nums[0], nums[1]), nums[1], max(nums[1], nums[2])
        
        for i in range(2, len(nums)-1):
            # rob from 0 to (n-1)
            dp_1[i] = max(dp_1[i-2] + nums[i], dp_1[i-1])
            # rob from 1 to n
            dp_2[i] = max(dp_2[i-2] + nums[i+1], dp_2[i-1])

        return max(dp_1[-1], dp_2[-1])
    
"""
Time complexity: O(n)
Space complexity: O(n)

Approach:
- can only pick from one of nums[0] or nums[-1], so check max for 0 to (n-1) and 1 to n respectively
- dp

TODO optimize space complexity to O(1)
"""