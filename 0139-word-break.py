# Leetcode 139 Word Break
# https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # dp[i] = True if s[0:i] (first i characters) can be segmented completely
        
        wordSet = set(wordDict) # faster lookup

        dp = [False] * (len(s) + 1)
        dp[0] = True # empty string is always valid

        for i in range (len(s)+1):
            for j in range (i):
                if dp[j] == True:
                    if s[j:i] in wordSet:
                        dp[i] = True
                        break
        
        return dp[-1]