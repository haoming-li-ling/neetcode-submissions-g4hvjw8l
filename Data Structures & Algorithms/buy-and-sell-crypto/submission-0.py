class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # N = len(prices)
        # buy = [0] * (N + 1)
        # sell = [0] * (N + 1)
        min_p = prices[0]
        max_p = 0
        for i, p in enumerate(prices):
            if i == 0:
                continue
            # index = i + 1
            # buy[index] = sell[index - 1] - p
            # sell[index] = p - min()
            if p - min_p > max_p:
                max_p = p - min_p
            if p < min_p:
                min_p = p

        return max_p


        