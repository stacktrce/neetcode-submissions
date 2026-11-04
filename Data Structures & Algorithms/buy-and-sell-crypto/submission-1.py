class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        sell = 0

        p1, p2 = 0, 0

        while p2 < len(prices) - 1:

            p2 += 1

            if prices[p2] < prices[p1]:
                p1 = p2

            profit = prices[p2] - prices[p1]

            if profit > sell:
                sell = profit

        return sell