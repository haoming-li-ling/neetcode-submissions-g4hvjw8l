class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = [[0, 0] for _ in range(N + 1)]
        dp[N - 1][1] = prices[N - 1]
        for i in range(N - 1, -1, -1):
            dp[i][0] = max(dp[i + 1][0], -prices[i] + dp[i + 1][1])
            if i <= N - 2:
                dp[i][1] = max(dp[i + 1][1], prices[i] + dp[i + 2][0]) 
        return dp[0][0]
        