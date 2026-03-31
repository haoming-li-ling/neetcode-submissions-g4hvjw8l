class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        max_p = 0
        for i, p in enumerate(prices):
            if i == 0:
                continue
            if p - min_p > max_p:
                max_p = p - min_p
            if p < min_p:
                min_p = p

        return max_p


        