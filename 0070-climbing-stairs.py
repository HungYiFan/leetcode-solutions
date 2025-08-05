# Leetcode 70 - Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n: int) -> int:
        res = [1, 1]
        
        if n > 1:
            for i in range (2, n+1):
                    res.append(res[-1] + res[-2])
        
        return res[-1]
    
"""
Time complexity: O(n)

Space complexity: O(n)

Approach:
- fibonacci: f(n) = f(n-1) + f(n-2)
- bottom up
"""