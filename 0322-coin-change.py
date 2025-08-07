# Leetcode - Coin Change
# https://leetcode.com/problems/coin-change/description/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bottom up: dp[i] = the minimum number of coins needed to get amount i

        # initialize dp to unreachable amounts
        dp = [amount + 1] * (amount + 1)

        # base case
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-c])
        
        return dp[amount] if dp[amount] != (amount + 1) else -1
        

