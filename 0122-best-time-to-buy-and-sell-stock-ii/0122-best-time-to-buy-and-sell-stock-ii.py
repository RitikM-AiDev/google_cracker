class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        dp = [0]*n
        min_ = prices[0]
        for i in range(1,n):
            dp[i]=max(prices[i]-prices[i-1],0)
        return sum(dp)
        