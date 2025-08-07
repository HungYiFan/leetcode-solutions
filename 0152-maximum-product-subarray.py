# Leetcode - Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/description/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # track max and min product 
        min_prod, max_prod = nums[0], nums[0]
        res = nums[0]

        for i in range (1, len(nums)):

            max_temp = max(nums[i], max_prod * nums[i], min_prod * nums[i])
            min_temp = min(nums[i], min_prod * nums[i], max_prod * nums[i])

            max_prod = max_temp
            min_prod = min_temp

            res = max(res, max_prod)

        return res