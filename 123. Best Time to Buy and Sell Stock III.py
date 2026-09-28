class Solution(object):
    def maxProfit(self, prices):
        buy1 = float('-inf')
        sell1 = 0
        buy2 = float('-inf')
        sell2 = 0

        for x in prices:
            buy1 = max(buy1, -x)
            sell1 = max(sell1, buy1 + x)

            buy2 = max(buy2, sell1 - x)
            sell2 = max(sell2, buy2 + x)

        return sell2