# Leetcode - Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        elif len(nums) == 1:
            return False
        else:
            target = total // 2
        
        if max(nums) > target:
            return False

        # dp[i] = True means "I can make sum i using some of the numbers"
        dp = [False] * (target + 1)
        dp[0] = True # base case: zero sum always possible
        
        for num in nums:
            for i in range(target, -1, -1):
                if dp[i] == True:
                    if (i + num) <= target:
                        dp[i + num] = True
            
            if dp[target] == True:
                return True

        return dp[target]
            