class Solution(object):
    def maxProfit(self, prices):
        low = prices[0]
        ans = 0

        for x in prices:
            low = min(low, x)
            ans = max(ans, x - low)

        return ans